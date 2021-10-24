/* file.c: Implementation of memory backed file object (mmaped object). */

#include "vm/vm.h"
#include "threads/vaddr.h"
#include "threads/mmu.h"
#include "vm/file.h"
#include <string.h>


static bool file_backed_swap_in (struct page *page, void *kva);
static bool file_backed_swap_out (struct page *page);
static void file_backed_destroy (struct page *page);

/* DO NOT MODIFY this struct */
static const struct page_operations file_ops = {
	.swap_in = file_backed_swap_in,
	.swap_out = file_backed_swap_out,
	.destroy = file_backed_destroy,
	.type = VM_FILE,
};

/* 3-4 MMAP */
struct list mmap_file_list;

struct mmap_file_info {
	struct list_elem elem;
	uint64_t start;
	uint64_t end;

};




/* The initializer of file vm */
void
vm_file_init (void) {
	list_init (&mmap_file_list);
}

/* Initialize the file backed page */
bool
file_backed_initializer (struct page *page, enum vm_type type, void *kva) {
	/* Set up the handler */
	struct file *file = ((struct mmap_info *)page->uninit.aux)->file;
	page->operations = &file_ops;


	struct file_page *file_page = &page->file;
	file_page->file = file;
	return true;
}

/* Swap in the page by read contents from the file. */
static bool
file_backed_swap_in (struct page *page, void *kva) {
	struct file_page *file_page UNUSED = &page->file;
}

/* Swap out the page by writeback contents to the file. */
static bool
file_backed_swap_out (struct page *page) {
	struct file_page *file_page UNUSED = &page->file;
}

/* Destory the file backed page. PAGE will be freed by the caller. */
static void
file_backed_destroy (struct page *page) {
	struct file_page *file_page UNUSED = &page->file;

	if (pml4_is_dirty (thread_current ()->pml4, page->va)) {
		file_seek (file_page->file, file_page->ofs);
		file_write (file_page->file, page->va, file_page->size);
	}
	file_close (file_page->file);

	if (page->frame != NULL) {
		list_remove (&page->frame->elem);
		free (page->frame);
	}
}

/* Do the mmap */  /* 3-4 */
void *
do_mmap (void *addr, size_t length, int writable,
		struct file *file, off_t offset) 
{
	off_t ofs;
	uint64_t read_bytes;
	for (uint64_t temp_ofs = 0; temp_ofs < length; temp_ofs += PGSIZE)
	{
		struct mmap_info *map_info = malloc (sizeof (struct mmap_info));
		ofs = offset + temp_ofs;
		read_bytes = length - temp_ofs >= PGSIZE ? PGSIZE : length - temp_ofs;
		map_info->file = file_reopen (file);
		map_info->offset = ofs;
		map_info->read_bytes = read_bytes;
		vm_alloc_page_with_initializer (VM_FILE, (void *) ((uint64_t)addr + temp_ofs), writable, lazy_load_file, (void *) map_info);
	}
	struct mmap_file_info *map_file_info = malloc (sizeof (struct mmap_file_info));
	map_file_info->start = (uint64_t) addr;
	map_file_info->end = (uint64_t) pg_round_down((uint64_t) addr + length - 1);
	list_push_back (&mmap_file_list, &map_file_info->elem);
	return addr;
}

/* Do the munmap */
void
do_munmap (void *addr)
{
	/* project 3-4 MUNMAP */
	if (list_empty (&mmap_file_list)) return ;
	// struct thread *curr = thread_current ();
	for (struct list_elem *e = list_front (&mmap_file_list); e != list_end (&mmap_file_list); e = list_next (e))
	{
		struct mmap_file_info *mfi = list_entry (e, struct mmap_file_info, elem);
		if (mfi->start == (uint64_t) addr) {
			for (uint64_t temp = (uint64_t) addr; temp <= mfi->end; temp += PGSIZE)
			{				
				struct page *p = spt_find_page (&thread_current ()->spt, (void *) temp);
				// struct file_page *fp = &p->file;
				// printf("\n\n %d \n\n", fp->size);
				// if (pml4_is_dirty (curr->pml4, p->va)) {
				// 	file_seek (fp->file, fp->ofs);
				// 	file_write (fp->file, p->va, fp->size);
				// 	pml4_set_dirty (curr->pml4, p->va, false);
				// }
				// // Set "not present" to page, and clear.
				// pml4_clear_page (curr->pml4, p->va);
				spt_remove_page (&thread_current ()->spt, p);
			}
			list_remove (&mfi->elem);
			free(mfi);
			return ;
		}
	}
}


static bool lazy_load_file (struct page *page, void *aux)
{
	struct mmap_info *map_info = (struct mmap_info *) aux;
	file_seek (map_info->file, map_info->offset);
	page->file.size = file_read (map_info->file, page->va, map_info->read_bytes);
	page->file.ofs = map_info->offset;
	if (page->file.size != PGSIZE) {
		memset (page->va + page->file.size, 0, PGSIZE - page->file.size);
	}
	pml4_set_dirty (thread_current ()->pml4, page->va, false);	// WHY!! dirty를 해제해주는 이유는??
	free(map_info);
	return true;
}

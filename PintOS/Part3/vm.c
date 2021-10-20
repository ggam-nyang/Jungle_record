/* vm.c: Generic interface for virtual memory objects. */

#include "threads/malloc.h"
#include "vm/vm.h"
#include "vm/inspect.h"
#include "threads/vaddr.h"
#include <debug.h>
#include "threads/mmu.h"
#include "vm/file.h"
#include <string.h>

/* global variables by ggam */
struct list frame_list; // frame list for claim page
struct lock spt_kill_lock;




/* Initializes the virtual memory subsystem by invoking each subsystem's
 * intialize codes. */
void
vm_init (void) {
	vm_anon_init ();
	vm_file_init ();
#ifdef EFILESYS  /* For project 4 */
	pagecache_init ();
#endif
	lock_init (&spt_kill_lock);
	register_inspect_intr ();
	/* DO NOT MODIFY UPPER LINES. */
	/* TODO: Your code goes here. */
	list_init (&frame_list);
}

/* Get the type of the page. This function is useful if you want to know the
 * type of the page after it will be initialized.
 * This function is fully implemented now. */
enum vm_type
page_get_type (struct page *page) {
	int ty = VM_TYPE (page->operations->type);
	switch (ty) {
		case VM_UNINIT:
			return VM_TYPE (page->uninit.type);
		default:
			return ty;
	}
}

/* Helpers */
static struct frame *vm_get_victim (void);
static bool vm_do_claim_page (struct page *page);
static struct frame *vm_evict_frame (void);

/* Create the pending page object with initializer. If you want to create a
 * page, do not create it directly and make it through this function or
 * `vm_alloc_page`. */
bool
vm_alloc_page_with_initializer (enum vm_type type, void *upage, bool writable,
		vm_initializer *init, void *aux) {


	struct supplemental_page_table *spt = &thread_current ()->spt;

	/* Check wheter the upage is already occupied or not. */
	if (spt_find_page (spt, upage) == NULL) {
		/* TODO: Create the page, fetch the initialier according to the VM type,
		 * TODO: and then create "uninit" page struct by calling uninit_new. You
		 * TODO: should modify the field after calling the uninit_new. */
		/* 3-2 uninit page 만들기! */
		ASSERT (VM_TYPE(type) != VM_UNINIT)
		struct page *p = malloc (sizeof (struct page));
		if (VM_TYPE(type) == VM_ANON)
			uninit_new (p, upage, init, type, aux, anon_initializer);
		else if (VM_TYPE(type) == VM_FILE)
			uninit_new (p, upage, init, type, aux, file_backed_initializer);

		p->writable = writable;
		/* TODO: Insert the page into the spt. */
		spt_insert_page(spt, p);
		return true;
	}
	return false;
}

/* Find VA from spt and return page. On error, return NULL. */
struct page *
spt_find_page (struct supplemental_page_table *spt UNUSED, void *va UNUSED) {
	/* 3-1  */   /* WHY!! malloc을 하지 않으면 thread_exit 시, thread_name이 없어진다?? REASON: page 포인터로 값을 줬기 때문이다. */
	struct page *page = (struct page *) malloc (sizeof (struct page));
	page->va = pg_round_down (va);
	struct hash_elem *e = hash_find (spt->page_table, &page->hash_elem);
	if (e == NULL)
		return NULL;
	struct page *result = hash_entry (e, struct page, hash_elem);
	free(page);
	ASSERT ((va < result->va + PGSIZE) && va >= result->va);
	return result;
}

/* Insert PAGE into spt with validation. */
bool
spt_insert_page (struct supplemental_page_table *spt UNUSED,
		struct page *page UNUSED) {
	int succ = false;

	/* 3-1  */
	struct hash_elem *e = hash_insert (spt->page_table, &page->hash_elem);
	if (e == NULL) {
		succ = true;
	}
	return succ;
}

void
spt_remove_page (struct supplemental_page_table *spt, struct page *page) {
	/* 3-2에서 하긴 했지만, 언제 필요한 경우인지? */
	struct hash_elem *e = hash_delete (spt->page_table, &page->hash_elem);
	if (e != NULL)
		vm_dealloc_page (page);
	return ;  // WHY!! return true와의 차이는?
}

/* Get the struct frame, that will be evicted. */
static struct frame *
vm_get_victim (void) {
	struct frame *victim = NULL;
	 /* TODO: The policy for eviction is up to you. */

	return victim;
}

/* Evict one page and return the corresponding frame.
 * Return NULL on error.*/
static struct frame *
vm_evict_frame (void) {
	struct frame *victim UNUSED = vm_get_victim ();
	/* TODO: swap out the victim and return the evicted frame. */

	return NULL;
}

/* palloc() and get frame. If there is no available page, evict the page
 * and return it. This always return valid address. That is, if the user pool
 * memory is full, this function evicts the frame to get the available memory
 * space.*/
static struct frame *
vm_get_frame (void) {
	struct frame *frame = malloc (sizeof (struct frame)); // WHY!! struct 포인터의 size가 아니고 struct??
	frame->kva = palloc_get_page (PAL_USER);
	frame->page = NULL;


	// swap 하는 경우
	if (frame->kva == NULL) {
		PANIC("******* need to make swap *******");
	// 	free (frame);
	// 	frame = vm_evict_frame ();
	}

	ASSERT (frame != NULL);
	ASSERT (frame->page == NULL);
	return frame;
}

/* Growing the stack. */
static void
vm_stack_growth (void *addr UNUSED) {
}

/* Handle the fault on write_protected page */
static bool
vm_handle_wp (struct page *page UNUSED) {
}

/* Return true on success */
bool
vm_try_handle_fault (struct intr_frame *f UNUSED, void *addr UNUSED,
		bool user UNUSED, bool write UNUSED, bool not_present UNUSED) {
	struct thread *curr = thread_current ();
	struct supplemental_page_table *spt UNUSED = &curr->spt;
	/* TODO: Validate the fault */
	/* TODO: Your code goes here */
	/* 3-2 validate fault*/
	if (is_kernel_vaddr (addr) && user) return false;
	void *stack_bottom = pg_round_down (curr->saved_rsp);
	/* 3-3 stack growth */
	// if (write && (stack_bottom - PGSIZE <= addr && (uintptr_t) addr < USER_STACK)) {
	// 	vm_stack_growth (addr);
	// 	return true;
	// }

	struct page *page = spt_find_page (spt, addr);
	if (page == NULL)
		return false;
	/* WHY!! Read-only */
	// if (write && !not_present)
	// 	return vm_handle_wp (page);

	return vm_do_claim_page (page);
}

/* Free the page.
 * DO NOT MODIFY THIS FUNCTION. */
void
vm_dealloc_page (struct page *page) {
	destroy (page);
	free (page);
}

/* Claim the page that allocate on VA. */
bool
vm_claim_page (void *va UNUSED) {
	struct page *page = spt_find_page (&thread_current ()->spt, va);
	if (page == NULL)
		return false;
	return vm_do_claim_page (page);
}

/* Claim the PAGE and set up the mmu. */
static bool
vm_do_claim_page (struct page *page) {
	struct frame *frame = vm_get_frame ();
	struct thread *curr = thread_current (); // 현재 thread 추가

	ASSERT (frame != NULL); // 혹시 모를 debuging
	/* Set links */
	frame->page = page;
	page->frame = frame;

	/* 3-1 memory */
	list_push_back(&frame_list, &frame->elem);

	if (!pml4_set_page (curr->pml4, page->va, frame->kva, page->writable))
		return false;

	return swap_in (page, frame->kva);
}

/* Initialize new supplemental page table */
void
supplemental_page_table_init (struct supplemental_page_table *spt UNUSED) {
	/* 3-1 memory management*/
	struct hash *p_table = malloc(sizeof (struct hash));
	hash_init (p_table, page_hash, page_less, NULL);
	spt->page_table = p_table;
}

/* Copy supplemental page table from src to dst */
bool
supplemental_page_table_copy (struct supplemental_page_table *dst UNUSED,
		struct supplemental_page_table *src UNUSED) {
	// if (src == NULL) return false;
	/* 3-2 for fork */
	struct hash_iterator i;
	hash_first (&i, src->page_table);
	while (hash_next (&i))
	{
		struct page *temp_page = hash_entry (hash_cur (&i), struct page, hash_elem);

		if (temp_page->operations->type == VM_UNINIT) {
			vm_initializer *init = temp_page->uninit.init;
			bool writable = temp_page->writable;
			int type = temp_page->uninit.type;
			void *aux = temp_page->uninit.aux;

			if (type & VM_ANON) {
				struct load_info *li = malloc (sizeof (struct load_info));
				li->file = file_duplicate (((struct load_info *) aux)-> file);
				li->ofs = ((struct load_info *) aux)-> ofs;
				li->page_read_bytes = ((struct load_info *) aux)->page_read_bytes;
				li->page_zero_bytes = ((struct load_info *) aux)->page_zero_bytes;
				vm_alloc_page_with_initializer (type, temp_page->va, writable, init, (void *) li);
			}

			else if (type & VM_FILE) {
				// WHY!! do nothing
			}
		}

		else if (page_get_type (temp_page) == VM_ANON) {
			if (!vm_alloc_page (temp_page->operations->type, temp_page->va, temp_page->writable))
				return false;
			struct page *new_page = spt_find_page (&thread_current ()->spt, temp_page->va); // WHY!! 고민해보기
			if (!vm_do_claim_page (new_page))
				return false;
			memcpy (new_page->frame->kva, temp_page->frame->kva, PGSIZE);
		}
		else if (page_get_type (temp_page) == VM_FILE) {
			// WHY!! do nothing
		}
	}
	return true;
}

/* Free the resource hold by the supplemental page table */
void
supplemental_page_table_kill (struct supplemental_page_table *spt UNUSED) {
	/* TODO: Destroy all the supplemental_page_table hold by thread and
	 * TODO: writeback all the modified contents to the storage. */
	if (spt->page_table == NULL) return false;

	// WHY!! lock이 필요할까??
	// lock_acquire (&spt_kill_lock);
	hash_destroy (spt->page_table, spt_destroy);
	free (spt->page_table);
	// lock_release (&spt_kill_lock);
}

unsigned
page_hash (const struct hash_elem *p_, void *aux UNUSED)
{
	const struct page *p = hash_entry (p_, struct page, hash_elem);
	return hash_bytes (&p->va, sizeof p->va);
}

/* Returns true if page a precedes page b. */
bool
page_less (const struct hash_elem *a_,
           const struct hash_elem *b_, void *aux UNUSED) {
  const struct page *a = hash_entry (a_, struct page, hash_elem);
  const struct page *b = hash_entry (b_, struct page, hash_elem);

  return a->va < b->va;
}

static void
spt_destroy (struct hash_elem *e, void *aux UNUSED)
{
	struct page *p = hash_entry (e, struct page, hash_elem);
	// vm_dealloc_page (p);
	ASSERT (p != NULL);
	destroy (p);
	free (p);
}
import sys
import itertools
read = sys.stdin.readline

word_N, alpha_N = map(int, read().strip().split())
sliced_words = []
for _ in range(word_N):
    word = read().strip()
    sliced_words.append(word[4:-4])

def count_word(words, k):
    if k < 5:
        return 0

    count = 0
    alpha = ['a', 'n', 't', 'i', 'c']
    k -= 5
    while k >= 0 and words:
        now_word = words.pop()
        for one_word in now_word:
            if one_word not in alpha:
                k -= 1
                if k < 0:
                    return count
                alpha.append(one_word)
        count += 1
    return count

max_count = 0
for words_list in itertools.permutations(sliced_words):
    max_count = max(max_count, count_word(list(words_list), alpha_N))

print(max_count)

import sys
read = sys.stdin.readline



A = read().strip()
B = read().strip()


def bm_match(txt, pat):
    skip = [None] * 256

    for pt in range(256):
        skip[pt] = len(pat)
    for pt in range(len(pat)):
        skip[ord(pat[pt])] = len(pat) - pt - 1

    while pt < len(txt):
        pp = len(pat) - 1
        while txt[pt] == pat[pp]:
            if pp == 0:
                return pt
            pt -= 1
            pp -= 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp

    return -1

answer = ''
if len(A) < len(B):
    short = A
    long = B
else:
    short = B
    long = A

for i in range(len(short) // 2 + 1):
    if bm_match(long, short[i:]) != -1:
        answer = short[i:]
        break

    if bm_match(long, short[:-i - 1]) != -1:
        answer = short[:-i - 1]
        break

print(len(answer))
print(answer)

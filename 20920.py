import sys

input = sys.stdin.readline
N, M = map(int, input().split())

words_dict: dict[str, int] = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words_dict[word] = words_dict.get(word, 0) + 1

words = list(words_dict.keys())
words.sort(key=lambda x: (-words_dict[x], -len(x), x))
print("\n".join(words))

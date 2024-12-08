def all_variants(text):
    n = len(text)

    for l in range(1, n + 1):
        for s in range(n - l + 1):
            e = s + l
            yield text[s:e]

a = all_variants('abc')
for i in a:
    print(i)

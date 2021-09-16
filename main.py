import string

lst = list(string.printable)
weights = {}
t = len(lst)
for i in range(t):
    weights[lst[i]] = i
print(weights)


def search_pattern(txt, pat):
    n = len(txt)
    m = len(pat)
    ht = 0
    hp = 0
    for i in range(m):
        hp += weights[pat[i]] * 10 ** (m - i - 1)
        ht += weights[txt[i]] * 10 ** (m - i - 1)

    while len(txt) >= m:
        if ht == hp:
            print('found')
        ht -= weights[txt[0]] * 10 ** (m - 1)
        txt = txt[1:]
        ht *= 10
        if m - 1 < len(txt):
            ht += weights[txt[m - 1]] * 10 ** 0


text = 'Geeks for Geeks'
pattern = 'Geek'
search_pattern(text, pattern)

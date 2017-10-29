w = input()
si = w.find('f')
i = si
if i != -1:
    while i < w.find('f', i + 1):
        i = w.find('f', i + 1)
    if i > si:
        print(si, i)
    else:
        print(si)

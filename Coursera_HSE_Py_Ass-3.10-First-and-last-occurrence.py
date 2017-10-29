w = input()
si = w.find('f')
i = w.rfind('f')
if i != -1:
    if i > si:
        print(si, i)
    else:
        print(si)

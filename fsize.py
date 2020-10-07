i = 0

with open('fsize.css', 'w') as f:
    while i != 257:
        s = '.size{0}{{font-size:{0}px}}'.format(str(i))
        f.write(s)
        i += 1

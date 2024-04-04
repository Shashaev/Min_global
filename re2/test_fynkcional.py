
with open('../ss') as f:
    n = f.readlines()

d = []

for i in n:
    i = i.split()[1: 4]
    try:
        k = int(i[0])
        d.append(' '.join(i))
    except Exception as e:
        print(e)

d = list(set(d))
# d.sort(key=lambda x: sum(map(int, x.split())))
with open('colors', 'w') as f:
    for i in d:
        f.write(i + '\n')

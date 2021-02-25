f = open('traf.txt', 'r')
a = 0
b = 0
for line in f:
    data = line.split(',')
    data[-1] = data[-1][:-2]
    f1 = open(str(data[-1]) + str(data[-1]) + '.txt', 'a')
    zap_line = line.rstrip('.\n')
    f1.write(zap_line)
    f1.write('\n')
    f1.close()
    a += 1
    if a % 4898 == 0:
        b += 0.1
        print(str(b) + ' %')
f.close()

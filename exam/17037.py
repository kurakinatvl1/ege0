with  open(r'1714.txt') as file:
    data = file.readline()
n = 0
for i in range(0,len(data)-2):
    a = data[i:i+3]
    if 1<=abs(int(data[i]))//10000<=9:
        n+=1
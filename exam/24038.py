with  open(r'24038.txt') as file:
    data = file.readline()
maxn =0
maxstr = ''
for i in range(0,len(data)-14):
    a = int(str(data[i:i+14]),14)
    if a%2!=0:
        if a >maxn:
            maxn = (int(str(data[i:i+14]),14))
            maxstr = data[i:i+14]
print(maxstr)
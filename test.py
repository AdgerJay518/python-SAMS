
file = open("students.txt", "r")
while True:
    s = file.readline()
    dic= {}
    for i in s.split(","):
        k_v=[]
        for k in i:
            k=k.strip()

            k_v.append(k)
        dic[k_v[0]]=k_v[1]
    print(dic)
    if s == '':
        break
file.close()


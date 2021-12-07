list=["gilven","064002100039","apa","404"]
jumlah=0
for i in list:
    if len(i)>=2:
        if i[0]==i[len(i)-1]:
            print(i)
            jumlah+=1
print("Terdapat",jumlah,"String Yang Memenuhi Kriteria") 
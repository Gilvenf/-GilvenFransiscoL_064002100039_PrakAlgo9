tpl=((20,7,20,3),(4,10,20,3),(25,10,14,17),(13,5,2,1))
list=[]
for i in range(len(tpl)):
    total=0
    for j in range (len(tpl[i])):
        total+=tpl[i][j]
    rata2=total/len(tpl[i])
    list.insert(i,rata2)
print("Rata-Rata Nilai tuple:")
print(list)
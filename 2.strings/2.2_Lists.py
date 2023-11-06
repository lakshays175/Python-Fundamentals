import re
mylist = ["$100","$200","#300","#600","600","600"]

updated_list=[]
sum=0 

for l in mylist:
    
    if l.isnumeric() :
        updated_list.append(l)
        sum+=int(l)
    else: 
        updated_list.append(l[1:])
        sum+=int(l[1:])


print(updated_list)
print(sum)
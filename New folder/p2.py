import random
list = []
for i in range(0,9):
    x =random.randint(0,9)   
    list.append(x)
print(list)


for i in range(0,len(list),2):
    print(list[i],end = " ",)
print("\n")


for j in range(len(list)):
    if (list[j]) % 2 == 0:
        print(list[j],end=" ")






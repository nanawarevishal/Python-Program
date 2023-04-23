n1 = int(input("Enter the number of element of list1: "))
ls1=[]

print("Enter the element: ")
for i in range(0,n1):
    ls1.append(int(input()))


n2 = int(input("Enter the number of element of list2: "))
ls2=[]

print("Enter the element: ")
for i in range(0,n2):
    ls2.append(int(input()))

print("The uncommon elements in list1 are:")
for i in ls1:
    if i not in ls2:
        print(i,end=" ")
    else:
        continue

print("\nThe uncommon elements in list2 are:")
for i in ls2:
    if i not in ls1:
        print(i,end=" ")
    
    else:
        continue
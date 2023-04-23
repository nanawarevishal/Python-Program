
n = int(input("Enter the number: "))
temp =n
sum=0
while temp!=0:
    rem = temp % 10
    sum = (sum + rem*rem*rem)
    temp = int(temp/10)

if(sum==n):
    print(n,"is a Amstrong number")

else:
     print(n,"is not a Amstrong number")



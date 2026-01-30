n=(int(input("Enter number: ")))
t=n
s=0
while n>0:
    d=n%10
    s=s+(d ** 3)
    n=n//10
if t==s:
    print(t,"is armstrong number")
else:
    print(t,"is not armstrong number")
n=int(input("Enter Number:"))
newlist=[]

for i in range(1,n+1):
    i=int(input("Enter {} Digit :".format(i)))
    newlist.append(i)

search=int(input("Which Number do you want to find :"))

Found=False
for i in range(len(newlist)):
    if newlist[i] == search:
        Found=True
        

if Found:
    print("Your Item is Found")
else:
    print("Not Found")







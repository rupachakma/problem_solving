# def isPrime(num): 
#     count=0
#     for i in range(2,num):
#         if num % i == 0:
#             count=1
#     if count == 0:
#         print("prime")
#     else:
#         print("not prime")
     
# number=int(input("Enter a Number to check is Prime: "))


# isPrime(number)


# n=int(input("A number to check prime or not :"))

# count=True
# for i in range(2,n):
#     if n % i == 0:
#         count = False
# if count == True:
#     print("prime")
# else:
#     print("not prime")

def prime(n):
    abc=True
    for i in range(2,n):
     if n % i == 0:
        abc=False
    if abc == True:
        print("number is prime")
    else:
        print("not prime")
num=int(input("Enter number to check prime :"))
prime(num)
# divisors of a number 
x = int(input("Type a number: "))
for i in range(1,int(x)+1):
    #print(i)
    if x % i ==0:
        print(i)
        continue

print("End")

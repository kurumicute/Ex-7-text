n = int(input("使用者輸入一個正整數:"))

sum = 0

for i in range(1,n+1):
 sum +=i

print("從1到{}的和為:{}".format(n,sum))
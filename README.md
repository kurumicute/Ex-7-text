# Python期中報告
11124121 林宜頌
# 期中報告第7題
使用者輸入數字，計算1~n的數字總和
# 程式碼
n = 使用者輸入數字  
```
n = int(input("使用者輸入一個正整數:"))
```

設定sum初始值  
```
sum = 0
```

從i到n+1的數字迴圈，sum= 從i+到n的值  
```
for i in range(1,n+1):
 sum +=i
```

列印從1到n的和為:sum  
```
print("從1到{}的和為:{}".format(n,sum))
```

列印結果  
![img](https://github.com/kurumicute/Ex-7-text/assets/90886946/eb129f9b-722f-4939-a057-7ab1ba96e619)

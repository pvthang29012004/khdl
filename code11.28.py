#nhập ma trận
a=[]
m = (input('nhập số tự nhiên m='))
n = (input('nhập số tự nhiên n='))
for i in range(m):
     print("chuẩn bị nhập ma trận hàng thứ", i+1,":")
     b=[]
     for j in range(n):
        x=int(input("nhập phần tử thứ"+ str(j+1)+":"))
        b=b+[x]
     a.append(b)  
print("ma trận a đã nhập xong") 
#in ma trận a ra màn hình
for i in range(m):
    for j in range(n):
        print(a[i][j], end="")
    print



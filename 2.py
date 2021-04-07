
N = int(input('Enter The Number Of Sets A: '))
print("Enter Collection Member: ")
n = set()
for i in range(N):
    n.add(input())


M = int(input('Enter The Number Of Sets B: '))
print("Enter Collection Member: ")
m = set()
for i in range(M):
    m.add(input())


#اجتماع
print('union : ', m | n)
# اشتراک
print('intersection : ', m.intersection(n))

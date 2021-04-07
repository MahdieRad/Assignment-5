
A = int(input('Enter Number Of Numerical Sequences : '))
x = 0
z = 1
FList = list()

for i in range(A):
    FList.append(x)
    Temp= x + z
    z = x
    x = Temp
Fibonochi= tuple(FList)
print(Fibonochi)

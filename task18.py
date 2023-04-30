# 18.Требуется найти в массиве A[1...N] самый близкий по величине элемент к заданному числу X
# Пользователь  в первой строке вводит натуральное число N -колличество элементов в массиве
# В последующих строках записаны N целых чисел Ai
# Последняя строка содержит число X.

N = int(input('Введите колличество элементов в массиве:'))
f_list = list()
for i in range(N):
    n=int(input())
    f_list.append(n)
X = int(input('Введите искомое число:'))    

f_list2 = []

for item in f_list:
    if item < 0:
        item = item * -1
    f_list2.append(item)

minn = f_list[0] - X 
number = f_list[0]
if minn < 0:
    minn = minn * -1
for i in range(len(f_list)):
    diff =  f_list[i] - X
    if diff < 0:
        diff = diff * -1
    if diff < minn:
        minn = diff
        number = f_list[i]
print(number)

    




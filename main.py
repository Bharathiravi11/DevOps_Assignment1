# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import collections

from numpy import sort
import math

@staticmethod
def draw_border(worksheet, str_format, num_columns, begin_row, num_rows=1):
    end_row = begin_row + num_rows
    for row in range(begin_row, end_row):
        for col in range(num_columns):
            worksheet.write(row, col, '', str_format)


def merge_list():
    list1 = [10, 12, 18, 20]
    list2 = [8, 11, 14, 19]
    merge = list1 + list2
    print(merge)
    print(sort(merge))


def sum_integers():
    x, y = input("Enter two values seperated by a space: ").split()
    x = int(x)
    y = int(y)
    z = int(input("Enter sum: "))
    print(f'SUm entered is correct: {z == x + y}')




def get_sq_num(num):
    sq_num = []
    for i in num:
        sq_num.append(i[0] * i[0] + i[1] * i[1])
    return sq_num


def get_sq_rt(arr):
    sqrt = []
    for i in arr:
        sqrt.append(math.sqrt(i))
    return sqrt


def test(n):
    arr = [[0, 3], [0, 1], [1, 2]]
    if n > len(arr):
        print('pls enter len less than size of input array')
        return
    sqrt_arr = get_sq_rt(get_sq_num(arr))
    print(sqrt_arr)
    mydict = {}
    count = 0
    for i in arr:
        mydict[sqrt_arr[count]] = i
        count = count + 1

    od = collections.OrderedDict(sorted(mydict.items()))
    print(od)
    print(mydict)

    c = 1
    for a, b in od.items():
        if (c <= n):
            print(b)
            c = c + 1


def calc_distance():
    arr = [[0, 1], [1, 2], [3, 2]]
    print(arr[0])
    x = arr[1]
    y = arr[2]
    print(x)
    print(y)
    distance = math.sqrt(((x[0]-y[0])**2)+((x[1]-y[1])**2))
    print(distance)




#test(2)
calc_distance()

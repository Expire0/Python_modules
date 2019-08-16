# Lab on how to capture every 5 values from a list of numbers 

mas= [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 333, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 52]

#index = 0
#count = 0
#kam = lambda x: x + 5

stripe = len(mas) / 10 + 1

#    print(mas[index])
#    while count < 10:
#        print(mas[index])
#        count += 1
#        index = kam(index)


def test(list,c,index):

    #index = 0
    count = 0
    kam = lambda x: x +5
    while count < c:
        print(list[index])
        count += 1
        index = kam(index)


for i in range(0,stripe -1):
    print("stripe " + str(i+1))
    index = i
    test(mas,10,index)

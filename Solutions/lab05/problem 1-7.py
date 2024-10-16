## Problem 1
def count_evens(L):
    count = 0
    for item in L:
        if item % 2 == 0:
            count += 1
    return count

if __name__ == "__main__":
    list = [1, 2, 3]

    print ("Problem 1: ")
    print (count_evens(list))

## Problem 2
def list_to_str(lis):
    output = ""
    for item in lis:
        output = output + str(item)
    return lis

if __name__ == "__main__":
    list = [1, 2, 3]

    print ("Problem 2: ")
    print (list_to_str(list))

## Problem 3
def lists_are_the_same(list1, list2):
    if len(list1) == len(list2):
        for item in range(len(list1)):
            if list1[item] != list2[item]:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    lista = [1, 2, 3]
    listb = [2, 3, 4]
    listc = [2, 3, 4]

    print ("Problem 3: ")
    print (lists_are_the_same(lista, listb))
    print (lists_are_the_same(listb, listc))

## Problem 4
def list1_start_with_list2(list1, list2):
    if len(list1) <= len(list2):
        for item in range(len(list1)):
            if list1[item] != list2[item]:
                return False
    else:
        return False
    return True

if __name__ == "__main__":
    lista = [1, 2, 3, 3, 4, 5]
    listb = [1, 2, 3]
    listc = [3, 4, 5]

    print ("Problem 4: ")
    print (list1_start_with_list2(listb, lista))
    print (list1_start_with_list2(listc, lista))

## Problem 5:
def match_pattern(list1, list2):
    if len(list1) <= len(list2):
        return False

    for i in range(len(list1)):
        if i + len(list2) <= len(list1):
            match_found = True

            for j in range(len(list2)):
                if list1[i + j] != list2[j]:
                    match_found = False
                    break

            if match_found:
                return True
    return False

if __name__ == "__main__":
    lista = [4, 10, 2, 3, 50, 100]
    listb = [2, 3, 50]
    listc = [1, 2, 3, 3, 4, 5]
    listd = [1, 2, 3]

    print ("Problem 5: ")
    print (match_pattern(lista, listb))
    print (match_pattern(listc, listd))
    print (match_pattern(listb, listc))

## Problem 6
def duplicates(list0):
    for item in list0:
        if item != len(list0):
            if list0[item - 1] == list0[item]:
                return True
    else:
        return False
    return False

if __name__ == "__main__":
    lista = [1, 2, 3, 3, 4, 5]
    listb = [1, 2, 3]

    print ("Problem 6: ")
    print (duplicates(lista))
    print (duplicates(listb))

## Problem 7(a)
# def weight_averages(coordinates, time):
#     large = 0
#     small = 0
#     if time - 1 <= 0 or time + 1 >= len(coordinates):
#         small = ("Small Average Failed, too close to edge.")
#     else:
#         small = (coordinates[time - 1] + coordinates[time + 1]) / 0.2
#     if time - 2 <= 0 or time + 2 >= len(coordinates):
#         large = ("Large Average Failed, too close to edge.")
#     else:
#         large = (coordinates[time - 2] + coordinates[time + 2]) / 0.4
#     print (str(small), str(large))
#
# if __name__ == "__main__":
#     lista = [0.5, 0.6, 0.89, 0.96, 1.85, 2.91]
#
#     print ("Problem 7(a): ")
#     print (weight_averages(lista, 3))

## Problem 7(b)
import random
def weight_averages(coordinates, time):
    large = 0
    small = 0
    if time - 1 <= 0 or time + 1 >= len(coordinates):
        small = ("Small Average Failed, too close to edge.")
    else:
        small = (coordinates[time - 1] + coordinates[time + 1]) / 0.2
    if time - 2 <= 0 or time + 2 >= len(coordinates):
        large = ("Large Average Failed, too close to edge.")
    else:
        large = (coordinates[time - 2] + coordinates[time + 2]) / 0.4
    print (str(small), str(large))

def add_noise(coordinates, noisiness):
    noisy_coordinates = []
    for item in coordinates:
        noisy_coordinates.append(item * noisiness * random.random())
    return noisy_coordinates

if __name__ == "__main__":
    lista = [0.5, 0.6, 0.89, 0.96, 1.85, 2.91]

    print ("Problem 7(b): ")
    count = 0.1
    while count <= 1:
        print ("Noisiness Factor: " + str(count))
        print (weight_averages((add_noise(lista, count)), 1))
        print (str(add_noise(lista, count)) + "\n")
        count += 0.1
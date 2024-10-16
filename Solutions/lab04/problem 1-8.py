## Problem 1
# def leibniz_formula(iterations):
#     total = 0
#
#     for item in range(iterations + 1):
#         total = total + (((-1) ** item) / (2 * item + 1))
#     return total * 4  # Multiply by 4 to get pi()
#
# if __name__ == "__main__":
#     print(leibniz_formula(1000))

## Problem 2
# def leibniz_formula(iterations):
#     total = 0
#     iteration_count = 0
#
#     while iteration_count <= iterations:
#         total = total + (((-1) ** iteration_count) / (2 * iteration_count + 1))
#         iteration_count += 1
#     return total * 4  # Multiply by 4 to get pi()
#
# if __name__ == "__main__":
#     print(leibniz_formula(1000))

## Problem 3 1(a)
# def gcd_bad(n, m):
#     for item in range(1, min(n, m) + 1):
#         # print (item)
#         if n % item == 0 and m % item == 0:
#             max_gcd = item
#     return max_gcd
#
# if __name__ == "__main__":
#     print ("GCD of 12 and 15: ")
#     print (gcd_bad(12, 15))
#
#     print ("GCD of 100 and 25:")
#     print (gcd_bad(100, 25))

## Problem 3 1(b)
# def gcd_okay(n, m):
#     max_gcd = 1
#
#     for item in range(min(n, m), 1, -1):
#         if n % item == 0 and m % item == 0:
#             max_gcd = item
#             # print (max_gcd)
#     return max_gcd
#
# if __name__ == "__main__":
#     print ("GCD of 12 and 15: ")
#     print (gcd_okay(12, 15))
#
#     print ("GCD of 100 and 25:")
#     print (gcd_okay(100, 25))

# def gcd_best(n, m):
#     max_gcd = 1
#
#     for item in range(1, min(n, m) + 1):
#         if n % item == 0 and m % item == 0:
#             max_gcd = item
#             # print (max_gcd)
#     return max_gcd
#
# if __name__ == "__main__":
#     print ("GCD of 12 and 15: ")
#     print (gcd_best(12, 15))
#
#     print ("GCD of 100 and 25:")
#     print (gcd_best(100, 25))

## Problem 4
def gcd(n, m):
    max_gcd = 1

    for item in range(1, min(n, m) + 1):
        if n % item == 0 and m % item == 0:
            max_gcd = item
    return max_gcd

def simplify_fraction(n , m):
    max_gcd = gcd(n, m)

    n /= max_gcd
    m /= max_gcd

    if n == 0:
        print (0)
    elif m != 1:
        print (str(int(n)) + "/" + (str(int(m))))
    else:
        print (str(int(n)))

if __name__ == "__main__":
    simplify_fraction(3, 6)
    simplify_fraction(8, 4)
    simplify_fraction(0, 4)

## Problem 5
# final_name = ""
# name_input = ""
# second_name = ""
#
# name_input = input("Enter a name: ")
# final_name = final_name + name_input
#
# while name_input != "END":
#     name_input = input("Enter a name: ")
#     if name_input != "END":
#         final_name = final_name + ", " + name_input
#
# print ("The names are: " + final_name)

## Problem 6
# import math
#
# def leibniz_formula(iterations):
#     total = 0
#     iteration_count = 0
#
#     while iteration_count <= iterations:
#         total = total + (((-1) ** iteration_count) / (2 * iteration_count + 1))
#         iteration_count += 1
#     return total * 4  # Multiply by 4 to get pi()
#
# def agree_to_n(n):
#     found_flag = False
#     iterations = 1
#
#     while found_flag != True:
#         if round((leibniz_formula(iterations)) * (10 ** n)) == round(math.pi * (10 ** n)):
#             # print ((leibniz_formula(iterations)))
#             # print (round(math.pi * (10 ** n)))
#             found_flag = True
#             return iterations
#         else:
#             iterations += 1
#             # if iterations % 100 == 0:
#             #     print (iterations)
#     return False
#
# if __name__ == "__main__":
#     print (agree_to_n(4))

## Problem 7 (Advanced)

## Problem 8 (Advanced)
# # We have to use recursive function here such that we keep using gcd() again and again until a final end case is reached.
#
# def euclid_main(n1, m1):
#     global n
#     global m
#     n = n1
#     m = m1
#
#     temp_value1 = -1
#     while gcd_eulicds(n, m):
#         pass
#
# def gcd_euclids(n1, m1):
#     global n
#     global m
#     n = n1
#     m = m1
#
#     if temp_value != 0:
#         if n1 >= m1:
#             temp_value1 = n % m
#             m = temp_value1
#         else:
#             temp_value1 = n % m
#             m = temp_value1
#         return True
#     else:
#         return False
#
# euclid_main(12, 15)
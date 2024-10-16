## Question 1

## Question 1(A)
# Nothing is input onto the screen as res is not printed or output to the screen, only the main values change.

## Question 1(B)
# def my_sqrt(x):
#     sqr = x**.5
#     return sqr
#
# if __name__ == "__main__":
#     res = my_sqrt(25)
#     print (sqr)
#
# An error is produced as a local variable that is constrianed to the function my_sqrt() has been called globally, this variable does not exist globally and thus it produces an eror.
#
# We can modify it by writing the code global sqr inside the function:
# def my_sqrt(x):
#     global sqr
#     sqr = x**.5
#     return sqr
#
# if __name__ == "__main__":
#     res = my_sqrt(25)
#     print (sqr)

##  Question 1(C)
def my_print_square(x):
    print (x**2)

if __name__ == "__main__":
    res = my_print_square(25)
    print(res)
#
# The output is "None" as the function my_print_square() does not return anything and so a Null pointer in memory is returned.
#
# my_print_square() returns the square of the value input, and my_sqrt() returns the square root of the variable input.

## Question 2
# Completed.
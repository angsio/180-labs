# # Question 1
# # Completed.
#
# # Question 2
# userInput = str(input("Enter your course: "))
# userInput = userInput.lower()
#
# if userInput == "praxis":
#     print ("Carrick")
# elif userInput == "civ":
#     print ("Bentz")
#
# # Question 3
# def greet_instructor(course, greeting):
#     if (greeting == "hello, prof.") and (course == "praxis"):
#         print (greeting+"Carrick")
#     elif (greeting == "hi, prof.") and (course == "civ"):
#         print (greeting+"BLentz")
#     else:
#         print ("Invalid Inputs.")
#
# if __name__ == "__main__":
#     userGreeting = str(input("Enter your greeting: "))
#     userCourse = str(input("Enter your course: "))
#     userGreeting = userGreeting.lower()
#     userCourse = userCourse.lower()
#
#     print(greet_instructor(userCourse, userGreeting))
#
# # Question 4
# # Completed.
#
# # Question 5
# # Completed.
#
# # Quesiton 6
# print ("Hello, Lucas Joshua Payant")
# print ("Hello, Ayan Ali")
#
# name1 = "Lucas Joshua Payant"
# name2 = "Ayan Ali"
#
# print ("Hello",name1,"and",name2+". Your names are",name1,"and",name2+". Hi there. Your are still",name1,"and",name2+".")
#
# # Question 7
# name1 = "Prof. Carrick"
# name2 = "Prof. Bentz"

# Question 8
greetee = str(input("Enter a name: "))
if greetee != "Lord Voldemort":
    print ("Hello",greetee+"!")
else:
    print ("I'm not talking to you.")

## Question 3
# outputvalue = 0
#
# if __name__ == "__main__":
#     print ("Welcome to the calculator program.")
#     print ("Current value", outputValue+".")

## Question 4
# # User-Defined Functions
# def display_current_value():
#     global outputValue
#     print ("Current value", str(outputValue)+".")
#
# # Variable Definitions
# outputValue = 0
#
# # Main Program
# if __name__ == "__main__":
#     print ("Welcome to the calculator program.")
#     display_current_value()

## Question 5
# # User-Defined Functions
# def display_current_value():
#     global outputValue
#     print ("Current value", str(outputValue)+".")
#
# def add(to_add):
#     global outputValue
#     outputValue = outputValue + to_add
#
# # Variable Definitions
# outputValue = 0
#
# # Main Program
# if __name__ == "__main__":
#     print ("Welcome to the calculator program.")
#     add(5)
#     display_current_value()

## Question 6 & 7 & 8 & 9
# User-Defined Functions
def display_current_value():
    global outputValue
    print ("Current value", str(outputValue)+".")

def add(to_add):
    global outputValue
    global functionArray
    outputValue = outputValue + to_add
    functionArray.append("A"+str(to_add))

def mult(to_mult):
    global outputValue
    global functionArray
    outputValue = outputValue * to_mult
    functionArray.append("M"+str(to_mult))

def div(to_div):
    global outputValue
    global functionArray
    outputValue = outputValue / to_div
    functionArray.append("D"+str(to_div))

def toMemory():
    global memoryValue
    memoryValue = outputValue

def callMemory():
    return memoryValue

def undo():
    global outputValue
    if not functionArray:
        print("No more undo actions.")
        return

    item = functionArray.pop()
    if item[0] == "A":
        outputValue = outputValue - int(item[1:])
    elif item[0] == "M":
        outputValue = outputValue / int(item[1:])
    elif item[0] == "D":
        outputValue = outputValue * int(item[1:])

def undoProper():
    global outputValue
    memoryValue = outputvalue
    restore()
    memory()

# Variable Definitions
outputValue = 25
memoryValue = 0
functionArray = []

# Main Program
if __name__ == "__main__":
    print ("Welcome to the calculator program.")
    display_current_value()
    add(5)
    display_current_value()
    add(-2)
    display_current_value()
    mult(2)
    display_current_value()
    div(3)
    display_current_value()
    add(5)
    display_current_value()
    mult(2)
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
    undo()
    display_current_value()
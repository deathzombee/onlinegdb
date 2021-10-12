# <Decisions and Comparisons with If Statements>

# Copyright © <2021> <Captain_dz>

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
# Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
# COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# 1). Create an input statement that asks the user to enter an integer number
# and store the number in a variable named operand1
operand1 = input("Please input a number ,positive or negative, but without fractions or decimals \nthis will be the "
                 "first number of your operation: ")
print(operand1)
# 2).  Do the same again and store the second number in operand2
operand2 = input("Please input a number ,positive or negative, but without fractions or decimals \nthis will be the "
                 "second number of your operation: ")
print(operand2)
# 3).  Create another input prompt that asks the user for the type of math problem, (+,-,*,/ are possible answers) naming the variable 'operation'
operation = input("this script evaluates basic math operations \n"
                 "options are +,-,*, or / : ")
print(operation)
# 4). Create another prompt that displays the math problem entered above in the form of '2 + 4 = ' by concatenating the input collected above.  Collect the user's answer into a variable.
answer = input(operand1 + operation + operand2 + '= ')
# 5). Test the operation variable using if...elif  statements to decide which operation to perform.
if operation == "+":
    eval = int(operand1) + int(operand2)

    if int(answer) == inst(eval):

        print("correct the answer is " + str(int(eval)))
    else:
        print("wrong")
elif operation == "-":
    eval = int(operand1) - int(operand2)

    if int(answer) == int(eval):

        print("correct the answer is " + str(int(eval)))
    else:
        print("wrong")
elif operation == "*":
    eval = int(operand1) * int(operand2)

    if int(answer) == int(eval):

        print("correct the answer is " + str(int(eval)))
    else:
        print("wrong")
elif operation == "/":
    eval = int(operand1) / int(operand2)

    if int(answer) == int(eval):

        print("correct the answer is " + str(int(eval)))
    else:
        print("wrong")
else:
    print("error")
# 6). In each if outcome perform the correct calculation for that operator type and store the answer into a variable called 'correctAnswer'

# 7). Test to see if the user's answer variable is the same '==' as the correct answer variable your program calculated and either print that they are correct or incorrect.

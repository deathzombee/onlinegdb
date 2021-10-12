# Name:
# Contact:
# Date:
# Purpose:
# Licence:
# <Introduction to Lists>

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

# 1). Instantiate (create in a code command) a list variable named myNumbers and initialize the list to the integers
# from 1 through 10
myNumbers = [*range(1,11)]
print(myNumbers)
# 2). Create a variable named total and create and initialize the variable to the sum of all values stored in the
# list above using a formula that adds each value in the list into the new variable
total = 0
for x in myNumbers:
    total += x
# 3). Print on a single line the contents of the list with each element separated by a comma and a tab
for x in myNumbers:
    print(x, end=',\t')
# 4). Remove the element from the list containing the value of 5.
myNumbers.remove(5)
# 5). Remove the element at position 4 (4th item) in the list.
myNumbers.pop(3)
# 6). Add the value 5 back to the end of the list
myNumbers.append(5)
# 7). Insert the value 12 at position 5 in the list
myNumbers.insert(12,4)
# 8).  Print the entire content of the list using just the name of the list
print(myNumbers)
# 9).  Print the list sorted.
myNumbers.sort()
print(myNumbers)
# 10). Pop the last three elements off the end of the list, storing each in a temporary variable, printing the
# variable and then popping the next value (pop, store, print, repeat 3
i=1
for x in range(1,4):

    num = len(myNumbers)-i
    #print(num)
    a = myNumbers.pop(num)
    print(a)

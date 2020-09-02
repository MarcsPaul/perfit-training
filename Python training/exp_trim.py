# program  to print the value of 'e' till the specified
import math

num = input("Enter the limit upto which the value should be printed after the decimal point")
e_value = math.e
formatter = "{:."+num+"f}"
txt = "the output is "+formatter
print(txt.format(e_value))

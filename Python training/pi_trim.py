# program  to print the value of 'pi' till the specified
import math

num = input("Enter the limit upto which the value should be printed after the decimal point")
pi_value = math.pi
formatter = "{:."+num+"f}"
txt = "the output is "+formatter
print(txt.format(pi_value))

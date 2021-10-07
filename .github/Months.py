# Programmer: [Will Grimmer]
# Course: CS701/GB-731, Dr. Rajeev
# Date: [10/6/2021]
# Programming Assignment: 2
# Program Inputs: [Month and Year]
# Program Outputs: [Days in the given month]

months = [31,28,31,30,31,30,31,31,30,31,30,31]
month=int(input("please give a number representative of a month from 1-12"))
year=int(input("please input a year"))
c=0
if month > 12 or month < 1:
    print("you did not give a month from 1-12 please try again")
else:
    if month == 2:
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    c = 1
            else:
                c = 1
    output=months[month-12]+c
    print("there are %d days in the month" %output)
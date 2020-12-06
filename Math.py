# Menu's
print("1. Multiplication Table")
print("2. Greatest Common Divisor (GCD)")
print("3. Least Common Multiple (LCM)")
print("4. Factors of a Number ")
print("5. Find Sum of Digits of a Number ")
print("6. Count Number of Digits in an Integer ")
print("-------------------------------")

# input item number from user
items = (input("Select Item : "))

# condition
if items == '1':
    print("Multiplication Table")
    inputNumber = int(input("Enter the Number : "))
    result = 1
    print(f"Multiplication Table of {inputNumber} :\n")
    for i in range(1, 10 + 1, 1):
        # multiply  user input number with index of i
        result = inputNumber * i
        # printing multiplication table
        print(f"{inputNumber} X {i} = {int(result)} ")
# Finding Greatest Common Divisor (GCD)
elif items == '2':
    num_1 = int(input("Enter the First Number : "))
    num_2 = int(input("Enter the Second Number : "))
    n1 = num_1
    n2 = num_2
    while n2 != 0:
        remainder = n1 % n2
        n1 = n2
        n2 = remainder
    print(f"The Greatest Common Divisor is between {num_1} and {num_2} = {int(n1)} ")
# The Latest Common Multiply

elif items == '3':
    lcm_num1 = int(input("Enter the First Number :"))
    lcm_num2 = int(input("Enter the First Number :"))
    lcm_n1 = lcm_num1
    lcm_n2 = lcm_num2

    while lcm_n2 != 0:
        lcm_remainder = lcm_n1 % lcm_n2
        lcm_n1 = lcm_n2
        lcm_n2 = lcm_remainder
    lcm_gcd = lcm_n1
    lcm = lcm_num1 * lcm_num2 // lcm_gcd
    print(f"The Latest Common Multiply between {lcm_num1} and {lcm_num2} is = {int(lcm)}")
# Program to find factors of any number
elif items == '4':
    factors = int(input("Enter the Number : "))
    print(f"All Factors of  {factors} are : ")
    for x in range(1,factors+1,1):
        if factors % x == 0:
            print(x)
# Logic to find sum of digits of a number
elif items == '5':
    sum_digit = int(input("Enter the Numbers : "))
    temp = sum_digit
    sum_number = 0
    while temp != 0:
        temp_remainder = temp % 10
        sum_number = sum_number + temp_remainder
        temp = temp // 10
    print(f"Sum of the {sum_digit} is : {sum_number}")

#  count number of digits in an integer
elif items == '6':
    integer_digit = int(input("Enter the digits : "))
    count = 0
    temp = integer_digit
    while temp != 0:
        count += 1
        temp = temp // 10


    print(int(count))
















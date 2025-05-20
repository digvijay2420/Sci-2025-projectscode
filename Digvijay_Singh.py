#1
num=int(input("enter a num:"))
if num>0:
  print(num,"is positive")
else:
  print(num,"is negative")

#2
a=int(input('Enter a number:'))
if a%2==0:
  print(a,"is an even number")
else:
  print(a,"is an odd number")

#3
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")

#4
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
if a>b:
  print(a,"is greater than",b)
else:
  print(b,"is greater than",a)

#5
a=int(input('Enter a number:'))
b=int(input('Enter a number:'))
c=int(input('Enter a number:'))

if a>b and a>c:
  print(a,"is greater than",b,"and",c)
elif b>a and b>c:
  print(b,"is greater than",a,"and",c)
else:
  print(c,"is greater than",a,"and",b)

#6

char = input("Enter a single character: ").lower()

# Check if input is a single alphabetic character
if len(char) != 1 or not char.isalpha():
    print("Invalid input: Please provide a single letter")
else:
    # Check for vowel
    vowels = 'aeiou'
    if char in vowels:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is a consonant")

#7
# Get input from user
number = int(input("Enter a number: "))

# Check divisibility by 5 and 11
if number % 5 == 0 :
  print(number,"is divisible by 5")
elif number% 11==0:
  print(number,"is divisible by 11")
else:
  print(number,"is not divisible by 5 and 11")

#8

number=int(input("N=Enter the number:"))

if number%3==0 and number%7==0:
  print(f"{number} is divisible by both 3 and 7")
else:
  print(f"{number} is not divisible by both 3 and 7")

#9

char=input("ENter a character:")

if char.islower():
  print(char,"is a lowercase chaarcter")
elif char.isupper():
  print(char,"is a uppercase chaarcter")
else:
  print(char,"is not a chaarcter")

#10

# Get input from user
number = int(input("Enter a number: "))

# Check if the number is a perfect square
sqrt = int(number ** 0.5)  # Integer part of square root
if sqrt * sqrt == number:
    print(f"{number} is a perfect square")
else:
    print(f"{number} is not a perfect square")

#11

number = input("Enter a number: ")


if number == number[::-1]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")

#12


number = input("Enter a number: ")

# Calculate the number of digits
num_digits = len(number)

# Calculate sum of each digit raised to the power of num_digits
sum_powers = sum(int(digit) ** num_digits for digit in number)

# Check if the number equals the sum of powers
if int(number) == sum_powers:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")

#13

num=int(input("Enter a number:"))

if num<2:
  print(num,"is niot a prime number")
else:
  is_prime=True
  for i in range(2,int(num**0.5+1)):
    if num%i==0:
      is_prime=False
      break
  if is_prime:
    print(num,"is a prime number")
  else:
    print(num,"is not a prime number")

#14


a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))


if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (b + c > a) and (c + a > b):
        print(f"A triangle with sides {a}, {b}, {c} is valid")
    else:
        print(f"A triangle with sides {a}, {b}, {c} is not valid")
else:
    print(f"A triangle with sides {a}, {b}, {c} is not valid (sides must be positive)")

#15

a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))
c = float(input("Enter the third side: "))


if a > 0 and b > 0 and c > 0:
    if (a + b > c) and (b + c > a) and (c + a > b):
        
        if a == b == c:
            print(f"A triangle with sides {a}, {b}, {c} is equilateral")
        elif a == b or b == c or c == a:
            print(f"A triangle with sides {a}, {b}, {c} is isosceles")
        else:
            print(f"A triangle with sides {a}, {b}, {c} is scalene")
    else:
        print(f"A triangle with sides {a}, {b}, {c} is not valid (fails triangle inequality)")
else:
    print(f"A triangle with sides {a}, {b}, {c} is not valid (sides must be positive)")

#16

char=input("Enter a character:")

if char.isalpha():
  print(char,"is a alphabet")
else:
  print(char,"is not a alphabet")

#17


percentage = float(input("Enter percentage marks (0-100): "))


if 0 <= percentage <= 100:
    # Determine grade based on percentage
    if percentage >= 90:
        grade = "A+ (Outstanding)"
    elif percentage >= 80:
        grade = "A (Excellent)"
    elif percentage >= 70:
        grade = "B (Good)"
    elif percentage >= 60:
        grade = "C (Satisfactory)"
    elif percentage >= 50:
        grade = "D (Pass)"
    else:
        grade = "F (Fail)"
    
    print(f"Percentage: {percentage}% - Grade: {grade}")
else:
    print("Invalid percentage! Please enter a value between 0 and 100.")

#18

age=int(input("Enter the age of person:"))

if age > 18:
  print("Person is eligible to vote")
else:
  print("Person is not eligible to vote")

#19


age = int(input("Enter your age: "))
country = input("Enter your country (e.g., India, US, UK, or others): ").strip().lower()


if country == "india":
    if age >= 18:
        print("You are eligible to apply for a permanent driving license for private vehicles in India.")
    elif age >= 16:
        print("You are eligible to apply for a learner's license for vehicles up to 50cc in India.")
    else:
        print("You are not eligible for a driving license in India (minimum age is 16 for learner's license or 18 for permanent license).")
elif country == "us":
    if age >= 18:
        print("You are eligible for a full driver's license in most US states.")
    elif age >= 16:
        print("You are eligible for a learner's permit in most US states.")
    else:
        print("You are not eligible for a driver's license in the US (minimum age is typically 16 for a learner's permit).")
elif country == "uk":
    if age >= 17:
        print("You are eligible to apply for a driving license for cars in the UK.")
    elif age >= 16:
        print("You are eligible to apply for a driving license for mopeds in the UK.")
    else:
        print("You are not eligible for a driving license in the UK (minimum age is 16 for mopeds or 17 for cars).")
else:
    
    if age >= 18:
        print(f"You are likely eligible for a driving license in {country.capitalize()} (assuming minimum age of 18), but check local regulations.")
    else:
        print(f"You may not be eligible for a driving license in {country.capitalize()} (common minimum age is 18). Please check local regulations.")

#20

x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))


if x == 0 and y == 0:
    print(f"The point ({x}, {y}) is at the origin")
elif x == 0:
    print(f"The point ({x}, {y}) lies on the y-axis")
elif y == 0:
    print(f"The point ({x}, {y}) lies on the x-axis")
elif x > 0 and y > 0:
    print(f"The point ({x}, {y}) lies in Quadrant I")
elif x < 0 and y > 0:
    print(f"The point ({x}, {y}) lies in Quadrant II")
elif x < 0 and y < 0:
    print(f"The point ({x}, {y}) lies in Quadrant III")
else:  # x > 0 and y < 0
    print(f"The point ({x}, {y}) lies in Quadrant IV")

#21


year = int(input("Enter a year: "))


if year % 100 == 0:
    print(f"{year} is a century year")
else:
    print(f"{year} is not a century year")

#22

unit = input("Enter temperature unit (C for Celsius, F for Fahrenheit): ").strip().upper()
temperature = float(input(f"Enter temperature in {unit}: "))

# Determine temperature category based on unit
if unit == "C":
    if temperature > 30:
        print(f"{temperature}°C is hot")
    elif 15 <= temperature <= 30:
        print(f"{temperature}°C is moderate")
    else:
        print(f"{temperature}°C is cold")
elif unit == "F":
    if temperature > 86:
        print(f"{temperature}°F is hot")
    elif 59 <= temperature <= 86:
        print(f"{temperature}°F is moderate")
    else:
        print(f"{temperature}°F is cold")
else:
    print("Invalid unit! Please enter 'C' for Celsius or 'F' for Fahrenheit.")

#23

number = float(input("Enter a number: "))


if number < 0:
    absolute_value = -number
else:
    absolute_value = number


print(f"The absolute value of {number} is {absolute_value}")

#24

unit = input("Enter height unit (cm or ft): ").strip().lower()
gender = input("Enter gender (male, female): ").strip().lower()

if unit == "cm":
    height = float(input("Enter height in cm: "))
elif unit == "ft":
    feet = int(input("Enter feet: "))
    inches = float(input("Enter inches: "))
    height = (feet * 30.48) + (inches * 2.54)  # Convert to cm
else:
    print("Invalid unit! Please enter 'cm' or 'ft'.")
    exit()


if gender == "male":
    if height > 175:
        category = "tall"
    elif 160 <= height <= 175:
        category = "average"
    else:
        category = "short"
elif gender == "female":
    if height > 162:
        category = "tall"
    elif 147 <= height <= 162:
        category = "average"
    else:
        category = "short"



print(f"A height of {height:.1f} cm is considered {category} for {gender}.")


#25

a=int(input("Enter the number:"))
b=int(input("Enter the number:"))
c=int(input("Enter the number:"))

if a<b and a<c:
  print("a is smallest")
elif b<a and b<c:
  print("b is smallest")
else:
  print("c is smallest")

#26

number = float(input("Enter the number: "))
min_value = float(input("Enter the minimum value of the range: "))
max_value = float(input("Enter the maximum value of the range: "))

if min_value <= number <= max_value:
    print(f"{number} is within the range [{min_value}, {max_value}]")
else:
    print(f"{number} is not within the range [{min_value}, {max_value}]")

#27


day = int(input("Enter a day number (1-7, where 1 is Monday and 7 is Sunday): "))


if 1 <= day <= 7:
    # Determine if it's a weekday or weekend
    if 1 <= day <= 5:
        print(f"Day {day} (Monday to Friday) is a weekday")
    else:  
        print(f"Day {day} (Saturday or Sunday) is a weekend")
else:
    print("Invalid day number! Please enter a number between 1 and 7.")

#28


number = float(input("Enter a number: "))


num = abs(int(number))


if num < 10:
    digit_count = 1
elif num < 100:
    digit_count = 2
else:
    digit_count = len(str(num))  # For 3 or more digits


if digit_count == 1:
    print(f"{number} is a single-digit number")
elif digit_count == 2:
    print(f"{number} is a two-digit number")
else:
    print(f"{number} has {digit_count} digits")

#29

usage = float(input("Enter monthly electricity usage (in kWh): "))


bill = 0
fixed_charge = 50  # Fixed monthly charge in ₹
tax_rate = 0.05    # 5% electricity duty


if usage < 0:
    print("Invalid usage! Usage cannot be negative.")
else:
    # Calculate bill based on slab rates (₹/kWh)
    if usage <= 100:
        bill = usage * 4  # ₹4 per kWh for 0–100 kWh
    elif usage <= 200:
        bill = (100 * 4) + ((usage - 100) * 5)  # ₹4 for first 100, ₹5 for next 100
    elif usage <= 500:
        bill = (100 * 4) + (100 * 5) + ((usage - 200) * 6)  # ₹4 for 0–100, ₹5 for 101–200, ₹6 for 201–500
    else:
        bill = (100 * 4) + (100 * 5) + (300 * 6) + ((usage - 500) * 7)  # ₹4 for 0–100, ₹5 for 101–200, ₹6 for 201–500, ₹7 for >500
    
    # Add fixed charge
    bill += fixed_charge
    
    # Add tax
    tax = bill * tax_rate
    total_bill = bill + tax
    
    # Print result
    print(f"Electricity Bill for {usage} kWh:")
    print(f"Base Charge: ₹{bill:.2f}")
    print(f"Tax (5%): ₹{tax:.2f}")
    print(f"Total Bill: ₹{total_bill:.2f}")

#30
password = input("Enter a password: ")

is_strong = (len(password) >= 8 and
             any(c.isupper() for c in password) and
             any(c.islower() for c in password) and
             any(c.isdigit() for c in password) and
             any(c in "!@#$%^&*" for c in password) and
             " " not in password)

print("Strong password" if is_strong else "Weak password")

#31

year = int(input("Enter a year: "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


#32

number = int(input("Enter a number: "))


if number % 2 == 0:
    if number % 4 == 0:
        print(f"{number} is even and divisible by 4")
    else:
        print(f"{number} is even but not divisible by 4")
else:
    print(f"{number} is not even (and thus not divisible by 4)")

#33
marks=int(input('Enter the marks out of 100: '))

if marks>= 33:
  print("Student is passed")
else:
  print("Student is failed")


#34

number = int(input("Enter a number: "))
digit = int(input("Enter the digit to check (0-9): "))


if 0 <= digit <= 9:
    
    last_digit = abs(number) % 10
    
    
    if last_digit == digit:
        print(f"{number} ends with the digit {digit}")
    else:
        print(f"{number} does not end with the digit {digit}")
else:
    print("Invalid digit! Please enter a digit between 0 and 9.")

#35

month = int(input("Enter a month number (1-12): "))
year = int(input("Enter a year (for February's leap year check): "))


if 1 <= month <= 12:
    
    if month in [4, 6, 9, 11]:
        print(f"Month {month} has 30 days")
    elif month == 2:
        # Check if it's a leap year
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print(f"Month {month} (February) has 29 days (leap year)")
                else:
                    print(f"Month {month} (February) has 28 days")
            else:
                print(f"Month {month} (February) has 29 days (leap year)")
        else:
            print(f"Month {month} (February) has 28 days")
    else:  
        print(f"Month {month} has 31 days")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")

#36

string1 = input("Enter first string: ")
string2 = input("Enter second string: ")


if string1 == string2:
    print("Strings are equal")
else:
    print("Strings are not equal")

#37
str1=input("Enter the string")
if str1=="":
  print("String is empty")
else:
  print("String is not empty")

#38

char = input("Enter a character: ")

# Check if the input is a single character
if len(char) == 1:
    
    if char.isdigit():
        print(f"'{char}' is a digit")
    else:
        print(f"'{char}' is not a digit")
else:
    print("Please enter a single character")

#39
n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
sum = n1+n2

if sum%2==0:
  print("Sum of two nos is even")
else:
  print("Sum of two nos is odd")

#40
value = input("Enter a value: ")

if value.isdigit() or (value.startswith('-') and value[1:].isdigit()):
    print("It is an integer.")
else:
    print("It is not an integer.")



#41
str1,str2=input(),input()
if len(str1)==len(str2):
  print("Strings are of same length")
else:
  print("Strings are not of same length")''

#42
number = input("Enter a number: ")

if number.isdigit() :
    num_str = number.lstrip('-')  # Remove negative sign if present
    if num_str[0] == num_str[-1]:
        print("First and last digits are the same.")
    else:
        print("First and last digits are different.")
else:
    print("Invalid input. Please enter an integer.")


#43
n = int(input("Enter a number: "))

a, b = 0, 1
is_fib = False

while b <= n:
    if b == n:
        is_fib = True
        break
    a, b = b, a + b

if is_fib or n == 0:
    print("It is a Fibonacci number.")
else:
    print("It is not a Fibonacci number.")


#44
hour = int(input("Enter hour (0-23): "))

if 0 <= hour < 12:
    print("AM")
elif 12 <= hour < 24:
    print("PM")
else:
    print("Invalid hour")


#45
month = int(input("Enter month number (1-12): "))

if 3 <= month <= 5:
    print("Spring")
elif 6 <= month <= 8:
    print("Summer")
elif 9 <= month <= 11:
    print("Autumn")
elif month == 12 or month == 1 or month == 2:
    print("Winter")
else:
    print("Invalid month")


#46

angle = float(input("Enter the angle in degrees: "))

if 0 < angle < 90:
    print("Acute angle")
elif angle == 90:
    print("Right angle")
elif 90 < angle < 180:
    print("Obtuse angle")
else:
    print("Invalid angle")

#47
n = int(input("Enter a number: "))

if n > 0 and (n & (n - 1)) == 0:
    print("It is a power of 2.")
else:
    print("It is not a power of 2.")


#48
char = input("Enter a single character: ")

if len(char) == 1:
    if not char.isalnum():
        print("It is a special symbol.")
    else:
        print("It is not a special symbol.")
else:
    print("Please enter exactly one character.")

#49
marks = float(input("Enter your marks (0-100): "))
income = float(input("Enter your family income (in USD): "))

# Example criteria:
# Marks must be at least 85
# Income must be less than or equal to 50000

if marks >= 85 and income <= 50000:
    print("Eligible for scholarship.")
else:
    print("Not eligible for scholarship.")

#50
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Sum of any two numbers is greater than the third.")
else:
    print("Condition not met.")

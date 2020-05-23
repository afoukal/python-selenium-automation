# 12. Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.
bill = int(input("What is the total?"))
count_men= int(input("how many people?"))
share = bill/count_men
print(f'Each person should pay {share}')

# 13 .Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
days = int(input("Tell me number if days?"))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(f' In {days} days there are {hours} hours, {minutes} minutes, {seconds} seconds')

# 14. Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
number_100 = int(input("Tell me any number over 100?"))
number_10 = int(input("Tell me any number less then 10?"))
result = round(number_100/number_10)
print(f'{number_10} goes {result} times into {number_100}')

# 15. Ask the integer number and return the second power of this number.
number_1 = int(input("Tell me any number?"))
print(number_1**2)

# 16. Ask the integer number and power what you would like to get. Return result
number_2 = int(input("Tell me any number"))
power_2 = int(input("Tell me any power for this number?"))
print(number_2 ** power_2)

# 17. Ask the user to enter their first name and then display the length of their name.
user_name = input("What is your name?")
print(len(user_name))

# 18. Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of the whole name.
first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
con_cat = first_name + ' ' + last_name
print(f'Your full name is {con_cat}. The length of your full name is {len(con_cat)}')

# 19. Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.
low_name = input("Type your name in lower case ")
low_lastname = input("Type your last name in lower case")
print( f'Your full name is {low_name.capitalize()} {low_lastname.capitalize()}')

# 20. Enter a random string, which includes only digits. Write a function sum_digits which will find a sum of digits in this string
string_1 = "123456789"
result_str = 0
for item in  string_1:
    result_str += int(item)
print(result_str)

# 21. Ask the user to enter their favorite color. If they enter “red”, “RED” or “Red” display the message “I like red too”, otherwise display the message “I don’t like [color], I prefer red”.
str_color = input("Tell me your favorit color? ")
if str_color.casefold() == 'red' :
    print("I like red too")
else:
    print(f'I do not like {str_color}. I like red.')

# 22. Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are under 16, display the message “You can go Trickor-Treating”.
num_age=int(input("Tell me your age? "))
if num_age >= 18 :
    print("You can vote")
elif num_age >= 17 :
    print("You can learn to drive")
elif num_age >= 16 :
    print("You can buy lottery ticket")
else:
    print("You can go trick or treating")

# 23. Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is between 10 and 20, display “Correct”, otherwise display “Too high”.
int_number = int(input("Tell me any number "))
if int_number > 20 :
    print("Too high")
elif 10 <= int_number <= 20 :
    print("Correct")
else:
    print("Too low")

# 24. Ask the user to enter 1, 2, or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.
int_123 = int(input("Tell me 1,2 or 3 "))
if int_123 == 1 :
    print("Thank you")
elif int_123 == 2 :
    print("Well done")
elif int_123 == 3 :
    print("Correct")
else:
    print("Error message")
# 12. Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay.
# bill = int(input("What is the total?"))
# count_men= int(input("how many people?"))
# share = bill/count_men
# print(f'Each person should pay {share}')

# 13 .Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of days.
# days = int(input("Tell me number if days?"))
# hours = days * 24
# minutes = hours * 60
# seconds = minutes * 60
# print(f' In {days} days there are {hours} hours, {minutes} minutes, {seconds} seconds')

# 14. Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number goes into the larger number in a user-friendly format.
# number_100 = int(input("Tell me any number over 100?"))
# number_10 = int(input("Tell me any number less then 10?"))
# result = round(number_100/number_10)
# print(f'{number_10} goes {result} times into {number_100}')

# 15. Ask the integer number and return the second power of this number.
# number_1 = int(input("Tell me any number?"))
# print(number_1**2)

# 16. Ask the integer number and power what you would like to get. Return result
# number_2 = int(input("Tell me any number"))
# power_2 = int(input("Tell me any power for this number?"))
# print(number_2 ** power_2)

# 17. Ask the user to enter their first name and then display the length of their name.
# user_name = input("What is your name?")
# print(len(user_name))

# 18. Ask the user to enter their first name and then ask them to enter their surname. Join them together with a space between and display the name and the length of the whole name.
# first_name = input("What is your first name?")
# last_name = input("What is your last name?")
# con_cat = first_name + ' ' + last_name
# print(f'Your full name is {con_cat}. The length of your full name is {len(con_cat)}')

# 19. Ask the user to enter their first name and surname in lower case. Change the case to title case and join them together. Display the finished result.
# low_name = input("Type your name in lower case")
# low_lastname = input("Type your last name in lower case")
# print( f'Your full name is {low_name.capitalize()} {low_lastname.capitalize()}')

# 20. Enter a random string, which includes only digits. Write a function sum_digits which will find a sum of digits in this string
string_1 = "123456789"
result_str = 0
for item in int(string_1):
    result_str += item
print(result_str)


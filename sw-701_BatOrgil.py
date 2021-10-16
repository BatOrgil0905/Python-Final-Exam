print("----First Question----")
# Question 1 Write menu driven program to add an delete data in SQL file
# Read it first the first question requires SQL file but i couldn't install and import SQL file so i did this simple
# file instead

value = []
while True:
    print("\n-Menu Driven Program-")
    print("\n'1' is for insert data ")
    print("'2' is for delete data ")
    print("'3' is for Exit ")
    user = int(input("\nEnter your number :> "))
    if user == 1:
        data = input("Enter the data :> ")
        value.append(data)

    elif user == 2:
        if not value:
            print("\n(Please insert a data first)")
        else:
            value.pop()

    else:
        break
    print("The added data(s) = ", value)

print("----Second Question----")
# Question 2 Write and Display 14 days weather schedule according to the website

print("Please wait few second until it's shown the graphic")

import matplotlib.pyplot as plt

Date1 = ['7.19', '7.20', '7.21', '7.22', '7.23', '7.24', '7.25', '7.26', '7.27', '7.28', '7.29', '7.30', '7.31', '8.1']
Temperature1 = [25, 23, 20, 24, 24, 21, 24, 23, 25, 24, 25, 27, 27, 25]
plt.plot(Date1, Temperature1, color='green',  marker='o', label="Day")

Date2 = ['7.19', '7.20', '7.21', '7.22', '7.23', '7.24', '7.25', '7.26', '7.27', '7.28', '7.29', '7.30', '7.31', '8.1']
Temperature2 = [15, 14, 16, 14, 12, 12, 13, 11, 14, 11, 15, 16, 16, 15]
plt.plot(Date2, Temperature2, color='blue', marker='o', label="Night")

plt.xlabel('Date')
plt.ylabel('Temperature ℃')
plt.title('Ulaanbaatar two week weather schedule')
plt.legend()
plt.show()

print("\n----Third Question----")
# Question 3 Compare and write differences of Dictionary, List, Tuples with small examples
print("--------------------------------------------------------")
print('Dictionary')
print("Dictionaries are used to store data values in key you can't duplicate data in key. "
      "And dictionary uses {} bracket")

apple = {'brand': 'Apple', 'model': 'iPhone 12', 'year': 2020, 'color': 'purple'}

print(apple)
print("--------------------------------------------------------")
print('List')
print("Lists are used to store multiple items in a single variable. Also you can add, delete using list"
      " And list uses [] bracket")

pizza_toppings = ['pepperoni', 'chicken', 'tomato', 'olive', 'cheese', 'pepper']
pizza_toppings.remove('chicken')
print(pizza_toppings)
print("--------------------------------------------------------")
print('Tuple')
print(' Same as the list but a tuple is a collection which is ordered and unchangeable. And tuple uses () bracket')

Veggies = ('potato', 'onion', 'cucumber', 'cabbage', 'pea', 'cucumber')
print(Veggies)

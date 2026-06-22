print("=" * 35) # prints '=' 35 times
print("   🧮  WELCOME TO MY CALCULATOR  🧮") # welcome message
print("=" * 35)# prints '=' 35 times

num1 = float(input("Enter 1st number: ")) # taking float number as input 
num2 = float(input("Enter 2nd number: ")) # taking float number as input

print("\n--------- RESULTS ---------") # result message
print(f"{num1} + {num2} = {num1 + num2}") # num + num through f string 
print(f"{num1} - {num2} = {num1 - num2}") # num - num through f string 
print(f"{num1} * {num2} = {num1 * num2}") # num * num through f string 
print(f"{num1} / {num2} = {num1 / num2:.2f}") # num / num through f string and restricted to 2 values after decimal
print(f"{num1} % {num2} = {num1 % num2}") # num % num through f string
print(f"{num1} ** {num2} = {num1 ** num2}") # num ** num through f string 
print("---------------------------") # for a clear look at the end of result 
def calculator():
  print("----Welcome to the Calculator----")
  print(" 1 For Addition ")
  print(" 2 For Subtraction ")
  print(" 3 For Multiplication ")
  print(" 4 For Division ")
  print(" 5 For Exponent ")
  print(" 6 For Square Root ")
  print(" 7 For Factorial ")
  print(" 8 For Percentage ")
  print(" 9 For Quit ")
  print("-------------------------------")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    print("----Your choice is Addition-----")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The sum of the two numbers is: ", a + b)
  elif choice == 2:
    print("----Your choice is Subtraction-----")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The difference of the two numbers is: ", a - b)
  elif choice == 3:
    print("----Your choice is Multiplication-----")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The product of the two numbers is: ", a * b)
  elif choice == 4:
    print("----Your choice is Division-----")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The quotient of the two numbers is: ", a / b)
  elif choice == 5:
    print("----Your choice is Exponent-----")
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    print("The exponent of the two numbers is: ", a**b)
  elif choice == 6:
    print("----Your choice is Square Root-----")
    a = int(input("Enter the number: "))
    print("The square root of the number is: ", a**0.5)
  elif choice == 7:
    print("----Your choice is Factorial-----")
    a = int(input("Enter the number: "))
    fact = 1
    for i in range(1, a + 1):
      fact = fact * i
    print("The factorial of the number is: ", fact)
  elif choice == 8:
    print("----Your choice is Percentage-----")
    a = int(input("Enter the number: "))
    b = int(input("Enter the percentage: "))
    print("The percentage of the number is: ", (a * b) / 100)
  elif choice == 9:
    print("----Your choice is Quit-----")
    print("Thank you for using the calculator")
  else:
    print("Invalid choice")
  print("-------------------------------")
  print("Do you want to continue?")

  print(" 1 For Yes ")
  print(" 2 For No ")
  print("-------------------------------")
  choice = int(input("Enter your choice: "))
  if choice == 1:
    calculator()
  elif choice == 2:
    print("Thank you for using the calculator")
  else:
    print("Invalid choice")

calculator()
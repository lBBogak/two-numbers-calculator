print ("This is calculator that can only calculate two numbers. \n", end = '')
print ("please choose the mathematical expression. \n", end = '')
print ("example : plus, subtract, multiply, devide, square \n")

a = 0

while a < 1:
  
  susic = input()
  if susic == "plus":
    print ("You chose plus. Right?")
    a += 1
  elif susic == "minus":
    print ("You chose minus. Right?")
    a += 1
  elif susic == "multiply":
    print ("You chose multiply. Right?")
    a += 1
  elif susic == "devide":
    print ("You chose devide. Right?")
    a += 1
  elif susic == "Plus":
    print ("You chose plus. Right?")
    a += 1
  elif susic == "Minus":
    print ("You chose minus. Right?")
    a += 1
  elif susic == "Multiply":
    print ("You chose multiply. Right?")
    a += 1
  elif susic == "Devide":
    print ("You chose devide. Right?")
    a += 1
  else:
    print ("Please Write down again.")
    
print ("What would you like to decide the first number? \n")
num1 = int(input())
print ("Okay Sir. The first number is ",num1,".")
print ("What would you like to decide the second number? \n")
num2 = int(input())
print ("Okay Sir. The second number is ",num2,".")

b = 0

while b < 1:
  print ("Calculate? (Yes for Y, No for N)")
  YorN = input()
  if YorN == "y":
    b += 1
    if susic == "plus":
      print ("Result:",num1 + num2)
    elif susic == "Plus":
      print ("Result:",num1 + num2)
    elif susic == "minus":
      print ("Result:",num1 - num2)
    elif susic == "Minus":
      print ("Result:",num1 - num2)
    elif susic == "multiply":
      print ("Result:",num1 * num2)
    elif susic == "Multiply":
      print ("Result:",num1 * num2)
    elif susic == "devide":
      print ("Result:",num1 / num2)
    elif susic == "Devide":
      print ("Result:",num1 / num2)

  elif YorN == "Y":
    b += 1
    if susic == "plus":
      print ("Result:",num1 + num2)
    elif susic == "Plus":
      print ("Result:",num1 + num2)
    elif susic == "minus":
      print ("Result:",num1 - num2)
    elif susic == "Minus":
      print ("Result:",num1 - num2)
    elif susic == "multiply":
      print ("Result:",num1 * num2)
    elif susic == "Multiply":
      print ("Result:",num1 * num2)
    elif susic == "devide":
       print ("Result:",num1 / num2)
    elif susic == "Devide":
      print ("Result:",num1 / num2)

  elif YorN == "n":
      print ("Okay Sir.")

  elif YorN == "N":
    print ("Okay Sir.")

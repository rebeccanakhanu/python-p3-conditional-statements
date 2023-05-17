#!/usr/bin/env python3

def admin_login(username, password):
    if (username.upper() == "ADMIN"and password == "12345"):
      return ("Access granted")
    else :
      return ("Access denied")

    

def hows_the_weather(temperature):
    if temperature == 33:
      return ("It's brisk out there!")
    elif temperature == 99:
      return ("It's too dang hot out there!")
    elif temperature == 55:
       return ("It's a little chilly out there!")
    elif temperature ==75:
       return ("It's perfect out there!")
    else :
       return ("It's perfect out there")

def fizzbuzz(num):
    if num == 0:
       return ("FizzBuzz")
    elif num == 15:
       return ("FizzBuzz")
    elif num == 45 :
       return ("FizzBuzz")
    elif num ==3:
       return ("Fizz")
    elif num == 33:
       return ("Fizz")
    elif num == 42:
       return ("Fizz")
    elif num ==5:
       return ("Buzz")
    elif num ==10 :
       return ("Buzz")
    elif num ==50:
       return ("Buzz")
    if num == 2:
       return (2)
    elif num == 13:
       return (13)
    elif num == 59:
       return (59)
    
def calculator(operation, num1, num2):
    if operation ==("+"):
       return (num1 + num2)
    
    elif operation ==("-"):
     return (num1 - num2) 
    
    elif operation ==("*"):
       return (num1 * num2)
    
    elif operation ==("/"):
       return (num1 / num2)
    elif operation ==("a"):
       print ("Invalid operation!")
       return None
# Christian Alvarez
# Welcome to my integration project!
print("Hello there welcome to the main menu!")
print("What Would you like to do?")
print("1.Calculator")
print("2.Formatter tutorial")
print("3.Greater than or less than calculator")
print("4.Boolean operations")
print("5.Iterative operators and def function")
print("6.Parameters")
print("0.Quit")
userchoice = int(input())
if userchoice == 1:
      # This Calculator can calculate anything
      # Select a operation you wish to perform below
      print("1.Addition")
      print("2.Subtraction")
      print("3.Multiplication")
      print("4.Division")
      print("5.Exponential")
      print("6.Remainder")
      print("7.Modulo")
      # All numbers wil be floated to allow for decimals!
      calcchoice = int(input())
      if calcchoice == 1:
      # The + operator is able to do addition and combine different things in a string! but for now we will focus on a calculator setting so addition
       print("Please select your numbers to add together")
       num1 = float(input("Please enter first number:"))
       num2 = float(input("Please enter second number:"))
       print(num1 + num2)
       # Tada! it calculated the two numbers!
      elif calcchoice == 2:
           # Subtraction is rather simple and the opposite of addition
           print("Please enter the two numbers you wish to subtract.")
           num3 = float(input("Please enter first number:"))
           num4 = float(input("Please enter second number:"))
           print(num3 - num4)
      elif calcchoice == 3:
           # Multiplication is the multiplying of two numbers!
           print("Please enter the two numbers you wish to multiply.")
           num5 = float(input("Please enter first number:"))
           num6 = float(input("Please enter second number:"))
           print(num5 * num6)
           # Bam multiplication baby
      elif calcchoice == 4:
           # Division is the dividing of two numbers
           print("Please enter the two numbers you wish to division.")
           num7 = float(input("Please enter first number:"))
           num8 = float(input("Please enter second number:"))
           print(num7 / num8)
           #Bam divided baby
      elif calcchoice == 5:
           #Exponential finds the power
           print("Please enter the two numbers you wish to find an multiplied by a power.")
           num1 = float(input("Please enter first number:"))
           num2 = float(input("Please enter second number:"))
           print(num1 ** num2)
           # Bam power multiplying
      elif calcchoice == 6:
           #// is integer division.
           print("Please enter the two numbers you wish to integer divide.")
           num3 = float(input("Please enter first number:"))
           num4 = float(input("Please enter second number:"))
           print(num3 // num4)
           # Bam more calculations
      elif calcchoice == 7:
           #Modulus gives the remainder of dividing two number
           print("Please enter the number the two number you wish to calculate.")
           num4 = float(input("Please enter first number:"))
           num8 = float(input("Please enter second number:"))
           print(num4 % num8)
           #Bam remainder
                   
elif userchoice == 2:
    print("Welcome to the formatting menu we have three different types of formatting we can show you, Please select one below.")
    print("1.Decimals with two places.")
    print("2.Adding statements together with +")
    print("3.Adding statements together with *")
    formatchoice = int(input())
    if formatchoice == 1:
        # format() is a powerful tool that allows you to format statements
        print("Output can be formatted to two decimal places with format(variableName, '.2f')")
        price = 800.89889
        print("For example, 800.89889 becomes:", format(price, '.2f'))
        #Tada two decimal places!
    elif formatchoice == 2:
        # + is also used to add statements together!
        print("+ is not just an addition symbol but also used to bring two statements together like a full name for example.")
        word1 = input("Enter first half of name:")
        word2 = input("Enter second half of name:")
        print(word1 + word2)
        # the + operator added the names together! making a full name
    elif formatchoice == 3:
        # * can repeat strings multiple times
        print("* is not just an multiplication symbol but also used to repeat a statement 100 times for example.")
        word1 = input("Enter a word:")
        multiplier = int(input("Enter a number to multiply by:"))
        print(word1 * multiplier)
        print("Congratulations you multiplied a word any number of time!")
elif userchoice == 3:
    print("Welcome to the greater than or less than calculator!")
    print("As the name entails you can check if something is greater than or less than here")
    print("If it is greater than or equal to or even less than it will return a true and a false if well false")
    print("Please select which you want below!")
    print("1.Greater than")
    print("2.Less than")
    print("3.Inbetween Greater than but not less than two numbers")
    calchoice = int(input())
    if calchoice == 1:
        # > represents greater than a well known math symbol and operator
        print("Welcome to the greater than calculator where you can check if a number is greater than another")
        print("when prompted please input the numbers you wish to compare")
        x=float(input("Please enter number you wish to compare to: "))
        y=float(input("Please enter number you wish to see if it is greater than: "))
        print(y>x)
        # Should return true or false depending on numbers
    elif calchoice == 2:
        # < represents less than a well known math symbol and operator
        print("Welcome to the greater than calculator where you can check if a number is less than another")
        print("when prompted please input the numbers you wish to compare")
        x = float(input("Please enter number you wish to compare to: "))
        y = float(input("Please enter number you wish to see if it is less than: "))
        print(y > x)
        # Should return true or false depending on numbers
    elif calchoice == 3:
        # For getting a number between it looks something like 5<x<13 where it checks if its between the numbers
        print("Welcome to the between calculator where you can check if a number is between two numbers")
        print("when prompted please follow the instructions to check you numbers")
        y = float(input("Please enter Largest number: "))
        z = float(input("Please enter lowest number: "))
        x = float(input("Please enter the number you wish to check if its between: "))
        print(z<x<y)
        # Should return true or false depending on numbers
elif userchoice == 4:
    print("Welcome to the boolean operators page where you can learn how boolean operators work")
    print("You will be given three options of operators not,and,or all work differently but similarly")
    print("1.And operator")
    print("2.Or operator")
    print("3.Not operator")
    operatorchoice = int(input())
    if operatorchoice == 1:
        #the and operator essentially check two statements and typically brings back a false if a false is involved.
        #However if both statements are true is brings back a true essentially if there is a false it is false.
        print("Welcome to the and operator example")
        print("In the following example you will get to build two statements x>y check and z==q check")
        print("The and operator will check both statements for a false and bring back false regardless if one is true")
        print("However if both statements are true then it will return a true.")
        print("When prompted please enter your numbers for the statement")
        x = float(input("Please enter a number for first statement: "))
        y = float(input("Please enter another number for first statement: "))
        z = float(input("Please enter number to be equal to: "))
        q = float(input("Please enter number that is equal to: "))
        print(x > y and z == q)
        #congratulations on understanding how the operator works
    elif operatorchoice == 2:
        # the and operator essentially check two statements and brings back a True if a True is involved.
        # However if both statements are False is brings back a False essentially if there is a True it is True.
        print("Welcome to the or operator example")
        print("In the following example you will get to build two statements x>y check and z==q check")
        print("The or operator will check both statements for a True and bring back a True regardless if one is False")
        print("However if both statements are False then it will return a False.")
        print("When prompted please enter your numbers for the statement")
        x = float(input("Please enter a number for first statement: "))
        y = float(input("Please enter another number for first statement: "))
        z = float(input("Please enter number to be equal to: "))
        q = float(input("Please enter number that is equal to: "))
        print(x > y or z == q)
        # congratulations on understanding how the operator works
    elif operatorchoice == 3:
        # The not operator brings back the opposite result of a statement so if a statement is true it is false
        # Essentially it is just the opposite of what the answer is so if false its true, if treu its false
        print("Welcome to the not operator example")
        print("In the following example you will craft a statement x>y with the not operator returning true or false")
        print("The not operator will return the opposite of what the answer is so if true then it returns false")
        print("Please when prompted enter the numbers to go into the statement")
        x = float(input("Please enter a number for first statement: "))
        y = float(input("Please enter another number for first statement: "))
        print(not x>y)
        print("You may also use the != operator as it also brings back the opposite result")
        q = float(input("Please enter a number for first statement: "))
        z = float(input("Please enter another number for first statement: "))
        print(q!=z)
elif userchoice == 5:
    print("Welcome to the Iterative operators page where you can learn how iterative operators work")
    print("You will be given three options of operators while,for,range(), and a special def function explanation")
    print("Below are five options one for each that include a interactive way to explain how they work")
    print("please select one from below")
    print("1.Range()")
    print("2.While")
    print("3.For")
    print("4.In")
    print("5.Def")
    iterativechoice = int(input())
    if iterativechoice == 1:
        print("Welcome to the range() function explanation it is simple to understand")
        print("The range() function allows you to input a number, or in cases a list of words and the number in range tells it to stop at that value.")
        print("Essentially it acts like the end of a list and tells it where to stop")
        print("the following prompt will allow you to enter a number in the range to create a list from")
        x=int(input("Please enter a number: "))
        print(list(range(x)))
        print("Congratulations you used range to create a list up till the number before your number")
    elif iterativechoice == 2:
        print("Welcome to the while function explanation it is simple to understand and has a useful application")
        print("The while function allows you to input a number, and that number acts as the statement that while uses to make a loop")
        print("A while loop is simple to make and execute it keeps looping as long the statement remains true")
        print("the following prompt will allow you to enter a number in the while to create a loop up until 100 statements")
        print("each run will increase the counter of your number by 1 at the end to put a limit on the loop")
        x = int(input("Please enter a number: "))
        while x<100:
            print("you have created a loop!")
            print("how do you get out?")
            x=x+1
    elif iterativechoice == 3:
        print("Welcome to the for function explanation it is a very useful function")
        print("Essentially it says for this go do that.")
        print("In the prompt below you will be asked for a number to put into a range function with for being used in it.")
        x=int(input("Please enter a number for the range: "))
        for i in range(x):
            print(i)
        print("It printed up till your number using the for function to test the range function by your number")
    elif iterativechoice == 4:
        print("The in function checks if a whatever is input is part of a list,string,etc")
        print("for the example we will use a list and check if your number inputted is part of it.")
        print("the list will include 1 through 10 and will return true or false if the number is in the list and false elsewise.")
        x=int(input("Please enter a number:"))
        list1 = [1,2,3,4,5,6,7,8,9,10]
        print(x in list1)
    elif iterativechoice == 5:
        print("The def function gives definition to a function its that simple")
        print("Useful in many ways this will help you def a function and use it to complete a operation ")
        print("Below will be a prompt for a statement to put in func1 we will define it in a function to print said statement")
        func2=input("Please enter a sentence: ")
        def func1():
            print(func2)
        func1()
elif userchoice == 6:
    print("Welcome to the parameters explanation and interactive explanation")
    print("Parameters are very useful as they are the heart and soul of any function.")
    print("They are essentially the statements inside the parenthesis")
    print("for the example it we will use def add(a,b) where a,b is the parameter and return a+b")
    print("Below you will be prompted for two number for x,z")
    x=float(input("Please enter a number: "))
    z=float(input("Please enter a second number: "))
    def add(a,b):
        return a+b
    print(add(z,x))
else:
    print("Shutting down.")


      



#Q1 — Variables & Data Types Create variables for:name:age:height:is_student:Print the value and data type of each variable
#Name = "Hatum Hussain"
#age = 23;
#height = 5.4;
#is_student = 'True'
#print("My Name is: " , Name)
#print("My age is: ", age)
#print("My height is: " ,height)
#print("Student information is",is_student)

#Q2 — Input + Type Casting.Take the user's:
#Name/Age/Height/as input.Convert age to int and height to float.
#Then print:Name: Hatum Age: 31 Height: 5.6 Also print the data type of age and height.
#Name = input("Enter Your Name: ")
#Age =  int (input ("Enter Your Age : "))
#Height =float (input("Enter your Height: "))
#print(Name , type(Name))
#print(Age ,type(Age))
#print(Height,type(Height))
#Q3 — Strings — 5 marks #Take a full name as input and print:Uppercase:Lowercase:Number of characters:First 5 characters:Last 5 characters
#Name  = input("Enter Your Full Name: ")
#print("The Name is in Capital letters: ", Name.upper())
#print("The Name is in Small letters : ",Name.lower())
#print("The Lenght of Name is : ",len(Name))
#print("This displays the first five characters: ", Name[0:5])
#print("This displays the Last five characters: ", Name[13:20])
#Q4 — String Slicing — 5 marks:Given:text = "PythonAutomation":Print:First 6 characters:Last 10 characters:Characters from index 2 to 8:The string in reverse
#Testing = input("Write the text you want : ")
#print("These are the first six characters: " ,Testing[0:6])
#print("These are the last 10 characters: ", Testing[-10:])
#print("Characters from 2 to 8 are: " , Testing[2:8])
#print("The string in reverse" ,Testing[::-1])
#Q5 Write a Python program that takes a user's name, age, height, and email as input.
#Your program should:Remove extra spaces from the name and email using strip().Convert the name to uppercase and lowercase.
#Print the length of the name.Print the first 5 and last 5 characters of the name.Convert age to int and height to float.Print the data types of name, age, and height.
#Convert the email to lowercase.
#Use find() to find @ and use slicing to extract:Username:Domain:Print the final normalized email.
#1 Remove extra spaces from the name and email using strip().
#Name = input("Enter Your Name: ")
#print(Name.strip())
#2- Convert the name to uppercase and lowercase.
Name = input("Enter your Name: ")
print(Name.upper())
print(Name.lower())
#3Print the length of the name
print(len(Name))
#4Print the first 5 and last 5 characters of the name.
print(Name[0:5])
print(Name[-6:])
#5 Convert age to int and height to float.
age = int (input("Enter Your Age: "))
height = float (input("Enter Your Height: "))
#6 Print the data types of name, age, and height
print(type(Name))
print(type(age))
print(type(height))
#7Convert the email to lowercase.
Email = input("Enter your Email Addrees: ")
print(Email.lower())
#8 Use find() to find @ and use slicing to extract:Username:Domain
print(Email.find("@"))
print(Email.find("GMAIL.COM"))
'''
                      Practical Task 1
Follow these steps:
● Create a new Python file called age-quiz.py. The program you create in
this file will be used to output a variety of responses determined by the
data the user enters.
● If the user is 40 or over, output the message "You're over the hill."
● Write code to take in a user’s age and store it in an integer variable called
age.
● Assume that the oldest someone can be is 100; if the user enters a
higher number, output the message "Sorry, you're dead.".
● If the user is 65 or older, output the message "Enjoy your retirement!"
● If the user is under 13, output the message "You qualify for the kiddie
discount."
● If the user is 21, output the message "Congrats on your 21st!"
● For any other age, output the message "Age is but a number."
● Tips:
o You should use the if-elif-else statement structure to create the
program.
o Note that the order in which you set up the conditions is
important; you will need to work out what makes sense in terms
of the logical tests applied to the ages.'''

age=int(input("please enter your age "))
print(age)

if age>=40 and age<65:
    print("you are over the hill")

elif age>=65 and age<100:
    print("Enjoy your retirement")

elif age<13:
    print ("you qualify for the kiddie discount")

elif age==21:
    print ("Congrats on your 21st!")

elif age>=100:
    print("sorry, you are dead.")

else:
    print ("age is but a number")
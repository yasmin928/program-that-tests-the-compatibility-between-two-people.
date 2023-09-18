# Welcome sentance
print("Welcome to the Love Calculator!")
# Input your name and your partenar
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

compine_name = name1 +name2

#Make the names all lower
lower_name = compine_name.lower()

#count true in the name
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

true = t + r + +u + e

#count love in the names
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

love = l + o + v + e

#calculate the love score
love_score = int(str(true)+ str(love))

#what is your setuation
if  love_score < 10 or love_score > 90 :
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50 :
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")    

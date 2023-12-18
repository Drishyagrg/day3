print("Welcome to the Love Calculator!")
name1=input("What is your name?\n")
name2=input("What is their name?\n")
name=name1+name2

lower_name=name.lower()

t=lower_name.count("t")
r=lower_name.count("r")
u=lower_name.count("u")
e=lower_name.count("e")

l=lower_name.count("l")
o=lower_name.count("o")
v=lower_name.count("v")
e=lower_name.count("e")

first=t+r+u+e
second=l+o+v+e

score=first*10+second
# score=str(first)+str(second)
# score=int(score)

if score <10 or score>90:
    print(f"Your score is {score}, you go together like coke and mentos. ")
elif score >40 and score<50:
    print(f"Your score is {score}, you are alright together.")    
else:
    print(f"Your score is {score}.")    

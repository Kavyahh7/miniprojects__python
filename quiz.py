print("Welcome to the python quiz...")
print("Are you ready.. ")
answers = {1: "c" , 2 : "d" , 3 : "b" , 4 : "c" , 5: "a"}
questions = ['''1. Who developed Python Programming Language?
a) Wick van Rossum
b) Rasmus Lerdorf
c) Guido van Rossum
d) Niene Stom''',
'''2. Which type of Programming does Python support?
a) object-oriented programming
b) structured programming
c) functional programming
d) all of the mentioned''',
'''3. Is Python case sensitive when dealing with identifiers?
a) no
b) yes
c) machine dependent
d) none of the mentioned''',
'''4. Which of the following is the correct extension of the Python file?
a) .python
b) .pl
c) .py
d) .p''',
'''5. Is Python code compiled or interpreted?
a) Python code is both compiled and interpreted
b) Python code is neither compiled nor interpreted
c) Python code is only compiled
d) Python code is only interpreted''']
count = 0
mistakes = {}
for i in range(0,5):
    print(questions[i])
    ans = input()
    if answers[i+1] == ans:
        count+= 1
    else:
        mistakes[i+1] = f"answer for {i+1} is option {answers[i+1]}"
print(f"Your score is : {count}")
print("Your mistakes are : ")
for j in mistakes.values():
    print(j)

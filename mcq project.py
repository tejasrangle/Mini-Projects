# mcq project

questions=["Who developed Python Programming Language?",
           "Which of the following character is used to give single-line comments in Python?",
            "Is Python case sensitive when dealing with identifiers?",
           "Which of the following is the correct extension of the Python file?",
            "Which keyword is used for function in Python language?"]
options=[["Wick van Rossum","Guido van Rossum"],
         ["#","!"],
         ["no","yes"],
         [".pl",".py"],
         ["Fun","Def"]]
answers=["Guido van Rossum","#","yes",".py","Def"]

j=0
score=0
for i in questions:
    print(i)
    print("1-",options[j][0],"\n2-",options[j][1])
    choice=int(input("choose answer 1 or 2:-"))
    if options[j][(choice-1)]==answers[j]:
        print("--CORRECT--")
        score=score+1
    else:
        print("--WRONG--")
        score=score-0.25
    j=j+1
    b=int(input('''
1-to continue
2-to break\n'''))
    print("\n")
    if b==2:
        break
print("your score:",score,"outof 5")
    
          
    

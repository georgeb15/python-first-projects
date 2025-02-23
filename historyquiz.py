print("welcome to the history quiz")
print("easy level")
result = 0
q1 = input("question 1: who was the first president of the united states?")
if q1.lower() == "george washington" or q1.lower() == "washington":
    print("correct")
    result += 1
else:
    print("incorrect")
    result -= 1
q2 = int(input("what year did ww1 start"))
if q2 == 1914:
    print("correct")
    result += 1
else:
    print("wrong!")
    result -= 1
print("medium level")
q3 = int(input("what year did the byzantine empire lose constantinople"))
if q3 == 1453:
    print("correct")
    result += 1
else:
    print("wrong!")
    result -= 1
q4 = input("what river allowed the egyptians to farm?")
if q4.lower() == "nile":
    print("correct")
    result += 1
else:
    print("wrong!")
    result -= 1
print("hard mode now")
q5 = input("how much did the louisiana purchase cost")
if q5 == "15 million":
    print("correct")
    result += 1
else:
    print("wrong!")
    result -= 1
print(result)
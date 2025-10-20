score=0

print("Q1: What is longest river in the world? : ")
ans1 = input() 
if ans1 == "Nile River":
    score += 1
else:
    print("Wrong : ")

print("Q2 : What is fastest mammal : ")
ans2 = input()
if ans2 == "The cheetah":
    score += 2
else:
    print("Wrong : ")

print(f"Total score {score}")


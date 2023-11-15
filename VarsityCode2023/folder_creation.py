import os

first = 3
last = 5
for i in range(first,last+1):
    directory = f"VarsityCode2023\Challenge {i}"
    solution = os.path.join(directory,"solution.py")
    tests = os.path.join(directory,"tests.py")
    description = os.path.join(directory,"description.md")
    if not os.path.exists(directory):
        os.makedirs(directory)
    open(solution, "a")
    open(tests,"a")
    open(description, "a")
    

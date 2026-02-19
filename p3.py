n = int(input("Enter students number"))

students = {}

for _ in range(n):
    name = input("Enter student name : ")
    marks = list(map(int,input("Enter students marks :").split()))
    students[name] = marks
    avg = sum(marks) / len(marks)
    print(f"Average of {name} is {avg}")




print(students)
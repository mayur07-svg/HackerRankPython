# Store Data into dict

n = int(input("Enter students numbers :"))
students = {}

for _ in range(n):
    name  = input("Enter students name : ")
    age = int(input("Enter age :"))
    students[name] = age



print(students)


# Store List as Value ...

n1 = int(input("Enter Students numbers"))

students1 = {}

for _ in range(n1):
    name = input("Enter student name :")
    marks =input().split()
    students1[name] = marks


print(students1)
print(students1[name])


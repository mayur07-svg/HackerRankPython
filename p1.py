n = int(input("Enter number of students"))

students  = {}

# Take input for each students

for _ in range(n):
    name = input("Enter the name of student : ")
    marks = list(map(float,input(f"Enter the marks for {name} separated by space: ").split()))
    students[name] = marks


#Query students 

query_name = input("Enter the name of the student to find average:")

if query_name in students:
    avg = sum(students[query_name]) / len(students[query_name])
    print(f"{query_name}'s average score is :{avg:2f}")
else:
    print(f"{query_name} not found.")

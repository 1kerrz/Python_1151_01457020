def search(students, id):
    _id = id.strip()
    if _id in students:
        name, score = students[_id]
        return name, score
    else:
        return None


student_num = int(input())
students = {}

for i in range(student_num):
    id, name ,score = input().split()
    students[id] = (name,score)

search_times = int(input())

for i in range(search_times):
    student_id = input()
    result = search(students, student_id)
    if result:
        name, score = result
        print(name, score)
    else:
        print("Not found")
    
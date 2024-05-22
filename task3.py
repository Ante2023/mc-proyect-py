
def qualify(students):
    for student in students:

        suma=0
        for num in student["grades"]:
            suma +=num
        media = suma/len(student["grades"])
        status="fail"
        if media >= 80:
            status="pass"
        print(f"{student["name"]} in {student["class"]} - Average Grade: {media}, Status:{status} ")

students = [
    {"name": "John", "grades": [88, 76, 92, 56], "class": "biology"},
    {"name": "Jane", "grades": [80, 80, 84], "class": "chemistry"},
    {"name": "Dave", "grades": [78, 80, 88,21,19], "class": "algebra"}
]
qualify(students)
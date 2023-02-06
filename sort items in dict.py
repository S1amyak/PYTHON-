students = {"john":80,"jane":90,"jim":85,"jack":75,"joe":95}
sorted_students = sorted(students.items(),key = lambda x: x[1])
for student in sorted_students:
    print(student[0],":",student[1])

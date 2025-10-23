from task1 import details, marks, grades


student_name = "Pratham"
student_course = "Data Science"
mark_list = [92, 85, 78, 90, 88]

details.display(student_name, student_course)
t = marks.total(mark_list)
a = marks.average(mark_list)
g = grades.assign_grade(a)

print("Total Marks :", t)
print("Average Marks:", round(a, 2))
print("Grade       :", g)
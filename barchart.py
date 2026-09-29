import matplotlib.pyplot as plt

students = ["A", "B", "C", "D"]
marks = [80, 65, 90, 75]

plt.bar(students, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
import matplotlib.pyplot as plt

subjects = ["Maths", "Physics", "Chemistry", "English"]
marks = [30, 25, 25, 20]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()
import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 60, 65, 70, 70, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5, edgecolor="black")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()
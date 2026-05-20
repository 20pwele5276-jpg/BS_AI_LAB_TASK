import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ===================================================
# TASK 1: LINE GRAPH (TEMPERATURE)
# ===================================================

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temp = [30, 32, 31, 35, 33]

plt.plot(days, temp)

plt.title("Temperature over 5 Days")
plt.xlabel("Days")
plt.ylabel("Temperature")

plt.grid()

plt.show()

# ===================================================
# TASK 2: BAR CHART (MARKS)
# ===================================================

students = ["Wajiha", "Saman", "Aiman", "Ayesha"]
marks = [78, 85, 90, 72]

plt.bar(students, marks, color=["red", "blue", "green", "orange"])

plt.title("Marks of Students")

for i in range(len(students)):
    plt.text(i, marks[i], marks[i])

plt.show()

# ===================================================
# TASK 3: HISTOGRAM
# ===================================================

data = np.random.randint(0, 100, 500)

plt.hist(data, bins=10)

plt.title("Histogram of Exam Scores")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()

# ===================================================
# TASK 4: SCATTER PLOT
# ===================================================

hours = [1,2,3,4,5,6,7]
marks2 = [40,45,50,60,70,80,90]

plt.scatter(hours, marks2, color="red")

plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")

plt.show()

# ===================================================
# TASK 5: SEABORN LINE PLOT
# ===================================================

x = [1,2,3,4,5]
y = [10,20,25,30,40]

sns.lineplot(x=x, y=y)

plt.title("Seaborn Line Plot")

plt.show()

# ===================================================
# TASK 6: HEATMAP
# ===================================================

data2 = np.random.rand(5,5)

sns.heatmap(data2, annot=True)

plt.title("Heatmap")

plt.show()

# ===================================================
# TASK 7: MATPLOTLIB VS SEABORN
# ===================================================

x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.scatter(x, y)
plt.title("Matplotlib Scatter")
plt.show()

sns.scatterplot(x=x, y=y)
plt.title("Seaborn Scatter")
plt.show()

# ===================================================
# TASK 8: MINI CLASS DATASET
# ===================================================

names = ["Wajiha","Sara","Ahmed","Ayesha","Zain"]
marks3 = [78,85,90,72,88]
attendance = [80,85,90,75,88]

plt.bar(names, marks3)
plt.title("Marks of Students")
plt.show()

plt.plot(names, attendance)
plt.title("Attendance Trend")
plt.show()

data3 = np.array([marks3, attendance])

sns.heatmap(data3, annot=True)

plt.title("Marks vs Attendance")

plt.show()
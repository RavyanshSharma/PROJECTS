import numpy as np

student = np.random.randint(40, 101, 30)

print("Lowest marks obtained:", student.min())
print("Average marks obtained:", student.mean())
print("Highest marks obtained:", student.max())
print("Standard deviation:", student.std())

A = np.sum(student >= 90)
B = np.sum((student >= 75) & (student < 90))
C = np.sum((student >= 60) & (student < 75))
F = np.sum(student < 60)

print(f"\nGrade breakdown — A:{A}  B:{B}  C:{C}  F:{F}")
print(f"Students who passed: {A+B+C}/30")
print(f"Students who failed: {F}/30")

top = np.argsort(student)[::-1]
print(f"\nTop student:    Student #{top[0]+1}  (score: {student[top[0]]})")

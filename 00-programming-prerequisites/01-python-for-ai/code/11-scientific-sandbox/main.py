import pandas as pd
df = pd.read_csv("students.csv")
print("First 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns)

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

import numpy as np
study_hours = df['study_hours'].to_numpy()
marks = df['marks'].to_numpy()

print("\nStudy Hours (NumPy Array):")
print(study_hours)
print("\nMarks (NumPy Array):")
print(marks)
print("\nMean of Study Hours:", np.mean(study_hours))
print("Maximum marks:", np.max(marks))
print("Minimum marks:", np.min(marks))

bonus_marks = marks + 5

print("\nMarks after bonus:")
print(bonus_marks)

print("\nOriginal marks:")
print(marks)

high_scorers = marks[marks > 60]

print("Students scoring above 60:")
print(high_scorers)
high_scorers_df=df[df["marks"]>60]
print("\nHigh Scoring Students:")
print(high_scorers_df)
print("\nAverage marks of high scorers:")
print(high_scorers_df["marks"].mean())

import matplotlib.pyplot as plt

plt.scatter(study_hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Relationship between Study Hours and Marks")
plt.show()

plt.hist(marks, bins=5, edgecolor='black')

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()

np.random.seed(42)

random_marks = np.random.randint(0, 101, size=5)

print(random_marks)
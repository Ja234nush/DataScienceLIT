import numpy as np

exams = np.array([
    [78, 85, 92, 88],
    [65, 72, 68, 70],
    [90, 88, 95, 92],
    [55, 60, 58, 62],
    [82, 79, 85, 80]
])
print(exams)
bonus = np.array([5, 10, 5, 10])
exams_with_bonus = exams + bonus
#print(exams_with_bonus)
multipliers = np.array([1.0, 1.1, 0.95, 1.15, 1.0])
final_scores = exams_with_bonus * multipliers.reshape(-1, 1)
print(final_scores)
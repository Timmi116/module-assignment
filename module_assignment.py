
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students1 = list(students)
students1.sort()
grades1 = sum(grades[0]) / len(grades[0])
grades2 = sum(grades[1]) / len(grades[1])
grades3 = sum(grades[2]) / len(grades[2])
grades4 = sum(grades[3]) / len(grades[3])
grades5 = sum(grades[4]) / len(grades[4])
assessments = {list(students1)[0]: grades1, list(students1)[1]: grades2,
               list(students1)[2]: grades3,
               list(students1)[3]: grades4, list(students1)[4]: grades5}
print(assessments)

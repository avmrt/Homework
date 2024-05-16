grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list_students = sorted(list(students))
GPA = {}
k=0

for i in list_students:
    GPA[i] = [sum(grades[k])/len(grades[k])]
    k=k+1

print(GPA)

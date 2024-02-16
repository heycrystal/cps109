grades = [1, 2, 4, 8, 16, 32]
type(grades)

min(grades)
max(grades)
sum(grades)

print(f' {grades}')
print(f' The minimum of the list above is {min(grades)} and the maximum is {max(grades)}.')
print(f' The total sum of the entire list is {sum(grades)}.')

for grade in grades:
    print(grade)

grad = int(input('Enter the grade here: '))
if grad > 70:
    print('You have at least a C average')
else:
    print('You are below a C average')

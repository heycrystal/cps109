grade = int(input('Enter the grade here: '))
letter_grade = 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'
if 93 <= grade <= 100:
    letter_grade = 'A'
    print(f'You have an A with a grade of {grade}.')

if 90 <= grade <= 92:
    letter_grade = 'A-'
    print(f'You have an A- with a grade of {grade}.')

if 87 <= grade <= 89:
    letter_grade = 'B+'
    print(f'You have a B+ with a grade of {grade}.')

if 83 <= grade <= 86:
    letter_grade = 'B'
    print(f'You have a B with a grade of {grade}.')

if 80 <= grade <= 82:
    letter_grade = 'B-'
    print(f'You have a B- with a grade of {grade}.')

if 77 <= grade <= 79:
    letter_grade = 'C+'
    print(f'You have a D+ with a grade of {grade}.')

if 73 <= grade <= 76:
    letter_grade = 'C'
    print(f'You have a C with a grade of {grade}.')

if 70 <= grade <= 72:
    letter_grade = 'C-'
    print(f'You have a C- with a grade of {grade}.')

if 67 <= grade <= 69:
    letter_grade = 'D+'
    print(f'You have a D+ with a grade of {grade}.')

if 63 <= grade <= 66:
    letter_grade = 'D'
    print(f'You have a D with a grade of {grade}.')

if 60 <= grade <= 62:
    letter_grade = 'D-'
    print(f'You have a D- with a grade of {grade}.')

if grade <= 59:
    letter_grade = 'F'
    print(f'You are failing with a grade of {grade}.')

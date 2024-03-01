grade = int(input('Enter the grade here: '))
letter_grade = 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'F'
if 93 <= grade <= 100:
    letter_grade = 'A'

elif 90 <= grade <= 92:
    letter_grade = 'A-'

elif 87 <= grade <= 89:
    letter_grade = 'B+'

elif 83 <= grade <= 86:
    letter_grade = 'B'

elif 80 <= grade <= 82:
    letter_grade = 'B-'

elif 77 <= grade <= 79:
    letter_grade = 'C+'

elif 73 <= grade <= 76:
    letter_grade = 'C'

elif 70 <= grade <= 72:
    letter_grade = 'C-'

elif 67 <= grade <= 69:
    letter_grade = 'D+'

elif 63 <= grade <= 66:
    letter_grade = 'D'

elif 60 <= grade <= 62:
    letter_grade = 'D-'

if grade <= 59:
    letter_grade = 'F'
    print(f'You are failing with a grade of {grade}.')

print(f' You have an {letter_grade} with a grade of {grade}.')

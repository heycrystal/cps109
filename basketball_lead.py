points = int(input('How many points is the team leading by?: '))
ball = input('Do they have the ball?: ')
seconds = int(input('How much time is left in the quarter? (Seconds): '))

lead = (points - 3)

if ball == 'Yes':
    lead = lead + 0.5
else:
    lead = lead - 0.5

if lead < 0:
    lead = 0

safety_point_margin = lead

lead = lead ** 2

if lead > seconds:
    print('The lead is safe.')
else:
    print('The lead is not safe.')

percent_safe = str(round(lead / seconds * 100)) + '%'
print(percent_safe, "percent safe,", safety_point_margin, "safety point margin")

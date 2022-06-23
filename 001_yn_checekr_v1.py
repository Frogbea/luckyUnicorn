# ask user if they have played before
s_instructions = input('Have you played this game before?').lower()

# if yes game start
if s_instructions == 'yes' or 'y':
    print('game continues')

elif s_instructions == 'no' or 'n':
    print('display instructions')

# if no instructions then start
else:
    print('please choose yes/no')

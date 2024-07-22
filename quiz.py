print('**********************************')
print('     Welcome to my Quiz Game      ')
print('**********************************')

isPlaying = input('Do you want to play ? ').lower()

if isPlaying != 'yes':
  print('Ok, Thanks for visit.')
  quit()

print('Lets go...')
score = 0

q1 = int(input('What comes after 10 : '))
if q1 == 11:
  print('Correct!')
  score += 1
else:
  print('Wrong!')

q2 = input('What does ML stand for ? ').lower()
if q2 == 'mechine learning':
  print('Correct')
  score += 1
else:
  print('Wrong!')

q3 = input('What does AI stand for ? ').lower()
if q3 == 'artificial intelligence':
  print('Correct')
  score += 1
else:
  print('Wrong!')

q4 = input('What does IP stand for ? ').lower()
if q4 == 'internet protocol':
  print('Correct')
  score += 1
else:
  print('Wrong!')

print('')
print('*********************')
print(f'your score {score}')
print(f'your got {(score / 4) * 100}%')
print('*********************')

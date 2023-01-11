#!/usr/bin/env python3

#using a counter to control while loop
round = 0

#something that will loop forever until false
while True:
    round = round + 1
    print('finish the movie title, "Movie Pythong\'s the life of ______"')
    answer = input("your guess -->")
    if answer.lower()== 'brian':
        print('correct')
        break
    elif round==3:
        print('sorry, the answer is Brian,')
        break
    else:
        print('sorry! try again')




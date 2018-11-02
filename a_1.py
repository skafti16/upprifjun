hole = 1

while hole <= 18:
    par = int(input('Par of hole ' + str(hole) + ': '))
    score = int(input('Sore on hole ' + str(hole) + ': '))

    hole += 1
    p = par - score
    if p > 3:
        print('invalid score')
        continue
    elif p == 3:
        print('albatross')
        continue
    elif p == 2:
        print('eagle')
        continue
    elif p == 1:
        print('birdie')
        continue
    elif p == 0:
        print('par')
        continue
    elif p == -1:
        print('bogey')
        continue
    elif p == -2:
        print('double bogey')
        continue
    elif p == -3:
        print('triple bogey')
        continue
    elif p <-3:
        print('bad hole')
        continue
    

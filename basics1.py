import random
secretnumber = random.randint(1,20)
print('Ich denke an eine Zahl zwischen 1 und 20.')
for guessesTaken in range(1,7):
    print('Rate mal!')
    guess = int(input())

    if guess < secretnumber:
        print('Zu niedrig!')
    elif guess > secretnumber:
        print('Zu hoch!')
    else:
        break

if guess == secretnumber:
    print('Richtig , du hast es in ' + str(guessesTaken) + ' Versuchen erraten.')
else:
    print('Nö, die Zahl an die ich gedacht habe war: ' + str(secretnumber))
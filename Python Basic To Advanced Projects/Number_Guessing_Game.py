import random

ran_number = random.randint(1,100)

while True:
    try:
        user_input = int(input('Guess the Number Between 1 and 100: '))
        if user_input < ran_number:
            print('Too Low!')
        elif user_input > ran_number:
            print('Too High!')
        else:
            print(' Congratulations You WIN! ')
            break
    except Exception:
        print('--Enter Valid input--')


#Generate random number
#loop
    #guss the number by user
    # if number not valid:
    #     error
        #if number < (random number)
            #Too Low
        #if number > (random number)
            #Too high
        # else:
        #     print well done
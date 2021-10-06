n = 25
print("You have overall 3 chances to guess the correct number.")
i = 1
while  i <= 3:
    user_in = input("Guess the number ")

    if int(user_in)< n:
        print("Try to increase your number.")       
        
    elif int(user_in) > n:
        print("Try to decrease your number.") 
        
    else:
        print('''Correct guess!! \nNo. of Times guessed =  ''' + str(i))
        break
    i+=1 
    print("number of guesses left ",i)
    
if i > 3:
    print("Game over!")
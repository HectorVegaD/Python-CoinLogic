#Hector De La Vega
#Assignment 2 Part 2
#CECS 424

#Global variables used for String manipulation and error checking.
quarterString = 'HHHHHTTTTT'
loopIndex = 0
userInitial = 0
userInput = 0
userFinal = 0
invalid = False
invalid2 = False
selection = ''

## This function will be used for Selecting the two coins
## that will be moved. Error checking that is done ensures that
## the user only inputs empty spaces to move their cursor. Furthermore
## another check is done to ensure that they have indeed selected
## a valid pair of coins.
def getCoins():
    #print the string and get input
    global loopIndex, quarterString, userInitial, userFinal, invalid, invalid2, selection, userInput
    invalid = True
    #Error checking loop
    while(invalid):
        print('Position your cursor under the left of the two coins to be moved:')
        print(quarterString)
        userInput = input('')
        #Validate User Input:
        invalid = checkInvalid(userInput)
        #If the user input is too large, or a '-' has been selected, invalid
        if(len(userInput) < 0 or len(userInput) >= (len(quarterString)-1)):
            invalid = True
        elif(quarterString[len(userInput)] == '-' or
             quarterString[len(userInput)+1] == '-'):
            invalid = True
        if(invalid):
            #If invalid print error message:
            print('Invalid: Please move your cursor only with space'
                  +' inputs and select a valid pair of coins')   
    return len(userInput)

##Get move destination is called to obtain the position that the user
##would like to move the coins they've selected. This function
##is only called when there are no empty spaces currently in the
##string, as coins are automatically moved to empty spaces when
##such spaces exist. Error checking that is done is to ensure that the
##destination location is a valid index. 
def getMoveDestination():
    global loopIndex, quarterString, userInitial, userFinal, invalid, invalid2, selection, userInput
    invalid = True
    invalid2 = True
    while(invalid or invalid2):
        print('Your selection: '+selection)
        #-----Ask for and get destination index:
        print('Position your cursor under the left position of your '
              +'destination location:')
        #If no empty spaces in string, print empty spaces on edges.
        #if('--' not in quarterString):
        quarterString = ' '+quarterString+' '
        print(quarterString)
        userFinal = input('')
        #check the basic validity of input characters
        invalid = checkInvalid(userFinal)
        #if input is too large
        if(len(userFinal) > (len(quarterString)-1)):
           invalid = True
        if(invalid):
            #error message display, continue to next iteration of loop
            print('Invalid: Please move your cursor only with space '
                  +'inputs and select a valid move location')
            quarterString = quarterString.strip()
            continue
        userFinal = len(userFinal)
        
        invalid2 = False
        #Another error check will be to not allow two coins at a certain end
        #of the string to be moved to their own location (no wasted moves)
        if((userInput == 0 and userFinal == 0) or (userInput == 8 and userFinal == 11)):
            invalid2 = True
            print('That coin pair is already at the end of the list.')
        elif(quarterString[userFinal] != ' '):
            invalid2 = True
            print('Invalid: You must move your coins to one of the two ends'
                    +' when no empty spaces \'--\' are available')
        if(invalid or invalid2):
            quarterString = quarterString.strip()

    #if a valid destination location was picked, return it to main
    return userFinal


##This function will be used to ensure that the user input is valid
##in terms of containing only ' ' space inputs. Returns True if valid,
##False otherwise.
def checkInvalid(userInput):
    global quarterString
    invalid = False
    for char in userInput:
        if (char != ' '):
            invalid = True
            return invalid
    return invalid

##Main function, where loop of main program will be executed.
##Other functions will be called from here, and the entirety of the
##String manipulation is done here
def main():
    global loopIndex, quarterString, userInitial, userFinal, invalid, invalid2, selection, userInput
    while loopIndex < 5:
        #get the user input index:
        print('Attempt number: '+str(loopIndex+1))
        ##get user selection from getCoins() function
        userInput = getCoins()
        #-----Save selection:
        selection = quarterString[ userInput : (userInput + 2) ]

        ##If no '--', then get Move destination
        if '--' not in quarterString:
            userFinal = getMoveDestination()
        #Otherwise make the move automatically
        else:
            print('Your selection: '+selection)
            userFinal = 0
            for char in quarterString:
                if char == '-':
                    break;
                userFinal += 1
                
        #
        if('--' in quarterString):
            #If there is an empty gap, split off of that gap and concatenate halves
            #with the selection. Then replace the original selection with '--'
            quarterString = quarterString.split('--')
            quarterString = quarterString[0] + selection + quarterString[1]
            if(userInput == 0):
                quarterString = quarterString[2:]
            elif(userInput == len(quarterString)-2):
                quarterString = quarterString[:-2]
            else:
                quarterString = quarterString[:userInput] + '--' + quarterString[userInput+2:]
        else:
            #This will do moves based off the fact that there are no empty gaps.
            #If user selects first two coins, then automatically move them to the other side or
            #string
            if(userInput == 0):
                quarterString = quarterString.strip()
                quarterString = quarterString[2:] + selection
                print(quarterString)
            elif(userInput == len(quarterString.strip())-2):
                #else if they select the last two, move them to the front.
                quarterString = quarterString.strip()
                quarterString = selection + quarterString[:8]
                print(quarterString)
            elif(userFinal == 0):
                #Then, if selection is inside, create a gap then move to front
                quarterString = quarterString.strip()
                quarterString = quarterString[:userInput] + '--' + quarterString[userInput+2:]
                quarterString = selection + quarterString
            else:
                #Or create a gap and move to end.
                quarterString = quarterString.strip()
                quarterString = quarterString[:userInput] + '--' + quarterString[userInput+2:]
                quarterString = quarterString + selection
        #increment index.
        loopIndex += 1

    #Check to see if the user has won, print corresponding message.
    if(quarterString == 'HTHTHTHTHT' or quarterString == 'THTHTHTHTH'):
        print('Congratulations! You win!')
    else:
        print('You lose, better luck next time.')

    #Pause the program before exitting.
    print('Press \'Enter\' to exit...')
    input('')
    

#Define the main of the program.
if __name__ == '__main__': 
  main()

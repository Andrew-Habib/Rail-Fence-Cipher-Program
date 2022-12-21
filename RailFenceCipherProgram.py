'''
Andrew Habib
12 March 2021
Rail Fence Cipher Program
'''

'''
 Function #1 - Encrypting (To be executed when str_choice is equivalent to the integer 1)
 Formulate a function that would encrypt a message that the user enters
 The function will contain 2 parameters:
 1) Message: The message that the user will enter to be encrypted
 2) Number(num): How many positions down the alphabet the user would like to replace each letter with
'''
def encrypt(message, num):
    
    # Declare 2 variables (Sub-strings) to represent each "rail of the fence"
    # Purpose is to select and manipulate the stance of each character to reorganize the order 
    
    # Declare a string variable to store every other character beginning with 0 and ending with the length of the message
    # Stores and combines characters positioned in the odd # indexes
    str_fenceRail1 = message[0:len(message):2]
    
    # Declare a string variable to store every other character beginning with 1 and ending with the length of the message
    # Stores and combines characters positioned in the even # indexes
    str_fenceRail2 = message[1:len(message):2]
    
    '''
    *Another way to execute the code above:
    
    currentIndex = 0
    str_fenceRail1 = ""
    str_fenceRail2 = ""
    while currentIndex < len(message):
        str_fenceRail1 = str_fenceRail1 + message[currentIndex]
        currentIndex += 2
     
    currentIndex = 1
    while currentIndex < len(message):
        str_fenceRail2 = str_fenceRail2 + message[currentIndex]
        currentIndex += 2
    ''' 
    
    # Update the message variable to resemble the new message following the rearranging of characters
    # The new manipulated message will be composed of the odd characters followed by the even characters of the user's message
    message = str_fenceRail1 + str_fenceRail2
    
    # Declare and initialize the variable that will store the final encrypted message when it has been formed
    str_encryption = ""
    
    # Commence a counted loop (for loop)
    # Purpose of loop is to increase the value of each letter in accordance with the ASCII table according to the key number stated by the user
    # Loop will cycle through each of the original characters in the order they appear in the latest alteration of the message
    for str_originalCharacter in message:
        
        # Declare a variable that would convert and store each character in the message as its correspondent integer ASCII Value
        asciiValue = ord(str_originalCharacter)
        
        # Check if the character itself is alphabetical in order to execute the code below
        if (chr(asciiValue)).isalpha() == True:
            
            # If the character is alphabetical, its ASCII value must increase by the key number stated by the user
            asciiValue = asciiValue + num
            
            '''
            The purpose of the if statement is to ensure that upper case letters remain upper case,
            lower case letters remain lower case and special characters (#, %, @, !,etc.) remain
            unaltered as per the encryption criteria for the program.
            ''' 
            
            # For characters that are all alphabetical:
            
            '''
            Check if:
            1) Each of the original characters are Upper-case and
            2) Each new ASCII Value is either greater than 90 or less than 65 (Before A or after Z)
            (Out of the range of upper case letters)
            '''
            if str_originalCharacter.isupper() == True and (asciiValue > 90 or asciiValue < 65):
            
                # Update the ASCII Value variable by subtracting its own current value by 26
                # This will only execute assuming that the new ASCII Value based on the key Number results in a character that is not upper case or alphabetical
                # If the ASCII Value passes Z, it will subtract 26 to resemble restarting at A until the new upper case value is reached from that point
                asciiValue = asciiValue - 26
                
                # Update the ASCII Value Variable
                # Re-convert each ASCII Value to a character to formulate the new encrypted character
                asciiValue = chr(asciiValue)
                
                '''
                This is the second condition that is to be checked after verifying that the character is not upper case
                Check if:
                1) Each of the original characters are Lower-case and
                2) Each new ASCII Value is either greater than 122 or less than 97 (Before a or after z)
                (Out of the range of lower case letters)
                '''
            elif str_originalCharacter.islower() == True and (asciiValue < 97 or asciiValue > 122):
                
                # Update the ASCII Value variable by subtracting its own current value by 26
                # This will only execute assuming that the new ASCII Value based on the key Number results in a character that is not lower case or alphabetical
                # If the new ASCII Value passes "z", it will subtract 26 to resemble restarting at "a" until the new lower case value is reached from that point
                asciiValue = asciiValue - 26
                
                # Update the ASCII Value Variable
                # Re-convert each ASCII Value to a character to formulate the new encrypted character 
                asciiValue = chr(asciiValue)
                
            # If the conditions above are not true, convert the ASCII Value to a character without further manipulation    
            else:
                asciiValue = chr(asciiValue)
                
        # If the original inputted character is not alphabetical to begin with, covert the special charcter's ASCII Value back to a character without altering it      
        else:
            asciiValue = chr(asciiValue)
        
        # Finally, each fully manipulated character will be added to the encryption variable one by one to complete the encryption
        # This variable will be used to formulate the final encrypted message and output it to the user
        str_encryption = str_encryption + asciiValue
    
    # Output the user's encrypted message    
    print("Your encrypted message is: ", str_encryption)
        

'''
 Function #2 - Decrypting (To be executed when str_choice is equivalent to the integer 2)
 Formulate a function that would decrypt a message that the user enters
 The function will contain 2 parameters:
 1) Message: The message that the user will enter to be decrypted
 2) Number(num): How many positions down the alphabet the user would like to replace each letter with
'''           
def decrypt(message, num):
    
    # Declare and initialize all new variables that will aid in storing string values to later manipulate them and output a decrypted message
    
    # Declare and initialize the first "Fence Rail"
    # Variable will be used to extract the first half of the message 
    str_fenceRail1 = ""
    
    # Declare and initialize the second "Fence Rail"
    # Variable will be used to extract the second half of the message
    str_fenceRail2 = ""
    
    # Declare and initialize a variable to resemble the user's message decrypted half-way
    str_halfDecryption = ""
    
    # Declare and initialize a variable to resemble the user's message fully decrypted
    # This variable will be the final product after manipulating the user's message's characters that will be outputted
    str_decryption = ""
    
    # Commence a counted loop (for loop) to start decrypting
    # Purpose of loop is to decrease the value of each letter in accordance with the ASCII table according to the key number stated by the user
    # Loop will cycle through each of the original characters in the order they appear 
    # This will formulate a half decrypted message that will proceed to be decrypted further in later code
    for str_originalCharacter in message:
        
        # Declare a variable that would convert and store each character in the message as its correspondent integer ASCII Value
        asciiValue = ord(str_originalCharacter)
        
        # Check if the character itself is alphabetical in order to execute the code below
        if (chr(asciiValue)).isalpha() == True:
            
            # Opposite to encryption as decryption will only decrease the ASCII value of each character (Value going left instead of right)
            # If the character is alphabetical, its ASCII value must decrease by the key number stated by the user
            asciiValue = asciiValue - num
            
            '''
            The purpose of the if statement is to ensure that upper case letters remain upper case,
            lower case letters remain lower case and special characters (#, %, @, !,etc.) remain
            unaltered as per the decryption criteria for the program.
            ''' 
            
            # For characters that are all alphabetical:
            
            '''
            Check if:
            1) Each of the original characters are Upper-case and
            2) Each new ASCII Value is either greater than 90 or less than 65 (Before A or after Z)
            (Out of the range of upper case letters)
            '''

            if str_originalCharacter.isupper() == True and (asciiValue > 90 or asciiValue < 65):
            
                # Update the ASCII Value variable by adding its own current value by 26
                # This will only execute assuming that the new ASCII Value based on the key Number results in a character that is not upper case or alphabetical
                # If the ASCII Value lies before A, it will add 26 to resemble restarting at Z until the new upper case value is reached from that point
                asciiValue = asciiValue + 26
                
                # Update the ASCII Value Variable
                # Re-convert each ASCII Value to a character to formulate the new decrypted character 
                asciiValue = chr(asciiValue)
                
                '''
                This is the second condition that is to be checked after verifying that the character is not upper case
                Check if:
                1) Each of the original characters are Lower-case and
                2) Each new ASCII Value is either greater than 122 or less than 97 (Before a or after z)
                (Out of the range of lower case letters)
                '''
            elif str_originalCharacter.islower() == True and (asciiValue < 97 or asciiValue > 122):
                
                # Update the ASCII Value variable by adding its own current value by 26
                # This will only execute assuming that the new ASCII Value based on the key Number results in a character that is not lower case or alphabetical
                # If the new ASCII Value lies before "a", it will add 26 to resemble restarting at "z" until the new lower case value is reached from that point
                asciiValue = asciiValue + 26
                
                # Update the ASCII Value Variable
                # Re-convert each ASCII Value to a character to formulate the new decrypted character
                asciiValue = chr(asciiValue)
                
            # If the conditions above are not true, convert the ASCII Value to a character without further manipulation    
            else:
                asciiValue = chr(asciiValue)
                
        # If the original inputted character is not alphabetical to begin with, covert the special charcter's ASCII Value back to a character without altering it      
        else:
            asciiValue = chr(asciiValue)
        
        # Finally, each fully manipulated character will be added to the half-decrypt variable one by one to complete the decryption
        # This variable will be used to formulate the half way decrypted message
        # This is only decrypted half way as only the individuals letters have been manilpulated
        # The next step is to manipulate their location in the message
        str_halfDecryption = str_halfDecryption + asciiValue    
    
    # Check if the half decrypted message has an even number of characters
    if len(str_halfDecryption) % 2 == 0:
        
        # Declare 2 variables (Sub-strings) to represent each "rail of the fence"
        # Purpose is to select and manipulate the stance of each character to reorganize the order 
        
        # Update a string variable to store the first half of the message
        # Each of the characters in this fence Rail will be placed in the odd number positions when creating the final decrypted message
        str_fenceRail1 = str_halfDecryption[0:(len(str_halfDecryption)//2)]
        
        # Update a string variable to store the second half of the message
        # Each of the characters in this fence Rail will be placed in the even number positions when creating the final decrypted message
        str_fenceRail2 = str_halfDecryption[(len(str_halfDecryption)//2):len(str_halfDecryption)]
    
    # Otherwise, the half decrypted message must be odd  
    else:
        
        # Update a string variable to store the first half of the message
        # The first half will have an extra string to its name to resemble the extra character from the odd number of characters
        # Each of the characters in this fence Rail will be placed in the odd number positions when creating the final decrypted message
        str_fenceRail1 = str_halfDecryption[0:(len(str_halfDecryption)//2) + 1]
        
        # Update a string variable to store the second half of the message
        # The second half will have the remaining characters and should have one less than the first rail
        # Each of the characters in this fence Rail will be placed in the even number positions when creating the final decrypted message
        str_fenceRail2 = str_halfDecryption[(len(str_halfDecryption)//2) + 1:len(str_halfDecryption)] 
    
    # Declare and initialize the current index
    # Variable will be used to go through each character as it will be updated every while loop
    str_currentIndex = 0
    
    
    # Do this while the current index is less than half the length of the half decrypted message
    while str_currentIndex < (len(str_halfDecryption) // 2):
        
        # Check if the half decrypted message has an even number of characters
        if len(str_halfDecryption) % 2 == 0:
            
            # Update the finally decrypted message according to the index
            # Start at the 0th index
            # The first fence rail's character will be added followed by the second fence rail's character until the index reaches half of the length of the half decrypted message
            str_decryption = str_decryption + str_fenceRail1[str_currentIndex]
            str_decryption = str_decryption + str_fenceRail2[str_currentIndex]
            
            # Update the current index by adding one to move on to the following characters 
            str_currentIndex = str_currentIndex + 1
            
        # Otherwise, the half decrypted message must be odd
        else:
            
            # Update the finally decrypted message according to the index
            # Start at the 0th index
            # The first fence rail's character will be added followed by the second fence rail's character until the index reaches half of the length of the half decrypted message
            str_decryption = str_decryption + str_fenceRail1[str_currentIndex]
            str_decryption = str_decryption + str_fenceRail2[str_currentIndex]
            
            # Update the current index by adding one to move on to the following characters 
            str_currentIndex = str_currentIndex + 1
            
            # Only applicable to messages with odd lengths
            # Check if the current index has finally reached the half of the length of the half decrypted message
            if str_currentIndex == len(str_halfDecryption) // 2:
                
                # Add the final odd character coming from the first fence rail to the final decrypted message before ending the loop
                str_decryption = str_decryption + str_fenceRail1[str_currentIndex]
    
    # Output the user's decrypted message
    print("Your decrypted message is: ", str_decryption)
           

'''
 Function #3 - Brute Forcing (To be executed when str_choice is equivalent to the integer 3)
 Formulate a function that would brute force a message that the user enters (Decrypting every possible combination according to the alphabet)
 The function will contain only 1 parameter:
 1) Message: The message that the user will enter to be brute forced
 --> The exact same as decrypting but with listing all 26 possibilities and decryptions
'''           
def bruteForce(message):
    
    '''
    Repeat the decryption 26 times to resemble all possible combination as there are 26 letters in the alphabet
    --> Instead of asking the user for a key number, the code below will automatically execute 26 times
    to output all possible decrypting possibilities
    '''
    for counter in range(1, 27):
        # Declare and initialize all new variables that will aid in storing string values to later manipulate them and output a decrypted message
    
        # Declare and initialize the first "Fence Rail"
        # Variable will be used to extract the first half of the message 
        str_fenceRail1 = ""
        
        # Declare and initialize the second "Fence Rail"
        # Variable will be used to extract the second half of the message
        str_fenceRail2 = ""
        
        # Declare and initialize a variable to resemble the user's message decrypted half-way
        str_halfDecryption = ""
        
        # Declare and initialize a variable to resemble the user's message fully decrypted
        # This variable will be the final product after manipulating the user's message's characters that will be outputted
        str_decryption = ""
        
        # Commence a counted loop (for loop) to start decrypting
        # Purpose of loop is to decrease the value of each letter in accordance with the ASCII table according to the key number stated by the user
        # Loop will cycle through each of the original characters in the order they appear 
        # This will formulate a half decrypted message that will proceed to be decrypted further in later code
        for str_originalCharacter in message:
            
            # Declare a variable that would convert and store each character in the message as its correspondent integer ASCII Value
            asciiValue = ord(str_originalCharacter)
            
            # Check if the character itself is alphabetical in order to execute the code below
            if (chr(asciiValue)).isalpha() == True:
                
                # Opposite to encryption as decryption will only decrease the ASCII value of each character (Value going left instead of right)
                # If the character is alphabetical, its ASCII value must decrease by the key number stated by the user
                asciiValue = asciiValue - counter
                
                '''
                The purpose of the if statement is to ensure that upper case letters remain upper case,
                lower case letters remain lower case and special characters (#, %, @, !,etc.) remain
                unaltered as per the decryption criteria for the program.
                ''' 
                
                # For characters that are all alphabetical:
                
                '''
                Check if:
                1) Each of the original characters are Upper-case and
                2) Each new ASCII Value is either greater than 90 or less than 65 (Before A or after Z)
                (Out of the range of upper case letters)
                '''
    
                if str_originalCharacter.isupper() == True and (asciiValue > 90 or asciiValue < 65):
                
                    # Update the ASCII Value variable by adding its own current value by 26
                    # This will only execute assuming that the new ASCII Value based on the key Number results in a character that is not upper case or alphabetical
                    # If the ASCII Value lies before A, it will add 26 to resemble restarting at Z until the new upper case value is reached from that point
                    asciiValue = asciiValue + 26
                    
                    # Update the ASCII Value Variable
                    # Re-convert each ASCII Value to a character to formulate the new decrypted character 
                    asciiValue = chr(asciiValue)
                    
                    '''
                    This is the second condition that is to be checked after verifying that the character is not upper case
                    Check if:
                    1) Each of the original characters are Lower-case and
                    2) Each new ASCII Value is either greater than 122 or less than 97 (Before a or after z)
                    (Out of the range of lower case letters)
                    '''
                elif str_originalCharacter.islower() == True and (asciiValue < 97 or asciiValue > 122):
                    
                    # Update the ASCII Value variable by adding its own current value by 26
                    # This will only execute assuming that the new ASCII Value based on the key Number results in a character that is not lower case or alphabetical
                    # If the new ASCII Value lies before "a", it will add 26 to resemble restarting at "z" until the new lower case value is reached from that point
                    asciiValue = asciiValue + 26
                    
                    # Update the ASCII Value Variable
                    # Re-convert each ASCII Value to a character to formulate the new decrypted character
                    asciiValue = chr(asciiValue)
                    
                # If the conditions above are not true, convert the ASCII Value to a character without further manipulation    
                else:
                    asciiValue = chr(asciiValue)
                    
            # If the original inputted character is not alphabetical to begin with, covert the special charcter's ASCII Value back to a character without altering it      
            else:
                asciiValue = chr(asciiValue)
            
            # Finally, each fully manipulated character will be added to the half-decrypt variable one by one to complete the decryption
            # This variable will be used to formulate the half way decrypted message
            # This is only decrypted half way as only the individuals letters have been manilpulated
            # The next step is to manipulate their location in the message
            str_halfDecryption = str_halfDecryption + asciiValue    
        
        # Check if the half decrypted message has an even number of characters
        if len(str_halfDecryption) % 2 == 0:
            
            # Declare 2 variables (Sub-strings) to represent each "rail of the fence"
            # Purpose is to select and manipulate the stance of each character to reorganize the order 
            
            # Update a string variable to store the first half of the message
            # Each of the characters in this fence Rail will be placed in the odd number positions when creating the final decrypted message
            str_fenceRail1 = str_halfDecryption[0:(len(str_halfDecryption)//2)]
            
            # Update a string variable to store the second half of the message
            # Each of the characters in this fence Rail will be placed in the even number positions when creating the final decrypted message
            str_fenceRail2 = str_halfDecryption[(len(str_halfDecryption)//2):len(str_halfDecryption)]
        
        # Otherwise, the half decrypted message must be odd  
        else:
            
            # Update a string variable to store the first half of the message
            # The first half will have an extra string to its name to resemble the extra character from the odd number of characters
            # Each of the characters in this fence Rail will be placed in the odd number positions when creating the final decrypted message
            str_fenceRail1 = str_halfDecryption[0:(len(str_halfDecryption)//2) + 1]
            
            # Update a string variable to store the second half of the message
            # The second half will have the remaining characters and should have one less than the first rail
            # Each of the characters in this fence Rail will be placed in the even number positions when creating the final decrypted message
            str_fenceRail2 = str_halfDecryption[(len(str_halfDecryption)//2) + 1:len(str_halfDecryption)] 
        
        # Declare and initialize the current index
        # Variable will be used to go through each character as it will be updated every while loop
        str_currentIndex = 0
        
        
        # Do this while the current index is less than half the length of the half decrypted message
        while str_currentIndex < (len(str_halfDecryption) // 2):
            
            # Check if the half decrypted message has an even number of characters
            if len(str_halfDecryption) % 2 == 0:
                
                # Update the finally decrypted message according to the index
                # Start at the 0th index
                # The first fence rail's character will be added followed by the second fence rail's character until the index reaches half of the length of the half decrypted message
                str_decryption = str_decryption + str_fenceRail1[str_currentIndex]
                str_decryption = str_decryption + str_fenceRail2[str_currentIndex]
                
                # Update the current index by adding one to move on to the following characters 
                str_currentIndex = str_currentIndex + 1
                
            # Otherwise, the half decrypted message must be odd
            else:
                
                # Update the finally decrypted message according to the index
                # Start at the 0th index
                # The first fence rail's character will be added followed by the second fence rail's character until the index reaches half of the length of the half decrypted message
                str_decryption = str_decryption + str_fenceRail1[str_currentIndex]
                str_decryption = str_decryption + str_fenceRail2[str_currentIndex]
                
                # Update the current index by adding one to move on to the following characters 
                str_currentIndex = str_currentIndex + 1
                
                # Only applicable to messages with odd lengths
                # Check if the current index has finally reached the half of the length of the half decrypted message
                if str_currentIndex == len(str_halfDecryption) // 2:
                    
                    # Add the final odd character coming from the first fence rail to the final decrypted message before ending the loop
                    str_decryption = str_decryption + str_fenceRail1[str_currentIndex]
        
        # Format the counter 10 spaces to the left as an integer to resemble the number of combinations
        # Also output the final decrypted message for each counter value (Each key number value)
        print("{:<10d}".format(counter), str_decryption)




# Formatting Variables

# Declare a variable to center the title within 70 spaces
str_centerTitle = "{:^70s}".format

# Declare a variable to left justify the user input within 35 spaces
'''
--> This variable will be used to format any input related data including the user's choice, 
their message along with the key number.
''' 
str_formatUserInput = "{:<35s}".format


# Main Program
# Declare and initialize the variable that asks for the user's choice to enable the program to start
int_choice = 0

# Output a centered title that would greet the player when they first enter the program
# Output 31 dashes center justified to compliment the length of the title
print(str_centerTitle("Welcome to Rail Fence Cipher!"))
print(str_centerTitle("-" * 31))
print()


# Do while the choice is not equivalent to 4 (Option to quit)
# The program will keep re-running until the user chooses not to keep going
while int_choice != 4: 
           
    # Outputting the user's options
    # Follows the greeting and informs the user of what number they may enter either encrypt, decrypt, brute force or quit
    print("Please select one of the following options:")
    print()
    print("1 - Encrypt a message")
    print("2 - Decrypt a message")
    print("3 - Brute force")
    print("4 - QUIT")
    print()
    
    # Declare and initialize a variable storing a boolean value for whether the user's choice is valid or not
    # Must start as false to commence the loop
    str_validChoice = False
    
    # Declare and initialize a variable storing a boolean value for whether the key number is valid or not
    # Must start as false to commence the loop
    str_validKeyNumber = False
    
    # Do while the user's choice is invalid
    while str_validChoice == False:
    
        # Formulating error handlers that catch ValueError errors or regular run-time errors when the user enters invalid input
        # Try to declare a variable that stores the user's choice
        try:
            
            # Declare a variable as an integer to store the user's choice
            # Prompt the user to enter a choice between 1 and 4
            # This variable will determine which function will be called to to serve the user's requirement
            int_choice = int(input(str_formatUserInput("Enter your choice (1-4):")))
        
        # Error Handler
        # Catch the exception that gets thrown if a ValueError rises when the user enters invalid input    
        except ValueError:
            
            # Inform the user that the value they entered is invalid and they must enter an integer
            print()
            print("Invalid choice! Please enter an integer.")
            print()
            
        # Otherwise, there is no ValueError and the program will check for other criteria
        else:
            
            # Check if the user did not enter a choice between 1 and 4
            if int_choice != 1 and int_choice != 2 and int_choice != 3 and int_choice != 4:
                
                # Update the variable to keep the validity equivalent to false to keep looping the prompt for the choice
                str_validChoice = False
                
                # Also, inform the user that their choice is invalid and they must enter a number between 1-4
                print()
                print("Invalid choice! Please enter a number between 1-4.")
                print()
                
            # Otherwise, the user entered a choice between 1-4 and the code below will execute
            else:
                
                # Make the validity variable true to break out of the choice loop
                str_validChoice = True
                print()
    
    # Check if the choice is not equivalent to 4 (Choice to quit)
    if int_choice != 4:
        
        # Declare a variable as a string to store the message that the user would like to manipulate
        # Prompt the player to enter their message
        # The message would be used as a parameter to the functions to manipulate their characters in order to encrypt, decrypt or brute force
        str_message = str(input(str_formatUserInput("Enter your message:")))
        print()
        
        # Check if the choice is not equivalent to 3
        if int_choice != 3:
            
            # Do while the Key number is invalid or False
            while str_validKeyNumber == False:
                
                # Formulating an error handler that catches ValueError errors or regular run-time errors when the user enters invalid input
                # Try to declare a variable that stores the key number as an integer (Error handler will come in if it is not an integer)
                try:
                    
                    # Declare a variable as an integer to store the key number
                    # Prompt the user to enter a key number between 1 and 26
                    # This variable will be used for encryption and decryption to determine how many numbers each character's ASCII Value will change
                    int_keyNumber = int(input(str_formatUserInput("Enter the key number (1-26):"))) 
                    
                # Error Handler
                # Catch the exception that gets thrown if a ValueError rises when the user enters invalid input
                except ValueError:
                    
                    # Inform the user that their key is invalid and they must enter an integer
                    print()
                    print("Invalid key! Please enter an integer.")
                    print()
                    
                # Otherwise, there is no ValueError and the program will check for other criteria   
                else:
                    
                    # Check if the user entered a key number between 1 and 26
                    if int_keyNumber >= 1 and int_keyNumber <= 26:
                        
                        # Make the validity of the key number true to break out of the loop 
                        str_validKeyNumber = True
                        print() 
                        
                    # Otherwise, the user entered an integer that is not between 1 and 26
                    else:
                        
                        # Update the variable to keep the validity equivalent to false to keep looping the prompt for the key number
                        str_validKeyNumber = False
                        
                        # Inform the user that they entered an invalid key number and they must enter a number between 1 and 26
                        print()
                        print("Invalid key! Please enter a number between 1-26.")
                        print()             
            
        
        # If the user chooses 1, the program will make a call to the encrypting function and encrypt the user's message    
        if int_choice == 1:
            encrypt(str_message, int_keyNumber)
            print()
        
        # If the user chooses 2, the program will make a call to the decrypting function and decrypt the user's message   
        elif int_choice == 2:
            decrypt(str_message, int_keyNumber)
            print()
        
        # If the user chooses 3, the program will make a call to the brute force function and brute force the user's message  
        elif int_choice == 3:
            print("Your decrypted message is:")
            print()
            bruteForce(str_message)
            print()
    
    # If the choice is equivalent to 4, the program will terminate altogether as the user is choosing to quit       
    else:
        break
       
                

            
            








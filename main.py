def welcomeMessage():
    print ("\n" + "Welcome to Caesar Cipher, this application allows users to encode or decode a message.")
    print ("The encode function identifies and shifts each letter within a message, alongside the alphabet a fixed number of times.")
    print ("This fixed number is called a Cipher key; these keys are defined when encoding a message and can be used to decode a message back to its original state." + "\n")
    return 0

def userInput():
    while True:
        userChoice = input("Would you like to encode or decode a message? ")
        userChoice = userChoice.upper()
        if (userChoice == "ENCODE" or userChoice == "DECODE"):
            break

        else:
            userChoice = input('ERROR: Incorrect input. Please type "Encode" or "Decode": ')

    while True:
        if (userChoice == "ENCODE"):
            userMessage = input("Enter a message to encode: ")
            break
            
        elif (userChoice == "DECODE"):
            userMessage = input("Enter a message to decode: ")
            break
    
    
    while True:
        userKey = input("Enter a Cipher Key? ")
        if (userKey.isdigit() == True):
            userKey = int(userKey)
            break
        else:
            userKey = input("ERROR: Incorrect input. Please type a numeric value: ")

    return userChoice, userMessage, userKey

try:
    running = True
    welcomeMessage()
    while (running == True):
        userData = userInput()
        print ("\n" + "userChoice = " + userData[0])
        print ("userMessage = " + userData[1])
        print ("userKey = " + str(userData[2]))

        exitApplication = input ("\n" + "Would you like to restart the application? ")
        exitApplication = exitApplication.upper()

        while True:
            if (exitApplication == "YES"):
                print ("Restarting the application." + "\n")
                break

            elif (exitApplication == "NO"):
                print ("Exiting the application." + "\n")
                running = False
                break

            else:
                exitApplication = input ('ERROR: Incorrect input. Please type "Yes" or "No": ')
                exitApplication = exitApplication.upper()

except KeyboardInterrupt:
    print ("\n" + "KEYBOARD INTERRUPT: Exiting the application.")
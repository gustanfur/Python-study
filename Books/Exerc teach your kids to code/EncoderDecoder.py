#Transforming letters and numbers       - pag 99 - Teach your kids to code

message = input("Enter a message to encode or decode: ")        #Get a message
message = message.upper()                   #Make it all UPPERCASE
output = ""                                 #Create an empty string to hold output
for letter in message:                      #Loop through each letter of the message
    if letter.isupper():                    #If the letter is in the alphabet (A-Z),
        value = ord(letter) + 13            #Shit the letter value up by 13
        if not letter.isupper():            #and check to see if we shfited too far
            value -= 26                     #if we did, wrap it back around Z->A
            letter = chr(value)             #by subtracting 26 from te letter value
    output += letter                        #Add the letter to our output string
print("Output message: ", output)
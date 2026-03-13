# Development Log

## 03-13-26 12:11 AM

In this project I need to implement three separate programs that communicate with each other using. The three programs are a logger, an encryption program, and a driver program that interacts with the user.

For this project, I plan on using Python, which means I will need to use the subprocess module to create the logger and encryption processes. Pipes will be used to communicate between the driver and these programs.

The encryption program will implement the Vigenère cipher as I was instructed. The driver program will manage the user menu, command parsing, and maintaining a history of encrypted/decrypted strings.

### Plan
The project will be implemented in the following order:

1. Create the logger program
2. Implement PASS and ENCRYPT in encryption program
3. Implement DECRYPT and QUIT in encryption program
4. Implement RESULT and ERROR response formatting
5. Implement password and encrypt commands in the driver
6. Implement decrypt and history commands in the driver
7. Implement quit functionality and final cleanup


## 03-13-26 12:20 AM

### Session 1
Starting implementation with the logger program. The logger only needs to read messages from standard input and write them to a file with timestamps.

### Plan
Implement logger.py that:

- Accepts log filename as command line argument
- Reads log messages from stdin
- Stops when receiving QUIT
- Adds timestamps in required format
- Use datetime module for the timestamps

## 03-13-26 12:39 AM

### Session Reflection
I succesfully implemented the logger program.

Initially I forgot to flush the file after writing which caused some messages not to appear immediately. After I added log.flush() this issue was fixed. I also realized that splitting the message needed to handle cases where only the action was provided with no additional message. Finally, I made sure it would log when the quit command was given as well to make the log files clear. I repeatedly tested with normal standard input into a temporary text file. The logger now correctly timestamps entries and writes them in the required format.

## 03-13-26 12:45 AM

### Session 2
Next I will begin implementing the encryption backend. This program will receive commands via stdin and output responses via stdout.

The first commands to implement will be PASS and ENCRYPT.

### Plan
- Store passkey variable
- Learn and then implement Vigenère encryption
- Return RESULT or ERROR responses

## 03-13-26 1:15 AM

### Session Reflection
PASS and ENCRYPT commands were implemented.

I initially only implemented code for the case where the key was the same length as the text. As such, I had to go back and fix this using a mod. I also realized that while testing, I initally forgot to add error handling if the key was not set yet. I assumed all input was provided in uppercase as stated in the project description. As for commands that are not in the list, I plan to add error handling for that after completing all commands for the encryptor program.

## 03-13-26 1:20 AM

### Session 3
Next I will add the DECRYPT and QUIT commands onto the if-elif chain. 

### Plan
- For DECRYPT, just do whatever I did for ENCRYPT backwards. 
- For QUIT, just break out of the for loop and terminate the program

## 03-13-26 1:29 AM

### Session Reflection
Implemented DECRYPT and QUIT commands.

I initially made an error in the decryption formula by adding instead of subtracting the shift value. This is because I was implementing the same formula for the encryption and forgot to switch it the first time around. This produced incorrect output. After correcting the formula the cipher worked properly. Handling the command itself was the same so it was pretty simple. QUIT command simply just breaks so that was very simple to implement. I tested the same way I did for ENCRYPT and all tests were passed, including wraparounds. 

## 03-13-26 1:35 AM

### Session 4
So I had a brain fart and realized that the RESULT and ERROR commands are not commands to be added to the if-elif chain and I already have them added as I was following the example on the docs. As such, my plan for this section is already completed from the prior code. I will just add error handling for an incorrect command and also label the first word with ERROR.

### Plan
- Just add an else statement if a command that does not exist is entered that outputs an error

## 03-13-26 1:40 AM

### Session Reflection
I added the else statement if a command that does not exist is entered and tested it really quick with random words as the command. Everything is as expected.
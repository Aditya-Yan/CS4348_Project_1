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

## 03-13-26 1:45 AM

### Session 5
The logger and encryption program are working fine, so I can now begin building the driver. This is the part of the project that ties everything together using subprocesses.

I expect this session to be harder than the earlier ones because the driver has to manage user interaction while also communicating correctly with the logger and encryption programs.

### Plan
This session will focus on the password and encrypt commands for the driver program.

- Start driver.py
- Launch the logger process with the log filename argument
- Launch the encryption program as a child process
- Connect to both processes using pipes
- Implement the password command
- Implement the encrypt command
- Store encrypted/decrypted strings in history
- Make sure passwords are not stored in history
- Make sure whatever happens is logged via the log process 
- Test communication between driver and encryption program

I will try to modularize as much as possible for clean code and ease of implementation.

## 03-13-26 2:07 AM

### Mid-Session Thought
Modularizing this session would make the code much more readable and better. I am catching myself reusing the same code especially when sending input to the other two processes. I will go back now and redo the code more modularly.

## 03-13-26 2:30 AM

### Mid-Session Thought
Error handling is being a big pain right now, I think before I continue coding I will write down all my test cases to figure out which errors need to be accounted for. Also, I am not sure if quick errors such as choosing an invalid index on the history selection shoul be logged or not. I think I will not log them as to make the log file less cluttered and will just reprompt the user in the terminal.

## 03-13-26 2:45 AM

### Session Reflection
This was the hardest section to implement by far. I started off by creating a method to just write standard input to my logger file to be logged in the text file and a method to write standard input to the encryptor program to run its commands. Then for simplification, I created many functions to help me such as outputting a menu for the user to choose from the history or enter a new string. I made this function multiuse for password and encrypt by having a flag to see if the string and output should be stored to memory or not. I also created a quick function to view the history. Getting into the main function, I started off by creating my two subprocesses using the subprocess library as instructed. Then I sent the start driver message to the logger using the function mentioned before. 

The biggest annoyances I had while coding this section was the error handling. I had to make sure the program did not break when an incorrect number was selected, when the history is empty, when an incorrect command is inputted. Another annoyance was forgetting to send messages to the log, so I had to go back many times to insert those commands. 

Finally, I introduced a way to go back to the previous menu or prompt if needed so the entire code does not need to be restarted if the user changes their mind. Also, I did not make the history persistent between sessions as I was not sure if that was a part of the requirement.

After doing all of this, my code works correctly and I tested it repeatedly by cycling through the commands. Everything is stored and logged as needed and the encryption is working correctly. With experience from this session, I hope to speed up the future sessions which should be similar to the code written in this one.

## 03-13-26 3:06 AM

### Session 5 Extended

I realized that when an encryption is tried without a key being set, the string is still saved to history. Made a quick update to make sure it does not save if there is not key set.

## 03-13-26 3:14 AM

### Session 6
Looking at the decrypt and history commands, it does not seem too complicated. I can reuse my code I used for encrypt with decrypt but just send a different command to the encryption program. For history, I just need to enumerate the array containing the history. I believe this session should not be too bad and should not take too long.

### Plan
- Reuse code used in encrypt command for decrypt command
- Use enumerate to show history. I already have a function to show history so I can just use it

## 03-13-26 3:20 AM

### Mid-Session Thought
I am changing my gameplan a little. I was able to implement decrypt and history very quickly and do not think quit will take long either. I will implement quit during this session. I plan on doing this by first shutting down the other two programs. I can send a QUIT command to the encrypot and logger as this was implemented in the previous sessions. Then I just use break to end the loop in the driver file and finish the driver process. I will then do final checkups tomorrow.

## 03-13-26 3:28 AM

### Session Reflection
As mentioned before, I was able to easily implement decrypt and history commands using previously done code. For the quit command, I simply sent standard input to both logger and encryption programs saying "QUIT" and then waited so they could peacefully end their programs. I have also tested out these newly added commands by running through the menus and commands multiple times. Everything seems in order. I will do my final checkup and test tomorrow.
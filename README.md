# GITHUB LINK

https://github.com/Aditya-Yan/CS4348_Project_1


## Overview

This project implements a small system consisting of three separate programs that communicate using pipes. The system allows a user to encrypt and decrypt strings using a Vigenère cipher while logging all actions to a file.

The entire system is started by running the **driver program**, which launches the **logger** and **encryption** programs as subprocesses and communicates with them.

The system was implemented in **Python** using the `subprocess` module.

---

# Files

## driver.py
This is the main program that the user runs.

Responsibilities:
- Starts the logger and encryption programs as subprocesses
- Communicates with them through pipes
- Displays the command menu
- Accepts user commands
- Maintains a history of strings entered during the program run
- Logs all commands and results to the logger program

Supported commands:
- `password` – set the encryption passkey
- `encrypt` – encrypt a string
- `decrypt` – decrypt a string
- `history` – display previously used strings
- `quit` – exit the program

The driver also allows users to:
- enter new strings
- reuse strings stored in history

---

## encryptor.py
This program performs encryption and decryption.

It runs as a subprocess and receives commands from the driver through **standard input**.

Supported commands:

- `PASS <key>`  
  Sets the passkey used for encryption/decryption.

- `ENCRYPT <text>`  
  Encrypts the given text using a Vigenère cipher.

- `DECRYPT <text>`  
  Decrypts the given text using the Vigenère cipher.

- `QUIT`  
  Terminates the encryption program.

Responses returned to the driver:

- `RESULT <value>` – successful command
- `ERROR <message>` – command failed

The encryption program assumes all input consists of **uppercase letters only**.

---

## logger.py
This program logs system activity to a log file.

It runs as a subprocess and receives log messages from the driver through **standard input**.

Each log entry is written in the format: YYYY-MM-DD HH:MM [ACTION] MESSAGE

# How to Run the Program

## Requirements
- Python 3 installed
- All three files located in the same directory

---

## Running the System

Run the driver program from the command line and include a text file as an argument so the log can be written somewhere


# Notes

- History only lasts for the duration of the program run.

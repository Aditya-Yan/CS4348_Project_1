import subprocess
import sys

history = []

logger = None
encryptor = None


def send_log(message):
    logger.stdin.write(message + "\n")
    logger.stdin.flush()

def send_encryptor_command(command, argument):
    encryptor.stdin.write(f"{command} {argument}\n")
    encryptor.stdin.flush()
    response = encryptor.stdout.readline().strip()
    return response

def show_history():
    if not history:
        print("History is empty.")
        return

    for i, item in enumerate(history):
        print(f"{i}: {item}")


def get_string_from_user(store_in_history=True, prompt_text="Enter text: "):
    while True:
        print("Choose input method:")
        print("1. Enter a new string")
        print("2. Use a string from history")
        print("3. Cancel")

        choice = input("Selection: ").strip()

        if choice == "1":
            user_text = input(prompt_text).strip().upper()
            if not user_text.isalpha():
                print("Error: input must contain only letters.")
                continue

            if store_in_history:
                history.append(user_text)

            return user_text

        elif choice == "2":
            if not history:
                print("History is empty. Please enter a new string instead.")
                continue

            show_history()
            selection = input("Enter history number or B to go back: ").strip()

            if selection.upper() == "B":
                continue

            if not selection.isdigit():
                print("Error: invalid history selection.")
                continue

            index = int(selection)
            if index < 0 or index >= len(history):
                print("Error: history selection out of range.")
                continue

            return history[index]

        elif choice == "3":
            return None

        else:
            print("Error: invalid menu option.")


def main():
    global logger, encryptor

    if len(sys.argv) != 2:
        print("Usage: python driver.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]

    logger = subprocess.Popen(
        ["python", "logger.py", logfile],
        stdin=subprocess.PIPE,
        text=True
    )

    encryptor = subprocess.Popen(
        ["python", "encryptor.py"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True
    )

    send_log("START Driver started")

    while True:
        cmd = input("Command: ").strip().lower()

        if cmd == "password":
            pwd = get_string_from_user(
                store_in_history=False,
                prompt_text="Enter password: "
            )

            if pwd is None:
                print("Password command cancelled.")
                continue

            response = send_encryptor_command("PASS", pwd)
            print(response)

            send_log("PASSWORD Password updated")
            send_log(f"RESULT {response}")

        elif cmd == "encrypt":
            text = get_string_from_user(
                store_in_history=True,
                prompt_text="Enter text: "
            )

            if text is None:
                print("Encrypt command cancelled.")
                continue

            response = send_encryptor_command("ENCRYPT", text)
            print(response)

            if response.startswith("RESULT "):
                encrypted_text = response.split(" ", 1)[1]
                history.append(encrypted_text)

            send_log(f"ENCRYPT Request to encrypt string")
            send_log(f"RESULT {response}")
        
        else:
            print("Unknown command entered. Please enter a valid command.")

        


if __name__ == "__main__":
    main()
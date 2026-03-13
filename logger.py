import sys
from datetime import datetime

def main():
    if len(sys.argv) != 2:
        print("Usage: python logger.py <logfile>")
        sys.exit(1)

    logfile = sys.argv[1]

    with open(logfile, "a") as log:
        for line in sys.stdin:
            message = line.strip()

            if message == "QUIT":
                log.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M')} [QUIT] Application terminated\n")
                break

            if not message:
                continue

            parts = message.split(" ", 1)
            action = parts[0]
            msg = parts[1] if len(parts) > 1 else ""

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            log.write(f"{timestamp} [{action}] {msg}\n")
            log.flush()

if __name__ == "__main__":
    main()
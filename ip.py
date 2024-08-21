import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    value = 0
    parts = ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        matches = re.search(r"^([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$", part)
        if not matches:
            return False
    return True







if __name__ == "__main__":
    main()

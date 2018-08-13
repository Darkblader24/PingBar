import subprocess
from time import sleep

url = "www.google.com"
tickrate = 2


def main():
    while True:
        request = subprocess.Popen(
            "ping -n 1 %s" % url,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        out, error = request.communicate()

        count = 0
        for char in url:
            if char == "=":
                count += 1

        ping = ""
        ping_str = str(out).split("=")[count + 1]
        for char in ping_str:
            if char.isdigit():
                ping += char
            else:
                break

        print(ping)

        sleep(1 / tickrate)


if __name__ == "__main__":
    main()

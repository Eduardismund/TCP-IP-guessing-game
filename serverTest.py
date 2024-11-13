
# ===Guess the Number Game (Chaos Edition)===
# Description: A server generates a random number. Multiple clients connect and take turns guessing the number. The server gives hints like "higher" or "lower."
#
# Twist: The server occasionally lies! Instead of giving the correct hint, it might say "higher" when the guess was too high, or "lower" when it was too low.
#
# Challenge: Clients have to decide whether to trust the server or try their luck with random guesses.

import socket
import os
from random import randint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("0.0.0.0", 9000))
s.listen(5)
rNumber = randint(1, 100)

print("The number to guess is: " + str(rNumber))

while True:
    cs, addr = s.accept()
    pid = os.fork()

    if pid == 0:
        s.close()

        while True:

            r = randint(1,5)
            b = cs.recv(10).decode('utf-8').strip()

            try:
                guess = int(b)

                if guess < rNumber:

                    if r != 1:
                        print(f"(The server might lie) Received guess from {addr}: {b} - \nThe result: higher!")
                    else:
                        print(f"(The server might lie) Received guess from {addr}: {b} - \nThe result: lower!")
                    cs.send(b"1\n")

                elif guess > rNumber:

                    if r != 1:
                        print(f"(The server might lie) Received guess from {addr}: {b} - \nThe result: lower!")
                    else:
                        print(f"(The server might lie) Received guess from {addr}: {b} - \nThe result: higher!")

                    cs.send(b"2\n")
                else:

                    print(f"Received guess from {addr}: {b} - The result: equals!")
                    cs.send(b"0\n")
                    break
            except ValueError:
                print(f"Invalid guess received from {addr}: {b}")
                break
        cs.close()
        os._exit(0)
    else:
        cs.close()

import collections
import sys

from Teque import Teque

file = sys.argv[1]
teque = Teque()

with open(file, 'r') as file:
    N = int(file.readline().strip())  # Read the first line as N
    for _ in range(N):
        operation, verdi= file.readline().strip().split()
        verdi= int(verdi)

        if operation == "push_back":
            teque.push_back(verdi)
        elif operation == "push_front":
            teque.push_front(verdi)
        elif operation == "push_middle":
            teque.push_middle(verdi)
        elif operation == "get":
            index = int(verdi)
            print(teque.get(index))

# Det kan  funka med denne koden -- python3 TequeTest.py input/input_100
# Det kan  funka med denne koden -- python3 TequeTest.py input/input_1000
# slikt går det videre...

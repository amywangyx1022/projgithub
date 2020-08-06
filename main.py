# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pandas as pd
import numpy as np

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def display_ages():
    age = [1, 2, 3]
    for number in age:
        print(number)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    display_ages()

    data = np.random.randint(3, 15, size=(10, 2))
    df = pd.DataFrame(data, columns=['randomnumbers', 'yrand'])
    print(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

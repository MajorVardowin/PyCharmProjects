# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from guiTest import gui_test
from gui_anwendung import open_exe


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.
    print("Test")


def testing_gui():
    print("START")

    print("STOP")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if gui_test():
        open_exe()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

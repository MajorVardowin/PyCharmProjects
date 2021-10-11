import PySimpleGUI as sg

nutzer = ''


def check(user, password):
    # for windows
    if user == 'Admin' and password == '1234':
        return True
    elif user == '' and password == '':
        return True
    return False


def gui_test():
    sg.theme('BlueMono')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text('Login to Admin Interface:')],
              [sg.Text('Username:'), sg.InputText(tooltip='Enter Username', key='-INPUT-')],
              [sg.Text('Password:'), sg.InputText(tooltip='Enter Password', key='-INPUT2-', password_char='*')],
              [sg.Button('Ok'), sg.Button('Clear')],
              [sg.Button('Exit')]]

    # Create the Window
    window = sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks Exit
            window.close()
            return False
        if event == 'Ok':
            if check(values['-INPUT-'], values['-INPUT2-']):
                print('Successfully logged in')
                print('You entered ', values['-INPUT-'])
                print('You entered ', values['-INPUT2-'])
                window.close()
                return True
            else:
                print("Wrong Username or Password!")

        if event == 'Clear':
            window['-INPUT-'].update(value='')
            window['-INPUT2-'].update(value='')


def get_user():
    return nutzer

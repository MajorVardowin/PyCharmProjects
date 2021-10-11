import PySimpleGUI as Sg

nutzer = ''


def check(user, password):
    # for windows
    if user == 'Admin' and password == '1234':
        return True
    elif user == '' and password == '':
        return True
    return False


def gui_test():
    Sg.theme('BlueMono')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[Sg.Text('Login to Admin Interface:')],
              [Sg.Text('Username:'), Sg.InputText(tooltip='Enter Username', key='-INPUT-')],
              [Sg.Text('Password:'), Sg.InputText(tooltip='Enter Password', key='-INPUT2-', password_char='*')],
              [Sg.Button('Ok'), Sg.Button('Clear')],
              [Sg.Button('Exit')]]

    # Create the Window
    window = Sg.Window('Window Title', layout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()

        if event == Sg.WIN_CLOSED or event == 'Exit':  # if user closes window or clicks Exit
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

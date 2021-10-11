import PySimpleGUI as exe


def open_exe():
    exe.theme('DarkAmber')
    layout = [[exe.Text('Your Exe has been started')],
              [exe.Input(key='-INPUT-')],
              [exe.Button('Print'), exe.Checkbox('Output', key='-CHECK-')],
              [exe.Button('Exit')]]

    window = exe.Window('Admin Tool', layout, size=(300, 200))

    while True:
        event, values = window.read()

        if event == 'Exit' or event == exe.WIN_CLOSED:
            window.close()
            break
        if window['-CHECK-'].get() and event == 'Print':
            print('Printing as an Admin')

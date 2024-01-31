import PySimpleGUI as sg

layout = [
    [sg.ProgressBar(max_value=180, key='-PROGRESS-', size=(60, 20), bar_color=('red', 'green'))],
    [sg.Text('Choose a game: '), sg.Input(key='-INPUT-', enable_events=True), sg.FileBrowse(key='-FILE-')],
    [sg.Button('Submit', key='-SUBMIT-'), sg.T('List of Games: '),
     sg.Listbox([], key='-LIST-', size=(55, 55), background_color='Black', text_color='Green')]
]

window = sg.Window('My Game Selector', layout, size=(600, 150))
file_list = []

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    elif event == "-SUBMIT-":
        selected_file = values['-FILE-']
        if selected_file is not None:
            file_list.append(selected_file)
            window['-LIST-'].update(file_list)

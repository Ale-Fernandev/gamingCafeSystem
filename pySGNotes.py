import time
import PySimpleGUI as sg

layout = [  # Every list acts as a row in the gui window.
    [sg.Text('Text', enable_events=True, key='-TEXT-')],
    [sg.Button('Button', key='-BUTTON1-')],
    [sg.Input(key='-INPUT-')],  # Giving my input a key
    [sg.Text('Hello'), sg.Button('Test-Button', key='-BUTTON2-')]
]

"""This is how you create the gui window 
read() waits for input. Basically reads the .Window
and looks for any kind of event or return value."""

window = sg.Window('Converter', layout)  # .read()

"""Since code is read from top to bottom, essentially it stops at line 15
then waits for any kind of return value or event to occur.
once it does, it closes out the application.
in order for us to resolve this we need to call the read method through a while true loop
and make sg.Window into a variable."""

while True:
    event, values = window.read()  # window.read() returns event and values
    """Events pertain to things triggered by other elements
    like pressing a button or closing the window.
    if the event in the window is closing the window, you want to break
    out of the while True loop that reads the window like so"""
    if event == sg.WIN_CLOSED:
        break

    if event == '-BUTTON1-':  # No need to call sg.'button' because it is not a return error
        # window['-TEXT-'].update(values['-INPUT-'])    #This is how to update values.
        window['-TEXT-'].update(visible=False)  # This is how to update the sg.Text to disappear
        # The update method can do a lot of different things.

    if event == '-BUTTON2-':
        print("Test-Button pressed")

# What if you wanted to call sg.Input() or any other element that isn't named?
# Every element has an argument we can pass in, and that is a key word argument called key
# Ex : sg.Button('Button', key = '-BUTTON1-')
# Standard is to name the key in all capitals with dashes

window.close()  # To make sure the window is closing after while loop.

"""
More Event Notes :

 - An event is triggered by a certain action.
 - closing the window triggers the WIN_CLOSED event
 - The name of the event will be the name of the element pressed

for example, if I press my button then Button event would be called
or Test-Button event would be called. This is called the key
of the event. you can give event keys by key = "key" or just
by the name given to the element

sg.Text has no event associated with it so when you click on it nothing happens.
You can give any element an event by passing it in as an argument

Example :
sg.Text('Hello World', enable_events=True, key = '-TEXT-'

"""

"""Values :
 - There are several elements that can contain values, like input
 - These values get stored in a dictionary called values

 Basically the way you access values will be that, every element has a key, and that key will lead to
 its value in the dictionary. Therefore you can access any value inside this 'values' dictionary.

 If an element doesn't have a key but does have a value, pysimplegui will give it a key by default
 and it'll be an integer from 0 to your last element.
"""

"""
Updating Elements :
Every element has an update method.
This update method you can use to change the value that is being displayed
for example you can change the text, visibility, and a ton more values

"""

# Messing around with PySimpleGUI, this is a theme browser template.
"""
sg.theme('DarkAmber')

layout = [
    [sg.Text('Theme Browser, layout')],
    [sg.Text('Click a Theme color to see demo window')],
    [sg.Listbox(values=sg.theme_list(), size=(105, 25), key='-LIST-', enable_events=True)],
    [sg.Button("Exit")]
]

window = sg.Window('Theme Browser', layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    sg.theme(values['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(values['-LIST-'][0]))

window.close()
"""

# This is an example for a timer tracker
"""
my_time = int(input("Enter the time in seconds"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("TIME'S UP")
"""

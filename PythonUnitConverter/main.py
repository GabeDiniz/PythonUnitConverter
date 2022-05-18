import PySimpleGUI as sg

## Creates New Window
layout = [
    [sg.Button('Submit', key = '-SUBMIT-'), sg.Input(key = '-INPUT-')],
    [sg.Spin(['km to miles', 'CAD to USD', 'hourly wage to yearly salary'], key = '-UNITS-')],
    [sg.Text("Output", key = '-OUTPUT-')]
    ]

window = sg.Window("Converter", layout)

def check_user_input(input):
    try:
        # Convert it into integer
        val = int(input)
        return True
    except ValueError:
        try:
            # Convert it into float
            val = float(input)
            return True
        except ValueError:
            return False

while True:
    event, values = window.read()

    # Closes Window with X
    if event == sg.WIN_CLOSED: 
        break

    if event == '-SUBMIT-': 
        input_val = (values['-INPUT-'])
        conversion = values['-UNITS-']
        
        if check_user_input(input_val):
            match values['-UNITS-']:
                case 'km to miles':
                    output = round(float(input_val) * 0.6214, 2)
                    output_string = f'{input_val} km are {output} miles.'
                case 'CAD to USD':
                    output = (float(input_val) * 0.78)
                    output_string = f'${input_val} CAD is equal to ${output:.2f} USD.'
                case 'hourly wage to yearly salary':
                    output = ((float(input_val) * 35)*52)
                    output_string = f'${input_val}/hour at 35 hours/week is ~${output:.2f}/year.'
            window['-OUTPUT-'].update(output_string)
        else:
            window['-OUTPUT-'].update('Entry includes a String... Please enter a number')
    

window.close()

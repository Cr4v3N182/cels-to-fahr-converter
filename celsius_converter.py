import PySimpleGUI as sg
from celsFunctions import fahrenheit_convertion

label = sg.Text("Enter celsius: ")
cels_input = sg.Input(key="celsius", size=(20, 5))
result_info = sg.Text("Result: ")
result_output = sg.Text("", key="output")
convert_button = sg.Button("Convert", key="convert")
exit_button = sg.Button("Exit", key="exit")


layout = [[label, cels_input],
          [result_info, result_output], [convert_button, exit_button]]

window = sg.Window("Celsius to Fahrenheit",
                   layout=layout, size=(300, 100))
while True:
    event, values = window.read()
    match event:
        case "exit":
            break
        case sg.WIN_CLOSED:
            break
    try:
        celsius = float(values['celsius'])
        #print(1, event) => print that checks a events
        #print(2, values) => print that checks a values
        result = fahrenheit_convertion(celsius)
        window["output"].update(value=f"{result} F", text_color="white", font=("Helvetica", 10))
    except ValueError:
        sg.popup("Enter a Celsius first.", font=("Helvetica", 10))

window.close()
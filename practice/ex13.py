import PySimpleGUI as sg
from feet_inch_converter import converter

label1 = sg.Text("Enter Feet   ")
input1 = sg.Input(key='feet')

label2 = sg.Text("Enter Inches")
input2 = sg.Input(key='inch')

enter_button = sg.Button("Convert")
output = sg.InputText("", key='meter')

window = sg.Window("Converter", layout=[[label1, input1], [label2, input2],[enter_button],[output]])

while True:
    event, values = window.read()
    feet = float(values['feet'])
    inch = float(values['inch'])
    meter = converter(feet, inch)
    window['meter'].update(value=meter)

print(1, event)
print(2, values)
window.close()

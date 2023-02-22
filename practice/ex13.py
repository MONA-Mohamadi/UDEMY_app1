import PySimpleGUI as sg

label1 = sg.Text("Enter Feet")
input1 = sg.Input()

label2 = sg.Text("Enter Inches")
input2 = sg.Input()

enter_button = sg.Button("Convert")

window = sg.Window("Converter", layout=[[label1, input1], [label2, input2],[enter_button]])
window.read()
window.close()

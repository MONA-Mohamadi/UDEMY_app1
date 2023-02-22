import function
import PySimpleGUI as sg
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip='Enter to do')
add_botton = sg.Button("Add")

window = sg.Window("My TO_Do App",layout=[[label], [input_box,add_botton]])
window.read()
window.close()
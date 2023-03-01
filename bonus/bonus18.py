import PySimpleGUI as sg

sg.theme('Dark')

label1 = sg.Text("Choose Zipfolder   ")
input_box1 = sg.Input()
button1 = sg.FileBrowse("Choose", key='file')

label2 = sg.Text("Choose destination")
input_box2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key='folder')

extract_button = sg.Button('Extract')
output_label = sg.Text(key='output', text_color='green')

window = sg.Window('Archive Extractor', layout=[[label1, input_box1, button1],
                                                [label2, input_box2, button2]])
window.read()
window.close()

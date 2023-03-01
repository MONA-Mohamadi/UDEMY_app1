import PySimpleGUI as sg
from zip_extractor import extractor_archive

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
                                                [label2, input_box2, button2],
                                                [extract_button, output_label]])

while True:
    event, value = window.read()
    print(1, event)
    print(2, value)
    filepath = value['file']
    des_dir = value['folder']
    extractor_archive(filepath,des_dir)

window.close()

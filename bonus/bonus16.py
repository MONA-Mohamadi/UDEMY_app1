import PySimpleGUI as sg
from zip_creator import make_archive

label1 = sg.Text("Choose your files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose', key='files')

label2 = sg.Text("Choose your destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose', key='directory')

compress_button = sg.Button('Compress')
output_label = sg.Text(key="output", text_color= 'green', font=(20))

window = sg.Window("file compressor",
                   layout=[[label1, input1, choose_button1],
                          [label2, input2, choose_button2], [compress_button,output_label]])
while True:

    event, value = window.read()
    filepath = value['files'].split(";")
    folder = value['directory']
    make_archive(filepath, folder)
    window['output'].update(value='compression completed')
    print(1, event)
    print(2, value)
window.close()

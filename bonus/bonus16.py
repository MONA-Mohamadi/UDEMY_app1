import PySimpleGUI as sg

label1 = sg.Text("Choose your files to compress")
input1 = sg.Input()
choose_button1 = sg.FileBrowse('Choose')

label2 = sg.Text("Choose your destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose')

compress_button = sg.Button('Compress')

window = sg.Window("file compressor",
                   layout=[[label1,input1,choose_button1],
                           [label2,input2,choose_button2],[compress_button]])
window.read()
window.close()

import PySimpleGUI as sg
import os.path

#first the window layout in 2 colums

file_list_column = [
    [
        sg.Text("Image Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(),
    ],
    [
        sg.Listbox(
            values=[], enable_events=True, size=(40, 20), key="-FILE LIST-"
        )
    ],
]

# For now will only show the name of the file that was chosen
image_viewer_column = [
    [sg.Text("Choosen an image from list on left:")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
]

#full layout
layout = [
    [
        sg.Column(file_list_column),
        sg.VSeparator(),
        sg.Column(image_viewer_column),
    ]
]

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

# folder name was filled in, make a list of files in the folder
if event == "-FOLDER-":
    folder = values["-FOLDER-"]
    try:
        #get lsit of files in folder
        file_list = os.listdir(folder)
    except:
        file_list = []

    fnames = [
        f
        for f in file_list
        if os.path.isfile(os.path.join(folder, f))
        and f.lower().endswith((".png", ".gif", ".jpg", ".jpeg"))
    ]
    window("-FILE LIST-").update(fnames)

elif event == "-FILE LIST-": # a file was chosen from the listbox
    try:
        filename = os.path.join(
            values["-FOLDER-"], values["-FILE LIST-"][0]
        )
        window["-TOUT-"].update(filename)

        try:
            window["-IMAGE-"].update(filename=filename)
        except Exception as e:
            print(f"Error updating image: {e}")
    except Exception as e:
        print(f"Error loading selected file: {e}")

    window.close()
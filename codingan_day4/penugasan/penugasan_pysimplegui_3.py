import PySimpleGUI as sg

sg.theme('LightBlue3')

# ===== Layout =====
layout = [
    [sg.Text('DATA SISWA BARU',
             font=('Arial', 20, 'bold'),
             justification='center',
             expand_x=True)],

    [sg.Text('Nama Lengkap')],
    [sg.Input('Siswa Baru', key='-NAMA-')],

    [sg.Text('Tanggal Lahir')],
    [sg.Input('7 Juli 2007', key='-TTL-')],

    [sg.Text('Asal Sekolah')],
    [sg.Input('SMP', key='-ASAL-')],

    [sg.Text('NISN')],
    [sg.Input('12345', key='-NISN-')],

    [sg.Text('Nama Ayah')],
    [sg.Input('Ayah', key='-AYAH-')],

    [sg.Text('Nama Ibu')],
    [sg.Input('Ibu', key='-IBU-')],

    [sg.Text('Nomor Telepon / HP')],
    [sg.Input('987654321', key='-HP-')],

    [sg.Text('Alamat')],
    [sg.Multiline('Rumah', key='-ALAMAT-', size=(40, 4))],

    [sg.Push(),
     sg.Button('Hapus', button_color=('white', 'brown')),
     sg.Button('Simpan', button_color=('white', 'green'))]
]

window = sg.Window(
    'MainWindow',
    layout,
    size=(500, 650),
    finalize=True
)

# ===== Event Loop =====
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == 'Hapus':
        for key in values:
            window[key].update('')
        sg.popup('Data berhasil dihapus')

    if event == 'Simpan':
        if values['-NAMA-'] == '' or values['-NISN-'] == '':
            sg.popup('Nama dan NISN wajib diisi!')
        else:
            sg.popup(
                'Data berhasil disimpan',
                f"Nama : {values['-NAMA-']}",
                f"NISN : {values['-NISN-']}"
            )

window.close()

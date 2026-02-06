import PySimpleGUI as sg

sg.theme('LightGray1')

BIAYA_PER_JAM = 2000

# ===== Layout Kiri (Input) =====
input_layout = [
    [sg.Text('Aplikasi Parkir Kelompok 6', font=('Arial', 12, 'bold'))],
    [sg.Text('No Plat Polisi')],
    [sg.Input(key='-PLAT-')],

    [sg.Text('Waktu Masuk (jam)')],
    [sg.Input(key='-MASUK-')],

    [sg.Text('Waktu Keluar (jam)')],
    [sg.Input(key='-KELUAR-')],

    [sg.Text('Biaya')],
    [sg.Input(key='-BIAYA-', disabled=True)],

    [sg.Button('Hitung'), sg.Button('Keluar')]
]

# ===== Layout Kanan (Info Biaya) =====
info_layout = [
    [sg.Text('Biaya Per Jam', text_color='red', font=('Arial', 14, 'bold'))],
    [sg.Text('Rp. 2.000', text_color='red', font=('Arial', 24, 'bold'))]
]

# ===== Layout Tabel =====
table_headings = ['No Plat Polisi', 'Masuk', 'Keluar', 'Biaya']

layout = [
    [
        sg.Column(input_layout),
        sg.VSeparator(),
        sg.Column(info_layout)
    ],
    [sg.Text('List Pelanggan Urut Terakhir Keluar', text_color='blue')],
    [sg.Table(
        values=[],
        headings=table_headings,
        key='-TABLE1-',
        auto_size_columns=True,
        justification='center',
        num_rows=5
    )],
    [sg.Text('List Pelanggan Banyak Bayar', text_color='blue')],
    [sg.Table(
        values=[],
        headings=table_headings,
        key='-TABLE2-',
        auto_size_columns=True,
        justification='center',
        num_rows=5
    )]
]

window = sg.Window('Program Parkir', layout, size=(800, 600))

data = []

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Keluar'):
        break

    if event == 'Hitung':
        try:
            plat = values['-PLAT-']
            masuk = int(values['-MASUK-'])
            keluar = int(values['-KELUAR-'])

            lama = keluar - masuk
            if lama <= 0:
                sg.popup('Waktu keluar harus lebih besar!')
                continue

            biaya = lama * BIAYA_PER_JAM
            window['-BIAYA-'].update(f'Rp. {biaya:,}')

            record = [plat, masuk, keluar, biaya]
            data.append(record)

            # Update tabel terakhir keluar
            window['-TABLE1-'].update(values=data[::-1])

            # Update tabel bayar terbanyak
            data_sorted = sorted(data, key=lambda x: x[3], reverse=True)
            window['-TABLE2-'].update(values=data_sorted)

        except ValueError:
            sg.popup('Masukkan data dengan benar!')

window.close()

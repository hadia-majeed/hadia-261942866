import PySimpleGUI as sg
sg.theme('DarkTeal8')

col_1 = [[sg.Button('Car Rental')],
         [sg.Button('Car Return')],
         [sg.Button('Total Finance Detail')]
         ]

col_2 = [[sg.Text('TG Enterprises', enable_events=True, size=(50, 1), justification="centre", text_color="red")]
         ]

cars = [
    ['CULTUS', 4, 3500, 300, 550],
    ['SONATA', 3, 5000, 350, 750],
    ['KIA Sportage', 3, 6000, 500, 700],
    ['Yaris', 5, 4000, 300, 600],
    ['HONDA CIVIC', 5, 5500, 300, 600],
    ['Pajero', 2, 7000, 500, 700]
]
rented_cars = []
header = ["Model", "Available", "price/Day",
          "Liability Insurance/Day", "Comprehensive Insurance/Day"]
layout1 = [
    [sg.Text('Select Function', justification="left")], [sg.Column(
        col_1, key="Col1", visible=True, justification="left"), sg.VSeparator(),]
]
layout2 = [
    [sg.Column(col_2)],
    [sg.Text('Select Car:', key='-selectcar-', visible='True')],
    [sg.Text('Car not Available', key='-carnot-',
             text_color="red", visible=False)],
    [sg.Table(
        values=cars,
        headings=header,
        key="-TABLE-",
        justification="left",
        enable_events="True")],
    [sg.Text("Number of Days"), sg.Input(key="-NUMOFDAYS-", size=(15, 1))],
    [sg.CB("Liability", key="-liability-")],
    [sg.CB("Comprehensive", key="-comprehensive-")],
    [sg.Button('Ok', key="-okrent-")]
]
layout3 = [
    [sg.Text('TG Enterprises', enable_events=True, size=(
        50, 1), justification="centre", text_color="red")],
    [sg.Text('Summary:', size=(30, 1))],
    [sg.Text('Car', size=(30, 1)), sg.T(
        'Car Type', key='-cartype-', size=(30, 1))],
    [sg.Text('Rent Cost', size=(30, 1)), sg.T(
        'PKR', key="-rentcost-", size=(30, 1))],
    [sg.Text('Insurance Cost', size=(30, 1)), sg.T(
        'PKR', key="-insurancecost-", size=(30, 1))],
    [sg.Text('Tax', size=(30, 1)), sg.T(' PKR', key=('-tax-'), size=(30, 1))],
    [sg.Text('==========================================')],
    [sg.Text('Total', size=(30, 1)), sg.T(
        'PKR', key=('-total-'), size=(30, 1))],
    [sg.Button('Confirm', key='-confirmrent-'),
     sg.Button('Cancel', key='-cancel-')]
]

layout4 = []
values = []
index = 0
for item in cars:

    values.append((item[0], index))
    index = index+1
    layout4 = [
        [sg.Text('Select a Car:')],
        [sg.DD(values, key='-dd-', size=(30, 1), enable_events=True)],
        [sg.Button('Confirm', key='-confirmreturn-')],
        [sg.Text('No more Cars to Return', key='-returnnot-', visible=False)],
    ]
    headers_2 = ['Car Model', 'Rent Cost', 'Days',
                 'Insurance Cost', 'Tax Cost', 'Total Cost']
    total_income = 0
    total_insurance = 0
    total_tax = 0

    layout5 = [
        [sg.Table(
            values=rented_cars,
            headings=headers_2,
            key="-TABLE2-",
            justification="left",
            enable_events="True")],
        [sg.Text("Total income : "), sg.T(
            'fdd', key='-income-',)],
        [sg.Text("Total Insurance : "), sg.T(
            'fdd', key='-insure-',)],
        [sg.Text("Totaal Tax "), sg.T(
            'fdd', key='-totaltax-',)]
    ]


layout = [[sg.Column(layout1, key='-lay1-'),
           sg.Column(layout2, visible=False, key='-lay2-'),
           sg.Column(layout3, visible=False, key='-lay3-'),
           sg.Column(layout4, visible=False, key='-lay4-'),
           sg.Column(layout5, visible=False, key='-lay5-')
           ]]

window = sg.Window('Car Rental System', layout,
                   size=(1000, 600), finalize=True)


def rent_car():
    window['-lay2-'].update(visible=True)
    window['-lay4-'].update(visible=False)
    window['-lay3-'].update(visible=False)
    window['-lay5-'].update(visible=False)
    window.refresh()


while True:

    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Car Rental':
        rent_car()
    if event == "-okrent-" and values['-TABLE-'] != []:
        window['-lay3-'].update(visible=True)
        window.refresh()
        window['-lay2-'].update(visible=False)
        car_cost = cars[values['-TABLE-'][0]][2]
        car_type = cars[values['-TABLE-'][0]]
        insurance_type = "Liability" if values["-liability-"] else "Comprehensive"
        insurance_cost1 = cars[values['-TABLE-'][0]
                               ][4] if insurance_type == "Comprehensive" else cars[values['-TABLE-'][0]][3]
        insurance_cost = insurance_cost1 * int(values['-NUMOFDAYS-'])
        rent_cost = car_cost * int(values['-NUMOFDAYS-'])
        tax = int(rent_cost) * 0.05
        total = rent_cost + tax + insurance_cost
        window['-cartype-'].update(value=f'{car_type[0]}')
        window['-rentcost-'].update(value=f'{rent_cost} PKR')
        window['-insurancecost-'].update(value=f'{insurance_cost} PKR')
        window['-tax-'].update(value=f'{tax} PKR')
        window['-total-'].update(value=f'{total} PKR')

    if event == '-confirmrent-':
        cars[values['-TABLE-'][0]][1] = cars[values['-TABLE-'][0]][1] - 1
        selected_car = cars[values['-TABLE-'][0]].copy()
        selected_car[2] = int(values['-NUMOFDAYS-'])
        selected_car[1] = rent_cost
        selected_car[3] = insurance_cost
        selected_car[4] = tax
        selected_car.append(total)
        rented_cars.append(selected_car)
        window['-lay3-'].update(visible=False)
        window['-lay2-'].update(visible=True)
        window['-lay4-'].update(visible=False)
        window['-lay5-'].update(visible=False)
        window['-TABLE-'].update(cars)
        total_income += rent_cost
        total_insurance += insurance_cost
        total_tax += tax

    if event != None:
        if values['-TABLE-'] != [] and event == '-TABLE-':
            if cars[values['-TABLE-'][0]][1] == 0:
                window['-carnot-'].update(visible=True)
                window['-lay3-'].update(visible=False)
                window['-TABLE-'].update(cars)

            else:
                window['-carnot-'].update(visible=False)

    def car_return():
        window['-lay4-'].update(visible=True)
        window['-lay3-'].update(visible=False)
        window['-lay2-'].update(visible=False)
        window['-lay5-'].update(visible=False)

    if event == 'Car Return':
        car_return()

    found = False
    if values != [] and event == '-confirmreturn-':

        for index, item in enumerate(rented_cars):
            if cars[values['-dd-'][1]][0] == rented_cars[index][0]:
                found = True
                rented_cars.remove(item)
                break
        if found == False:
            window['-returnnot-'].update(visible=True)
        else:
            cars[values['-dd-'][1]][1] = cars[values['-dd-'][1]][1]+1

            window['-lay3-'].update(visible=False)
            window['-lay4-'].update(visible=False)
            window['-lay2-'].update(visible=True)
            window['-lay5-'].update(visible=False)
            window['-TABLE-'].update(cars)
            window.refresh()
            found = False

    if event == 'Total Finance Detail':
        window['-income-'].update(value=f'{total_income}')
        window['-insure-'].update(value=f'{total_insurance}')
        window['-totaltax-'].update(value=f'{total_tax}')
        window['-lay5-'].update(visible=True)
        window['-lay4-'].update(visible=False)
        window['-lay3-'].update(visible=False)
        window['-lay2-'].update(visible=False)
        window['-TABLE2-'].update(rented_cars)

import PySimpleGUI as sg
import time
import random
import sys, os
import socket
#from gpiozero import CPUTemperature, DiskUsage, LoadAverage
sys.path.insert(0, "..")

default_font  = ("Consolas", 16)

def title_bar(title, text_color, background_color):
    bc = background_color
    tc = text_color
    font = 'Consolas 12' #Consolas

    return [sg.Col([[sg.T(title, text_color=tc, background_color=bc, font=font, grab=True)]], pad=(0, 0), background_color=bc),
            sg.Col([[sg.T('_', text_color=tc, background_color=bc, enable_events=True, font=font, key='-MINIMIZE-'), sg.Text('❎', text_color=tc, background_color=bc, font=font, enable_events=True, key='Exit')]], element_justification='r', key='-C-', grab=True,
                   pad=(0, 0), background_color=bc)]

def get_cpu_temp():
    cpu = CPUTemperature()
    return cpu.temperature

def get_disk_usage():
    disk = DiskUsage()
    return disk.usage

def get_cpu_load():
    cpu = LoadAverage()
    return cpu.load

def get_ip_addr(hostname):
    ip_addr = socket.gethostbyname(hostname)
    return ip_addr

def ping(hostname):
    """pings a host name and gets a response

    Parameters
    ----------
    hostname : str
        A string that is either a hostname or IP addr of the device.

    Returns
    -------
    list(str, bool)
        A two part message that can be unpacked into a color for display purposes and a boolean for logic purposes.
    """
    response = os.system("ping -n 1 " + hostname)
    if response == 0:
        return ["green", True]
    else:
        return ["red", False]

def LEDIndicator(key=None, radius=30):
    return sg.Graph(canvas_size=(radius, radius),
             graph_bottom_left=(-radius, -radius),
             graph_top_right=(radius, radius),
             pad=(0, 0), key=key, background_color='gray')

def SetLED(window, key, color):
    graph = window[key]
    graph.erase()
    graph.draw_circle((0, 0), 16, fill_color=color, line_color=color)

def random_gen():
    cpu =  round(random.gauss(50, 20), 2)
    disk =  round(random.gauss(35, 10), 2)
    temperature = round(random.gauss(35, 2), 2)
    
    return [cpu, disk, temperature]

background_layout = [title_bar('IIoT Case', sg.theme_text_color('white'), sg.theme_background_color('orange')), [sg.Image(r'C:\Users\JK88UY\OneDrive - Aalborg Universitet\Dokumenter\university_projects\Learning_factory\data-driven-decisions\code\python\iiot_box_wallpaper.png')]]
col_layout_r = [[sg.Text('ESPBoxes:', size=(20,1), background_color='gray', font=("Consolas", 20))],
          [sg.Text('ESPBox1:', background_color='gray', font=default_font), sg.Text('10.3.141.115', background_color='gray', font=default_font, text_color='yellow', key='_ipaddr_box1_'), sg.Button('ping', button_color='gray',font=default_font, key='ping1'), LEDIndicator('_espbox1_')],
          [sg.Text('ESPBox2:', background_color='gray', font=default_font), sg.Text('10.3.141.87', background_color='gray', font=default_font, text_color='yellow', key='_ipaddr_box2_'), sg.Button('ping', button_color='gray', font=default_font, key='ping2'), LEDIndicator('_espbox2_')],
          [sg.Text('IIoT Box Status:', background_color='gray', font=("Consolas", 20))],
          [sg.Text('Temperature:', background_color='gray', font=default_font), sg.Text('N/A', background_color='gray', font=default_font, key='_temp_')],
          [sg.Text('CPU Usage:', background_color='gray', font=default_font), sg.Text('N/A', background_color='gray', font=default_font, key='_cpu_')],
          [sg.Text('Disk Usage:', background_color='gray', font=default_font), sg.Text('N/A', background_color='gray', font=default_font, key='_disk_')],
          [sg.Text('IP Address:', background_color='gray', font=default_font), sg.Text('10.3.141.1', background_color='gray', font=default_font, text_color='yellow', key='_ipaddr_pi_')],
          [sg.Button('Exit', button_color='red', font=default_font)]]


layout  =[[sg.Text('Status Board', size=(30, 2), justification='left', font=("Consolas", 25), relief=sg.RELIEF_RIDGE, background_color=sg.theme_background_color('gray'))],
            [[sg.Col(col_layout_r, element_justification='left')]]]

background_window = sg.Window('background', background_layout, no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=[[''], ['Exit',]])
background_window['-C-'].expand(True, False, False)  # expand the titlebar's rightmost column so that it resizes correctly
top_window = sg.Window('My new window', layout, finalize=True, keep_on_top=True, grab_anywhere=False,  transparent_color=sg.theme_background_color('gray'), no_titlebar=True)
#top_window.move(1050,250)
top_window.move(650, 50)

while True:  # Event Loop
    event, value = top_window.read(timeout=300)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if event == 'ping1':
        color, connected = ping("AAU122002")
        SetLED(top_window, '_espbox1_', color)
    elif event == 'ping2':
        color, connected = ping("10.3.141.100")
        SetLED(top_window, '_espbox2_', color)

    rand_lst = random_gen()
    ids = ['_cpu_', '_disk_', '_temp_']

    for num, idd in zip(rand_lst, ids):
        if num < 30:
            top_window[idd].update(num, text_color='green')
        elif 30 < num < 60:
            top_window[idd].update(num, text_color='yellow')
        elif num > 61:
            top_window[idd].update(num, text_color='red')
    time.sleep(0.5)


'''
while True:  # Event Loop
    event, value = top_window.read(timeout=400)
    if event == 'Exit' or event == sg.WIN_CLOSED:
        break
    if value is None:
        break
    if event == 'Lamp' and off == True:
        SetLED(top_window, '_lamp_', 'cyan')
        off = False
    elif event == 'Lamp' and off == False:
        SetLED(top_window, '_lamp_', 'red')
        off = True

    SetLED(top_window, '_cpu_', 'cyan' if random.randint(1, 10) > 5 else 'red')
    SetLED(top_window, '_ram_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(top_window, '_temp_', 'green' if random.randint(1, 10) > 5 else 'red')
    SetLED(top_window, '_server1_', 'green' if random.randint(1, 10) > 5 else 'red')
    



          column1 = [[sg.Text('Column 1', justification='right', size=(10, 1))],
            [sg.Spin(values=('Spin Box 1', 'Spin Box 2', 'Spin Box 3'),
                    initial_value='Spin Box 1')],
            [sg.Spin(values=['Spin Box 1', '2', '3'],
                    initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
layout = [
        [sg.Text('Window + Background Image\nWith tkinter', size=(30, 2), justification='right', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
        [sg.Text('Here is some text.... and a place to enter text')],
        [sg.InputText('This is my text')],
        [sg.Frame(layout=[
            [sg.CBox('Checkbox', size=(10, 1)),
             sg.CBox('My second checkbox!', default=True)],
            [sg.Radio('My first Radio!     ', "RADIO1", default=True, size=(10, 1)),
             sg.Radio('My second Radio!', "RADIO1")]], title='Options', relief=sg.RELIEF_SUNKEN, tooltip='Use these to set flags')],
        [sg.MLine(default_text='This is the default Text should you decide not to type anything', size=(35, 3)),
         sg.MLine(default_text='A second multi-line', size=(35, 3))],
        [sg.Combo(('Combobox 1', 'Combobox 2'),default_value='Combobox 1', size=(20, 1)),
         sg.Slider(range=(1, 100), orientation='h', size=(34, 20), default_value=85)],
        [sg.OptionMenu(('Menu Option 1', 'Menu Option 2', 'Menu Option 3'))],
        [sg.Listbox(values=('Listbox 1', 'Listbox 2', 'Listbox 3'), size=(30, 3)),
         sg.Frame('Labelled Group', [[
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=25, tick_interval=25),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=75),
             sg.Slider(range=(1, 100), orientation='v', size=(5, 20), default_value=10),
             sg.Col(column1, element_justification='right')]])
        ],
        [sg.Text('_' * 80)],
        [sg.Text('Choose A Folder', size=(35, 1))],
        [sg.Text('Your Folder', size=(15, 1), justification='right'),
         sg.InputText('Default Folder'), sg.FolderBrowse()],
        [sg.Submit(tooltip='Click to submit this form'), sg.Cancel()],
    [sg.Text('Right Click To Exit', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_SUNKEN)], ]

    '''
top_window.close()

import PySimpleGUI as sg
import time
import random
import sys, os
import socket
from gpiozero import CPUTemperature, DiskUsage, LoadAverage
sys.path.insert(0, "..")


default_font  = ("Consolas", 16)

def get_scaling():
    # called before window created
    root = sg.tk.Tk()
    scaling = root.winfo_fpixels('1i')/72
    root.destroy()
    return scaling2

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
    return cpu.load_average * 100 

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
    list[str, bool]
        A two part message that can be unpacked into a color for display purposes and a boolean for logic purposes.
    """
    response = os.system("ping -c 1 " + hostname)
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


# Find the number in original screen when GUI designed.
my_scaling = 1      # call get_scaling()
my_width, my_height = 1031, 881   # call sg.Window.get_screen_size()

# Get the number for new screen
scaling_old = get_scaling()
width, height = sg.Window.get_screen_size()

scaling = scaling_old * min(width / my_width, height / my_height)

sg.set_options(scaling=scaling)

background_layout = [title_bar('IIoT Case', sg.theme_text_color('white'), sg.theme_background_color('orange')), [sg.Image(r'/home/pi/Documents/data-driven-decisions/code/python/iiot_box_wallpaper_small.png', size=(1031, 581))]]
col_layout_r = [[sg.Text('ESPBoxes:', size=(20,1), background_color='gray', font=("Consolas", 20))],
          [sg.Text('ESPBox1:', background_color='gray', font=default_font), sg.Text('10.3.141.115', background_color='gray', font=default_font, text_color='yellow', key='_ipaddr_box1_'), sg.Button('ping', button_color='gray',font=default_font, key='ping1'), LEDIndicator('_espbox1_')],
          [sg.Text('ESPBox2:', background_color='gray', font=default_font), sg.Text('10.3.141.87', background_color='gray', font=default_font, text_color='yellow', key='_ipaddr_box2_'), sg.Button('ping', button_color='gray', font=default_font, key='ping2'), LEDIndicator('_espbox2_')],
          [sg.Text('IIoT Box Status:', background_color='gray', font=("Consolas", 20))],
          [sg.Text('Temperature:', background_color='gray', font=default_font), sg.Text('N/A', background_color='gray', font=default_font, key='_temp_')],
          [sg.Text('CPU Usage:', background_color='gray', font=default_font), sg.Text('N/A', background_color='gray', font=default_font, key='_cpu_')],
          [sg.Text('Disk Usage:', background_color='gray', font=default_font), sg.Text('N/A', background_color='gray', font=default_font, key='_disk_')],
          [sg.Text('IP Address:', background_color='gray', font=default_font), sg.Text('10.3.141.1', background_color='gray', font=default_font, text_color='yellow', key='_ipaddr_pi_')],
          [sg.Button('Exit', button_color='red', font=default_font)]]


layout = [[sg.Text('Status Board', size=(30, 2), justification='left', font=("Consolas", 25), relief=sg.RELIEF_RIDGE, background_color=sg.theme_background_color('gray'))],
            [[sg.Col(col_layout_r, element_justification='left')]]]

background_window = sg.Window('background', background_layout, size=(1031, 581), no_titlebar=True, finalize=True, margins=(0, 0), element_padding=(0,0), right_click_menu=[[''], ['Exit',]])
background_window['-C-'].expand(True, False, False)  # expand the titlebar's rightmost column so that it resizes correctly

top_window = sg.Window('My new window', layout, finalize=True, keep_on_top=True, force_toplevel=True, grab_anywhere=False,  transparent_color=sg.theme_background_color('gray'), no_titlebar=True)
top_window.move(500, 75)
background_window.move(0, 0)

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

    current_temp = get_cpu_temp()
    current_load = get_cpu_load()
    current_disk = round(get_disk_usage(), 2)

    if current_temp < 50:
        top_window['_temp_'].update(current_temp, text_color='green')
    elif 51 < current_temp < 65:
        top_window['_temp_'].update(current_temp, text_color='yellow')
    elif 66 < current_temp:
        top_window['_temp_'].update(current_temp, text_color='red') 

    if current_load < 40:
        top_window['_cpu_'].update(current_load, text_color='green')
    elif 41 < current_load < 70:
        top_window['_cpu_'].update(current_load, text_color='yellow')
    elif current_load > 71:
        top_window['_cpu_'].update(current_load, text_color='red')

    if current_disk < 40:
        top_window['_disk_'].update(current_disk, text_color='green')
    elif 41 < current_disk < 70:
        top_window['_cpu_'].update(current_load, text_color='yellow')
    elif current_disk > 71:
        top_window['_cpu_'].update(current_load, text_color='red')
    time.sleep(0.5)

top_window.close()

#!/usr/bin/python3

###  aryainjas ###
import hashlib
import os
import random
import binascii
import ecdsa
import base58
import datetime
import webbrowser
import PySimpleGUI as sg
from json import (load as jsonload, dump as jsondump)
from os import path
import json
import pyperclip

start_time = datetime.datetime.now()


def secret(num):
    a = binascii.hexlify(os.urandom(int(num))).decode('utf-8')
    b = '0x ' + a
    return hashlib.sha256(b.encode("utf-8")).hexdigest().upper()


def check_balance(address):
    url = f'https://blockchain.info/q/addressbalance/{address}'
    webbrowser.open(url)


def pubkey(secret_exponent):
    privatekey = binascii.unhexlify(secret_exponent)
    s = ecdsa.SigningKey.from_string(privatekey, curve=ecdsa.SECP256k1)
    return '04' + binascii.hexlify(s.verifying_key.to_string()).decode('utf-8')


def addr(public_key):
    output = []
    alphabet = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    var = hashlib.new('ripemd160')
    var.update(hashlib.sha256(binascii.unhexlify(public_key.encode())).digest())
    var = '00' + var.hexdigest() + hashlib.sha256(
        hashlib.sha256(binascii.unhexlify(('00' + var.hexdigest()).encode())).digest()).hexdigest()[0:8]
    count = [char != '0' for char in var].index(True) // 2
    n = int(var, 16)
    while n > 0:
        n, remainder = divmod(n, 58)
        output.append(alphabet[remainder])
    for i in range(count):
        output.append(alphabet[0])
    return ''.join(output[::-1])


def wif(secret_exponent):
    var80 = "80" + secret_exponent
    var = hashlib.sha256(binascii.unhexlify(hashlib.sha256(binascii.unhexlify(var80)).hexdigest())).hexdigest()
    return str(base58.b58encode(binascii.unhexlify(str(var80) + str(var[0:8]))), 'utf-8')


def database(address, sect=None, WIF=None):
    with open("data-base", "r") as m:
        add = m.read().split()
        for ad in add:
            continue
        if address in add:
            data = open("Win.txt", "a")
            data.write("Bingo " + str(sect) + "\n" + str(address) + "\n" + str(WIF) + "\n" + "\n")
            data.close()

            return address
        else:
            i = 'No address with balance'
            return i


SETTINGS_FILE = path.join(path.dirname(__file__), r'settings_file.cfg')
DEFAULT_SETTINGS = {'theme': sg.theme()}
SETTINGS_KEYS_TO_ELEMENT_KEYS = {'theme': '-THEME-'}


def load_settings(settings_file, default_settings):
    try:
        with open(settings_file, 'r') as f:
            settings = jsonload(f)
    except Exception as e:
        sg.popup_quick_message(f'exception {e}', 'Defualt setting is just good for anyone :) ', keep_on_top=True,
                               background_color='red', text_color='white')
        settings = default_settings
        save_settings(settings_file, settings, None)
    return settings


def save_settings(settings_file, settings, values):
    if values:
        for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
            try:
                settings[key] = values[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]]
            except Exception as e:
                print(f'Problem updating settings (no Problem). Key = {key}')

    with open(settings_file, 'w') as f:
        jsondump(settings, f)

    sg.popup('Settings saved')


def create_settings_window(settings):
    sg.theme(settings['theme'])

    def TextLabel(text):
        return sg.Text(text + ':', justification='r', size=(15, 1))

    layout = [[sg.Text('Settings', font='Any 15')],
              [TextLabel('Theme'), sg.Combo(sg.theme_list(), size=(20, 20), key='-THEME-')],
              [sg.Button('Save'), sg.Button('Exit')]]

    window = sg.Window('Settings', layout, keep_on_top=True, finalize=True)

    for key in SETTINGS_KEYS_TO_ELEMENT_KEYS:
        try:
            window[SETTINGS_KEYS_TO_ELEMENT_KEYS[key]].update(value=settings[key])
        except Exception as e:
            print(f'Problem updating PySimpleGUI (no Problem). Key = {key}')

    return window


def create_main_window(settings):
    sg.theme(settings['theme'])

    menu_def = [['&Menu', ['&Settings', 'Copy', ['Address', 'Privatekey', 'WIF'], 'E&xit']]]

    layout = [[sg.Menu(menu_def)],
              [sg.Text('aryainjas-microllect{beta version-you can pay for higher-speed}', size=(50, 1),
                       font=('Comic sans ms', 13)), sg.Button('', key='paypal', size=(12, 1), button_color=(
              sg.theme_background_color(), sg.theme_background_color()),
                                                              image_filename='paypal.png', image_size=(80, 50),
                                                              image_subsample=2, border_width=0),
               sg.Button('', key='bitcoin', size=(12, 1),
                         button_color=(sg.theme_background_color(), sg.theme_background_color()),
                         image_filename='donation-button.png', image_size=(80, 60), image_subsample=2, border_width=0)],
              [sg.Text('This program has been running for... ', size=(30, 1), font=('Comic sans ms', 10)),
               sg.Text('', size=(30, 1), font=('Comic sans ms', 10), key='_DATE_')],
              [sg.Text('Select number of bytes', size=(30, 1), font=('Comic sans ms', 10)),
               sg.Spin(values=('256', '512', '1024', '2048', '4096'), size=(6, 1), key='num')],
              [sg.Image('vahm.png', size=(250, 250))],
              [sg.Image('bitcoin.png', size=(200, 200))],
              [sg.Text('Address: ', size=(12, 1), font=('Comic sans ms', 10)),
               sg.Text('', size=(70, 1), font=('Comic sans ms', 10), key='address')],
              [sg.Text('Privatekey: ', size=(12, 1), font=('Comic sans ms', 10)),
               sg.Text('', size=(70, 1), font=('Comic sans ms', 10), key='privatekey')],
              [sg.Text('WIF: ', size=(12, 1), font=('Comic sans ms', 10)),
               sg.Text('', size=(70, 1), font=('Comic sans ms', 10), key='wif')],
              [sg.Text('Address \nwith balance: ', size=(12, 2), font=('Comic sans ms', 10)),
               sg.Text('', size=(70, 1), font=('Comic sans ms', 10), key='found')],
              [sg.Button('Start/Stop', font=('Comic sans ms', 10)),
               sg.Button('Exit', button_color=('white', 'red'), font=('Comic sans ms', 10))]]

    return sg.Window('microllect by aryainjas',
                     layout=layout,
                     default_element_size=(9, 1))


def main():
    window, settings = None, load_settings(SETTINGS_FILE, DEFAULT_SETTINGS)
    generator = False
    while 1:
        if window is None:
            window = create_main_window(settings)
        event, values = window.Read(timeout=10)
        if event in (None, 'Exit'):
            break
        elif event == 'Start/Stop':
            generator = not generator
        if generator:
            num = values['num']
            secret_exponent = secret(num)
            public_key = pubkey(secret_exponent)
            address = addr(public_key)
            WIF = wif(secret_exponent)
            data_base = database(address)
            window.Element('_DATE_').Update(str(datetime.datetime.now() - start_time))
            window.Element('address').Update(str(address))
            window.Element('privatekey').Update(str(secret_exponent))
            window.Element('wif').Update(str(WIF))
            window.Element('found').Update(str(data_base))

        elif event == 'Settings':
            event, values = create_settings_window(settings).read(close=True)
            if event == 'Save':
                window.close()
                window = None
                save_settings(SETTINGS_FILE, settings, values)


        elif event == 'paypal':
            webbrowser.open_new_tab("https://www.paypal.com/donate/?hosted_button_id=D8AXHXAMNZ3WY")

        elif event == 'bitcoin':
            webbrowser.open_new_tab("https://nowpayments.io/donation?api_key=8NWRRT9-GWM4NDE-JXPJF75-74ZY5D0")

        elif event == 'Address':
            pyperclip.copy(str(address))
            pyperclip.paste()

        elif event == 'Privatekey':
            pyperclip.copy(str(secret_exponent))
            pyperclip.paste()

        elif event == 'WIF':
            pyperclip.copy(str(WIF))
            pyperclip.paste()
        # check balance of address
        elif event == 'found':
            check_balance(address)
            pyperclip.copy(str(data_base))
            pyperclip.paste()

    window.Close()


main()

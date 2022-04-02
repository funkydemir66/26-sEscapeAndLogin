import sys
from g_python.gextension import Extension
from g_python.hmessage import Direction
from time import sleep
import threading


extension_info = {
    "title": "26'sEscapeAndLogin",
    "description": "ej: on&off&room ",
    "version": "1.1",
    "author": "funkydemir66"
}

ext = Extension(extension_info, sys.argv, silent=True)
ext.start()

KATMER = "FlatCreated"

KASAR = "CloseTrading"

kod = ""



sec_kod = sc = False


def main():
    while sc:
        for i in range(256):
            if sc:
                ext.send_to_client('{in:'+str(KATMER)+'}{i:'+str(kod)+'}{s:"asdsadasd"}')
                sleep(0.7)
                ext.send_to_server('{out:Quit}')
                sleep(1.0)

def konusma(msj):
    global sc, sec_kod

    text = msj.packet.read_string()

    if text == ':ej room':
        msj.is_blocked = True
        sec_kod = True
        ext.send_to_client('{in:Chat}{i:123456789}{s:" You can start spamming by typing :ej on "}{i:0}{i:30}{i:0}{i:0}')

    if text == ':ej on':
        msj.is_blocked = True
        sc = True
        thread = threading.Thread(target=main)
        thread.start()
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: on "}{i:0}{i:30}{i:0}{i:0}')

    if text == ':ej off':
        msj.is_blocked = True
        sc = False
        ext.send_to_client('{in:Chat}{i:123456789}{s:"Script: off "}{i:0}{i:30}{i:0}{i:0}')


def yukle_kod(p):
    global kod, sec_kod

    if sec_kod:
        sec_kod = False
        user_id, _, _ = p.packet.read("iii")
        kod = str(user_id)
        ext.send_to_client('{in:Chat}{i:123456789}{s:"idd: saved "}{i:0}{i:30}{i:0}{i:0}')

def engelle(eng):
    global sc, eng2



ext.intercept(Direction.TO_SERVER, konusma, 'Chat')
ext.intercept(Direction.TO_SERVER, yukle_kod, 'AddFavouriteRoom')
ext.intercept(Direction.TO_CLIENT, engelle, 'GenericError')


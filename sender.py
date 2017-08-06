#! /bin/python2
"""
Script to send keypresses to the RPI Zero over a socket. It receives them
by running server.py.
"""
from __future__ import print_function
import socket
from key_codes import KEY, MOD_KEY


def get_socket(ip_address):
    """Sets up a socket connected to PI on port 80."""
    # create an INET, STREAMing socket
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect((ip_address, 80))
    return clientsocket


def mainloop(clientsocket):
    """Runs the mainloop that receives from the socket and sends to USB.
    Send to the socket four bytes per character:
        1: Character Modifier (shift, ctrl etc)
        2: Character
        3: 00
        4: 00
    """
    while True:
        # Get one char
        got = raw_input("------>")
        for character in got:
            upperC = character.upper()
            if upperC in KEY:
                c = chr(KEY[upperC])
                m = chr(MOD_KEY["LSHIFT"]) if character == upperC else "\x00"
                clientsocket.send(m + c + "\x00\x00")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Send keypresses to pizero')
    parser.add_argument('ip', type=str,
                        help='The IP address of the PI')
    args = parser.parse_args()
    print("Connecting to:", args.ip)
    mainloop(get_socket(args.ip))

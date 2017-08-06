#! /bin/python2
"""
Script to be run on the RPI zero to listen on a socket for characters and
to send them as keypresses over the emulated HID keyboard.
"""
from __future__ import print_function
import socket


def get_ip_address():
    """Prints + returns\ the ip address of this machine so that the client
    can connect."""
    # Assuming there is an internet connection:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    print(ip)
    s.close()
    return ip


def get_socket(ip_address):
    """Sets up a socket listening on port 80."""
    # create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind the socket to a public host,
    # and a well-known port
    serversocket.bind((ip_address, 80))
    # become a server socket
    # Dont allow connections while dealing with a connection
    serversocket.listen(0)
    return serversocket


def process(modifier, character):
    """Takes a modifier and a character byte and sends them as a keypress.

    A keypress is two packets:
        1) Show which key(s) are pressed   0x XX00 YY00 0000 0000
        2) State all keys released         0x 0000 0000 0000 0000

    XX is for modifier keys eg shift/ctrl
    YY is for normal keys eg A key"""
    assert 0 <= modifier < 256
    assert 0 <= character < 256
    with open("/dev/hidg0", "wb") as fHandle:
        fHandle.write(chr(modifier))
        fHandle.write("\x00")
        fHandle.write(chr(character))
        for i in range(13):  # 5 to finish this packet, 8 for the null packet
            fHandle.write("\x00")


def mainloop(serversocket):
    """Runs the mainloop that receives from the socket and sends to USB.
    Send to the socket four bytes per character:
        1: Character Modifier (shift, ctrl etc)
        2: Character
        3: 00
        4: 00
    """
    while True:
        client, addr = serversocket.accept()
        print("Connected to", addr)
        while True:  # Get each character
            new = client.recv(4)
            if not(ord(new[2]) == 0 and ord(new[3]) == 0):
                print("Discarding", new)
            else:
                process(ord(new[0]), ord(new[1]))


if __name__ == "__main__":
    s = get_socket(get_ip_address())
    try:
        mainloop(s)
    finally:
        s.close()

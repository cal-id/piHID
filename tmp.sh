#! /bin/bash

# This script tests sending key presses over USB
# The keys are hard coded as variables and the 
# print function writes the packets.

A="\0\x4\0\0\0\0\0"
B="\0\x5\0\0\0\0\0"
C="\0\x6\0\0\0\0\0"
D="\0\x7\0\0\0\0\0"
E="\0\x8\0\0\0\0\0"
F="\0\x9\0\0\0\0\0"
G="\0\xa\0\0\0\0\0"
H="\0\xb\0\0\0\0\0"
I="\0\xc\0\0\0\0\0"
J="\0\xd\0\0\0\0\0"
K="\0\xe\0\0\0\0\0"
L="\0\xf\0\0\0\0\0"
M="\0\x10\0\0\0\0\0"
N="\0\x11\0\0\0\0\0"
O="\0\x12\0\0\0\0\0"
P="\0\x13\0\0\0\0\0"
Q="\0\x14\0\0\0\0\0"
R="\0\x15\0\0\0\0\0"
S="\0\x16\0\0\0\0\0"
T="\0\x17\0\0\0\0\0"
U="\0\x18\0\0\0\0\0"
V="\0\x19\0\0\0\0\0"
W="\0\x1a\0\0\0\0\0"
X="\0\x1b\0\0\0\0\0"
Y="\0\x1c\0\0\0\0\0"
Z="\0\x1d\0\0\0\0\0"

null="\0\0\0\0\0\0\0\0"


function print {
    echo -ne $1 > /dev/hidg0
    echo -ne $null > /dev/hidg0
}




print "\0"$A
print "\0"$B
print "\0"$C
print "\0"$Z

print "\x2"$A
print "\x2"$B
print "\x2"$C
print "\x2"$Z

print "\x2\0\x1d\0\0\0\0\0"


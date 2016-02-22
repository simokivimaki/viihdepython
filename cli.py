# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, 
import sys
import getpass
import argparse
from user_input import get_input


def init_argparser():
    parser = argparse.ArgumentParser(description='Elisa viihde library scripts.')
    parser.add_argument('-u', '--user', help='username')
    parser.add_argument('-p', '--passfile', help='password file')
    return parser


def read_from_file(filename):
    with open(filename, "r") as f:
        # assuming utf-8 encoded file
        return f.read().decode('utf-8')


def read_input(param, question, default=None):
    result = param
    if result is None:
        result = get_input(question + ': ')
    if result:
        if sys.hexversion > 0x03000000:
            #if python3
            return result
        else:
            return result.decode(sys.stdin.encoding)
    return default


def read_password(passfileparam, question):
    if passfileparam is not None:
        return read_from_file(passfileparam)
    if sys.hexversion > 0x03000000:
        # python3
        return getpass.getpass(question + ': ')
    else:
        return getpass.getpass(question + ': ').decode(sys.stdin.encoding)

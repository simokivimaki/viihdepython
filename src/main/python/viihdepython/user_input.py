from __future__ import absolute_import, division, print_function, unicode_literals
import sys

def get_input(prompt):
    """
    Get input from the user maintaining the compatibility with python 2 and 3.
    """
    if sys.hexversion > 0x03000000:
        return input(prompt)
    else:
        return raw_input(prompt)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 21:28:35 2018
@author: Shubham
"""

# A module for storing/retrieving python objects. (Using JSON/XML..etc.)

from yaml import load , dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    print("CLoader and CDumper are unavailable")
    from yaml import Loader, Dumper

if __name__ == "__main__":
    print(load)
    f = open('learnyaml.yaml','r')
    data = load(f,Loader)
    print(data)



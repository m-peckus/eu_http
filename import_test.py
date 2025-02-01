#!/usr/bin/env python3
from test_file import *


if isinstance(result, tuple) and len(result) ==3:
    print(f"EU data\ncity: {result[0]}\ncountry: {result[1]}\ncurrency: {result[2]}")
elif isinstance(result, str):
    print(f"None EU data\ncity: {result}")

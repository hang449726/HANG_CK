# -*- coding: utf-8 -*-
import sys

d = {"20010101":"刘备","20010102":"关羽","20010103":"张飞"}
print(f"System encoding: {sys.stdout.encoding}")
print(f"String length: {len(d['20010101'])}") # Should be 2
print(f"String content (repr): {ascii(d['20010101'])}")
print(d['20010101'])

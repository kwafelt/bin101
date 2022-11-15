#!/usr/bin/python3
import binascii

def str_to_hex(stt):
  stt = stt.encode("ascii")# ORIG: bytes(stt, "ascii")
  stt = binascii.hexlify(stt)# ORIG: binascii.hexlify(stt, "$")
  stt = stt.decode("ascii")
  return stt
def hex_to_str(stt):
  stt = stt.encode("ascii")
  stt = binascii.unhexlify(stt)
  stt = stt.decode("ascii")
  return stt

def create(txt):
  txt = txt.split(":")
  usr = txt[0]; pwd = txt[1]
  pwd = str_to_hex(pwd)[::-1]
  print(f"{usr}:{pwd}")
def bypass(txt):
  txt = txt.split(":")
  usr = txt[0]; pwd = txt[1]
  pwd = hex_to_str(pwd[::-1])
  print(f"{usr}:{pwd}")

USAGE = """

ENCRYPT:
txt = "USERNAME:PASSWORD"
create(txt)

DECRYPT:
txt = "USERNAME:PASSWORD"
bypass(txt)

"""

# -*- coding: utf-8 -*-
"""
@Time    : 2022/11/21  021 下午 15:15
@Author  : Jan
@File    : ttt.py
"""
import base64

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

""" {} """

# ASE-CBC加密
def AESEncrypt(text: str, key, iv):
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    encrypt_text = aes.encrypt(pad(text.encode('utf-8'), AES.block_size, style='zero'))     # 自定义新增Padding58-59
    encrypt_text = str(base64.encodebytes(encrypt_text), encoding='utf-8').replace("\n", "")
    return encrypt_text

# ASE-CBC解密
def AESDecrypt(text, key, iv):  # base64 格式
    decode_encrypt_text = base64.b64decode(text)
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    decrypt_text = aes.decrypt(decode_encrypt_text).decode('utf8')
    decrypt_text = decrypt_text.replace(b'\x00'.decode(), "")
    return decrypt_text

e = '{"device_id":"5d25317d91fd2c612ee3c2ec316f90b0","lot_number":"1edd2a57d0e84a0986a5764355353bf5","pow_msg":"1|4|md5|2022-11-20T16:18:15.805813+08:00|32727fa8d208a82e46754c2e5055a679|1edd2a57d0e84a0986a5764355353bf5||e24baa56b2e73772","pow_sign":"0b94428c077f0761983eb1c100fdaed0","geetest":"captcha","lang":"zh","ep":"123","qca4":"1909887014","em":{"ph":0,"cp":0,"ek":"11","wd":1,"nt":0,"si":0,"sc":0}}'
i = "94f422eec3054d0d"

iv = '0000000000000000'
out1 = "4426350bfdda7cc2c6355f1165551c739a7a074b9bfc48549016a98ed45924c0055cd2a8cd361fb60c43016536e3429a98ce75b78b53232d583140d1dbb41d01c5e1c246ca8129350b749d61bd4b0efcfa6109eb252fd246216c2b607ad042d074a2b15c666b928937e31c5d1dc79a2f394891544bd6c7152797b9237c2ac8507a8c5bc502fd604202ccd07060505bd44558f2138229709f19ba4d0dd113ea61b292409bfab20ca299ca4a0f61df267511899c9ca703208ef1cb1858d89bbf262429e6543b5f519856ce624e9ca451a40cda08653d23027eb00348b96132e19b057d8db6cd319eb436294d02d24faadb030ed86439ca13437cd653661e0eaa4e00ae8a97482cb9452f5ecb399a3ed41208cc9a59d10303745afa9b2ded07b96ab266fe65277923f8cc9c11c10f158e23721d50c0b04915b86d404c2cf733f67c074fdf30c2affb688a7f78fcd39a55cdbd2f6c19f69c806fa02fb2096741f588a32d894a0f6e53b84bb31fe8755c9d8cef6d5fa856ebe8b54cf3adbf4202bb7d2bdc0b8e33b5752ba36d6adecd7a6f8ec422ccd41b2eff481da7ffacf178f5734426350bfdda7cc2c6355f1165551c739a7a074b9bfc48549016a98ed45924c0055cd2a8cd361fb60c43016536e3429a98ce75b78b53232d583140d1dbb41d01c5e1c246ca8129350b749d61bd4b0efcfa6109eb252fd246216c2b607ad042d074a2b15c666b928937e31c5d1dc79a2f394891544bd6c7152797b9237c2ac8507a8c5bc502fd604202ccd07060505bd44558f2138229709f19ba4d0dd113ea61b292409bfab20ca299ca4a0f61df267511899c9ca703208ef1cb1858d89bbf262429e6543b5f519856ce624e9ca451a40cda08653d23027eb00348b96132e19b057d8db6cd319eb436294d02d24faadb030ed86439ca13437cd653661e0eaa4e00ae8a97482cb9452f5ecb399a3ed41208cc9a59d10303745afa9b2ded07b96ab266fe65277923f8cc9c11c10f158e23721d50c0b04915b86d404c2cf733f67c074fdf30c2affb688a7f78fcd39a55cdbd2f6c19f69c806fa02fb2096741f588a32d894a0f6e53b84bb31fe8755c9d8cef6d5fa856ebe8b54cf3adbf4202bb7d2bdc0b8e33b5752ba36d6adecd7a6f8ec422ccd41b2eff481da7ffacf178f57384a4f682f939cf1d8fc541072a41c5a24408b0cf6e0b61d206c28369e0a88e1732ab00a219d1af5e394becadb52f3b64d5e06bb7d3c09cf15a056954dc59e763b9913b386a5eb11a89bdb8d6e6fe600b4024df5cd294dc91cded194a68fbca8e5acec7d637e4725066b03cca73250c9a4f33b9ae1065f4cd85eec450616748ab"
out2="RCY1C/3afMLGNV8RZVUcc5p6B0ub/EhUkBapjtRZJMAFXNKozTYftgxDAWU240KamM51t4tTIy1YMUDR27QdAcXhwkbKgSk1C3SdYb1LDvz6YQnrJS/SRiFsK2B60ELQdKKxXGZrkok34xxdHceaLzlIkVRL1scVJ5e5I3wqyFB6jFvFAv1gQgLM0HBgUFvURVjyE4IpcJ8Zuk0N0RPqYbKSQJv6sgyimcpKD2HfJnURiZycpwMgjvHLGFjYm78mJCnmVDtfUZhWzmJOnKRRpAzaCGU9IwJ+sANIuWEy4ZsFfY22zTGetDYpTQLST6rbAw7YZDnKE0N81lNmHg6qTgCuipdILLlFL17LOZo+1BIIzJpZ0QMDdFr6my3tB7lqsmb+ZSd5I/jMnBHBDxWOI3IdUMCwSRW4bUBMLPcz9nwHT98wwq/7aIp/ePzTmlXNvS9sGfacgG+gL7IJZ0H1iKMtiUoPblO4S7Mf6HVcnYzvbV+oVuvotUzzrb9CArt9K9wLjjO1dSujbWrezXpvjsQizNQbLv9IHaf/rPF49XM="

def base64_to_hex(payload_base64):
    bytes_out = base64.b64decode(payload_base64)
    str_out = bytes_out.hex()
    return str_out


def hex_to_base64(payload_hex2):
    bytes_out = bytes.fromhex(payload_hex2)
    str_out = base64.b64encode(bytes_out)
    print("hex_to_base64:", str_out)
    return str_out


def strToBase64(s):
    strEncode = base64.b64encode(s.encode('utf8'))
    return str(strEncode, encoding='utf8')


def base64ToStr(s):
    strDecode = base64.b64decode(bytes(s, encoding='gbk'))
    return str(strDecode, encoding='gbk')


print(AESEncrypt(e, i, iv),1)
print(base64_to_hex(AESEncrypt(e, i, iv)),1)
print(AESDecrypt(out2, i, iv),2)
print(AESDecrypt(AESEncrypt(e, i, iv), i, iv),3)






















































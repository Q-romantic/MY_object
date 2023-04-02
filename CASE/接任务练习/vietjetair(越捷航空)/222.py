#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File  : rsaUtil.py
# Author: DaShenHan&道长-----先苦后甜，任凭晚风拂柳颜------
# Date  : 2021-04-16
import json

from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto.PublicKey import RSA
import base64


class documentRsa():
    __public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCmuYcy3TlrCbh4n34VKFt0swBBXYy5sHMkKr91nYJjoG98kbPgR2n6iYWoU9mI/Zi0geVX2b3YV1Y9Aq/5l5DoJVyG52ZNmnKxtD8ZYJFnah3/Lr8YEGsvXxjv41mxgEQYuoa+OTcd1KOUmeP8R+ZheJj6KhFmhaU40ocjSVXDTQIDAQAB"

    def __init__(self):
        """
        类初始化，传入config对象内配置的俩字段，内部储存的公钥私钥为不带开头的文本
        :param rsa_publicKey: config.rsa_publicKey
        :param rsa_privateKey: config.rsa_privateKey
        """
        self._public_key = documentRsa.__public_key

    def get_public_key(self):
        """
        公开获取拼接完整的公钥
        :return:
        """
        return "-----BEGIN PUBLIC KEY-----\n" + self._public_key + "\n-----END PUBLIC KEY-----"

    @staticmethod
    def _rsa_encrypt(pub_key_str, msg):
        """
        静态方法,根据公钥加密字符串
        :param pub_key_str: 公钥完整
        :param msg: 待加密json文本
        :return:
        """
        msg = msg.encode('utf-8')
        length = len(msg)
        default_length = 117
        # default_length = 100
        # 公钥加密
        pubobj = Cipher_pkcs1_v1_5.new(RSA.importKey(pub_key_str))
        # 长度不用分段
        if length < default_length:
            return base64.b64encode(pubobj.encrypt(msg))
        # 需要分段
        offset = 0
        res = []
        while length - offset > 0:
            if length - offset > default_length:
                res.append(pubobj.encrypt(msg[offset:offset + default_length]))
            else:
                res.append(pubobj.encrypt(msg[offset:]))
            offset += default_length
        byte_data = b''.join(res)

        return base64.b64encode(byte_data)


    def rsa_encrypt(self, msg, pub_key=None):
        """
        加密一段字符串变成 b'二进制
        :param msg: 待加密文本
        :param pub_key: 公钥，不填默认获取初始化的
        :return:
        """
        pub_key = pub_key or self.get_public_key()
        return self._rsa_encrypt(pub_key, msg)

    def rsa_encrypt2str(self, msg, pub_key=None):
        """
        加密文本到文本
        :param msg: 待加密文本
        :return:
        """
        return self.rsa_encrypt(msg, pub_key).decode("utf-8")  # 加密成待传输的字符串

# print(documentRsa().rsa_encrypt2str("123"))

#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @author: A.L.Kun
# @file : test.py
# @time : 2022/4/25 6:22
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP as PKCS1_cipher
# from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def get_key(key_file):
    with open(key_file) as f:
        data = f.read()  # 获取，密钥信息
        key = RSA.importKey(data)
    return key


def encrypt_data(msg):
    public_key = get_key('public_key.pem')  # 读取公钥信息
    cipher = PKCS1_cipher.new(public_key)  # 生成一个加密的类
    encrypt_text = base64.b64encode(cipher.encrypt(msg.encode()))  # 对数据进行加密
    return encrypt_text.decode()  # 对文本进行解码码


def decrypt_data(encrypt_msg):
    private_key = get_key('rsa_private_key.pem')  # 读取私钥信息
    cipher = PKCS1_cipher.new(private_key)  # 生成一个解密的类
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)  # 进行解密
    return back_text.decode()  # 对文本内容进行解码


# msg = "A"*214
# encrypt_text = encrypt_data(msg)  # 加密
# # decrypt_text = decrypt_data(encrypt_text)  # 解密
# print(encrypt_text)

for i in range(1,512):
    if i * int(1024/i) == 1024:
        print(i, 1024/i, 496/(i+1))


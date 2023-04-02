# -*- coding: utf-8 -*-
"""
@Time    : 2023/3/26  026 下午 21:47
@Author  : Jan
@File    : 123.py
"""

import base64
import rsa
from rsa import common


# 使用 rsa库进行RSA签名和加解密
class RsaUtil(object):
    PUBLIC_KEY_PATH = 'public_key.pem'  # 公钥

    # PRIVATE_KEY_PATH = '../Scrape/private_key.pem'  # 私钥

    # 初始化key
    def __init__(self,
                 company_pub_file=PUBLIC_KEY_PATH,
                 # company_pri_file=PRIVATE_KEY_PATH
                 ):

        if company_pub_file:
            self.company_public_key = rsa.PublicKey.load_pkcs1_openssl_pem(open(company_pub_file, 'rb').read())
        # if company_pri_file:
        #     self.company_private_key = rsa.PrivateKey.load_pkcs1(open(company_pri_file, 'rb').read())

    def get_max_length(self, rsa_key, encrypt=True):
        """加密内容过长时 需要分段加密 换算每一段的长度.
         :param rsa_key: 钥匙.
         :param encrypt: 是否是加密.
        """
        blocksize = common.byte_size(rsa_key.n)
        reserve_size = 11  # 预留位为11
        if not encrypt:  # 解密时不需要考虑预留位
            reserve_size = 0
        maxlength = blocksize - reserve_size
        return maxlength

    def encrypt_by_public_key(self, message):  # 加密 支付方公钥 base64转码
        """使用公钥加密.
         :param message: 需要加密的内容.
         加密之后需要对接过进行base64转码
        """
        encrypt_result = b''
        max_length = self.get_max_length(self.company_public_key)
        while message:
            input = message[:max_length]
            message = message[max_length:]
            out = rsa.encrypt(input, self.company_public_key)
            encrypt_result += out
        encrypt_result = base64.b64encode(encrypt_result)
        return encrypt_result.decode()


s = '{"adultCount":1,"arrival":"HAN","childCount":0,"currency":"USD","daysAfterDeparture":0,"daysBeforeDeparture":0,"departureDate":"2023-03-31","departurePlace":"SGN","infantCount":0,"oneway":1,"requestId":"6QJE2ZKSYNVV-1679838690998","sessionId":null,"user-agent-ls-data":"ea82cb66-5b13-4755-8a1a-212f21909f17-1679838690998","x-power-web-s-d":"1742549136-1214521564-4593-b494-7bdd394235c5","_signature":"898c312fb3011f92a2037d478a012bba23b104703526851e83bfc1a4eb6105e5"}'
# rsa_obj = RsaUtil()
# ency_text = rsa_obj.encrypt_by_public_key(s.encode())
# print(ency_text)


# import rsa
# import base64
# from Crypto.PublicKey import RSA
# from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
# # rsa加密，通常对加密结果进行base64编码
# def handle_pub_key(key):
#     start = '-----BEGIN PUBLIC KEY-----\n'
#     end = '-----END PUBLIC KEY-----'
#     result = ''
#     # 分割key，每64位长度换一行
#     divide = int(len(key) / 64)
#     divide = divide if (divide > 0) else divide + 1
#     line = divide if (len(key) % 64 == 0) else divide + 1
#     for i in range(line):
#         result += key[i * 64:(i + 1) * 64] + '\n'
#     result = start + result + end
#     return result
#
# def get_param(message, public_key):
#     """
#     处理长消息 不经过 这个处理回报下面error
#     OverflowError: 458 bytes needed for message, but there is only space for 117
#     :param message 消息
#     :param public_key 公钥
#     :return:
#     """
#     pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
#     crypto = b''
#     divide = int(len(message) / 117)
#     divide = divide if (divide > 0) else divide + 1
#     line = divide if (len(message) % 117 == 0) else divide + 1
#     for i in range(line):
#         crypto += rsa.encrypt(message[i * 117:(i + 1) * 117].encode(), pubkey)
#     crypto = base64.b64encode(crypto)
#     return crypto.decode()
#
#
# if __name__ == '__main__':
#     message = "infodownloadermiddlewareshttpcompressionHttpCompressionMiddleware" * 10
#     public_key = "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQClsqQiK5KMBO88nf2CE6I5aGJQX9jTXorDveudfSKts2/5i/ipCLo68rl4gsPYwzjP5ef5IJTK0Xdzrrfkn5d2GCVA7n/jN3rlqjfSy1w2D4JqMUtqEhRQr7KfofZbZBnPOooiepRht+W0D9rIAceLLD5UPpstZ4lPCW2t/PG0hQIDAQAB"
#     public_key = handle_pub_key(public_key)
#     param = get_param(message, public_key)
#     print(param)


import rsa
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
#rsa加密，通常对加密结果进行base64编码

def handle_pub_key(key):
    """
    处理公钥
    公钥格式pem，处理成以-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾的格式
    :param key:pem格式的公钥，无-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾
    :return:
    """
    start = '-----BEGIN PUBLIC KEY-----\n'
    end = '-----END PUBLIC KEY-----'
    result = ''
    # 分割key，每64位长度换一行
    divide = int(len(key) / 64)
    divide = divide if (divide > 0) else divide + 1
    line = divide if (len(key) % 64 == 0) else divide + 1
    for i in range(line):
        result += key[i * 64:(i + 1) * 64] + '\n'
    result = start + result + end
    print(result)
    return result


def get_param(message, public_key):
    """
    处理长消息 不经过 这个处理回报下面error
    OverflowError: 458 bytes needed for message, but there is only space for 117
    :param message 消息
    :param public_key 公钥
    :return:
    """
    # pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
    # crypto = b''
    # divide = int(len(message) / 117)
    # divide = divide if (divide > 0) else divide + 1
    # line = divide if (len(message) % 117 == 0) else divide + 1
    # for i in range(line):
    #     crypto += rsa.encrypt(message[i * 117:(i + 1) * 117].encode(), pubkey)

    N = 190
    pubkey = rsa.PublicKey.load_pkcs1_openssl_pem(public_key)
    crypto = b''
    divide = int(len(message) / N)
    divide = divide if (divide > 0) else divide + 1
    line = divide if (len(message) % N == 0) else divide + 1
    for i in range(line):
        crypto += rsa.encrypt(message[i * N:(i + 1) * N].encode(), pubkey)

    crypto1 = base64.b64encode(crypto)
    return crypto1.decode()





if __name__ == '__main__':
    message = '{"adultCount":1,"arrival":"HAN","childCount":0,"currency":"USD","daysAfterDeparture":0,"daysBeforeDeparture":0,"departureDate":"2023-03-31","departurePlace":"SGN","infantCount":0,"oneway":1,"requestId":"QX3DFYOI1XCV-1679758370760","sessionId":null,"user-agent-ls-data":"7a5766db-24b1-4fa4-a342-db1c2bb740ef-1679758370759","x-power-web-s-d":"6130551311-1911511106-43cb-af10-1e42ca8b66e7","_signature":"bab214cf948b348015144acedfa604cb744aa896e1bb05dcc460f7353ee837db"}'
    public_key = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAok58IrYXjeFjb6hPgrcvKis43ARDVIqowS2AJKivDp4+8uKDCWnjzBZTsuVvwKPzvVCxBzON2/DPpHU3wnRtdKSVzWju7HMKhuLxe04FsVw8+xvZTmguBj4jTczNLSLjK13lQr46J8j7JrmVUlPqGxIL/Bd3HNAIFuarZQkDsgx5fvdNrMbmT4edr1b3A8wRkhfo9tuE5Tmlx0YVUwybzcI6hgLggCfNwwaClXyBt08NbGSIBcKYKjiQErND0EOnWcGyto7EhkpgGRfAeESo3hbmsiabThLd4t9iOWVHFSl+7B0q+1IGFjSo9qkvNdMUI4ZYdIKq+nCHufpuFMl7SwIDAQAB"

    public_key = handle_pub_key(public_key)
    param = get_param(message, public_key)
    print(param)


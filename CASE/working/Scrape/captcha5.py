# -*- coding: utf-8 -*-
import json
import time
import random

import requests

""" 对接空间推理验证码，适合空间推理验证码分析处理。 """
""" 提示：对于字典嵌套字典传参方式用json.dumps()函数处理 """

# t = int(time.time() * 1000)
# url_init = f'https://captcha5.scrape.center/api/init?t={t}'
# resp = requests.get(url_init)
# data = resp.json()
# print(data)
# gt = data['gt']
# challenge = data['challenge']
#
# url_gettype_php = 'https://api.geetest.com/gettype.php'
# params = {'gt': gt, 'callback': f'geetest_{int(random.random() * 10000) + t}'}
# resp = requests.get(url_gettype_php, params=params)
# print(resp.text)


import base64
from Crypto.Cipher import AES


def get_aes_128_ecb(key, text, encrypt=True):
    def add_to_16(value):  # 需要补位，str不是16的倍数那就补足为16的倍数
        while len(value) % 16 != 0:
            value += '0'
        return value.encode()  # 返回bytes

    if encrypt == True:
        def encrypt(key, text):  # 加密方法
            aes = AES.new(add_to_16(key), AES.MODE_OCB)  # 初始化加密器
            encrypt_aes = aes.encrypt(add_to_16(text))  # 先进行aes加密
            # encrypted_text = str(base64.encodebytes(encrypt_aes), encoding='utf-8')  # 执行加密并转码返回bytes
            encrypted_text = base64.encodebytes(encrypt_aes).decode().replace('\n', '')  # 执行加密并转码返回bytes
            return encrypted_text

        result_51 = encrypt(key, text)
        return result_51
    else:
        def decrypt(key, text):  # 解密方法
            aes = AES.new(add_to_16(key), AES.MODE_ECB)  # 初始化加密器
            base64_decrypted = base64.decodebytes(text.encode(encoding='utf-8'))  # 优先逆向解密base64成bytes
            decrypted_text = str(aes.decrypt(base64_decrypted), encoding='utf-8').replace('0', '')  # 执行解密密并转码返回str
            return decrypted_text

        result_52 = decrypt(key, text)
    return result_52

# s = '156!!3494!!CSS1Compat!!1!!-1!!-1!!-1!!-1!!1!!-1!!-1!!-1!!1!!2!!2!!12!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!-1!!2!!-1!!-1!!-1!!-1!!0!!0!!0!!0!!315!!929!!1920!!1032!!zh-CN!!zh-CN,en,en-GB,en-US!!-1!!1!!24!!Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47!!1!!1!!1920!!1080!!1920!!1032!!1!!1!!1!!-1!!Win32!!0!!-8!!fbc51f370bbc3e59e5d4507aa346cc53!!0!!internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer,internal-pdf-viewer!!0!!-1!!0!!8!!Arial,ArialBlack,ArialNarrow,BookAntiqua,BookmanOldStyle,Calibri,Cambria,CambriaMath,Century,CenturyGothic,CenturySchoolbook,ComicSansMS,Consolas,Courier,CourierNew,Garamond,Georgia,Helvetica,Impact,LucidaBright,LucidaCalligraphy,LucidaConsole,LucidaFax,LucidaHandwriting,LucidaSans,LucidaSansTypewriter,LucidaSansUnicode,MicrosoftSansSerif,MonotypeCorsiva,MSGothic,MSPGothic,MSReferenceSansSerif,MSSansSerif,MSSerif,PalatinoLinotype,SegoePrint,SegoeScript,SegoeUI,SegoeUILight,SegoeUISemibold,SegoeUISymbol,Tahoma,Times,TimesNewRoman,TrebuchetMS,Verdana,Wingdings,Wingdings2,Wingdings3!!1652700174093!!-1!!-1!!-1!!20!!-1!!-1!!-1!!5!!-1!!-1'
# # result_51='T1RHcqsn5q6goyb1uNtw4bARzoWtpZx(5p5M0HPvT4AbaRzuv91OabUYEaxOANRKAflid)QIVkIiWB8CZFrzAOPgJYumDRoh(TqX3RDk2Dc4()bqUT4KihTE6Snkv3fx2C4bQoxO2hx0XyzpU5TMk0jI1fzugpscdVzuio1fNT2fIpwIQ85jjBMEjZ8dDMG1Ofsxl3kxPf4(LfTcfbqXJa8MRLaPaOkRnuOBSTQKGBk0290pHnGwOevKli88Fjn7SPxOR3KkOO6pI4JbIwkEYQSw)PAfstDvhWqT17TN3m8uEq6N2yY93Q35DtCjgu8dEb3X8mJRYvEi1qSzy)Q1iZV2NJFPz8qBg0oE)G(eYdFd)z9)iICQlmvzcXWRFEsR8bAaI7GL(VRcILIPNEAHpiz(h2RRAyouLlYSECfokx7FzoVvFhdi6hYSmYz9YadFyE548lpZvUQA5fiANelIfWJiScxJ9JlpkqEk)OCCl3xUNeoUrwhV1(Sv1u5XRCj8qf(juPmlC3TsfvRJEcmOaJEc7mjxxE187D0VNKRqHCMDOZbKs17XUgJrsnixC8BCTcMHn8FVibmxoNVoShCuwk05wHZn3fsLvM)caY9ACmbAwRLMwAR(sF)xDkflQ0e(BR1xTM)3o51xLSYrkeQeuaik3R4ueyFTFSyyPQh9jOw1GwDONfnExMJaTttbEUER2cgAoidjjZ6kMbzn9)lf7Zrqq22)pS3jg5JB)ZuA160jeIVv4BtlNEz2Gnq5OUwJinjZZOFep3j1(U2i3NxPgYYEvnkVsnlZBUCypLNAX52xMx(TMYowEe0V18a)51lrA5rG(QrFnq2sklVryK0hTTnxJwi7ceShCBz9SDknu14Ce24q0L0HHncxT0zfa0k43fSKkfkaXj1tFu5R0JeFpeVFbopzBJ5DmRWAdOtoW2Hr8OXXZn1uKnRqTF6EMGyk3AKdV7fdbx4dOVkj3vG)0eOJuNOwL)TpT2eM9GoxhrdOg7ycapA9YSVpIQKMAQqCb5pGatl4fsqIzLg3qHVan4U4tZcGDa)1314T7ij)Ell)PoanuU0ZXEMxLxzxDBjvgqTeZRtnQelll0fF0onJ5CP9RchivHhyuuI9b4sdFWBea5XgX(xYxmxax1MDwIgpTpOyTFNndJcjrsphjsYzYbEZahNdErrBJbwbAv4fsgVa6La7ZFB4oMtW21sdfICp3pD46J3E(s8ySKfVR8(c9pHwTxdgaI7jGF9yjXt2rCdB0LOJHuVmjXhnUxRWBYhaghHZTOuuiJb0ZzAJpdz38KXEWrl8yR6OvTnHAIxhjzRmAJr3HTiJfsgJfv0k9rDN3X))HXP(ax4f1kTTtoUuYXu(kmre(VmNhmf2DJDxNCbBL9B0DVmEN68ejwAhPWLmdcEtgVU4vOtoe6LkOgBEU9GaO2nl8Qt9tf)Uirl1uSe5P7NJiNskwrHmnQKReyfBRqHtudwHZf7XIoYePF7xTDWF)A2vkhPYd2g)sA6Kqb3jfE8AOaBOTW(TZhnuYcrwE(oISxfiKf4aKKXyF20zSwcUieUCufDE5yYfAOQIpWDFq1pEEsCzBJJGWG2s7HDnDbRBUch3HMKLekECrhKYy(eoK)(2OnCYXvksGvk3e)aTlMItlwwrKrBNMflCa1ebBLlURKpqyBNG9F5lnuUE4dA9bs(EMni6ct3)Twdn5MXS3Oe0fsaGlqJmGAKy0ENof2pzO0A5LoIcH24qSyKrIHCXVajFU1qSkdY6sCoSxAH5h3)XskVM)mSzbiFgvNQY3qxaBa81y4AqlyK1otoNgjqT6dIjgju2c00hS19YVAx1VjEiLBVj0UbG5qjRbv78mgyuOsDhplFWyrZmHAwRy6V(If2j4nZvmNE0KEGJh9d8(R3IrkkNiKfw82Ukj5PN4BUXrOZUwAMktH7l13AoX)ajLMDMBiTsc9kUW7TAdoYXiUlaHnqL8r)zyGjMd65XnDm(x1omZzN0YkW2w8yEQzDu)DISJiWSz6dG3)AVyxj8Vssyj)Wde(KLj8HdrX7iyPCy0Xsfhw)BzOx64nj4mBvL7QsXgL)2T5ceQ9J2r5ybvozKdkuA5ubSg17YuPbiLr1E9Ia6rYvHqgN8w)HTwBN1otmnmecmeuNr)8FAZHNBEPWEV0HiBnV1Y7psQeToRCLH99gUMSIZzbZvguj8ZybBhGa9R5A15hYt9X0xLzYR4(02jjc(DZIwz3K8utxNV3wS)VPYsT0q0N)Yor2KjvhCM)m(KnRQBhIoTESbMQsMMVZri5h6cu5MNKXHMgKx7SkkhkJ5OVXw3Hzia9ZAjcH6fGXjEM(2KClmegW7NH4.'
# key = 'd5ad4393a478566c'  # 密钥长度必须为16、24或32位，分别对应AES-128、AES-192和AES-256
# result_51 = get_aes_128_ecb(key, s)
# # result_52 = get_aes_128_ecb(key, result_51, False)
# # print('AES-128 加密：', len(result_51), result_51, '\t\tAES 解密：\t', result_52)
# print(result_51)
"6a2f1e57ce08f4d98ecaf4f300f4049fb5b06e08b9089688b7f1e492ef84af86e7c31cfca8fdfb5013e03788d600e67cf83ba41378387422f5f06757b1e3623f3ee2a215ce57461d7c86e52dc17ea6a2ab4ac5340f92713923519add66d7620e3bee489abbecb2e927d5bff12e7ba8e37a6ec784b2bb5fcb8ada4c3be783ba41"
s = 'UklGRi4AAABXRUJQVlA4TCEAAAAvAUAAEB8wAiMwAgSSNtse/cXjxyCCmrYNWPwmHRH9jwMA'
print(base64.b64decode(s).decode('gbk'))







"""d5ad4393a478566c

url = 'https://captcha6.scrape.center/api/login'
data1 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "6334bc0ad720bc197d66cbcc443435446z",
        "geetest_validate": "630559a530279fbea624a95e20724d09",
        "geetest_seccode": "630559a530279fbea624a95e20724d09|jordan",
        "status": 1,
        "type": "geetest",
    }

}

data2 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "1ffbadee6ff0abf2b78eee17cda99689",
        "geetest_validate": "fa9a7ae8b09dc3b94920b20382b1e551",
        "geetest_seccode": "fa9a7ae8b09dc3b94920b20382b1e551|jordan",
        "status": 1,
        "type": "geetest"
    }
}

data3 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "9bb47edf2890baff9241896bedc6fbd9",
        "geetest_validate": "1fd828ccba8651d790b1b037db4429e6",
        "geetest_seccode": "1fd828ccba8651d790b1b037db4429e6|jordan",
        "status": 1,
        "type": "geetest"
    }
}
data4 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "2f786ad6240e1ae89afecc2f8f5e0f8d",
        "geetest_validate": "cb4688edb29f3e175754723b376197ec",
        "geetest_seccode": "cb4688edb29f3e175754723b376197ec|jordan",
        "status": 1,
        "type": "geetest"
    }
}

data5 = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "536fb16afcf0c1a34c7b2e36a5e94ac3",
        "geetest_validate": "986d696310f149f23e2fb1f39e6d6113",
        "geetest_seccode": "986d696310f149f23e2fb1f39e6d6113|jordan",
        "status": 1,
        "type": "geetest"
    }
}
data = {
    "username": "admin",
    "password": "admin",
    "captcha": {
        "geetest_challenge": "654a8976d3292eb9aebb31c9be805c6f",
        "geetest_validate": "8a3f6fa49f46c1df1695213e949dd39d",
        "geetest_seccode": "8a3f6fa49f46c1df1695213e949dd39d|jordan",
        "status": 1,
        "type": "geetest"
    }
}

resp = requests.post(url, data=json.dumps(data))
print(resp.status_code)
print(resp.text)
"""

# -*- coding: utf-8 -*-
import json
import time
import random
import requests

""" 对接空间推理验证码，适合空间推理验证码分析处理。 """
""" 提示：对于字典嵌套字典传参方式用json.dumps()函数处理 """

t = int(time.time() * 1000)
url_init = f'https://captcha5.scrape.center/api/init?t={t}'
resp = requests.get(url_init)
data = resp.json()
print(resp.url, data)
gt = data['gt']
challenge = data['challenge']

url_gettype_php = 'https://api.geetest.com/gettype.php'
params = {'gt': gt, 'callback': f'geetest_{int(random.random() * 10000) + t}'}
resp = requests.get(url_gettype_php, params=params)
print(resp.url, resp.text)


def s_to_dic(headers_str):
    # headers_str = """
    # # origin: https://sou.zhaopin.com
    # referer: https://sou.zhaopin.com/?p=3&jl=765&kw=python&kt=3
    # sec-fetch-dest: empty
    # sec-fetch-mode: cors
    # sec-fetch-site: same-site
    # user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36
    # """
    import re
    pattern = '^(.*?): (.*)$|^(.*?):(.*)$'
    h = {}
    for line in headers_str.splitlines():
        if line == '' or line.startswith('#'):
            continue
        if ': ' not in line:
            line.replace(':', ': ')
        # print(re.sub(pattern, "\'\\1\': \'\\2\',", line))
        s = re.sub(pattern, '{\'\\1\': \'\\2\'}', line)
        h.update(eval(s))
    return h


url_get_php = 'https://api.geetest.com/get.php'

params_1 = f"""
gt: {gt}
challenge: {challenge}
lang: zh-cn
pt: 0
client_type: web
# w: tnD6fB4bhIiz9ukuC6VGIyV6m70Z4ryRaSDuGjtQ8AOjH4)Wvato4HEW)6Di8RV(Q25Hj7c0aQAwSJ(3ww2zQUOR0aW3o0qs6fDEX3DZOL2h89ls8XAElWTMFlhOpkeZYPjL30tEV2fUxtwO88MpOjj5EdrdUTQvEcoAGWW)yuJkTvHlNVflw1KwllcWCkqRg4b5ezRgVL)ZHiKXQl)sZocONmzsW(VX0pldjXgXYlooaFwBo5kjUDaWK2qmme2f8))bgyY6PNlrHzHtqpWIaccQAuG9E86iBfJHvuP8Y1)YnvN7gwPr7kBhoF8MWgobimNPu0FcJy6y3uq69bcUfGYIvYrhpxZBowG(gUSwdiSNHsW(OqcFecJ5sRtpSOSaABptLDYWXKxCVELdpvZL9vfSkdv12LI9WIGBJgCS(KgoP2MerZO(oCCrt(Fh8nN240qbFtpEjP7ra30EydGLkSEB0fmme(PsZB29Sd0Nzz7WEemr)DtRS4nYRT7c5syxzNkslvlPpdR9b5YTVLLb0qIBmetU13rbz)5nczEmNC2MbXG(iKArS6O50rrZDJWfMLB1Y9ch4sMEZMNzJTFE(LHhiv2AEVmcGuaD2vMjfVAkufEtWrGZL2dQcluXVbliKBI4f7cDmqwRPA2B2okHR(7RTlQTOW0OjSbXY)GJyeko89CNbT92kTod3R74uLQ7zSdMuUvTrlbrRvEgDo7Tsd7jWxuncuUAqfSp7b8ZWaQI0FfD1HQ3cLsvyi07YZgf9DOC)rYhSinuRrbV5UC0v5G8)3WIcXHh0p3UbPLqIhJpKxvLeoicXYxPhdUb90UEDEV9Zm7OSUuCk6pDu3mCxJFQqqvBbs2NwF)AlGp4z)33ChYXCzkNGjnIhvnSjJppj(RtGzjNHCwpFTsFWNegsfQ83VsGzVd1t4TU23b0PnKoKwS0iPqSLzvL97RmOaRn3tWNvJrAPpRYrzAycg8ipJHq6Eq(tewnFe5iF30bR0Zf3K3gRXZIhhViS)QqlTcZLLcV2fJsv6pBFMjNqAPU9ILS9IchwkZO8VZdMSiXs)mUH128OV1tsR(310nEGQ2jiy79fVbKeUwJF7mBoZ4vBw9QrRKK12styMnYwqO(YxezDgrIe8GMpfOVD5jEv8iv0XpS(en7f)q0vRoYKZbWx5HdmUtHB4JAvIcJNDM0OKxxVUbuWGjwWyGpC8T8oFRLc(6uO(pvXEtUtHE9j8L)ekM3QBfWAuZsJWD(crTierA0YEKXGOkUO(GENwQIl9ie4dHT5ZaQYHU12qsHk3(EEXWi)gMPWSPpuk)TtkJkAtYOnugOXl5RqbjyGkoYnPvS7N6nY5sNTI4D4)G()sOT7UeRPa3E)PFNE0k1HbZEVrrValiDJvdGTn(98ZRjMQUGmQZp(CxN(9uFbXMNWE1AtPCoOoF5AgB4Uko(x9IyoIy76kndGqwVDoRhgoxK5GC1CDGmLWCJ75oCLSXKCbn0o0Jqh7ao0Aj47BIz6OTvVYNv8MEP(UB3MQn5NaspCzEK0GRxUwfjnvMvuXV4Z4lXHTOL6pXHAdGxZW74BUBQgMXCG3UMmLgUTU9D51AERmdLYhGybNXAup2x2qoNavJuZSeZsULeSqMr0wO(HB)olVSH7Ppxw(idX2NqZwy3Ljp91v0l6Jn0K3pevdrMO(EemT(baJlSnUdtNAa0vaI1sYsCbC3Rp(IvuJpleASuht)k10J2g7Ufl)bYeSWUXOETLN1Wx99OmcA0pjPSYSmhkQ)jTXkIH0nBUoO52Did3urRBruR(S4JOu1wnFrw1uRaImBv8lztz((UiVtEDA7S(BpA9uj0fI5BMYETZHs(w5AHFslBF0OGepnE9G(WJ4uMDi(cnkJTc2fqTpyHLFy805cKJtk6hYtaPbzJ8Reg8qFHOa3(P435zFwt3G3LuyKqWowKrnwR1WjzzOzSMbiqtnso()NsdsohHsxkjhwsgu2SLzDhYArLN5)5bLbh2TPBQhuL36sIoQtpvjCckVXiUNYnO7YcdK(oCimWXqMXCV1XWZlmDL1VIybkxHWIHYDRxaLeaKjH1mSgPblQtk8Hk()LOIt29LV82d0Gnmf7nDh9PKsZYV8RLc3)HhmInJrWlZeUmT7NZSHZtUBLYYRfrw2FtQkMGs6z139TdYUfsI8L7aRRimSxCqPt015T1equrxFLJoTuYNbi(p4Mcf6mhvKIAXM(5OKcf5ZOmd1h0pz7OKxJqNlT0BArClQWjBKQ9VoT8EtgHUonkudP64w7ZDo5Qb8ZLC2VGjoCSvSk7AMZUieWlrLytjPwDR(TpHwkrJ02KwszyxKrggrC0GfH9E0.3bbffb586b020257e3e0aa45e6acc8a113e70149b62846412cc0febe5611b7b7630266f5c877ac7b3273cbf8e4f6cb1f621233d80b0ffd5f97ef9e2277388ee88e151010fe40214b2aa7ce37e64801b8f4ff063ef0007d82374b3b374232e88916763c99b1a8c4f539f69e8d3a34ff7cf4adcfe804cbd599e8dbb42db74153ed
callback: geetest_{int(random.random() * 10000) + t}
"""

params_1 = s_to_dic(params_1)
resp = requests.get(url_get_php, params=params_1)
print(resp.url, resp.text)


url_ajax_php = 'https://api.geetest.com/ajax.php'
params_2 = f"""
gt: {gt}
challenge: {challenge}
lang: zh-cn
pt: 0
client_type: web
# w: INIt2fOko5LHxxlY1JUObCSl2smZBhWl4Ao3o8BlVF6)OxqLOO1tJAOVuPIIdra4KhNI)jVlZi6uMUhM(cxABGY82w)TLyW(PNczWrNGJr(fgoi(lIJ92u)s51CP5UcxvxmzEqfgXI0cAY9PPulGKa99BoHFmNCHGzVEB0xmt)6onHzAVbQxPbwsauFs4vAv4UbePJQqR1uygexRcc6YUmaJYcMNoDoDbyFWCSOQLlgByd)Oe2w7ukSgaOVgusmyqdi56ghlfKXlQ3p3QwbvXnrTkboDFiMjdKMzw7OBoCO25POhGJuj5uyxcEmd2LZySrB4ZnK6KVC17BcWH(Cp4zCWD7KV9Fl4VCPXB847612WhrTvqog1mmw7xnqyHXnwBbycUI5AKeSPJiACNsb8L5qrzD0mHgfPLz1U70NybbNomWEtIPuThv4eFE)iTd(PS)oEjMQqa4)iS1BOiMMh8rG2pBykZ2lGZMa8MOTHs429PxOt84Bp80wArHPie5mtcJzrfhiWEwkwV42lLNAPdr6tbA76vTo69aMmKGvZZiIJj1he6ww6(HUNQDZOMW2O3BF4ECr)bvujZeVCrPp0CpdeNbsn7Re2ZqJtGrRbDy6GflRfomYYeCK9JyjS(01u6YHyefJ4gHJuku2ZCU1yL8A40rIouU4r3g9Q(bjebey7vfxUlbid(SZVF12F66t7wb7R2pD(4QzB9oa4cmD2tvZTWBvP5NlOlkFBGZqYa8yLHG5RloN4MM8AEkLwUn8dQFKmfWJTrsrwEOQB15FL019w)hDKIbSgKFCo9L1p3ywIKgHE5kSyf8DzHIVaZX7tHMAvSa0BiCV0ovLgC(NtnS5j3Bz0OAs4V6FC11KJ2Ff)fBstGR1H4BDx6tv4j9mOzW9FdxqjjLhoss3tLB)vOF7wMU69A0MIsr302GaQH)IbR1tG(78nC1nDUgkrYI)t1Iop3BozubybzsvOutLj2oogWJWjH2VGA3ZH)1q(5)92VwTWNIRG0ZVkM4EbyPOo)xH6kZuiZ)baUCip2J1hcarV1FhEuneHH((CNXMFvX9Mo4xLBanTy5WIjhZ0oW9fKQhfuP89YcMmMe53kPpT)KwwXgZVoz35rrBky5G7D8YWYSGQyQJE(ikzfI7Zr7joTOzp8CN2Imf6IAP2VhFmlTStk)GXlw)44C2vSumRdZnpT1F8CMa9qhgQ(mnVDmgdMvGHGtGougYXi6HBCJvAwogH8a4r9xf3w3ksq78KJfFcqgsxw(ypUE7YVEjR0AuefXZv6Ado48PX6K)KLETpyn7rGNnW(pslpDei1X(Ub)Vl9bc9aIZjR459LL948SyFPUHkGRRAc30EWgakAeGScet(JHW7hYWx1z9ImBcXb)E.
callback: geetest_{int(random.random() * 10000) + t}
"""
params_2 = s_to_dic(params_2)
resp = requests.get(url_ajax_php, params=params_2)
print(resp.url, resp.text)




params_3 = f"""
is_next: true
type: slide3
gt: {gt}
challenge: {challenge}
lang: zh-cn
https: true
protocol: https://
offline: false
product: embed
api_server: api.geetest.com
isPC: true
autoReset: true
width: 100%
callback: geetest_{int(random.random() * 10000) + t}
"""
params_3 = s_to_dic(params_3)
resp = requests.get(url_get_php, params=params_3)
print(resp.url, resp.text)


params_4 = f"""
gt: {gt}
challenge: {challenge}
lang: zh-cn
$_BBF: 0
client_type: web
# w: HCnn2SsLJCvfQi)HCB7Uag2XQm4ipeXwMpfVQqCFtfgoQDYMZ4cFACLCINqakPMyEN2WJcpf)ek2N9YTy5jbbsqxm0vGgfs)bwLrektvG(aQdONP5qkwZO9XBbx9kTxenS2N8R4WbMMKf7VPoxrHER(ZlPu5mhj6pkhuf6UZGjskxz7piZY8Um7G1IadbzEpguelDYIwHzIy7CZrnbaB3ChrvwomYPgNM8gOgHUyF)h5pZXkXnjO2YTeYrXQJhpohrm1Waw9toAuZSbhB)FS(BrysESydWQzTWDDKbR)iSIUsUljpDh5bxjguFVaaRzx8joXMScDXufuxvRcmtrid4DP3k25nMqICGLsCxi24AazcAT0YroxOeV0yOAPQVv3)r9YxVhFIADNUcXafeQ3I47pKYcVu2f3JVs04aqNdpCeLpMydT(BCvLcVskO(Md0dz5J88xzXC5thhQMnhr1JOg4ZOKPq96oSgdFvCkDGsU)xllh3z3CseO043MfBJNvGSYJbrTnmuskME038XwG1cftM8Fr6pCZMnLt6RFB8efFl660fIZicKJNK6zHyUprjG9)UBKcVnsUV41uwraBbMwrvPrHJS7Mc)7Hp)sJjc3SpqrqH(6TRwIu9S7GX16oRcYLsh9NLULmYKorc5mRGGHNgTnhNSbr2255aN1(UAbWB)hhBI5bslxmZQQqaCzQViSIFVPsPO3x9t)XF6qj2pzs8qJURS2Nyzp9SnKUilDMzTZdqi6uIMDqW84T1Gyk0gbSvYrv7NeqN(n4RMRwh9k5fOsyoIaJ527JlGbRtziyUGnl6CGTBgqy40e9x95JxcnBcQHMId5PHRVG5S)WOzFtuFIkQaAizdH6KiY2diWk1yZ)QyGYYvNgiUOrMZFh1mpQbg5XOW)h3dxMuAZoenZQIPd)4p2jRK(SWLfqm7aZbSjtnJ0ONq6e4ZmOeP0pHaT99OrHCIsI4bXUiWiaRKdt5pazn(crwghD5D(wlDc2RUnrDS8kQwBZM3k3g7EecvkWgSV4(p(ZztMe5ItyZQ..c1390b57867fbf2b425ead8b19c8ab9d9439cf5a938ea81c34729096c43f38abfae647a8f340c86cac1c2a227823d5a062c670fb47a09ea97c2bb06a047f4753b8e4bb2d5f425189ceaa77a11f5b5c282a34d991b92783880ae97b68793b2692d0008890f39089cf34a8188d151fec0c9c8bebdb8967f568482dbbad9f802e66
callback: geetest_{int(random.random() * 10000) + t}
"""
params_4 = s_to_dic(params_4)
resp = requests.get(url_ajax_php, params=params_4)
print(resp.url, resp.text)












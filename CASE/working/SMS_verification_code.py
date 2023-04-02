import requests
import re
from lxml import etree

""" 亦可访问获取：https://www.zusms.com/phone/china """

def get_code(phone: str = 11):
    url_code = f'https://k8s1.com/messages/{phone}'
    response = requests.get(url_code)
    response.encoding = 'utf-8'
    # print(response.text)
    xml = etree.HTML(response.text)
    codes = xml.xpath('/html/body/main/div[2]/div/div[1]/div/div[position()>=1 and position()<=3]/div[2]/div/text()')  # 最近前三条短信
    # codes = xml.xpath('/html/body/main/div[2]/div/div[1]/div/div[1]/div[2]/div/text()')
    for code in codes:
        code_info = code.strip()
        obj = re.compile('\d{4,6}')
        code = obj.findall(code_info)[0]
        print(phone, code, '\t', code_info)
        # break
        # return code

def k8s1(url):
    for page in range(1, 12):
        url = f'{url}/?page={page}'
        # headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'}
        response = requests.get(url)
        # print(response.text)
        xml = etree.HTML(response.text)
        phones = xml.xpath('//h3/a/text()')
        print(phones)
        for phone in phones:
            code = get_code(phone)
            print(code)
            # return phone, code
            break
        break



def zusms(url):
    response = requests.get(url)
    xml = etree.HTML(response.text)
    phones = xml.xpath('/html/body/div/div[2]/div/div/div/h2/a/text()')
    phones_href = xml.xpath('/html/body/div/div[2]/div/div/div/h2/a/@href')
    for phone, link in zip(phones, phones_href):
        phone = phone[4:]
        url_info = 'https://www.zusms.com' + link
        response = requests.get(url_info)
        # print(response.text)
        xml = etree.HTML(response.text)
        code_info = xml.xpath('/html/body/div/div[1]/div[1]/div/h1/div[5]/text()')[0]
        obj = re.compile('\d{4,6}')
        code = obj.findall(code_info)[0]
        print(phone, code, '\t', code_info)
        break
        # return phone, code


if __name__ == '__main__':
    # k8s1('https://k8s1.com')
    # zusms('https://www.zusms.com/phone/china')
    print(get_code('15442717267'))

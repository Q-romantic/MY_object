import os, re, execjs, json, img2pdf
# 安装：python39 -m pip install PyExecJS
# 安装：python39 -m pip install img2pdf
import requests
from requests_html import HTMLSession

session = HTMLSession()


class DOC88Spider(object):
    os_path = os.getcwd() + '/道客巴巴文档/'
    if not os.path.exists(os_path):
        os.mkdir(os_path)

    '''js处理密文代码'''
    js_demo = """
    var m_END_OF_INPUT = -1;
	var m_base64Chars_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
	var m_base64Chars = new Array(
		'P', 'J', 'K', 'L', 'O', 'N', 'M', 'I',
		'3', 'x', 'y', 'z', '0', '1', '2', 'w',
		'v', 'p', 'r', 'q', 's', 't', 'u', 'o',
		'H', 'B', 'C', 'D', 'E', 'F', 'G', 'A',
		'n', 'h', 'i', 'j', 'k', 'l', 'm', 'g',
		'f', 'Z', 'a', 'b', 'c', 'd', 'e', 'Y',
		'X', 'R', 'S', 'T', 'U', 'V', 'W', 'Q',
		'!', '5', '6', '7', '8', '9', '+', '4'
	);
	m_base64Chars[4] = 'M';
	m_base64Chars[6] = 'O';
	var m_base64Chars_r = new Array(
		'P', 'J', 'L', 'K', 'M', 'N', 'O', 'I',
		'3', 'x', 'y', 'z', '0', '2', '1', 'w',
		'v', 'r', 'p', 'q', 's', 't', 'o', 'u',
		'H', 'C', 'F', 'B', 'D', 'E', 'G', 'A',
		'n', 'h', 'i', 'k', 'j', 'l', 'm', 'g',
		'f', 'Z', 'b', 'a', 'c', 'e', 'd', 'Y',
		'R', 'X', 'T', 'S', 'U', 'V', 'Q', 'W',
		'!', '5', '6', '7', '8', '9', '+', '4'
	);
	var m_reverseBase64Chars = new Array(128);
	for (var i = 0; i < m_base64Chars_r.length; i++) {
		m_reverseBase64Chars[m_base64Chars_r[i]] = i;
	}
	var m_base64Str;
	var m_base64Count;
	m_setBase64Str = function(str) {
		m_base64Str = str;
		m_base64Count = 0;
	};
	m_readBase64 = function() {
		if (!m_base64Str) return m_END_OF_INPUT;
		if (m_base64Count >= m_base64Str.length) return m_END_OF_INPUT;
		var c = m_base64Str.charCodeAt(m_base64Count) & 0xff;
		m_base64Count++;
		return c;
	};
	m_encodeBase64 = function(str) {
		str = m_utf16to8(str);
		m_setBase64Str(str);
		var result = '';
		var inBuffer = new Array(3);
		var lineCount = 0;
		var done = false;
		while (!done && (inBuffer[0] = m_readBase64()) != m_END_OF_INPUT) {
			inBuffer[1] = m_readBase64();
			inBuffer[2] = m_readBase64();
			result += (m_base64Chars[inBuffer[0] >> 2]);
			if (inBuffer[1] != m_END_OF_INPUT) {
				result += (m_base64Chars[((inBuffer[0] << 4) & 0x30) | (inBuffer[1] >> 4)]);
				if (inBuffer[2] != m_END_OF_INPUT) {
					result += (m_base64Chars[((inBuffer[1] << 2) & 0x3c) | (inBuffer[2] >> 6)]);
					result += (m_base64Chars[inBuffer[2] & 0x3F]);
				} else {
					result += (m_base64Chars[((inBuffer[1] << 2) & 0x3c)]);
					result += ('=');
					done = true;
				}
			} else {
				result += (m_base64Chars[((inBuffer[0] << 4) & 0x30)]);
				result += ('=');
				result += ('=');
				done = true;
			}

		}
		return result;
	};
	m_readReverseBase64 = function() {
		if (!m_base64Str) return m_END_OF_INPUT;
		while (true) {
			if (m_base64Count >= m_base64Str.length) return m_END_OF_INPUT;
			var nextCharacter = m_base64Str.charAt(m_base64Count);
			m_base64Count++;
			if (m_reverseBase64Chars[nextCharacter]) {
				return m_reverseBase64Chars[nextCharacter];
			}
			if (nextCharacter == 'P') return 0;
		}
		return m_END_OF_INPUT;
	};
	m_ntos = function(n) {
		n = n.toString(16);
		if (n.length == 1) n = "0" + n;
		n = "%" + n;
		return unescape(n);
	};

	m_decodeBase64 = function(str) {
		m_setBase64Str(str);
		var result = "";
		var inBuffer = new Array(4);
		var done = false;
		while (!done && (inBuffer[0] = m_readReverseBase64()) != m_END_OF_INPUT && (inBuffer[1] = m_readReverseBase64()) != m_END_OF_INPUT) {
			inBuffer[2] = m_readReverseBase64();
			inBuffer[3] = m_readReverseBase64();
			result += m_ntos((((inBuffer[0] << 2) & 0xff) | inBuffer[1] >> 4));
			if (inBuffer[2] != m_END_OF_INPUT) {
				result += m_ntos((((inBuffer[1] << 4) & 0xff) | inBuffer[2] >> 2));
				if (inBuffer[3] != m_END_OF_INPUT) {
					result += m_ntos((((inBuffer[2] << 6) & 0xff) | inBuffer[3]));
				} else {
					done = true;
				}
			} else {
				done = true;
			}
		}
		result = m_utf8to16(result);
		return result;
	};
	m_utf16to8 = function(str) {
		var out, i, len, c;
		out = "";
		len = str.length;
		for (i = 0; i < len; i++) {
			c = str.charCodeAt(i);
			if ((c >= 0x0001) && (c <= 0x007F)) {
				out += str.charAt(i);
			} else if (c > 0x07FF) {
				out += String.fromCharCode(0xE0 | ((c >> 12) & 0x0F));
				out += String.fromCharCode(0x80 | ((c >> 6) & 0x3F));
				out += String.fromCharCode(0x80 | ((c >> 0) & 0x3F));
			} else {
				out += String.fromCharCode(0xC0 | ((c >> 6) & 0x1F));
				out += String.fromCharCode(0x80 | ((c >> 0) & 0x3F));
			}
		}
		return out;
	};

	m_utf8to16 = function(str) {
		var out, i, len, c;
		var char2, char3;
		out = "";
		len = str.length;
		i = 0;
		while (i < len) {
			c = str.charCodeAt(i++);
			switch (c >> 4) {
				case 0:
				case 1:
				case 2:
				case 3:
				case 4:
				case 5:
				case 6:
				case 7:
					out += str.charAt(i - 1);
					break;
				case 12:
				case 13:
					char2 = str.charCodeAt(i++);
					out += String.fromCharCode(((c & 0x1F) << 6) | (char2 & 0x3F));
					break;
				case 14:
					char2 = str.charCodeAt(i++);
					char3 = str.charCodeAt(i++);
					out += String.fromCharCode(((c & 0x0F) << 12) |
						((char2 & 0x3F) << 6) |
						((char3 & 0x3F) << 0));
					break;
			}
		}
		return out;
	};
    """
    ctx = execjs.compile(js_demo)

    def __init__(self):
        # 用户输入
        # self.user_input = input('请输入文档地址(例如：https://m.doc88.com/p-6387803978819.html)：\n')
        self.user_input = 'https://m.doc88.com/p-05429759423388.html'
        # 响应为加密密文地址
        self.base_64_url = 'https://m.doc88.com/doc.php?act=info&p_code={}&key=8e9f31554a68fb6eef61d4c069646723&v=1&pid=1401638899'
        # pdf内容图片地址
        self.img_url = 'https://gif1.doc88.com/get-{}.gif'
        # 通用的请求头
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/94.0.4606.81'
        }
        # 获取当前文档类型后缀（.doc/.pptx/.pdf/.xls/.txt）
        # self.suffix = re.findall(r'<p>格式：<span>(.*?)</span></p>', session.get(self.user_input, headers=self.headers).text)[0].lower()
        self.suffix = 'pdf'

    def parse_join_url_data(self):
        # 获取文档id
        p_code = re.findall(r'p-(\d+)\.html', self.user_input)[0]
        # 拼接地址
        base_64_url = self.base_64_url.format(p_code)
        # print(base_64_url)
        response = session.get(base_64_url, headers=self.headers).content.decode()
        # print(response)
        self.parse_js_parse_data(response)

    def parse_js_parse_data(self, response_data):
        # 调用js环境，执行
        result = self.ctx.call('m_decodeBase64', response_data)
        # print(result)
        # 将字符串转换成字典
        json_dict = json.loads(result)
        # print(json_dict)
        # 提取文档名称
        name = json_dict['p_name']
        # 提取文档数据大列表
        pageInfo = json_dict['pageInfo']
        json_list = self.ctx.call('m_decodeBase64', pageInfo).split(',')
        '''类中函数方法之间调用'''
        self.parse_json_list_data(name, json_list, json_dict)

    def parse_json_list_data(self, name, json_list, json_dict):
        data_list = []
        m_header = json_list[0][0] + "-0-" + json_dict['headerInfo'][1:-1] + "-" + json_dict['p_swf']
        m_headerUrl = "https://ebt202mn.doc88.com/getebt-" + self.ctx.call('m_encodeBase64', m_header) + ".ebt"
        # print(m_headerUrl)
        data = requests.get(m_headerUrl).text
        js_fn = """
        get_buffer = function (sss) {
        let encoder = new TextEncoder();
        // 字符 转 Uint8Array
            let uint8Array = encoder.encode(sss);
        // Uint8Array 转 ArrayBuffer
            let arrayBuffer = uint8Array.buffer
            console.log(uint8Array)
            return uint8Array
        }
                    """
        z = execjs.compile(js_fn)
        f = lambda x: z.call('get_buffer', x)
        print(len(f(data)))

        data_list.append(data)
        tmp = []
        for page, i in enumerate(json_list):
            i = i.split('-')
            m_page = i[0] + "-" + i[-2] + "-" + i[-1] + "-" + json_dict['p_swf'] + "-" + str(page + 1) + "-" + json_dict['p_code']
            m_pageUrl = "https://ebt202mn.doc88.com/getebt-" + self.ctx.call('m_encodeBase64', m_page) + ".ebt"
            # print(m_page)
            data = requests.get(m_pageUrl).text
            # resp = requests.get(m_pageUrl, allow_redirects=False)
            # location = resp.headers.get('location')
            # data = requests.get(location).text
            print('-----' * 15)
            print(data)


#             js_fn = """
#             get_buffer = function (sss) {
#     let encoder = new TextEncoder();
# // 字符 转 Uint8Array
#     let uint8Array = encoder.encode(sss);
# // Uint8Array 转 ArrayBuffer
#     let arrayBuffer = uint8Array.buffer
#     console.log(uint8Array)
#     return uint8Array.toString()
# }
#             """
#             z = execjs.compile(js_fn)
#             f = lambda x: z.call('get_buffer', x)
#             print(f(data))




            # data_list.append(data)
            # print(f'正在下载-----{m_page}页-----下载完成')
            break
        # # 定义pdf的格式：是以A4纸格式定义的
        # a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        # # 应用
        # layout_fun = img2pdf.get_layout_fun(a4inpt)
        # with open(self.os_path + name + '.' + self.suffix, 'wb') as f:
        #     f.write(img2pdf.convert(data_list, layout_fun=layout_fun))
        #     print(f'文档：{name}------下载完成！')


if __name__ == '__main__':
    d = DOC88Spider()
    d.parse_join_url_data()

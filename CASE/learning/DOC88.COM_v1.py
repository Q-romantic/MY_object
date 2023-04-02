import os, re, execjs, json, img2pdf
# 安装：python39 -m pip install PyExecJS
# 安装：python39 -m pip install img2pdf

from requests_html import HTMLSession

session = HTMLSession()


class DOC88Spider(object):
    os_path = os.getcwd() + '/道客巴巴文档/'
    if not os.path.exists(os_path):
        os.mkdir(os_path)

    '''js处理密文代码'''
    js_demo = """
    var m_END_OF_INPUT = -1;
    var m_base64Chars_r = new Array(
            'P','J','K','L','M','N','O','I',
            '3','y','x','z','0','1','2','w',
            'v','p','r','q','s','t','u','o',
            'B','H','C','D','E','F','G','A',
            'h','n','i','j','k','l','m','g',
            'f','Z','a','b','c','d','e','Y',
            'X','R','S','T','U','V','W','Q',
            '!','5','6','7','8','9','+','4'
    );
    var m_reverseBase64Chars = new Array(128);
    for (var i=0; i < m_base64Chars_r.length; i++)
    {
        m_reverseBase64Chars[m_base64Chars_r[i]] = i;
    }

    var m_base64Str;
    var m_base64Count;
    function m_setBase64Str(str)
    {
        m_base64Str = str;
        m_base64Count = 0;
    }
    function m_readBase64()
    {
        if (!m_base64Str) return m_END_OF_INPUT;
        if (m_base64Count >= m_base64Str.length) return m_END_OF_INPUT;
        var c = m_base64Str.charCodeAt(m_base64Count) & 0xff;
        m_base64Count++;
        return c;
    }

    function m_readReverseBase64()
    {
        if (!m_base64Str) return m_END_OF_INPUT;
        while (true)
        {
            if (m_base64Count >= m_base64Str.length) return m_END_OF_INPUT;
            var nextCharacter = m_base64Str.charAt(m_base64Count);
            m_base64Count++;
            if (m_reverseBase64Chars[nextCharacter])
            {
                return m_reverseBase64Chars[nextCharacter];
            }
            if (nextCharacter == 'P') return 0;
        }
        return m_END_OF_INPUT;
    }

    function m_ntos(n)
    {
        n = n.toString(16);
        if (n.length == 1) n = "0" + n;
        n = "%" + n;
        return unescape(n);
    }

    function m_decodeBase64(str)
    {
        m_setBase64Str(str);
        var result = "";
        var inBuffer = new Array(4);
        var done = false;
        while (!done && (inBuffer[0] = m_readReverseBase64()) != m_END_OF_INPUT&& (inBuffer[1] = m_readReverseBase64()) != m_END_OF_INPUT){
            inBuffer[2] = m_readReverseBase64();
            inBuffer[3] = m_readReverseBase64();
            result += m_ntos((((inBuffer[0] << 2) & 0xff)| inBuffer[1] >> 4));
            if (inBuffer[2] != m_END_OF_INPUT){
                result +=  m_ntos((((inBuffer[1] << 4) & 0xff)| inBuffer[2] >> 2));
                if (inBuffer[3] != m_END_OF_INPUT){
                    result +=  m_ntos((((inBuffer[2] << 6)  & 0xff) | inBuffer[3]));
                } else {
                    done = true;
                }
            } else {
                done = true;
            }
        }
        result = m_utf8to16(result);
        return result;
    }
    function m_utf16to8(str) {
        var out, i, len, c;
        out = "";
        len = str.length;
        for(i = 0; i < len; i++) {
            c = str.charCodeAt(i);
            if ((c >= 0x0001) && (c <= 0x007F)) {
                out += str.charAt(i);
            } else if (c > 0x07FF) {
                out += String.fromCharCode(0xE0 | ((c >> 12) & 0x0F));
                out += String.fromCharCode(0x80 | ((c >>  6) & 0x3F));
                out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
            } else {
                out += String.fromCharCode(0xC0 | ((c >>  6) & 0x1F));
                out += String.fromCharCode(0x80 | ((c >>  0) & 0x3F));
            }
        }
        return out;
    }

    function m_utf8to16 (str)
    {
        var out, i, len, c;
        var char2, char3;
        out = "";
        len = str.length;
        i = 0;
        while(i < len) {
            c = str.charCodeAt(i++);
            switch(c >> 4)
            {
                case 0: case 1: case 2: case 3: case 4: case 5: case 6: case 7:
                out += str.charAt(i-1);
                break;
                case 12: case 13:
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
    }
    """
    ctx = execjs.compile(js_demo)

    def __init__(self):
        # 用户输入
        # self.user_input = input('请输入文档地址(例如：https://m.doc88.com/p-6387803978819.html)：\n')
        self.user_input = 'https://m.doc88.com/p-05429759423388.html'
        # 响应为加密密文地址，注意：如下 &v=2，或非1可以得到未加密（即解密后内容）数据
        self.base_64_url = 'https://m.doc88.com/doc.php?act=info&p_code={}&key=3854933de90d1dbb321d8ca29eac130a&v=1'
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
        print(base_64_url)
        response = session.get(base_64_url, headers=self.headers).content.decode()
        print(response)
        self.parse_js_parse_data(response)

    def parse_js_parse_data(self, response_data):
        # 调用js环境，执行
        result = self.ctx.call('m_decodeBase64', response_data)
        # print(result)
        # 将字符串转换成字典
        json_dict = json.loads(result)
        print(json_dict)
        # 提取文档名称
        name = json_dict['filename']
        # 提取文档数据大列表
        try:
            gif_struct = json_dict['gif_struct']
        except:
            gif_struct = json_dict['struct']
        # 将字符串转换成列表
        json_list = json.loads(gif_struct)
        '''类中函数方法之间调用'''
        self.parse_json_list_data(name, json_list)

    def parse_json_list_data(self, name, json_list):
        data_list = []
        for j_data in json_list:
            page_num = j_data['p']
            u_id = j_data['u']
            # print(self.ctx.call('m_decodeBase64', u_id))
            doc_info_url = self.img_url.format(u_id)
            data = session.get(doc_info_url).content
            # from PIL import Image
            # from io import BytesIO
            # img = Image.open(BytesIO(data))
            # img.show()
            data_list.append(data)
            print(f'正在下载-----{page_num}页-----下载完成')
            # break
        # 定义pdf的格式：是以A4纸格式定义的
        a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        # 应用
        layout_fun = img2pdf.get_layout_fun(a4inpt)
        with open(self.os_path + name + '.' + self.suffix, 'wb') as f:
            f.write(img2pdf.convert(data_list, layout_fun=layout_fun))
            print(f'文档：{name}------下载完成！')


if __name__ == '__main__':
    d = DOC88Spider()
    d.parse_join_url_data()

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
m_setBase64Str = function (str) {
    m_base64Str = str;
    m_base64Count = 0;
};
m_readBase64 = function () {
    if (!m_base64Str) return m_END_OF_INPUT;
    if (m_base64Count >= m_base64Str.length) return m_END_OF_INPUT;
    var c = m_base64Str.charCodeAt(m_base64Count) & 0xff;
    m_base64Count++;
    return c;
};
m_encodeBase64 = function (str) {
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
m_readReverseBase64 = function () {
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
m_ntos = function (n) {
    n = n.toString(16);
    if (n.length == 1) n = "0" + n;
    n = "%" + n;
    return unescape(n);
};

m_decodeBase64 = function (str) {
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
m_utf16to8 = function (str) {
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

m_utf8to16 = function (str) {
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



// let resBlob = new Blob([xxx]) //res为arraybuffer型数据
// let reader = new FileReader()
// reader.readAsText(resBlob, "utf-8")
// reader.onload = () => {
// 	let tmpResObj = JSON.parse(reader.result)
// }


// // 1、TextEncoder => ArrayBuffer
// let encoder = new TextEncoder();
// // 字符 转 Uint8Array
// let uint8Array = encoder.encode("你好啊");
// // Uint8Array 转 ArrayBuffer
// let arrayBuffer = uint8Array.buffer
// console.log(uint8Array)
// console.log(arrayBuffer)


// // 2、Blob => ArrayBuffer
// let str = 'hello，你好吗？'
// let blob = new Blob([str],{type:'text/plain;charset=utf-8'});
// let utf8decoder = new TextDecoder()
// blob.arrayBuffer().then(buffer=>{
//   // ArrayBuffer
//   console.log(buffer)
//   let text = utf8decoder.decode(buffer)
//   // String
//   console.log(text)
// })

sss = "uâIÌÀ³Ü!1Ù¯PB;¡f×¯#zÛålÐ(xÚuy<ÔÛÿÇ1ø}lc7fÆ¾KÈ`5¡"
get_buffer = function (sss) {
    let encoder = new TextEncoder();
// 字符 转 Uint8Array
    let uint8Array = encoder.encode(sss);
// Uint8Array 转 ArrayBuffer
    let arrayBuffer = uint8Array.buffer
    console.log(uint8Array)
}
get_buffer(sss)

// _I2_buf: 6071808
// _I2_counts: 391
// HEAPU8.subarray(_I2_buf, _I2_buf + _I2_counts * 4).toString()
// HEAPU8.subarray(6071808, 6071808 + 391 * 4).toString()
// [6071808 - 6073372]
HEAPU8 = [53, 0, 0, 0, 51, 0, 0, 0, 10, 0, 0, 0, 50, 0, 0, 0, 48, 0, 0, 0, 49, 0, 0, 0, 52, 0, 0, 0, 32, 0, 0, 0, 116, 94, 0, 0, 127, 137, 0, 0, 87, 83, 0, 0, 39, 89, 0, 0, 102, 91, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 3, 128, 0, 0, 20, 120, 0, 0, 31, 119, 0, 0, 152, 152, 0, 0, 10, 0, 0, 0, 54, 0, 0, 0, 51, 0, 0, 0, 53, 0, 0, 0, 32, 0, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 26, 144, 0, 0, 186, 139, 0, 0, 10, 0, 0, 0, 0, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 249, 91, 0, 0, 186, 78, 0, 0, 132, 118, 0, 0, 44, 103, 0, 0, 39, 96, 0, 0, 238, 149, 0, 0, 152, 152, 0, 0, 132, 118, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 29, 96, 0, 0, 3, 128, 0, 0, 8, 255, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 140, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 186, 139, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 14, 78, 0, 0, 151, 91, 0, 0, 89, 101, 0, 0, 132, 118, 0, 0, 115, 81, 0, 0, 251, 124, 0, 0, 8, 255, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 9, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 176, 115, 0, 0, 227, 78, 0, 0, 209, 121, 0, 0, 102, 91, 0, 0, 59, 78, 0, 0, 73, 78, 0, 0, 29, 96, 0, 0, 110, 111, 0, 0, 132, 118, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 194, 137, 0, 0, 196, 139, 0, 0, 144, 103, 0, 0, 8, 255, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 219, 86, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 249, 91, 0, 0, 142, 127, 0, 0, 132, 118, 0, 0, 44, 103, 0, 0, 40, 141, 0, 0, 132, 118, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 29, 96, 0, 0, 3, 128, 0, 0, 8, 255, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 148, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 186, 139, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 14, 78, 0, 0, 56, 94, 0, 0, 198, 139, 0, 0, 132, 118, 0, 0, 115, 81, 0, 0, 251, 124, 0, 0, 8, 255, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 56, 0, 0, 0, 52, 0, 0, 0, 51, 0, 0, 0, 32, 0, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 252, 126, 0, 0, 8, 84, 0, 0, 10, 0, 0, 0, 0, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 125, 84, 0, 0, 152, 152, 0, 0, 6, 82, 0, 0, 144, 103, 0, 0, 8, 255, 0, 0, 9, 78, 0, 0, 9, 144, 0, 0, 140, 78, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 207, 107, 0, 0, 152, 152, 0, 0, 32, 0, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 113, 81, 0, 0, 32, 0, 0, 0, 54, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 49, 0, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 11, 119, 0, 0, 60, 79, 0, 0, 224, 101, 0, 0, 40, 117, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 116, 83, 0, 0, 9, 103, 0, 0, 39, 89, 0, 0, 40, 117, 0, 0, 10, 0, 0, 0, 50, 0, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 186, 78, 0, 0, 31, 117, 0, 0, 12, 128, 0, 0, 234, 129, 0, 0, 49, 117, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 116, 83, 0, 0, 224, 101, 0, 0, 128, 95, 0, 0, 13, 78, 0, 0, 40, 87, 0, 0, 183, 103, 0, 0, 1, 149, 0, 0, 75, 78, 0, 0, 45, 78, 0, 0, 10, 0, 0, 0, 51, 0, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 17, 98, 0, 0, 29, 96, 0, 0, 69, 101, 0, 0, 17, 98, 0, 0, 40, 87, 0, 0, 10, 0, 0, 0, 140, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 72, 104, 0, 0, 139, 79, 0, 0, 6, 82, 0, 0, 144, 103, 0, 0, 152, 152, 0, 0, 8, 255, 0, 0, 207, 107, 0, 0, 152, 152, 0, 0, 32, 0, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 49, 0, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 247, 139, 0, 0, 238, 149, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 83, 95, 0, 0, 202, 78, 0, 0, 45, 78, 0, 0, 253, 86, 0, 0, 250, 81, 0, 0, 176, 115, 0, 0, 132, 118, 0, 0, 28, 32, 0, 0, 13, 78, 0, 0, 98, 101, 0, 0, 118, 98, 0, 0, 84, 100, 0, 0, 18, 80, 0, 0, 132, 118, 0, 0, 1, 128, 0, 0, 186, 78, 0, 0, 29, 32, 0, 0, 32, 0, 0, 0, 132, 118, 0, 0, 176, 115, 0, 0, 97, 140, 0, 0, 152, 98, 0, 0, 4, 92, 0, 0, 250, 81, 0, 0, 14, 96, 0, 0, 55, 104, 0, 0, 132, 118, 0, 0, 62, 121, 0, 0, 10, 0, 0, 0, 26, 79, 0, 0, 176, 115, 0, 0, 158, 91, 0, 0, 238, 149, 0, 0, 152, 152, 0, 0, 31, 255, 0, 0, 32, 0, 0, 0, 17, 98, 0, 0, 236, 78, 0, 0, 148, 94, 0, 0, 229, 139, 0, 0, 14, 96, 0, 0, 55, 104, 0, 0, 112, 141, 0, 0, 250, 81, 0, 0, 217, 143, 0, 0, 55, 104, 0, 0, 132, 118, 0, 0, 83, 144, 0, 0, 183, 95, 0, 0, 240, 86, 0, 0, 131, 88, 0, 0, 31, 255, 0, 0, 10, 0, 0, 0, 50, 0, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 247, 139, 0, 0, 40, 117, 0, 0, 242, 84, 0, 0, 102, 91, 0, 0, 132, 118, 0, 0, 6, 82, 0, 0, 144, 103, 0, 0, 185, 101, 0, 0, 213, 108, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 49, 92, 0, 0, 17, 98, 0, 0, 253, 86, 0, 0, 130, 89, 0, 0, 85, 79, 0, 0, 158, 91, 0, 0, 176, 115, 0, 0, 108, 143, 0, 0, 139, 87, 0, 0, 209, 83, 0, 0, 85, 92, 0, 0, 8, 140, 0, 0, 8, 140, 0, 0, 96, 79, 0, 0, 132, 118, 0, 0, 11, 119, 0, 0, 213, 108, 0, 0, 2, 48, 0, 0, 10, 0, 0, 0, 9, 78, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 153, 81, 0, 0, 92, 79, 0, 0, 152, 152, 0, 0, 8, 255, 0, 0, 51, 0, 0, 0, 48, 0, 0, 0, 32, 0, 0, 0, 6, 82, 0, 0, 9, 255, 0, 0, 10, 0, 0, 0, 49, 0, 0, 0, 1, 48, 0, 0, 32, 0, 0, 0, 247, 139, 0, 0, 57, 104, 0, 0, 110, 99, 0, 0, 96, 79, 0, 0, 64, 98, 0, 0, 165, 98, 0, 0, 3, 128, 0, 0, 132, 118, 0, 0, 102, 91, 0, 0, 209, 121, 0, 0, 19, 78, 0, 0, 26, 78, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 229, 78, 0, 0, 10, 48, 0, 0, 17, 98, 0, 0, 249, 91, 0, 0, 42, 0, 0, 0, 42, 0, 0, 0, 102, 91, 0, 0, 132, 118, 0, 0, 164, 139, 0, 0, 198, 139, 0, 0, 11, 48, 0, 0, 32, 0, 0, 0, 58, 78, 0, 0, 152, 152, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 153, 81, 0, 0, 0, 78, 0, 0, 199, 123, 0, 0, 15, 92, 0, 0, 10, 0, 0, 0, 186, 139, 0, 0, 135, 101, 0, 0, 12, 255, 0, 0, 32, 0, 0, 0, 87, 91, 0, 0, 112, 101, 0, 0, 13, 78, 0, 0, 80, 150, 0, 0, 2, 48, 0, 0, 10, 0, 0, 0]
var _I2_str = "";
for (var i = 0; i < HEAPU8.length; i++) {
    var _QF = HEAPU8[i + 1].toString(16);
    var _tf = HEAPU8[i].toString(16);
    if (_QF.length == 1) {
        _QF = "0" + _QF
    }
    if (_tf.length == 1) {
        _tf = "0" + _tf
    }
    i++;
    i++;
    i++;
    var unicode = "\\u" + _QF + _tf;
    _I2_str = _I2_str + unicode
}
m_text = unescape(_I2_str.replace(/\\u/g, '%u'));
console.log(m_text)


// _I2_rects: 5707032
// _I2_counts: 391
// HEAPU8.subarray(_I2_rects, _I2_rects + _I2_counts * 16).toString()
// [5707032 - 5713288]
_I2_rects = 0
HEAPU8 = [241, 1, 0, 0, 16, 3, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 245, 1, 0, 0, 16, 3, 0, 0, 5, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 177, 0, 0, 0, 86, 0, 0, 0, 9, 0, 0, 0, 17, 0, 0, 0, 186, 0, 0, 0, 86, 0, 0, 0, 9, 0, 0, 0, 17, 0, 0, 0, 195, 0, 0, 0, 86, 0, 0, 0, 9, 0, 0, 0, 17, 0, 0, 0, 204, 0, 0, 0, 86, 0, 0, 0, 13, 0, 0, 0, 17, 0, 0, 0, 217, 0, 0, 0, 86, 0, 0, 0, 0, 0, 0, 0, 17, 0, 0, 0, 217, 0, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 235, 0, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 254, 0, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 17, 1, 0, 0, 86, 0, 0, 0, 18, 0, 0, 0, 17, 0, 0, 0, 35, 1, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 53, 1, 0, 0, 86, 0, 0, 0, 18, 0, 0, 0, 17, 0, 0, 0, 71, 1, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 89, 1, 0, 0, 86, 0, 0, 0, 18, 0, 0, 0, 17, 0, 0, 0, 107, 1, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 125, 1, 0, 0, 86, 0, 0, 0, 19, 0, 0, 0, 17, 0, 0, 0, 144, 1, 0, 0, 86, 0, 0, 0, 18, 0, 0, 0, 17, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 135, 0, 0, 0, 9, 0, 0, 0, 14, 0, 0, 0, 98, 0, 0, 0, 135, 0, 0, 0, 8, 0, 0, 0, 14, 0, 0, 0, 105, 0, 0, 0, 135, 0, 0, 0, 12, 0, 0, 0, 14, 0, 0, 0, 117, 0, 0, 0, 135, 0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 117, 0, 0, 0, 135, 0, 0, 0, 15, 0, 0, 0, 14, 0, 0, 0, 131, 0, 0, 0, 135, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 145, 0, 0, 0, 135, 0, 0, 0, 15, 0, 0, 0, 14, 0, 0, 0, 159, 0, 0, 0, 135, 0, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 172, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 231, 0, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 243, 0, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 255, 0, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 11, 1, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 23, 1, 0, 0, 172, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 35, 1, 0, 0, 172, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 41, 1, 0, 0, 172, 0, 0, 0, 9, 0, 0, 0, 12, 0, 0, 0, 50, 1, 0, 0, 172, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 50, 1, 0, 0, 172, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 62, 1, 0, 0, 172, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 195, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 195, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 195, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 195, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 195, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 231, 0, 0, 0, 195, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 243, 0, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 255, 0, 0, 0, 195, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 5, 1, 0, 0, 195, 0, 0, 0, 10, 0, 0, 0, 12, 0, 0, 0, 14, 1, 0, 0, 195, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 14, 1, 0, 0, 195, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 26, 1, 0, 0, 195, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 219, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 231, 0, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 243, 0, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 255, 0, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 11, 1, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 23, 1, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 35, 1, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 47, 1, 0, 0, 219, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 59, 1, 0, 0, 219, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 65, 1, 0, 0, 219, 0, 0, 0, 10, 0, 0, 0, 12, 0, 0, 0, 74, 1, 0, 0, 219, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 74, 1, 0, 0, 219, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 86, 1, 0, 0, 219, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 242, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 242, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 242, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 242, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 242, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 231, 0, 0, 0, 242, 0, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 243, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 255, 0, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 11, 1, 0, 0, 242, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 17, 1, 0, 0, 242, 0, 0, 0, 9, 0, 0, 0, 12, 0, 0, 0, 26, 1, 0, 0, 242, 0, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 26, 1, 0, 0, 242, 0, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 38, 1, 0, 0, 242, 0, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 10, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 10, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 10, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 10, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 10, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 231, 0, 0, 0, 10, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 243, 0, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 255, 0, 0, 0, 10, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 5, 1, 0, 0, 10, 1, 0, 0, 10, 0, 0, 0, 12, 0, 0, 0, 14, 1, 0, 0, 10, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 14, 1, 0, 0, 10, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 26, 1, 0, 0, 10, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 67, 1, 0, 0, 9, 0, 0, 0, 14, 0, 0, 0, 98, 0, 0, 0, 67, 1, 0, 0, 8, 0, 0, 0, 14, 0, 0, 0, 105, 0, 0, 0, 67, 1, 0, 0, 12, 0, 0, 0, 14, 0, 0, 0, 117, 0, 0, 0, 67, 1, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 117, 0, 0, 0, 67, 1, 0, 0, 15, 0, 0, 0, 14, 0, 0, 0, 131, 0, 0, 0, 67, 1, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 144, 0, 0, 0, 67, 1, 0, 0, 15, 0, 0, 0, 14, 0, 0, 0, 159, 0, 0, 0, 67, 1, 0, 0, 14, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 231, 0, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 243, 0, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 255, 0, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 11, 1, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 11, 1, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 23, 1, 0, 0, 103, 1, 0, 0, 15, 0, 0, 0, 12, 0, 0, 0, 38, 1, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 38, 1, 0, 0, 103, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 44, 1, 0, 0, 103, 1, 0, 0, 9, 0, 0, 0, 12, 0, 0, 0, 53, 1, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 53, 1, 0, 0, 103, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 65, 1, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 77, 1, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 77, 1, 0, 0, 103, 1, 0, 0, 16, 0, 0, 0, 12, 0, 0, 0, 92, 1, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 92, 1, 0, 0, 103, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 98, 1, 0, 0, 103, 1, 0, 0, 9, 0, 0, 0, 12, 0, 0, 0, 107, 1, 0, 0, 103, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 107, 1, 0, 0, 103, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 119, 1, 0, 0, 103, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 127, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 127, 0, 0, 0, 127, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 127, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 127, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 151, 0, 0, 0, 127, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 163, 0, 0, 0, 127, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 175, 0, 0, 0, 127, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 187, 0, 0, 0, 127, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 199, 0, 0, 0, 127, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 211, 0, 0, 0, 127, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 223, 0, 0, 0, 127, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 223, 0, 0, 0, 127, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 235, 0, 0, 0, 127, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 247, 0, 0, 0, 127, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 3, 1, 0, 0, 127, 1, 0, 0, 11, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 150, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 127, 0, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 150, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 151, 0, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 163, 0, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 175, 0, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 187, 0, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 199, 0, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 211, 0, 0, 0, 150, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 211, 0, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 223, 0, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 235, 0, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 247, 0, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 3, 1, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 15, 1, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 28, 1, 0, 0, 150, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 40, 1, 0, 0, 150, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 52, 1, 0, 0, 150, 1, 0, 0, 11, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 174, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 127, 0, 0, 0, 174, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 174, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 174, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 151, 0, 0, 0, 174, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 163, 0, 0, 0, 174, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 175, 0, 0, 0, 174, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 187, 0, 0, 0, 174, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 197, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 197, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 197, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 197, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 197, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 197, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 197, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 197, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 195, 0, 0, 0, 197, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 207, 0, 0, 0, 197, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 219, 0, 0, 0, 197, 1, 0, 0, 15, 0, 0, 0, 12, 0, 0, 0, 234, 0, 0, 0, 197, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 234, 0, 0, 0, 197, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 240, 0, 0, 0, 197, 1, 0, 0, 9, 0, 0, 0, 12, 0, 0, 0, 249, 0, 0, 0, 197, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 249, 0, 0, 0, 197, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 5, 1, 0, 0, 197, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 220, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 127, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 220, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 151, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 163, 0, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 176, 0, 0, 0, 220, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 176, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 188, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 200, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 212, 0, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 225, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 237, 0, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 249, 0, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 5, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 18, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 30, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 42, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 54, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 66, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 78, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 91, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 103, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 115, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 127, 1, 0, 0, 220, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 127, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 139, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 151, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 164, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 176, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 188, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 200, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 213, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 225, 1, 0, 0, 220, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 237, 1, 0, 0, 220, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 133, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 145, 0, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 157, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 169, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 181, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 193, 0, 0, 0, 244, 1, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 193, 0, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 205, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 217, 0, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 229, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 241, 0, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 253, 0, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 9, 1, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 21, 1, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 33, 1, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 46, 1, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 58, 1, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 70, 1, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 82, 1, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 94, 1, 0, 0, 244, 1, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 106, 1, 0, 0, 244, 1, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 118, 1, 0, 0, 244, 1, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 11, 2, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 127, 0, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 11, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 151, 0, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 163, 0, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 175, 0, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 187, 0, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 199, 0, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 211, 0, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 223, 0, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 235, 0, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 247, 0, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 3, 1, 0, 0, 11, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 3, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 15, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 28, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 40, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 52, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 64, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 76, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 88, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 100, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 112, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 124, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 136, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 148, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 160, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 172, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 184, 1, 0, 0, 11, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 196, 1, 0, 0, 11, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 208, 1, 0, 0, 11, 2, 0, 0, 5, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 111, 0, 0, 0, 35, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 123, 0, 0, 0, 35, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 35, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 135, 0, 0, 0, 35, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 147, 0, 0, 0, 35, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 159, 0, 0, 0, 35, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 171, 0, 0, 0, 35, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 183, 0, 0, 0, 35, 2, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 189, 0, 0, 0, 35, 2, 0, 0, 10, 0, 0, 0, 12, 0, 0, 0, 198, 0, 0, 0, 35, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 198, 0, 0, 0, 35, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 210, 0, 0, 0, 35, 2, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 58, 2, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 127, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 58, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 139, 0, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 151, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 163, 0, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 176, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 188, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 200, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 212, 0, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 225, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 237, 0, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 249, 0, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 5, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 18, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 30, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 42, 1, 0, 0, 58, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 42, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 54, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 66, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 78, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 90, 1, 0, 0, 58, 2, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 96, 1, 0, 0, 58, 2, 0, 0, 6, 0, 0, 0, 12, 0, 0, 0, 102, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 115, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 127, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 139, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 151, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 164, 1, 0, 0, 58, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 164, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 176, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 188, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 200, 1, 0, 0, 58, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 200, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 213, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 225, 1, 0, 0, 58, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 237, 1, 0, 0, 58, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 121, 0, 0, 0, 81, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 133, 0, 0, 0, 81, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 145, 0, 0, 0, 81, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 157, 0, 0, 0, 81, 2, 0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 157, 0, 0, 0, 81, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 169, 0, 0, 0, 81, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 181, 0, 0, 0, 81, 2, 0, 0, 12, 0, 0, 0, 12, 0, 0, 0, 193, 0, 0, 0, 81, 2, 0, 0, 13, 0, 0, 0, 12, 0, 0, 0, 205, 0, 0, 0, 81, 2, 0, 0, 5, 0, 0, 0, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
var _I2_rect = {};
var _I2_rect_ori = {};
var _I2_num = 0;
for (var _W4 = 0; _W4 < HEAPU8.length; _W4++) {
    _I2_rect_ori[_I2_num] = HEAPU8[_I2_rects + _W4] + "," + HEAPU8[_I2_rects + _W4 + 1] + "," + HEAPU8[_I2_rects + _W4 + 2] + "," + HEAPU8[_I2_rects + 3];
    var _AF = "00000000" + HEAPU8[_I2_rects + _W4 + 3].toString(2);
    var _Os = "00000000" + HEAPU8[_I2_rects + _W4 + 2].toString(2);
    var _pB = "00000000" + HEAPU8[_I2_rects + _W4 + 1].toString(2);
    var _Wf = "00000000" + HEAPU8[_I2_rects + _W4].toString(2);
    _AF = _AF.substring(_AF.length - 8);
    _Os = _Os.substring(_Os.length - 8);
    _pB = _pB.substring(_pB.length - 8);
    _Wf = _Wf.substring(_Wf.length - 8);
    var _j4 = _AF + _Os + _pB + _Wf;
    _W4++;
    _W4++;
    _W4++;
    _I2_rect[_I2_num] = parseInt(_j4, 2);
    _I2_num++
}
// console.log(_I2_rect_ori)


var _I2_rect_str = "";
var _I2_rect_ori_str = "";
for (var _W4 = 0; _W4 < _I2_num; _W4++) {
    _I2_rect_str = _I2_rect_str + _I2_rect[_W4] + "," + _I2_rect[_W4 + 1] + "," + _I2_rect[_W4 + 2] + "," + _I2_rect[_W4 + 3] + ";";
    _I2_rect_ori_str = _I2_rect_ori_str + _I2_rect_ori[_W4] + ";";
    _W4++;
    _W4++;
    _W4++
}
// console.log(_I2_rect_str)
// console.log(_I2_rect_ori_str)


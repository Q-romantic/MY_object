// 例子
// function t(a, b, c) {
//
//     return a + b + c
// }


const CryptoJS = require("crypto-js");

////////////////////////////////////////////////////////////////////////////////// 生成指定位数且指定字符集随机数
function a(a) {
    var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
    for (d = 0; a > d; d += 1)
        e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
    return c // 生成指定位数且指定字符集随机数
}

function b() {
    for (var t = [], e = 0; e < 36; e++)
        t[e] = "0123456789abcdef".substr(Math.floor(16 * Math.random()), 1);
    return t[14] = "4",
        t[19] = "0123456789abcdef".substr(3 & t[19] | 8, 1),
        t[8] = t[13] = t[18] = t[23] = "",
        t.join("")
}


////////////////////////////////////////////////////////////////////////////////// AES-CFB 加/解密
aes_Encrypt_CFB = function (data, key, iv) {
    data = CryptoJS.enc.Utf8.parse(JSON.stringify(data))
    key = CryptoJS.enc.Utf8.parse(key)
    iv = CryptoJS.enc.Utf8.parse(iv)
    var ciphertext = CryptoJS.AES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CFB,
        padding: CryptoJS.pad.NoPadding
    });
    console.log(ciphertext.toString(), ciphertext.ciphertext.toString());
    // return ciphertext.ciphertext.toString() // 输出hex格式
    return ciphertext.toString()              // 输出base64格式
}

aes_Decrypt_CFB = function (ciphertext, key, iv) {
    key = CryptoJS.enc.Utf8.parse(key)
    iv = CryptoJS.enc.Utf8.parse(iv)
    var bytes = CryptoJS.AES.decrypt(ciphertext, key, {
        iv: iv,
        mode: CryptoJS.mode.CFB,
        padding: CryptoJS.pad.NoPadding
    });
    var originalText = bytes.toString(CryptoJS.enc.Utf8);
    return originalText
}

////////////////////////////////////////////////////////////////////////////////// AES-CBC 加/解密
aes_Encrypt_CBC = function (data, key, iv) {
    key = CryptoJS.enc.Utf8.parse(key)
    ciphertext = CryptoJS.AES.encrypt(data, key, {
        iv: CryptoJS.enc.Utf8.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    })
    // return ciphertext.ciphertext.toString() // 输出hex格式
    return ciphertext.toString()              // 输出base64格式
}

// str_base64 = Buffer.from(str_hex, 'hex').toString('base64')  // hex/base64 互转换
// str_utf8 = Buffer.from(str_hex, 'hex').toString('utf8')  // hex/utf8 互转换
// str_hex = Buffer.from(str_base64, 'utf8').toString('hex')
// str_hex = Buffer.from(str_base64, 'base64').toString('hex')

aes_Decrypt_CBC = function (ciphertext, key, iv) {
    key = CryptoJS.enc.Utf8.parse(key)
    originalText = CryptoJS.AES.decrypt(ciphertext, key, {
        iv: CryptoJS.enc.Utf8.parse(iv),
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.ZeroPadding
    })
    return originalText.toString(CryptoJS.enc.Utf8)
}

////////////////////////////////////////////////////////////////////////////////// AES-ECB 加/解密
aes_Encrypt_ECB = function (data, key) {
    key = CryptoJS.enc.Utf8.parse(key)
    ciphertext = CryptoJS.AES.encrypt(data, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    ciphertext = ciphertext.toString()
    ciphertext = ciphertext.replace(/\//g, "_")
    return encryptedData.replace(/\+/g, "-"), ciphertext
}

aes_Decrypt_ECB = function (ciphertext, key) {
    ciphertext = ciphertext.replace(/\-/g, "+").replace(/_/g, "/")
    key = CryptoJS.enc.Utf8.parse(key)
    originalText = CryptoJS.AES.decrypt(ciphertext, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    originalText = originalText.toString(CryptoJS.enc.Utf8)
    return originalText
}
////////////////////////////////////////////////////////////////////////////////// 生成UUID
uuid = function () {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
        var r = Math.random() * 16 | 0;
        var v = c === 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
};
callback = "geetest_" + (parseInt(Math.random() * 10000) + (new Date()).valueOf());
console.log(uuid(), callback) // challenge参数

////////////////////////////////////////////////////////////////////////////////// 校验身份证号是否合规（18位、15位）
checkPsidno = function (value) {
    /**
     * @description : 校验身份证号是否合规（18位、15位）
     * @param        {String|Number} value
     * @return       {Boolean} true-合规 false-不合规
     */
    const psidno = String(value)
    // 1.校验身份证号格式和长度
    const regPsidno = /^(^[1-9]\d{7}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])\d{3}$)|(^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[X])$)$/
    if (!regPsidno.test(psidno)) {
        return false
    }
    // 2.校验前两位的省份编码是否正确
    const province = {
        11: '北京',
        12: '天津',
        13: '河北',
        14: '山西',
        15: '内蒙古',
        21: '辽宁',
        22: '吉林',
        23: '黑龙江 ',
        31: '上海',
        32: '江苏',
        33: '浙江',
        34: '安徽',
        35: '福建',
        36: '江西',
        37: '山东',
        41: '河南',
        42: '湖北 ',
        43: '湖南',
        44: '广东',
        45: '广西',
        46: '海南',
        50: '重庆',
        51: '四川',
        52: '贵州',
        53: '云南',
        54: '西藏 ',
        61: '陕西',
        62: '甘肃',
        63: '青海',
        64: '宁夏',
        65: '新疆',
        71: '台湾',
        81: '香港',
        82: '澳门',
        91: '国外'
    }
    if (!province[Number(psidno.slice(0, 2))]) {
        return false
    }
    // 3.校验出生日期
    if (psidno.length === 15) {
        // 15位号码 省（2位）市（2位）县（2位）年（2位）月（2位）日（2位）校验码（3位）
        const reg = new RegExp(/^(\d{6})(\d{2})(\d{2})(\d{2})(\d{3})$/)
        const arrSplit = psidno.match(reg)
        // 15位号码在年份前补 19 或 20
        const year = Number(arrSplit[2].charAt(0)) > 0 ? '19' + arrSplit[2] : '20' + arrSplit[2]
        const month = arrSplit[3]
        const day = arrSplit[4]
        if (!validateBirthday(year, month, day)) {
            return false
        }
    } else if (psidno.length === 18) {
        // 18位号码 省（2位）市（2位）县（2位）年（4位）月（2位）日（2位）校验码（4位）
        const reg = new RegExp(/^(\d{6})(\d{4})(\d{2})(\d{2})(\d{3})([0-9]|X)$/)
        const arrSplit = psidno.match(reg)
        const year = arrSplit[2]
        const month = arrSplit[3]
        const day = arrSplit[4]
        if (!validateBirthday(year, month, day)) {
            return false;
        }
    } else {
        return false;
    }

    // 校验出生日期是否合理
    function validateBirthday(year, month, day) {
        year = Number(year) // 年
        month = Number(month) // 月
        day = Number(day) // 日
        const nowTime = new Date().getTime() // 当前时间戳
        const birthTime = new Date(`${year}-${month}-${day}`).getTime() // 获取出生日期的时间戳
        // 不能是明天出生的吧
        if (birthTime > nowTime) {
            return false
        }
        // 一般人活不到150岁吧
        const nowYear = new Date().getFullYear()
        if ((nowYear - year) > 150) {
            return false
        }
        // 不能是13月出生的吧
        if (month < 1 || month > 12) {
            return false
        }
        // 不能是2月30号、4月31号、5月32号出生的吧
        const date = new Date(year, month, 0) // 获取当月的最后一天
        if (day < 1 || day > date.getDate()) {
            return false
        }
        return true
    }

    // 4.18位号码校验生成的校验码
    if (psidno.length === 18) {
        const Wi = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] // 加权因子
        const parity = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2'] // 校验码
        let sum = 0
        for (let i = 0; i < 17; i++) {
            sum += Number(psidno.charAt(i)) * Wi[i]
        }
        if (parity[sum % 11] !== psidno[17]) {
            return false
        }
    }
    return true
}
// console.log(checkPsidno('511527199507234738'))

////////////////////////////////////////////////////////////////////////////////// 人民币大写在线转换
function convertCurrency(currencyDigits) {
// Constants:
    var MAXIMUM_NUMBER = 99999999999.99;
    // Predefine the radix characters and currency symbols for output:
    var CN_ZERO = "零";
    var CN_ONE = "壹";
    var CN_TWO = "贰";
    var CN_THREE = "叁";
    var CN_FOUR = "肆";
    var CN_FIVE = "伍";
    var CN_SIX = "陆";
    var CN_SEVEN = "柒";
    var CN_EIGHT = "捌";
    var CN_NINE = "玖";
    var CN_TEN = "拾";
    var CN_HUNDRED = "佰";
    var CN_THOUSAND = "仟";
    var CN_TEN_THOUSAND = "万";
    var CN_HUNDRED_MILLION = "亿";
    var CN_SYMBOL = "";
    var CN_DOLLAR = "元";
    var CN_TEN_CENT = "角";
    var CN_CENT = "分";
    var CN_INTEGER = "整";

// Variables:
    var integral;    // Represent integral part of digit number.
    var decimal;    // Represent decimal part of digit number.
    var outputCharacters;    // The output result.
    var parts;
    var digits, radices, bigRadices, decimals;
    var zeroCount;
    var i, p, d, ds;
    var quotient, modulus;

// Validate input string:
    currencyDigits = currencyDigits.toString();
    if (currencyDigits == "") {
        alert("不能为空 请输入数字金额!如：123.23");
        return "";
    }
    if (currencyDigits.match(/[^,.\d]/) != null) {
        alert("输入字符串中的字符无效!");
        return "";
    }
    if ((currencyDigits).match(/^((\d{1,3}(,\d{3})*(.((\d{3},)*\d{1,3}))?)|(\d+(.\d+)?))$/) == null) {
        alert("请输入正确的数字金额!");
        return "";
    }

// Normalize the format of input digits:
    currencyDigits = currencyDigits.replace(/,/g, "");    // Remove comma delimiters.
    currencyDigits = currencyDigits.replace(/^0+/, "");    // Trim zeros at the beginning.
    // Assert the number is not greater than the maximum number.
    if (Number(currencyDigits) > MAXIMUM_NUMBER) {
        alert("Too large a number to convert!");
        return "";
    }

// Process the coversion from currency digits to characters:
    // Separate integral and decimal parts before processing coversion:
    parts = currencyDigits.split(".");
    if (parts.length > 1) {
        integral = parts[0];
        decimal = parts[1];
        // Cut down redundant decimal digits that are after the second.
        decimal = decimal.substr(0, 2);
    } else {
        integral = parts[0];
        decimal = "";
    }
    // Prepare the characters corresponding to the digits:
    digits = new Array(CN_ZERO, CN_ONE, CN_TWO, CN_THREE, CN_FOUR, CN_FIVE, CN_SIX, CN_SEVEN, CN_EIGHT, CN_NINE);
    radices = new Array("", CN_TEN, CN_HUNDRED, CN_THOUSAND);
    bigRadices = new Array("", CN_TEN_THOUSAND, CN_HUNDRED_MILLION);
    decimals = new Array(CN_TEN_CENT, CN_CENT);
    // Start processing:
    outputCharacters = "";
    // Process integral part if it is larger than 0:
    if (Number(integral) > 0) {
        zeroCount = 0;
        for (i = 0; i < integral.length; i++) {
            p = integral.length - i - 1;
            d = integral.substr(i, 1);
            quotient = p / 4;
            modulus = p % 4;
            if (d == "0") {
                zeroCount++;
            } else {
                if (zeroCount > 0) {
                    outputCharacters += digits[0];
                }
                zeroCount = 0;
                outputCharacters += digits[Number(d)] + radices[modulus];
            }
            if (modulus == 0 && zeroCount < 4) {
                outputCharacters += bigRadices[quotient];
            }
        }
        outputCharacters += CN_DOLLAR;
    }
    // Process decimal part if there is:
    if (decimal != "") {
        for (i = 0; i < decimal.length; i++) {
            d = decimal.substr(i, 1);
            ds = decimal.substr(-1, 1);
            if (d == 0) {
                if (ds == 0) {
                    outputCharacters += "";
                } else {
                    outputCharacters += digits[Number(d)];
                }
            } else {

                outputCharacters += digits[Number(d)] + decimals[i];

            }
        }
    }
    // Confirm and return the final output string:
    if (outputCharacters == "") {
        outputCharacters = CN_ZERO + CN_DOLLAR;
    }
    if (decimal == "") {
        outputCharacters += CN_INTEGER;
    }
    outputCharacters = CN_SYMBOL + outputCharacters;
    return outputCharacters;
}

// num = '1010.01'
// result = convertCurrency(num)
// console.log(num, result)
//////////////////////////////////////////////////////////////////////////////////














// const AES = require("crypto-js/aes");
const SHA256 = require("crypto-js/sha256");

z = function (e, t) {
    return e.localeCompare(t)
};
d = {
    "addQueryPrefix": false,
    "allowDots": false,
    "charset": "utf-8",
    "charsetSentinel": false,
    "delimiter": "&",
    "encode": true,
    "encodeValuesOnly": false,
    "format": "RFC3986",
    "indices": false,
    "skipNulls": false,
    "strictNullHandling": false
}
o = {
    RFC1738: "RFC1738",
    RFC3986: "RFC3986"
};
i = {
    default: o.RFC3986,
    formatters: {
        RFC1738: function (e) {
            return r.call(e, i, "+")
        },
        RFC3986: function (e) {
            return String(e)
        }
    }
}
pp = i.formatters.RFC3986
f = function e(t, n, i, a, o, u, l, A, f, h, p, m, g) {
    var b, v = t;
    if ("function" == typeof l ? v = l(n, v) : v instanceof Date ? v = h(v) : "comma" === i && s(v) && (v = r.maybeMap(v, (function (e) {
            return e instanceof Date ? h(e) : e
        }
    )).join(",")),
    null === v) {
        if (a)
            return u && !m ? u(n, d.encoder, g, "key") : n;
        v = ""
    }
    if ("string" == typeof (b = v) || "number" == typeof b || "boolean" == typeof b || "symbol" == typeof b || "bigint" == typeof b || r.isBuffer(v))
        return u ? [pp(m ? n : u(n, d.encoder, g, "key")) + "=" + pp(u(v, d.encoder, g, "value"))] : [pp(n) + "=" + pp(String(v))];
    // 此处改写，可能函数名字有冲突
    // return u ? [String(m ? n : u(n, d.encoder, g, "key")) + "=" + String(u(v, d.encoder, g, "value"))] : [String(n) + "=" + String(String(v))];
    var y, w = [];
    if (void 0 === v)
        return w;
    if (s(l))
        y = l;
    else {
        var B = Object.keys(v);
        y = A ? B.sort(A) : B
    }
    for (var O = 0; O < y.length; ++O) {
        var C = y[O]
            , E = v[C];
        if (!o || null !== E) {
            var _ = s(v) ? "function" == typeof i ? i(n, C) : n : n + (f ? "." + C : "[" + C + "]");
            c(w, e(E, _, i, a, o, u, l, A, f, h, p, m, g))
        }
    }
    return w
};
s = Array.isArray
    , u = Array.prototype.push
    , c = function (e, t) {
    u.apply(e, s(t) ? t : [t])
}

D_a_stringify = function (e, t) {
    var n, r = e, u = function (e) {
        if (!e)
            return d;
        if (null !== e.encoder && void 0 !== e.encoder && "function" != typeof e.encoder)
            throw new TypeError("Encoder has to be a function.");
        var t = e.charset || d.charset;
        if (void 0 !== e.charset && "utf-8" !== e.charset && "iso-8859-1" !== e.charset)
            throw new TypeError("The charset option must be either utf-8, iso-8859-1, or undefined");
        var n = i.default;
        if (void 0 !== e.format) {
            if (!a.call(i.formatters, e.format))
                throw new TypeError("Unknown format option provided.");
            n = e.format
        }
        var r = i.formatters[n]
            , o = d.filter;
        return ("function" == typeof e.filter || s(e.filter)) && (o = e.filter),
            {
                addQueryPrefix: "boolean" == typeof e.addQueryPrefix ? e.addQueryPrefix : d.addQueryPrefix,
                allowDots: void 0 === e.allowDots ? d.allowDots : !!e.allowDots,
                charset: t,
                charsetSentinel: "boolean" == typeof e.charsetSentinel ? e.charsetSentinel : d.charsetSentinel,
                delimiter: void 0 === e.delimiter ? d.delimiter : e.delimiter,
                encode: "boolean" == typeof e.encode ? e.encode : d.encode,
                encoder: "function" == typeof e.encoder ? e.encoder : d.encoder,
                encodeValuesOnly: "boolean" == typeof e.encodeValuesOnly ? e.encodeValuesOnly : d.encodeValuesOnly,
                filter: o,
                formatter: r,
                serializeDate: "function" == typeof e.serializeDate ? e.serializeDate : d.serializeDate,
                skipNulls: "boolean" == typeof e.skipNulls ? e.skipNulls : d.skipNulls,
                sort: "function" == typeof e.sort ? e.sort : null,
                strictNullHandling: "boolean" == typeof e.strictNullHandling ? e.strictNullHandling : d.strictNullHandling
            }
    }(t);
    "function" == typeof u.filter ? r = (0,
        u.filter)("", r) : s(u.filter) && (n = u.filter);
    var l, A = [];
    if ("object" != typeof r || null === r)
        return "";
    l = t && t.arrayFormat in o ? t.arrayFormat : t && "indices" in t ? t.indices ? "indices" : "repeat" : "indices";
    var h = o[l];
    n || (n = Object.keys(r)),
    u.sort && n.sort(u.sort);
    for (var p = 0; p < n.length; ++p) {
        var m = n[p];
        u.skipNulls && null === r[m] || c(A, f(r[m], m, h, u.strictNullHandling, u.skipNulls, u.encode ? u.encoder : null, u.filter, u.sort, u.allowDots, u.serializeDate, u.formatter, u.encodeValuesOnly, u.charset))
    }
    var g = A.join(u.delimiter)
        , b = !0 === u.addQueryPrefix ? "?" : "";
    return u.charsetSentinel && ("iso-8859-1" === u.charset ? b += "utf8=%26%2310003%3B&" : b += "utf8=%E2%9C%93&"),
        g.length > 0 ? b + g : ""
}
// 加密结构为如下
// N()("xxx").toString()
N = function () {
    f = function (s) {
        return SHA256(s)
    }
    return f
}

// o = {
//     "adultCount": 1,
//     "arrival": "HAN",
//     "childCount": 0,
//     "currency": "USD",
//     "daysAfterDeparture": 0,
//     "daysBeforeDeparture": 0,
//     "departureDate": "2023-03-31",
//     "departurePlace": "SGN",
//     "infantCount": 0,
//     "oneway": 1,
//     "requestId": params['requestId'],
//     "sessionId": null,
//     "user-agent-ls-data": params["user-agent-ls-data"],
//     "x-power-web-s-d": params["x-power-web-s-d"],
// }

get_full_o = function (o) {
    xxx = D_a_stringify(o, {
        arrayFormat: "repeat",
        sort: z
    })
    // console.log(xxx)
    _signature = N()(xxx).toString()
    o["_signature"] = _signature
    return o
}
// console.log(get_full_o(o))
// dancheng = o
// data = JSON.stringify(dancheng)
// console.log(data)


// o ---正常加密后---> 900463b1dc2f3010a3a50f4e436fa53629539c249feaa06a42e06c8264698aa5
// o ---异常加密后---> 0d034db3529968c42da1b5b65bf5ed836e64fbc39a39c62e733dea97faf8e8c3
// // 不能使用如下方法结构，可能是有变量干扰，很奇怪 ？？？
// _signature = N()(D_a_stringify(o, {
//     arrayFormat: "repeat",
//     sort: z
// })).toString()
// o["_signature"] = _signature
// console.log(o)


// wangfan = {
//     "currency": "USD",  // 货币
//     "departureDate": "2023-03-24", // 离开时间
//     "daysBeforeDeparture": 0,
//     "daysAfterDeparture": 0,
//     "departurePlace": "SGN", // 出发地
//     "arrival": "BMV",   // 到达
//     "oneway": 0,    // 往返为0 单向为1
//     "adultCount": 1,
//     "childCount": 0,
//     "infantCount": 0,
//     "returnDate": "2023-04-21", // 返回时间
//     "daysBeforeReturn": 0,
//     "daysAfterReturn": 0,
//     "requestId": params['requestId'],
//     "sessionId": null,
//     "user-agent-ls-data": params["user-agent-ls-data"],
//     "x-power-web-s-d": params["x-power-web-s-d"],
//     // "_signature": "3170bbea8487a0e34d9bbc7e80a680f983d303ec56e85b0a3d4bd5d713874ca6"
// }


// const publicKey = "-----BEGIN PUBLIC KEY-----\nMIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAok58IrYXjeFjb6hPgrcv\nKis43ARDVIqowS2AJKivDp4+8uKDCWnjzBZTsuVvwKPzvVCxBzON2/DPpHU3wnRt\ndKSVzWju7HMKhuLxe04FsVw8+xvZTmguBj4jTczNLSLjK13lQr46J8j7JrmVUlPq\nGxIL/Bd3HNAIFuarZQkDsgx5fvdNrMbmT4edr1b3A8wRkhfo9tuE5Tmlx0YVUwyb\nzcI6hgLggCfNwwaClXyBt08NbGSIBcKYKjiQErND0EOnWcGyto7EhkpgGRfAeESo\n3hbmsiabThLd4t9iOWVHFSl+7B0q+1IGFjSo9qkvNdMUI4ZYdIKq+nCHufpuFMl7\nSwIDAQAB\n-----END PUBLIC KEY-----"
// sss = '{"currency":"USD","departureDate":"2023-03-31","daysBeforeDeparture":0,"daysAfterDeparture":0,"departurePlace":"SGN","arrival":"HAN","oneway":1,"adultCount":1,"childCount":0,"infantCount":0,"requestId":"TM34DMA5VPJB-1679732805861","sessionId":null,"x-power-web-s-d":"1191511111-1116518261-4cac-9b83-7b84d34abc20","user-agent-ls-data":"c94e2320-8ded-4c8d-b89a-c4678151e330-1679709436117","_signature":"94a519cbf17fce92f16822ac10669803e1af5d5245108fcd6deb892b3e86f87c"}'
//
// // 公钥加密
// function rsaEncrypt(message) {
//     const buffer = Buffer.from(message, 'utf8');
//     const encrypted = crypto.publicEncrypt({key: publicKey, padding: crypto.constants.RSA_PKCS1_PADDING}, buffer);
//     return encrypted.toString('hex');
// }
//
// function rsaEncryptToLong(message) {
//     // const padding = 117;
//     const padding = 245;
//     const count = message.length;
//     const num = Math.floor(count / padding);
//     const remainder = count % padding;
//     let str = '';
//     for (let i = 0; i < num; i++) {
//         const value = message.slice(i * 8, i * padding + padding);
//         str += rsaEncrypt(value);
//         // str += ';';
//     }
//     if (remainder !== 0) {
//         const value = message.slice(-remainder);
//         str += rsaEncrypt(value);
//         // str += ';';
//     }
//     if (str.length > 0) str = str.slice(0, str.length - 1);
//     return Buffer.from(str, 'hex').toString('base64');
// }
//
// // console.log(rsaEncryptToLong(sss));
// // console.log(rsaEncryptToLong(data));



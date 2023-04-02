var e = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
var n = {
    rotl: function (t, e) {
        return t << e | t >>> 32 - e
    },
    rotr: function (t, e) {
        return t << 32 - e | t >>> e
    },
    endian: function (t) {
        if (t.constructor == Number)
            return 16711935 & n.rotl(t, 8) | 4278255360 & n.rotl(t, 24);
        for (var e = 0; e < t.length; e++)
            t[e] = n.endian(t[e]);
        return t
    },
    randomBytes: function (t) {
        for (var e = []; t > 0; t--)
            e.push(Math.floor(256 * Math.random()));
        return e
    },
    bytesToWords: function (t) {
        for (var e = [], n = 0, r = 0; n < t.length; n++,
            r += 8)
            e[r >>> 5] |= t[n] << 24 - r % 32;
        return e
    },
    wordsToBytes: function (t) {
        for (var e = [], n = 0; n < 32 * t.length; n += 8)
            e.push(t[n >>> 5] >>> 24 - n % 32 & 255);
        return e
    },
    bytesToHex: function (t) {
        for (var e = [], n = 0; n < t.length; n++)
            e.push((t[n] >>> 4).toString(16)),
                e.push((15 & t[n]).toString(16));
        return e.join("")
    },
    hexToBytes: function (t) {
        for (var e = [], n = 0; n < t.length; n += 2)
            e.push(parseInt(t.substr(n, 2), 16));
        return e
    },
    bytesToBase64: function (t) {
        for (var n = [], r = 0; r < t.length; r += 3)
            for (var i = t[r] << 16 | t[r + 1] << 8 | t[r + 2], o = 0; o < 4; o++)
                8 * r + 6 * o <= 8 * t.length ? n.push(e.charAt(i >>> 6 * (3 - o) & 63)) : n.push("=");
        return n.join("")
    },
    base64ToBytes: function (t) {
        t = t.replace(/[^A-Z0-9+\/]/gi, "");
        for (var n = [], r = 0, i = 0; r < t.length; i = ++r % 4)
            0 != i && n.push((e.indexOf(t.charAt(r - 1)) & Math.pow(2, -2 * i + 8) - 1) << 2 * i | e.indexOf(t.charAt(r)) >>> 6 - 2 * i);
        return n
    }
};

e = n

var rr = {
    utf8: {
        stringToBytes: function (t) {
            return rr.bin.stringToBytes(unescape(encodeURIComponent(t)))
        },
        bytesToString: function (t) {
            return decodeURIComponent(escape(rr.bin.bytesToString(t)))
        }
    },
    bin: {
        stringToBytes: function (t) {
            for (var e = [], n = 0; n < t.length; n++)
                e.push(255 & t.charCodeAt(n));
            return e
        },
        bytesToString: function (t) {
            for (var e = [], n = 0; n < t.length; n++)
                e.push(String.fromCharCode(t[n]));
            return e.join("")
        }
    }
};


a = function t(n, a) {
    n.constructor == String ? n = a && "binary" === a.encoding ? rr.bin.stringToBytes(n) : rr.utf8.stringToBytes(n) : i(n) ? n = Array.prototype.slice.call(n, 0) : Array.isArray(n) || n.constructor === Uint8Array || (n = n.toString());
    for (var s = e.bytesToWords(n), c = 8 * n.length, u = 1732584193, l = -271733879, f = -1732584194, h = 271733878, p = 0; p < s.length; p++)
        s[p] = 16711935 & (s[p] << 8 | s[p] >>> 24) | 4278255360 & (s[p] << 24 | s[p] >>> 8);
    s[c >>> 5] |= 128 << c % 32,
        s[14 + (c + 64 >>> 9 << 4)] = c;
    var d = t._ff
        , m = t._gg
        , v = t._hh
        , y = t._ii;
    for (p = 0; p < s.length; p += 16) {
        var g = u
            , b = l
            , w = f
            , _ = h;
        u = d(u, l, f, h, s[p + 0], 7, -680876936),
            h = d(h, u, l, f, s[p + 1], 12, -389564586),
            f = d(f, h, u, l, s[p + 2], 17, 606105819),
            l = d(l, f, h, u, s[p + 3], 22, -1044525330),
            u = d(u, l, f, h, s[p + 4], 7, -176418897),
            h = d(h, u, l, f, s[p + 5], 12, 1200080426),
            f = d(f, h, u, l, s[p + 6], 17, -1473231341),
            l = d(l, f, h, u, s[p + 7], 22, -45705983),
            u = d(u, l, f, h, s[p + 8], 7, 1770035416),
            h = d(h, u, l, f, s[p + 9], 12, -1958414417),
            f = d(f, h, u, l, s[p + 10], 17, -42063),
            l = d(l, f, h, u, s[p + 11], 22, -1990404162),
            u = d(u, l, f, h, s[p + 12], 7, 1804603682),
            h = d(h, u, l, f, s[p + 13], 12, -40341101),
            f = d(f, h, u, l, s[p + 14], 17, -1502002290),
            u = m(u, l = d(l, f, h, u, s[p + 15], 22, 1236535329), f, h, s[p + 1], 5, -165796510),
            h = m(h, u, l, f, s[p + 6], 9, -1069501632),
            f = m(f, h, u, l, s[p + 11], 14, 643717713),
            l = m(l, f, h, u, s[p + 0], 20, -373897302),
            u = m(u, l, f, h, s[p + 5], 5, -701558691),
            h = m(h, u, l, f, s[p + 10], 9, 38016083),
            f = m(f, h, u, l, s[p + 15], 14, -660478335),
            l = m(l, f, h, u, s[p + 4], 20, -405537848),
            u = m(u, l, f, h, s[p + 9], 5, 568446438),
            h = m(h, u, l, f, s[p + 14], 9, -1019803690),
            f = m(f, h, u, l, s[p + 3], 14, -187363961),
            l = m(l, f, h, u, s[p + 8], 20, 1163531501),
            u = m(u, l, f, h, s[p + 13], 5, -1444681467),
            h = m(h, u, l, f, s[p + 2], 9, -51403784),
            f = m(f, h, u, l, s[p + 7], 14, 1735328473),
            u = v(u, l = m(l, f, h, u, s[p + 12], 20, -1926607734), f, h, s[p + 5], 4, -378558),
            h = v(h, u, l, f, s[p + 8], 11, -2022574463),
            f = v(f, h, u, l, s[p + 11], 16, 1839030562),
            l = v(l, f, h, u, s[p + 14], 23, -35309556),
            u = v(u, l, f, h, s[p + 1], 4, -1530992060),
            h = v(h, u, l, f, s[p + 4], 11, 1272893353),
            f = v(f, h, u, l, s[p + 7], 16, -155497632),
            l = v(l, f, h, u, s[p + 10], 23, -1094730640),
            u = v(u, l, f, h, s[p + 13], 4, 681279174),
            h = v(h, u, l, f, s[p + 0], 11, -358537222),
            f = v(f, h, u, l, s[p + 3], 16, -722521979),
            l = v(l, f, h, u, s[p + 6], 23, 76029189),
            u = v(u, l, f, h, s[p + 9], 4, -640364487),
            h = v(h, u, l, f, s[p + 12], 11, -421815835),
            f = v(f, h, u, l, s[p + 15], 16, 530742520),
            u = y(u, l = v(l, f, h, u, s[p + 2], 23, -995338651), f, h, s[p + 0], 6, -198630844),
            h = y(h, u, l, f, s[p + 7], 10, 1126891415),
            f = y(f, h, u, l, s[p + 14], 15, -1416354905),
            l = y(l, f, h, u, s[p + 5], 21, -57434055),
            u = y(u, l, f, h, s[p + 12], 6, 1700485571),
            h = y(h, u, l, f, s[p + 3], 10, -1894986606),
            f = y(f, h, u, l, s[p + 10], 15, -1051523),
            l = y(l, f, h, u, s[p + 1], 21, -2054922799),
            u = y(u, l, f, h, s[p + 8], 6, 1873313359),
            h = y(h, u, l, f, s[p + 15], 10, -30611744),
            f = y(f, h, u, l, s[p + 6], 15, -1560198380),
            l = y(l, f, h, u, s[p + 13], 21, 1309151649),
            u = y(u, l, f, h, s[p + 4], 6, -145523070),
            h = y(h, u, l, f, s[p + 11], 10, -1120210379),
            f = y(f, h, u, l, s[p + 2], 15, 718787259),
            l = y(l, f, h, u, s[p + 9], 21, -343485551),
            u = u + g >>> 0,
            l = l + b >>> 0,
            f = f + w >>> 0,
            h = h + _ >>> 0
    }
    return e.endian([u, l, f, h])
}
a._ff = function (t, e, n, r, i, o, a) {
    var s = t + (e & n | ~e & r) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}
a._gg = function (t, e, n, r, i, o, a) {
    var s = t + (e & r | n & ~r) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}
a._hh = function (t, e, n, r, i, o, a) {
    var s = t + (e ^ n ^ r) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}
a._ii = function (t, e, n, r, i, o, a) {
    var s = t + (n ^ (e | ~r)) + (i >>> 0) + a;
    return (s << o | s >>> 32 - o) + e
}
a._blocksize = 16;
a._digestsize = 16;


get_aaid = function (t) {
    var r = e.wordsToBytes(a(t, n));
    var res = n && n.asBytes ? r : n && n.asString ? o.bytesToString(r) : e.bytesToHex(r)
    return res
}
t = '1677131213694H+98HE4ddVwCAT0w0m6bwJ8n'
aaid = get_aaid(t)
console.log(aaid)
t = "1677131213694null"
aaid = get_aaid(t)
console.log(aaid)
//"06f32c142b14a68c5e6f3c443bb54bf7"



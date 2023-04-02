flag = {
    'method': 'GET',
    'channelId': 40011,
    'sVersion': 1,
    'type': 'object'
}
var getMD5Sign = function (x = flag) {
    var c = x['method'],
        e = x['channelId'],
        _ = void 0 === e ? 40011 : e,
        t = x['sVersion'],
        n = x['type'],
        a = void 0 === n ? "qs" : n,
        // i = 3,
        // d = 1657348359279,
        i = Math['ceil'](10 * Math.random()),
        d = (new Date)['getTime'](),
        s = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
        u = 'method=' + c + '&timeStamp=' + d + '&User-Agent=' + s + '&index=' + i + '&channelId=' + _ + '&sVersion=' + t;
    f = '&key=A013F70DB97834C0A5492378BD76C53A';
    return {
        randomNum: i,
        timeStamp: d,
        md5sign: default2(u + f),
        channelId: _,
        sVersion: t,
        params: {webdriver: false}
    }
};
var default2 = function (x) {
    if (void 0 === x || null === x)
        throw new Error(x);
    var _ = wordsToBytes(a(x));
    return bytesToHex(_);
};
var _ff = function (x, c, e, _, t, n, a) {
    var r = x + (c & e | ~c & _) + (t >>> 0) + a;
    return (r << n | r >>> 32 - n) + c
};
var _gg = function (x, c, e, _, t, n, a) {
    var r = x + (c & _ | e & ~_) + (t >>> 0) + a;
    return (r << n | r >>> 32 - n) + c
};
var _hh = function (x, c, e, _, t, n, a) {
    var r = x + (c ^ e ^ _) + (t >>> 0) + a;
    return (r << n | r >>> 32 - n) + c
};
var _ii = function (x, c, e, _, t, n, a) {
    var r = x + (e ^ (c | ~_)) + (t >>> 0) + a;
    return (r << n | r >>> 32 - n) + c
};
var a = function (x) {
    x = stringToBytes(x);
    // x['constructor'] == String ? x = e && e['encoding'] === 'binary' ? stringToBytes(x) : stringToBytes(x) : t(x) ? x = Array.prototype.slice.call(x, 0) : Array['isArray'](x) || x.constructor === Uint8Array || (x = x['toString']());
    for (var r = bytesToWords(x), i = 8 * x['length'], d = 1732584193, s = -271733879, o = -1732584194, u = 271733878, f = 0; f < r['length']; f++)
        r[f] = 16711935 & (r[f] << 8 | r[f] >>> 24) | 4278255360 & (r[f] << 24 | r[f] >>> 8);
    r[i >>> 5] |= 128 << i % 32,
        r[14 + (i + 64 >>> 9 << 4)] = i;
    for (var l = _ff, m = _gg, h = _hh, b = _ii, f = 0; f < r.length; f += 16) {
        var y = d,
            p = s,
            L = o,
            M = u;
        d = l(d, s, o, u, r[f + 0], 7, -680876936),
            u = l(u, d, s, o, r[f + 1], 12, -389564586),
            o = l(o, u, d, s, r[f + 2], 17, 606105819),
            s = l(s, o, u, d, r[f + 3], 22, -1044525330),
            d = l(d, s, o, u, r[f + 4], 7, -176418897),
            u = l(u, d, s, o, r[f + 5], 12, 1200080426),
            o = l(o, u, d, s, r[f + 6], 17, -1473231341),
            s = l(s, o, u, d, r[f + 7], 22, -45705983),
            d = l(d, s, o, u, r[f + 8], 7, 1770035416),
            u = l(u, d, s, o, r[f + 9], 12, -1958414417),
            o = l(o, u, d, s, r[f + 10], 17, -42063),
            s = l(s, o, u, d, r[f + 11], 22, -1990404162),
            d = l(d, s, o, u, r[f + 12], 7, 1804603682),
            u = l(u, d, s, o, r[f + 13], 12, -40341101),
            o = l(o, u, d, s, r[f + 14], 17, -1502002290),
            s = l(s, o, u, d, r[f + 15], 22, 1236535329),
            d = m(d, s, o, u, r[f + 1], 5, -165796510),
            u = m(u, d, s, o, r[f + 6], 9, -1069501632),
            o = m(o, u, d, s, r[f + 11], 14, 643717713),
            s = m(s, o, u, d, r[f + 0], 20, -373897302),
            d = m(d, s, o, u, r[f + 5], 5, -701558691),
            u = m(u, d, s, o, r[f + 10], 9, 38016083),
            o = m(o, u, d, s, r[f + 15], 14, -660478335),
            s = m(s, o, u, d, r[f + 4], 20, -405537848),
            d = m(d, s, o, u, r[f + 9], 5, 568446438),
            u = m(u, d, s, o, r[f + 14], 9, -1019803690),
            o = m(o, u, d, s, r[f + 3], 14, -187363961),
            s = m(s, o, u, d, r[f + 8], 20, 1163531501),
            d = m(d, s, o, u, r[f + 13], 5, -1444681467),
            u = m(u, d, s, o, r[f + 2], 9, -51403784),
            o = m(o, u, d, s, r[f + 7], 14, 1735328473),
            s = m(s, o, u, d, r[f + 12], 20, -1926607734),
            d = h(d, s, o, u, r[f + 5], 4, -378558),
            u = h(u, d, s, o, r[f + 8], 11, -2022574463),
            o = h(o, u, d, s, r[f + 11], 16, 1839030562),
            s = h(s, o, u, d, r[f + 14], 23, -35309556),
            d = h(d, s, o, u, r[f + 1], 4, -1530992060),
            u = h(u, d, s, o, r[f + 4], 11, 1272893353),
            o = h(o, u, d, s, r[f + 7], 16, -155497632),
            s = h(s, o, u, d, r[f + 10], 23, -1094730640),
            d = h(d, s, o, u, r[f + 13], 4, 681279174),
            u = h(u, d, s, o, r[f + 0], 11, -358537222),
            o = h(o, u, d, s, r[f + 3], 16, -722521979),
            s = h(s, o, u, d, r[f + 6], 23, 76029189),
            d = h(d, s, o, u, r[f + 9], 4, -640364487),
            u = h(u, d, s, o, r[f + 12], 11, -421815835),
            o = h(o, u, d, s, r[f + 15], 16, 530742520),
            s = h(s, o, u, d, r[f + 2], 23, -995338651),
            d = b(d, s, o, u, r[f + 0], 6, -198630844),
            u = b(u, d, s, o, r[f + 7], 10, 1126891415),
            o = b(o, u, d, s, r[f + 14], 15, -1416354905),
            s = b(s, o, u, d, r[f + 5], 21, -57434055),
            d = b(d, s, o, u, r[f + 12], 6, 1700485571),
            u = b(u, d, s, o, r[f + 3], 10, -1894986606),
            o = b(o, u, d, s, r[f + 10], 15, -1051523),
            s = b(s, o, u, d, r[f + 1], 21, -2054922799),
            d = b(d, s, o, u, r[f + 8], 6, 1873313359),
            u = b(u, d, s, o, r[f + 15], 10, -30611744),
            o = b(o, u, d, s, r[f + 6], 15, -1560198380),
            s = b(s, o, u, d, r[f + 13], 21, 1309151649),
            d = b(d, s, o, u, r[f + 4], 6, -145523070),
            u = b(u, d, s, o, r[f + 11], 10, -1120210379),
            o = b(o, u, d, s, r[f + 2], 15, 718787259),
            s = b(s, o, u, d, r[f + 9], 21, -343485551),
            d = d + y >>> 0,
            s = s + p >>> 0,
            o = o + L >>> 0,
            u = u + M >>> 0
    }
    return endian([d, s, o, u]);
};
var rotl = function (x, c) {
    return x << c | x >>> 32 - c;
};
var rotr = function (x, c) {
    return x << 32 - c | x >>> c;
};
var endian = function (x) {
    if (x['constructor'] == Number)
        return 16711935 & rotl(x, 8) | 4278255360 & rotl(x, 24);
    for (var c = 0; c < x['length']; c++)
        x[c] = endian(x[c]);
    return x
};
var bytesToWords = function (x) {
    for (var c = [], e = 0, _ = 0; e < x['length']; e++,
        _ += 8)
        c[_ >>> 5] |= x[e] << 24 - _ % 32;
    return c
};
var wordsToBytes = function (x) {
    for (var c = [], e = 0; e < 32 * x['length']; e += 8)
        c['push'](x[e >>> 5] >>> 24 - e % 32 & 255);
    return c
};
var stringToBytes = function (x) {
    for (var c = [], e = 0; e < x.length; e++)
        c['push'](255 & x.charCodeAt(e));
    return c;
};
var bytesToHex = function (x) {
    for (var c = [], e = 0; e < x.length; e++)
        c['push']((x[e] >>> 4)['toString'](16)),
            c['push']((15 & x[e])['toString'](16));
    return c['join']("")
};
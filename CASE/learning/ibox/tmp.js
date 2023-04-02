const CryptoJS = require("crypto-js");
var window = this;


function o(t) {
    return "0123456789abcdefghijklmnopqrstuvwxyz".charAt(t)
}

function s(t, e) {
    return t & e
}

function a(t, e) {
    return t | e
}

function l(t, e) {
    return t ^ e
}

function c(t, e) {
    return t & ~e
}

function u(t) {
    if (0 == t)
        return -1;
    var e = 0;
    return 0 == (65535 & t) && (t >>= 16,
        e += 16),
    0 == (255 & t) && (t >>= 8,
        e += 8),
    0 == (15 & t) && (t >>= 4,
        e += 4),
    0 == (3 & t) && (t >>= 2,
        e += 2),
    0 == (1 & t) && ++e,
        e
}

function h(t) {
    for (var e = 0; 0 != t;)
        t &= t - 1,
            ++e;
    return e
}

var d, f = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";

function p(t) {
    var e, n, i = "";
    for (e = 0; e + 3 <= t.length; e += 3)
        n = parseInt(t.substring(e, e + 3), 16),
            i += f.charAt(n >> 6) + f.charAt(63 & n);
    for (e + 1 == t.length ? (n = parseInt(t.substring(e, e + 1), 16),
        i += f.charAt(n << 2)) : e + 2 == t.length && (n = parseInt(t.substring(e, e + 2), 16),
        i += f.charAt(n >> 2) + f.charAt((3 & n) << 4)); (3 & i.length) > 0;)
        i += "=";
    return i
}

function v(t) {
    var e, n = "", i = 0, r = 0;
    for (e = 0; e < t.length && "=" != t.charAt(e); ++e) {
        var s = f.indexOf(t.charAt(e));
        s < 0 || (0 == i ? (n += o(s >> 2),
            r = 3 & s,
            i = 1) : 1 == i ? (n += o(r << 2 | s >> 4),
            r = 15 & s,
            i = 2) : 2 == i ? (n += o(r),
            n += o(s >> 2),
            r = 3 & s,
            i = 3) : (n += o(r << 2 | s >> 4),
            n += o(15 & s),
            i = 0))
    }
    return 1 == i && (n += o(r << 2)),
        n
}

var m, g = function (t) {
        var e;
        if (void 0 === d) {
            var n = "0123456789ABCDEF"
                , i = " \f\n\r\t \u2028\u2029";
            for (d = {},
                     e = 0; e < 16; ++e)
                d[n.charAt(e)] = e;
            for (n = n.toLowerCase(),
                     e = 10; e < 16; ++e)
                d[n.charAt(e)] = e;
            for (e = 0; e < i.length; ++e)
                d[i.charAt(e)] = -1
        }
        var r = []
            , o = 0
            , s = 0;
        for (e = 0; e < t.length; ++e) {
            var a = t.charAt(e);
            if ("=" == a)
                break;
            if (-1 != (a = d[a])) {
                if (void 0 === a)
                    throw new Error("Illegal character at offset " + e);
                o |= a,
                    ++s >= 2 ? (r[r.length] = o,
                        o = 0,
                        s = 0) : o <<= 4
            }
        }
        if (s)
            throw new Error("Hex encoding incomplete: 4 bits missing");
        return r
    }, b = {
        decode: function (t) {
            var e;
            if (void 0 === m) {
                var n = "= \f\n\r\t \u2028\u2029";
                for (m = Object.create(null),
                         e = 0; e < 64; ++e)
                    m["ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/".charAt(e)] = e;
                for (m["-"] = 62,
                         m._ = 63,
                         e = 0; e < n.length; ++e)
                    m[n.charAt(e)] = -1
            }
            var i = []
                , r = 0
                , o = 0;
            for (e = 0; e < t.length; ++e) {
                var s = t.charAt(e);
                if ("=" == s)
                    break;
                if (-1 != (s = m[s])) {
                    if (void 0 === s)
                        throw new Error("Illegal character at offset " + e);
                    r |= s,
                        ++o >= 4 ? (i[i.length] = r >> 16,
                            i[i.length] = r >> 8 & 255,
                            i[i.length] = 255 & r,
                            r = 0,
                            o = 0) : r <<= 6
                }
            }
            switch (o) {
                case 1:
                    throw new Error("Base64 encoding incomplete: at least 2 bits missing");
                case 2:
                    i[i.length] = r >> 10;
                    break;
                case 3:
                    i[i.length] = r >> 16,
                        i[i.length] = r >> 8 & 255
            }
            return i
        },
        re: /-----BEGIN [^-]+-----([A-Za-z0-9+\/=\s]+)-----END [^-]+-----|begin-base64[^\n]+\n([A-Za-z0-9+\/=\s]+)====/,
        unarmor: function (t) {
            var e = b.re.exec(t);
            if (e)
                if (e[1])
                    t = e[1];
                else {
                    if (!e[2])
                        throw new Error("RegExp out of sync");
                    t = e[2]
                }
            return b.decode(t)
        }
    }, y = 1e13, w = function () {
        function t(t) {
            this.buf = [+t || 0]
        }

        return t.prototype.mulAdd = function (t, e) {
            var n, i, r = this.buf, o = r.length;
            for (n = 0; n < o; ++n)
                (i = r[n] * t + e) < y ? e = 0 : i -= (e = 0 | i / y) * y,
                    r[n] = i;
            e > 0 && (r[n] = e)
        }
            ,
            t.prototype.sub = function (t) {
                var e, n, i = this.buf, r = i.length;
                for (e = 0; e < r; ++e)
                    (n = i[e] - t) < 0 ? (n += y,
                        t = 1) : t = 0,
                        i[e] = n;
                for (; 0 === i[i.length - 1];)
                    i.pop()
            }
            ,
            t.prototype.toString = function (t) {
                if (10 != (t || 10))
                    throw new Error("only base 10 is supported");
                for (var e = this.buf, n = e[e.length - 1].toString(), i = e.length - 2; i >= 0; --i)
                    n += (y + e[i]).toString().substring(1);
                return n
            }
            ,
            t.prototype.valueOf = function () {
                for (var t = this.buf, e = 0, n = t.length - 1; n >= 0; --n)
                    e = e * y + t[n];
                return e
            }
            ,
            t.prototype.simplify = function () {
                var t = this.buf;
                return 1 == t.length ? t[0] : this
            }
            ,
            t
    }(), x = /^(\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/,
    _ = /^(\d\d\d\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])([01]\d|2[0-3])(?:([0-5]\d)(?:([0-5]\d)(?:[.,](\d{1,3}))?)?)?(Z|[-+](?:[0]\d|1[0-2])([0-5]\d)?)?$/;

function S(t, e) {
    return t.length > e && (t = t.substring(0, e) + "…"),
        t
}

var C, E = function () {
        function t(e, n) {
            this.hexDigits = "0123456789ABCDEF",
                e instanceof t ? (this.enc = e.enc,
                    this.pos = e.pos) : (this.enc = e,
                    this.pos = n)
        }

        return t.prototype.get = function (t) {
            if (void 0 === t && (t = this.pos++),
            t >= this.enc.length)
                throw new Error("Requesting byte offset " + t + " on a stream of length " + this.enc.length);
            return "string" == typeof this.enc ? this.enc.charCodeAt(t) : this.enc[t]
        }
            ,
            t.prototype.hexByte = function (t) {
                return this.hexDigits.charAt(t >> 4 & 15) + this.hexDigits.charAt(15 & t)
            }
            ,
            t.prototype.hexDump = function (t, e, n) {
                for (var i = "", r = t; r < e; ++r)
                    if (i += this.hexByte(this.get(r)),
                    !0 !== n)
                        switch (15 & r) {
                            case 7:
                                i += "  ";
                                break;
                            case 15:
                                i += "\n";
                                break;
                            default:
                                i += " "
                        }
                return i
            }
            ,
            t.prototype.isASCII = function (t, e) {
                for (var n = t; n < e; ++n) {
                    var i = this.get(n);
                    if (i < 32 || i > 176)
                        return !1
                }
                return !0
            }
            ,
            t.prototype.parseStringISO = function (t, e) {
                for (var n = "", i = t; i < e; ++i)
                    n += String.fromCharCode(this.get(i));
                return n
            }
            ,
            t.prototype.parseStringUTF = function (t, e) {
                for (var n = "", i = t; i < e;) {
                    var r = this.get(i++);
                    n += r < 128 ? String.fromCharCode(r) : r > 191 && r < 224 ? String.fromCharCode((31 & r) << 6 | 63 & this.get(i++)) : String.fromCharCode((15 & r) << 12 | (63 & this.get(i++)) << 6 | 63 & this.get(i++))
                }
                return n
            }
            ,
            t.prototype.parseStringBMP = function (t, e) {
                for (var n, i, r = "", o = t; o < e;)
                    n = this.get(o++),
                        i = this.get(o++),
                        r += String.fromCharCode(n << 8 | i);
                return r
            }
            ,
            t.prototype.parseTime = function (t, e, n) {
                var i = this.parseStringISO(t, e)
                    , r = (n ? x : _).exec(i);
                return r ? (n && (r[1] = +r[1],
                    r[1] += +r[1] < 70 ? 2e3 : 1900),
                    i = r[1] + "-" + r[2] + "-" + r[3] + " " + r[4],
                r[5] && (i += ":" + r[5],
                r[6] && (i += ":" + r[6],
                r[7] && (i += "." + r[7]))),
                r[8] && (i += " UTC",
                "Z" != r[8] && (i += r[8],
                r[9] && (i += ":" + r[9]))),
                    i) : "Unrecognized time: " + i
            }
            ,
            t.prototype.parseInteger = function (t, e) {
                for (var n, i = this.get(t), r = i > 127, o = r ? 255 : 0, s = ""; i == o && ++t < e;)
                    i = this.get(t);
                if (0 === (n = e - t))
                    return r ? -1 : 0;
                if (n > 4) {
                    for (s = i,
                             n <<= 3; 0 == (128 & (+s ^ o));)
                        s = +s << 1,
                            --n;
                    s = "(" + n + " bit)\n"
                }
                r && (i -= 256);
                for (var a = new w(i), l = t + 1; l < e; ++l)
                    a.mulAdd(256, this.get(l));
                return s + a.toString()
            }
            ,
            t.prototype.parseBitString = function (t, e, n) {
                for (var i = this.get(t), r = "(" + ((e - t - 1 << 3) - i) + " bit)\n", o = "", s = t + 1; s < e; ++s) {
                    for (var a = this.get(s), l = s == e - 1 ? i : 0, c = 7; c >= l; --c)
                        o += a >> c & 1 ? "1" : "0";
                    if (o.length > n)
                        return r + S(o, n)
                }
                return r + o
            }
            ,
            t.prototype.parseOctetString = function (t, e, n) {
                if (this.isASCII(t, e))
                    return S(this.parseStringISO(t, e), n);
                var i = e - t
                    , r = "(" + i + " byte)\n";
                i > (n /= 2) && (e = t + n);
                for (var o = t; o < e; ++o)
                    r += this.hexByte(this.get(o));
                return i > n && (r += "…"),
                    r
            }
            ,
            t.prototype.parseOID = function (t, e, n) {
                for (var i = "", r = new w, o = 0, s = t; s < e; ++s) {
                    var a = this.get(s);
                    if (r.mulAdd(128, 127 & a),
                        o += 7,
                        !(128 & a)) {
                        if ("" === i)
                            if ((r = r.simplify()) instanceof w)
                                r.sub(80),
                                    i = "2." + r.toString();
                            else {
                                var l = r < 80 ? r < 40 ? 0 : 1 : 2;
                                i = l + "." + (r - 40 * l)
                            }
                        else
                            i += "." + r.toString();
                        if (i.length > n)
                            return S(i, n);
                        r = new w,
                            o = 0
                    }
                }
                return o > 0 && (i += ".incomplete"),
                    i
            }
            ,
            t
    }(), k = function () {
        function t(t, e, n, i, r) {
            if (!(i instanceof O))
                throw new Error("Invalid tag value.");
            this.stream = t,
                this.header = e,
                this.length = n,
                this.tag = i,
                this.sub = r
        }

        return t.prototype.typeName = function () {
            switch (this.tag.tagClass) {
                case 0:
                    switch (this.tag.tagNumber) {
                        case 0:
                            return "EOC";
                        case 1:
                            return "BOOLEAN";
                        case 2:
                            return "INTEGER";
                        case 3:
                            return "BIT_STRING";
                        case 4:
                            return "OCTET_STRING";
                        case 5:
                            return "NULL";
                        case 6:
                            return "OBJECT_IDENTIFIER";
                        case 7:
                            return "ObjectDescriptor";
                        case 8:
                            return "EXTERNAL";
                        case 9:
                            return "REAL";
                        case 10:
                            return "ENUMERATED";
                        case 11:
                            return "EMBEDDED_PDV";
                        case 12:
                            return "UTF8String";
                        case 16:
                            return "SEQUENCE";
                        case 17:
                            return "SET";
                        case 18:
                            return "NumericString";
                        case 19:
                            return "PrintableString";
                        case 20:
                            return "TeletexString";
                        case 21:
                            return "VideotexString";
                        case 22:
                            return "IA5String";
                        case 23:
                            return "UTCTime";
                        case 24:
                            return "GeneralizedTime";
                        case 25:
                            return "GraphicString";
                        case 26:
                            return "VisibleString";
                        case 27:
                            return "GeneralString";
                        case 28:
                            return "UniversalString";
                        case 30:
                            return "BMPString"
                    }
                    return "Universal_" + this.tag.tagNumber.toString();
                case 1:
                    return "Application_" + this.tag.tagNumber.toString();
                case 2:
                    return "[" + this.tag.tagNumber.toString() + "]";
                case 3:
                    return "Private_" + this.tag.tagNumber.toString()
            }
        }
            ,
            t.prototype.content = function (t) {
                if (void 0 === this.tag)
                    return null;
                void 0 === t && (t = 1 / 0);
                var e = this.posContent()
                    , n = Math.abs(this.length);
                if (!this.tag.isUniversal())
                    return null !== this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + n, t);
                switch (this.tag.tagNumber) {
                    case 1:
                        return 0 === this.stream.get(e) ? "false" : "true";
                    case 2:
                        return this.stream.parseInteger(e, e + n);
                    case 3:
                        return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseBitString(e, e + n, t);
                    case 4:
                        return this.sub ? "(" + this.sub.length + " elem)" : this.stream.parseOctetString(e, e + n, t);
                    case 6:
                        return this.stream.parseOID(e, e + n, t);
                    case 16:
                    case 17:
                        return null !== this.sub ? "(" + this.sub.length + " elem)" : "(no elem)";
                    case 12:
                        return S(this.stream.parseStringUTF(e, e + n), t);
                    case 18:
                    case 19:
                    case 20:
                    case 21:
                    case 22:
                    case 26:
                        return S(this.stream.parseStringISO(e, e + n), t);
                    case 30:
                        return S(this.stream.parseStringBMP(e, e + n), t);
                    case 23:
                    case 24:
                        return this.stream.parseTime(e, e + n, 23 == this.tag.tagNumber)
                }
                return null
            }
            ,
            t.prototype.toString = function () {
                return this.typeName() + "@" + this.stream.pos + "[header:" + this.header + ",length:" + this.length + ",sub:" + (null === this.sub ? "null" : this.sub.length) + "]"
            }
            ,
            t.prototype.toPrettyString = function (t) {
                void 0 === t && (t = "");
                var e = t + this.typeName() + " @" + this.stream.pos;
                if (this.length >= 0 && (e += "+"),
                    e += this.length,
                    this.tag.tagConstructed ? e += " (constructed)" : !this.tag.isUniversal() || 3 != this.tag.tagNumber && 4 != this.tag.tagNumber || null === this.sub || (e += " (encapsulates)"),
                    e += "\n",
                null !== this.sub) {
                    t += "  ";
                    for (var n = 0, i = this.sub.length; n < i; ++n)
                        e += this.sub[n].toPrettyString(t)
                }
                return e
            }
            ,
            t.prototype.posStart = function () {
                return this.stream.pos
            }
            ,
            t.prototype.posContent = function () {
                return this.stream.pos + this.header
            }
            ,
            t.prototype.posEnd = function () {
                return this.stream.pos + this.header + Math.abs(this.length)
            }
            ,
            t.prototype.toHexString = function () {
                return this.stream.hexDump(this.posStart(), this.posEnd(), !0)
            }
            ,
            t.decodeLength = function (t) {
                var e = t.get()
                    , n = 127 & e;
                if (n == e)
                    return n;
                if (n > 6)
                    throw new Error("Length over 48 bits not supported at position " + (t.pos - 1));
                if (0 === n)
                    return null;
                e = 0;
                for (var i = 0; i < n; ++i)
                    e = 256 * e + t.get();
                return e
            }
            ,
            t.prototype.getHexStringValue = function () {
                var t = this.toHexString()
                    , e = 2 * this.header
                    , n = 2 * this.length;
                return t.substr(e, n)
            }
            ,
            t.decode = function (e) {
                var n;
                n = e instanceof E ? e : new E(e, 0);
                var i = new E(n)
                    , r = new O(n)
                    , o = t.decodeLength(n)
                    , s = n.pos
                    , a = s - i.pos
                    , l = null
                    , c = function () {
                    var e = [];
                    if (null !== o) {
                        for (var i = s + o; n.pos < i;)
                            e[e.length] = t.decode(n);
                        if (n.pos != i)
                            throw new Error("Content size is not correct for container starting at offset " + s)
                    } else
                        try {
                            for (; ;) {
                                var r = t.decode(n);
                                if (r.tag.isEOC())
                                    break;
                                e[e.length] = r
                            }
                            o = s - n.pos
                        } catch (a) {
                            throw new Error("Exception while decoding undefined length content: " + a)
                        }
                    return e
                };
                if (r.tagConstructed)
                    l = c();
                else if (r.isUniversal() && (3 == r.tagNumber || 4 == r.tagNumber))
                    try {
                        if (3 == r.tagNumber && 0 != n.get())
                            throw new Error("BIT STRINGs with unused bits cannot encapsulate.");
                        l = c();
                        for (var u = 0; u < l.length; ++u)
                            if (l[u].tag.isEOC())
                                throw new Error("EOC is not supposed to be actual content.")
                    } catch (h) {
                        l = null
                    }
                if (null === l) {
                    if (null === o)
                        throw new Error("We can't skip over an invalid tag with undefined length at offset " + s);
                    n.pos = s + Math.abs(o)
                }
                return new t(i, a, o, r, l)
            }
            ,
            t
    }(), O = function () {
        function t(t) {
            var e = t.get();
            if (this.tagClass = e >> 6,
                this.tagConstructed = 0 != (32 & e),
                this.tagNumber = 31 & e,
            31 == this.tagNumber) {
                var n = new w;
                do {
                    e = t.get(),
                        n.mulAdd(128, 127 & e)
                } while (128 & e);
                this.tagNumber = n.simplify()
            }
        }

        return t.prototype.isUniversal = function () {
            return 0 === this.tagClass
        }
            ,
            t.prototype.isEOC = function () {
                return 0 === this.tagClass && 0 === this.tagNumber
            }
            ,
            t
    }(),
    T = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997],
    L = (1 << 26) / T[T.length - 1], $ = function () {
        function t(t, e, n) {
            null != t && ("number" == typeof t ? this.fromNumber(t, e, n) : null == e && "string" != typeof t ? this.fromString(t, 256) : this.fromString(t, e))
        }

        return t.prototype.toString = function (t) {
            if (this.s < 0)
                return "-" + this.negate().toString(t);
            var e;
            if (16 == t)
                e = 4;
            else if (8 == t)
                e = 3;
            else if (2 == t)
                e = 1;
            else if (32 == t)
                e = 5;
            else {
                if (4 != t)
                    return this.toRadix(t);
                e = 2
            }
            var n, i = (1 << e) - 1, r = !1, s = "", a = this.t, l = this.DB - a * this.DB % e;
            if (a-- > 0)
                for (l < this.DB && (n = this[a] >> l) > 0 && (r = !0,
                    s = o(n)); a >= 0;)
                    l < e ? (n = (this[a] & (1 << l) - 1) << e - l,
                        n |= this[--a] >> (l += this.DB - e)) : (n = this[a] >> (l -= e) & i,
                    l <= 0 && (l += this.DB,
                        --a)),
                    n > 0 && (r = !0),
                    r && (s += o(n));
            return r ? s : "0"
        }
            ,
            t.prototype.negate = function () {
                var e = j();
                return t.ZERO.subTo(this, e),
                    e
            }
            ,
            t.prototype.abs = function () {
                return this.s < 0 ? this.negate() : this
            }
            ,
            t.prototype.compareTo = function (t) {
                var e = this.s - t.s;
                if (0 != e)
                    return e;
                var n = this.t;
                if (0 != (e = n - t.t))
                    return this.s < 0 ? -e : e;
                for (; --n >= 0;)
                    if (0 != (e = this[n] - t[n]))
                        return e;
                return 0
            }
            ,
            t.prototype.bitLength = function () {
                return this.t <= 0 ? 0 : this.DB * (this.t - 1) + H(this[this.t - 1] ^ this.s & this.DM)
            }
            ,
            t.prototype.mod = function (e) {
                var n = j();
                return this.abs().divRemTo(e, null, n),
                this.s < 0 && n.compareTo(t.ZERO) > 0 && e.subTo(n, n),
                    n
            }
            ,
            t.prototype.modPowInt = function (t, e) {
                var n;
                return n = t < 256 || e.isEven() ? new D(e) : new P(e),
                    this.exp(t, n)
            }
            ,
            t.prototype.clone = function () {
                var t = j();
                return this.copyTo(t),
                    t
            }
            ,
            t.prototype.intValue = function () {
                if (this.s < 0) {
                    if (1 == this.t)
                        return this[0] - this.DV;
                    if (0 == this.t)
                        return -1
                } else {
                    if (1 == this.t)
                        return this[0];
                    if (0 == this.t)
                        return 0
                }
                return (this[1] & (1 << 32 - this.DB) - 1) << this.DB | this[0]
            }
            ,
            t.prototype.byteValue = function () {
                return 0 == this.t ? this.s : this[0] << 24 >> 24
            }
            ,
            t.prototype.shortValue = function () {
                return 0 == this.t ? this.s : this[0] << 16 >> 16
            }
            ,
            t.prototype.signum = function () {
                return this.s < 0 ? -1 : this.t <= 0 || 1 == this.t && this[0] <= 0 ? 0 : 1
            }
            ,
            t.prototype.toByteArray = function () {
                var t = this.t
                    , e = [];
                e[0] = this.s;
                var n, i = this.DB - t * this.DB % 8, r = 0;
                if (t-- > 0)
                    for (i < this.DB && (n = this[t] >> i) != (this.s & this.DM) >> i && (e[r++] = n | this.s << this.DB - i); t >= 0;)
                        i < 8 ? (n = (this[t] & (1 << i) - 1) << 8 - i,
                            n |= this[--t] >> (i += this.DB - 8)) : (n = this[t] >> (i -= 8) & 255,
                        i <= 0 && (i += this.DB,
                            --t)),
                        0 != (128 & n) && (n |= -256),
                        0 == r && (128 & this.s) != (128 & n) && ++r,
                        (r > 0 || n != this.s) && (e[r++] = n);
                return e
            }
            ,
            t.prototype.equals = function (t) {
                return 0 == this.compareTo(t)
            }
            ,
            t.prototype.min = function (t) {
                return this.compareTo(t) < 0 ? this : t
            }
            ,
            t.prototype.max = function (t) {
                return this.compareTo(t) > 0 ? this : t
            }
            ,
            t.prototype.and = function (t) {
                var e = j();
                return this.bitwiseTo(t, s, e),
                    e
            }
            ,
            t.prototype.or = function (t) {
                var e = j();
                return this.bitwiseTo(t, a, e),
                    e
            }
            ,
            t.prototype.xor = function (t) {
                var e = j();
                return this.bitwiseTo(t, l, e),
                    e
            }
            ,
            t.prototype.andNot = function (t) {
                var e = j();
                return this.bitwiseTo(t, c, e),
                    e
            }
            ,
            t.prototype.not = function () {
                for (var t = j(), e = 0; e < this.t; ++e)
                    t[e] = this.DM & ~this[e];
                return t.t = this.t,
                    t.s = ~this.s,
                    t
            }
            ,
            t.prototype.shiftLeft = function (t) {
                var e = j();
                return t < 0 ? this.rShiftTo(-t, e) : this.lShiftTo(t, e),
                    e
            }
            ,
            t.prototype.shiftRight = function (t) {
                var e = j();
                return t < 0 ? this.lShiftTo(-t, e) : this.rShiftTo(t, e),
                    e
            }
            ,
            t.prototype.getLowestSetBit = function () {
                for (var t = 0; t < this.t; ++t)
                    if (0 != this[t])
                        return t * this.DB + u(this[t]);
                return this.s < 0 ? this.t * this.DB : -1
            }
            ,
            t.prototype.bitCount = function () {
                for (var t = 0, e = this.s & this.DM, n = 0; n < this.t; ++n)
                    t += h(this[n] ^ e);
                return t
            }
            ,
            t.prototype.testBit = function (t) {
                var e = Math.floor(t / this.DB);
                return e >= this.t ? 0 != this.s : 0 != (this[e] & 1 << t % this.DB)
            }
            ,
            t.prototype.setBit = function (t) {
                return this.changeBit(t, a)
            }
            ,
            t.prototype.clearBit = function (t) {
                return this.changeBit(t, c)
            }
            ,
            t.prototype.flipBit = function (t) {
                return this.changeBit(t, l)
            }
            ,
            t.prototype.add = function (t) {
                var e = j();
                return this.addTo(t, e),
                    e
            }
            ,
            t.prototype.subtract = function (t) {
                var e = j();
                return this.subTo(t, e),
                    e
            }
            ,
            t.prototype.multiply = function (t) {
                var e = j();
                return this.multiplyTo(t, e),
                    e
            }
            ,
            t.prototype.divide = function (t) {
                var e = j();
                return this.divRemTo(t, e, null),
                    e
            }
            ,
            t.prototype.remainder = function (t) {
                var e = j();
                return this.divRemTo(t, null, e),
                    e
            }
            ,
            t.prototype.divideAndRemainder = function (t) {
                var e = j()
                    , n = j();
                return this.divRemTo(t, e, n),
                    [e, n]
            }
            ,
            t.prototype.modPow = function (t, e) {
                var n, i, r = t.bitLength(), o = G(1);
                if (r <= 0)
                    return o;
                n = r < 18 ? 1 : r < 48 ? 3 : r < 144 ? 4 : r < 768 ? 5 : 6,
                    i = r < 8 ? new D(e) : e.isEven() ? new B(e) : new P(e);
                var s = []
                    , a = 3
                    , l = n - 1
                    , c = (1 << n) - 1;
                if (s[1] = i.convert(this),
                n > 1) {
                    var u = j();
                    for (i.sqrTo(s[1], u); a <= c;)
                        s[a] = j(),
                            i.mulTo(u, s[a - 2], s[a]),
                            a += 2
                }
                var h, d, f = t.t - 1, p = !0, v = j();
                for (r = H(t[f]) - 1; f >= 0;) {
                    for (r >= l ? h = t[f] >> r - l & c : (h = (t[f] & (1 << r + 1) - 1) << l - r,
                    f > 0 && (h |= t[f - 1] >> this.DB + r - l)),
                             a = n; 0 == (1 & h);)
                        h >>= 1,
                            --a;
                    if ((r -= a) < 0 && (r += this.DB,
                        --f),
                        p)
                        s[h].copyTo(o),
                            p = !1;
                    else {
                        for (; a > 1;)
                            i.sqrTo(o, v),
                                i.sqrTo(v, o),
                                a -= 2;
                        a > 0 ? i.sqrTo(o, v) : (d = o,
                            o = v,
                            v = d),
                            i.mulTo(v, s[h], o)
                    }
                    for (; f >= 0 && 0 == (t[f] & 1 << r);)
                        i.sqrTo(o, v),
                            d = o,
                            o = v,
                            v = d,
                        --r < 0 && (r = this.DB - 1,
                            --f)
                }
                return i.revert(o)
            }
            ,
            t.prototype.modInverse = function (e) {
                var n = e.isEven();
                if (this.isEven() && n || 0 == e.signum())
                    return t.ZERO;
                for (var i = e.clone(), r = this.clone(), o = G(1), s = G(0), a = G(0), l = G(1); 0 != i.signum();) {
                    for (; i.isEven();)
                        i.rShiftTo(1, i),
                            n ? (o.isEven() && s.isEven() || (o.addTo(this, o),
                                s.subTo(e, s)),
                                o.rShiftTo(1, o)) : s.isEven() || s.subTo(e, s),
                            s.rShiftTo(1, s);
                    for (; r.isEven();)
                        r.rShiftTo(1, r),
                            n ? (a.isEven() && l.isEven() || (a.addTo(this, a),
                                l.subTo(e, l)),
                                a.rShiftTo(1, a)) : l.isEven() || l.subTo(e, l),
                            l.rShiftTo(1, l);
                    i.compareTo(r) >= 0 ? (i.subTo(r, i),
                    n && o.subTo(a, o),
                        s.subTo(l, s)) : (r.subTo(i, r),
                    n && a.subTo(o, a),
                        l.subTo(s, l))
                }
                return 0 != r.compareTo(t.ONE) ? t.ZERO : l.compareTo(e) >= 0 ? l.subtract(e) : l.signum() < 0 ? (l.addTo(e, l),
                    l.signum() < 0 ? l.add(e) : l) : l
            }
            ,
            t.prototype.pow = function (t) {
                return this.exp(t, new I)
            }
            ,
            t.prototype.gcd = function (t) {
                var e = this.s < 0 ? this.negate() : this.clone()
                    , n = t.s < 0 ? t.negate() : t.clone();
                if (e.compareTo(n) < 0) {
                    var i = e;
                    e = n,
                        n = i
                }
                var r = e.getLowestSetBit()
                    , o = n.getLowestSetBit();
                if (o < 0)
                    return e;
                for (r < o && (o = r),
                     o > 0 && (e.rShiftTo(o, e),
                         n.rShiftTo(o, n)); e.signum() > 0;)
                    (r = e.getLowestSetBit()) > 0 && e.rShiftTo(r, e),
                    (r = n.getLowestSetBit()) > 0 && n.rShiftTo(r, n),
                        e.compareTo(n) >= 0 ? (e.subTo(n, e),
                            e.rShiftTo(1, e)) : (n.subTo(e, n),
                            n.rShiftTo(1, n));
                return o > 0 && n.lShiftTo(o, n),
                    n
            }
            ,
            t.prototype.isProbablePrime = function (t) {
                var e, n = this.abs();
                if (1 == n.t && n[0] <= T[T.length - 1]) {
                    for (e = 0; e < T.length; ++e)
                        if (n[0] == T[e])
                            return !0;
                    return !1
                }
                if (n.isEven())
                    return !1;
                for (e = 1; e < T.length;) {
                    for (var i = T[e], r = e + 1; r < T.length && i < L;)
                        i *= T[r++];
                    for (i = n.modInt(i); e < r;)
                        if (i % T[e++] == 0)
                            return !1
                }
                return n.millerRabin(t)
            }
            ,
            t.prototype.copyTo = function (t) {
                for (var e = this.t - 1; e >= 0; --e)
                    t[e] = this[e];
                t.t = this.t,
                    t.s = this.s
            }
            ,
            t.prototype.fromInt = function (t) {
                this.t = 1,
                    this.s = t < 0 ? -1 : 0,
                    t > 0 ? this[0] = t : t < -1 ? this[0] = t + this.DV : this.t = 0
            }
            ,
            t.prototype.fromString = function (e, n) {
                var i;
                if (16 == n)
                    i = 4;
                else if (8 == n)
                    i = 3;
                else if (256 == n)
                    i = 8;
                else if (2 == n)
                    i = 1;
                else if (32 == n)
                    i = 5;
                else {
                    if (4 != n)
                        return void this.fromRadix(e, n);
                    i = 2
                }
                this.t = 0,
                    this.s = 0;
                for (var r = e.length, o = !1, s = 0; --r >= 0;) {
                    var a = 8 == i ? 255 & +e[r] : V(e, r);
                    a < 0 ? "-" == e.charAt(r) && (o = !0) : (o = !1,
                        0 == s ? this[this.t++] = a : s + i > this.DB ? (this[this.t - 1] |= (a & (1 << this.DB - s) - 1) << s,
                            this[this.t++] = a >> this.DB - s) : this[this.t - 1] |= a << s,
                    (s += i) >= this.DB && (s -= this.DB))
                }
                8 == i && 0 != (128 & +e[0]) && (this.s = -1,
                s > 0 && (this[this.t - 1] |= (1 << this.DB - s) - 1 << s)),
                    this.clamp(),
                o && t.ZERO.subTo(this, this)
            }
            ,
            t.prototype.clamp = function () {
                for (var t = this.s & this.DM; this.t > 0 && this[this.t - 1] == t;)
                    --this.t
            }
            ,
            t.prototype.dlShiftTo = function (t, e) {
                var n;
                for (n = this.t - 1; n >= 0; --n)
                    e[n + t] = this[n];
                for (n = t - 1; n >= 0; --n)
                    e[n] = 0;
                e.t = this.t + t,
                    e.s = this.s
            }
            ,
            t.prototype.drShiftTo = function (t, e) {
                for (var n = t; n < this.t; ++n)
                    e[n - t] = this[n];
                e.t = Math.max(this.t - t, 0),
                    e.s = this.s
            }
            ,
            t.prototype.lShiftTo = function (t, e) {
                for (var n = t % this.DB, i = this.DB - n, r = (1 << i) - 1, o = Math.floor(t / this.DB), s = this.s << n & this.DM, a = this.t - 1; a >= 0; --a)
                    e[a + o + 1] = this[a] >> i | s,
                        s = (this[a] & r) << n;
                for (a = o - 1; a >= 0; --a)
                    e[a] = 0;
                e[o] = s,
                    e.t = this.t + o + 1,
                    e.s = this.s,
                    e.clamp()
            }
            ,
            t.prototype.rShiftTo = function (t, e) {
                e.s = this.s;
                var n = Math.floor(t / this.DB);
                if (n >= this.t)
                    e.t = 0;
                else {
                    var i = t % this.DB
                        , r = this.DB - i
                        , o = (1 << i) - 1;
                    e[0] = this[n] >> i;
                    for (var s = n + 1; s < this.t; ++s)
                        e[s - n - 1] |= (this[s] & o) << r,
                            e[s - n] = this[s] >> i;
                    i > 0 && (e[this.t - n - 1] |= (this.s & o) << r),
                        e.t = this.t - n,
                        e.clamp()
                }
            }
            ,
            t.prototype.subTo = function (t, e) {
                for (var n = 0, i = 0, r = Math.min(t.t, this.t); n < r;)
                    i += this[n] - t[n],
                        e[n++] = i & this.DM,
                        i >>= this.DB;
                if (t.t < this.t) {
                    for (i -= t.s; n < this.t;)
                        i += this[n],
                            e[n++] = i & this.DM,
                            i >>= this.DB;
                    i += this.s
                } else {
                    for (i += this.s; n < t.t;)
                        i -= t[n],
                            e[n++] = i & this.DM,
                            i >>= this.DB;
                    i -= t.s
                }
                e.s = i < 0 ? -1 : 0,
                    i < -1 ? e[n++] = this.DV + i : i > 0 && (e[n++] = i),
                    e.t = n,
                    e.clamp()
            }
            ,
            t.prototype.multiplyTo = function (e, n) {
                var i = this.abs()
                    , r = e.abs()
                    , o = i.t;
                for (n.t = o + r.t; --o >= 0;)
                    n[o] = 0;
                for (o = 0; o < r.t; ++o)
                    n[o + i.t] = i.am(0, r[o], n, o, 0, i.t);
                n.s = 0,
                    n.clamp(),
                this.s != e.s && t.ZERO.subTo(n, n)
            }
            ,
            t.prototype.squareTo = function (t) {
                for (var e = this.abs(), n = t.t = 2 * e.t; --n >= 0;)
                    t[n] = 0;
                for (n = 0; n < e.t - 1; ++n) {
                    var i = e.am(n, e[n], t, 2 * n, 0, 1);
                    (t[n + e.t] += e.am(n + 1, 2 * e[n], t, 2 * n + 1, i, e.t - n - 1)) >= e.DV && (t[n + e.t] -= e.DV,
                        t[n + e.t + 1] = 1)
                }
                t.t > 0 && (t[t.t - 1] += e.am(n, e[n], t, 2 * n, 0, 1)),
                    t.s = 0,
                    t.clamp()
            }
            ,
            t.prototype.divRemTo = function (e, n, i) {
                var r = e.abs();
                if (!(r.t <= 0)) {
                    var o = this.abs();
                    if (o.t < r.t)
                        return null != n && n.fromInt(0),
                            void (null != i && this.copyTo(i));
                    null == i && (i = j());
                    var s = j()
                        , a = this.s
                        , l = e.s
                        , c = this.DB - H(r[r.t - 1]);
                    c > 0 ? (r.lShiftTo(c, s),
                        o.lShiftTo(c, i)) : (r.copyTo(s),
                        o.copyTo(i));
                    var u = s.t
                        , h = s[u - 1];
                    if (0 != h) {
                        var d = h * (1 << this.F1) + (u > 1 ? s[u - 2] >> this.F2 : 0)
                            , f = this.FV / d
                            , p = (1 << this.F1) / d
                            , v = 1 << this.F2
                            , m = i.t
                            , g = m - u
                            , b = null == n ? j() : n;
                        for (s.dlShiftTo(g, b),
                             i.compareTo(b) >= 0 && (i[i.t++] = 1,
                                 i.subTo(b, i)),
                                 t.ONE.dlShiftTo(u, b),
                                 b.subTo(s, s); s.t < u;)
                            s[s.t++] = 0;
                        for (; --g >= 0;) {
                            var y = i[--m] == h ? this.DM : Math.floor(i[m] * f + (i[m - 1] + v) * p);
                            if ((i[m] += s.am(0, y, i, g, 0, u)) < y)
                                for (s.dlShiftTo(g, b),
                                         i.subTo(b, i); i[m] < --y;)
                                    i.subTo(b, i)
                        }
                        null != n && (i.drShiftTo(u, n),
                        a != l && t.ZERO.subTo(n, n)),
                            i.t = u,
                            i.clamp(),
                        c > 0 && i.rShiftTo(c, i),
                        a < 0 && t.ZERO.subTo(i, i)
                    }
                }
            }
            ,
            t.prototype.invDigit = function () {
                if (this.t < 1)
                    return 0;
                var t = this[0];
                if (0 == (1 & t))
                    return 0;
                var e = 3 & t;
                return (e = (e = (e = (e = e * (2 - (15 & t) * e) & 15) * (2 - (255 & t) * e) & 255) * (2 - ((65535 & t) * e & 65535)) & 65535) * (2 - t * e % this.DV) % this.DV) > 0 ? this.DV - e : -e
            }
            ,
            t.prototype.isEven = function () {
                return 0 == (this.t > 0 ? 1 & this[0] : this.s)
            }
            ,
            t.prototype.exp = function (e, n) {
                if (e > 4294967295 || e < 1)
                    return t.ONE;
                var i = j()
                    , r = j()
                    , o = n.convert(this)
                    , s = H(e) - 1;
                for (o.copyTo(i); --s >= 0;)
                    if (n.sqrTo(i, r),
                    (e & 1 << s) > 0)
                        n.mulTo(r, o, i);
                    else {
                        var a = i;
                        i = r,
                            r = a
                    }
                return n.revert(i)
            }
            ,
            t.prototype.chunkSize = function (t) {
                return Math.floor(Math.LN2 * this.DB / Math.log(t))
            }
            ,
            t.prototype.toRadix = function (t) {
                if (null == t && (t = 10),
                0 == this.signum() || t < 2 || t > 36)
                    return "0";
                var e = this.chunkSize(t)
                    , n = Math.pow(t, e)
                    , i = G(n)
                    , r = j()
                    , o = j()
                    , s = "";
                for (this.divRemTo(i, r, o); r.signum() > 0;)
                    s = (n + o.intValue()).toString(t).substr(1) + s,
                        r.divRemTo(i, r, o);
                return o.intValue().toString(t) + s
            }
            ,
            t.prototype.fromRadix = function (e, n) {
                this.fromInt(0),
                null == n && (n = 10);
                for (var i = this.chunkSize(n), r = Math.pow(n, i), o = !1, s = 0, a = 0, l = 0; l < e.length; ++l) {
                    var c = V(e, l);
                    c < 0 ? "-" == e.charAt(l) && 0 == this.signum() && (o = !0) : (a = n * a + c,
                    ++s >= i && (this.dMultiply(r),
                        this.dAddOffset(a, 0),
                        s = 0,
                        a = 0))
                }
                s > 0 && (this.dMultiply(Math.pow(n, s)),
                    this.dAddOffset(a, 0)),
                o && t.ZERO.subTo(this, this)
            }
            ,
            t.prototype.fromNumber = function (e, n, i) {
                if ("number" == typeof n)
                    if (e < 2)
                        this.fromInt(1);
                    else
                        for (this.fromNumber(e, i),
                             this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), a, this),
                             this.isEven() && this.dAddOffset(1, 0); !this.isProbablePrime(n);)
                            this.dAddOffset(2, 0),
                            this.bitLength() > e && this.subTo(t.ONE.shiftLeft(e - 1), this);
                else {
                    var r = []
                        , o = 7 & e;
                    r.length = 1 + (e >> 3),
                        n.nextBytes(r),
                        o > 0 ? r[0] &= (1 << o) - 1 : r[0] = 0,
                        this.fromString(r, 256)
                }
            }
            ,
            t.prototype.bitwiseTo = function (t, e, n) {
                var i, r, o = Math.min(t.t, this.t);
                for (i = 0; i < o; ++i)
                    n[i] = e(this[i], t[i]);
                if (t.t < this.t) {
                    for (r = t.s & this.DM,
                             i = o; i < this.t; ++i)
                        n[i] = e(this[i], r);
                    n.t = this.t
                } else {
                    for (r = this.s & this.DM,
                             i = o; i < t.t; ++i)
                        n[i] = e(r, t[i]);
                    n.t = t.t
                }
                n.s = e(this.s, t.s),
                    n.clamp()
            }
            ,
            t.prototype.changeBit = function (e, n) {
                var i = t.ONE.shiftLeft(e);
                return this.bitwiseTo(i, n, i),
                    i
            }
            ,
            t.prototype.addTo = function (t, e) {
                for (var n = 0, i = 0, r = Math.min(t.t, this.t); n < r;)
                    i += this[n] + t[n],
                        e[n++] = i & this.DM,
                        i >>= this.DB;
                if (t.t < this.t) {
                    for (i += t.s; n < this.t;)
                        i += this[n],
                            e[n++] = i & this.DM,
                            i >>= this.DB;
                    i += this.s
                } else {
                    for (i += this.s; n < t.t;)
                        i += t[n],
                            e[n++] = i & this.DM,
                            i >>= this.DB;
                    i += t.s
                }
                e.s = i < 0 ? -1 : 0,
                    i > 0 ? e[n++] = i : i < -1 && (e[n++] = this.DV + i),
                    e.t = n,
                    e.clamp()
            }
            ,
            t.prototype.dMultiply = function (t) {
                this[this.t] = this.am(0, t - 1, this, 0, 0, this.t),
                    ++this.t,
                    this.clamp()
            }
            ,
            t.prototype.dAddOffset = function (t, e) {
                if (0 != t) {
                    for (; this.t <= e;)
                        this[this.t++] = 0;
                    for (this[e] += t; this[e] >= this.DV;)
                        this[e] -= this.DV,
                        ++e >= this.t && (this[this.t++] = 0),
                            ++this[e]
                }
            }
            ,
            t.prototype.multiplyLowerTo = function (t, e, n) {
                var i = Math.min(this.t + t.t, e);
                for (n.s = 0,
                         n.t = i; i > 0;)
                    n[--i] = 0;
                for (var r = n.t - this.t; i < r; ++i)
                    n[i + this.t] = this.am(0, t[i], n, i, 0, this.t);
                for (r = Math.min(t.t, e); i < r; ++i)
                    this.am(0, t[i], n, i, 0, e - i);
                n.clamp()
            }
            ,
            t.prototype.multiplyUpperTo = function (t, e, n) {
                --e;
                var i = n.t = this.t + t.t - e;
                for (n.s = 0; --i >= 0;)
                    n[i] = 0;
                for (i = Math.max(e - this.t, 0); i < t.t; ++i)
                    n[this.t + i - e] = this.am(e - i, t[i], n, 0, 0, this.t + i - e);
                n.clamp(),
                    n.drShiftTo(1, n)
            }
            ,
            t.prototype.modInt = function (t) {
                if (t <= 0)
                    return 0;
                var e = this.DV % t
                    , n = this.s < 0 ? t - 1 : 0;
                if (this.t > 0)
                    if (0 == e)
                        n = this[0] % t;
                    else
                        for (var i = this.t - 1; i >= 0; --i)
                            n = (e * n + this[i]) % t;
                return n
            }
            ,
            t.prototype.millerRabin = function (e) {
                var n = this.subtract(t.ONE)
                    , i = n.getLowestSetBit();
                if (i <= 0)
                    return !1;
                var r = n.shiftRight(i);
                (e = e + 1 >> 1) > T.length && (e = T.length);
                for (var o = j(), s = 0; s < e; ++s) {
                    o.fromInt(T[Math.floor(Math.random() * T.length)]);
                    var a = o.modPow(r, this);
                    if (0 != a.compareTo(t.ONE) && 0 != a.compareTo(n)) {
                        for (var l = 1; l++ < i && 0 != a.compareTo(n);)
                            if (0 == (a = a.modPowInt(2, this)).compareTo(t.ONE))
                                return !1;
                        if (0 != a.compareTo(n))
                            return !1
                    }
                }
                return !0
            }
            ,
            t.prototype.square = function () {
                var t = j();
                return this.squareTo(t),
                    t
            }
            ,
            t.prototype.gcda = function (t, e) {
                var n = this.s < 0 ? this.negate() : this.clone()
                    , i = t.s < 0 ? t.negate() : t.clone();
                if (n.compareTo(i) < 0) {
                    var r = n;
                    n = i,
                        i = r
                }
                var o = n.getLowestSetBit()
                    , s = i.getLowestSetBit();
                if (s < 0)
                    e(n);
                else {
                    o < s && (s = o),
                    s > 0 && (n.rShiftTo(s, n),
                        i.rShiftTo(s, i));
                    var a = function () {
                        (o = n.getLowestSetBit()) > 0 && n.rShiftTo(o, n),
                        (o = i.getLowestSetBit()) > 0 && i.rShiftTo(o, i),
                            n.compareTo(i) >= 0 ? (n.subTo(i, n),
                                n.rShiftTo(1, n)) : (i.subTo(n, i),
                                i.rShiftTo(1, i)),
                            n.signum() > 0 ? setTimeout(a, 0) : (s > 0 && i.lShiftTo(s, i),
                                setTimeout((function () {
                                        e(i)
                                    }
                                ), 0))
                    };
                    setTimeout(a, 10)
                }
            }
            ,
            t.prototype.fromNumberAsync = function (e, n, i, r) {
                if ("number" == typeof n)
                    if (e < 2)
                        this.fromInt(1);
                    else {
                        this.fromNumber(e, i),
                        this.testBit(e - 1) || this.bitwiseTo(t.ONE.shiftLeft(e - 1), a, this),
                        this.isEven() && this.dAddOffset(1, 0);
                        var o = this
                            , s = function () {
                            o.dAddOffset(2, 0),
                            o.bitLength() > e && o.subTo(t.ONE.shiftLeft(e - 1), o),
                                o.isProbablePrime(n) ? setTimeout((function () {
                                        r()
                                    }
                                ), 0) : setTimeout(s, 0)
                        };
                        setTimeout(s, 0)
                    }
                else {
                    var l = []
                        , c = 7 & e;
                    l.length = 1 + (e >> 3),
                        n.nextBytes(l),
                        c > 0 ? l[0] &= (1 << c) - 1 : l[0] = 0,
                        this.fromString(l, 256)
                }
            }
            ,
            t
    }(), I = function () {
        function t() {
        }

        return t.prototype.convert = function (t) {
            return t
        }
            ,
            t.prototype.revert = function (t) {
                return t
            }
            ,
            t.prototype.mulTo = function (t, e, n) {
                t.multiplyTo(e, n)
            }
            ,
            t.prototype.sqrTo = function (t, e) {
                t.squareTo(e)
            }
            ,
            t
    }(), D = function () {
        function t(t) {
            this.m = t
        }

        return t.prototype.convert = function (t) {
            return t.s < 0 || t.compareTo(this.m) >= 0 ? t.mod(this.m) : t
        }
            ,
            t.prototype.revert = function (t) {
                return t
            }
            ,
            t.prototype.reduce = function (t) {
                t.divRemTo(this.m, null, t)
            }
            ,
            t.prototype.mulTo = function (t, e, n) {
                t.multiplyTo(e, n),
                    this.reduce(n)
            }
            ,
            t.prototype.sqrTo = function (t, e) {
                t.squareTo(e),
                    this.reduce(e)
            }
            ,
            t
    }(), P = function () {
        function t(t) {
            this.m = t,
                this.mp = t.invDigit(),
                this.mpl = 32767 & this.mp,
                this.mph = this.mp >> 15,
                this.um = (1 << t.DB - 15) - 1,
                this.mt2 = 2 * t.t
        }

        return t.prototype.convert = function (t) {
            var e = j();
            return t.abs().dlShiftTo(this.m.t, e),
                e.divRemTo(this.m, null, e),
            t.s < 0 && e.compareTo($.ZERO) > 0 && this.m.subTo(e, e),
                e
        }
            ,
            t.prototype.revert = function (t) {
                var e = j();
                return t.copyTo(e),
                    this.reduce(e),
                    e
            }
            ,
            t.prototype.reduce = function (t) {
                for (; t.t <= this.mt2;)
                    t[t.t++] = 0;
                for (var e = 0; e < this.m.t; ++e) {
                    var n = 32767 & t[e]
                        , i = n * this.mpl + ((n * this.mph + (t[e] >> 15) * this.mpl & this.um) << 15) & t.DM;
                    for (t[n = e + this.m.t] += this.m.am(0, i, t, e, 0, this.m.t); t[n] >= t.DV;)
                        t[n] -= t.DV,
                            t[++n]++
                }
                t.clamp(),
                    t.drShiftTo(this.m.t, t),
                t.compareTo(this.m) >= 0 && t.subTo(this.m, t)
            }
            ,
            t.prototype.mulTo = function (t, e, n) {
                t.multiplyTo(e, n),
                    this.reduce(n)
            }
            ,
            t.prototype.sqrTo = function (t, e) {
                t.squareTo(e),
                    this.reduce(e)
            }
            ,
            t
    }(), B = function () {
        function t(t) {
            this.m = t,
                this.r2 = j(),
                this.q3 = j(),
                $.ONE.dlShiftTo(2 * t.t, this.r2),
                this.mu = this.r2.divide(t)
        }

        return t.prototype.convert = function (t) {
            if (t.s < 0 || t.t > 2 * this.m.t)
                return t.mod(this.m);
            if (t.compareTo(this.m) < 0)
                return t;
            var e = j();
            return t.copyTo(e),
                this.reduce(e),
                e
        }
            ,
            t.prototype.revert = function (t) {
                return t
            }
            ,
            t.prototype.reduce = function (t) {
                for (t.drShiftTo(this.m.t - 1, this.r2),
                     t.t > this.m.t + 1 && (t.t = this.m.t + 1,
                         t.clamp()),
                         this.mu.multiplyUpperTo(this.r2, this.m.t + 1, this.q3),
                         this.m.multiplyLowerTo(this.q3, this.m.t + 1, this.r2); t.compareTo(this.r2) < 0;)
                    t.dAddOffset(1, this.m.t + 1);
                for (t.subTo(this.r2, t); t.compareTo(this.m) >= 0;)
                    t.subTo(this.m, t)
            }
            ,
            t.prototype.mulTo = function (t, e, n) {
                t.multiplyTo(e, n),
                    this.reduce(n)
            }
            ,
            t.prototype.sqrTo = function (t, e) {
                t.squareTo(e),
                    this.reduce(e)
            }
            ,
            t
    }();

function j() {
    return new $(null)
}

function M(t, e) {
    return new $(t, e)
}

var A = "undefined" != typeof navigator;
A && "Microsoft Internet Explorer" == navigator.appName ? ($.prototype.am = function (t, e, n, i, r, o) {
    for (var s = 32767 & e, a = e >> 15; --o >= 0;) {
        var l = 32767 & this[t]
            , c = this[t++] >> 15
            , u = a * l + c * s;
        r = ((l = s * l + ((32767 & u) << 15) + n[i] + (1073741823 & r)) >>> 30) + (u >>> 15) + a * c + (r >>> 30),
            n[i++] = 1073741823 & l
    }
    return r
}
    ,
    C = 30) : A && "Netscape" != navigator.appName ? ($.prototype.am = function (t, e, n, i, r, o) {
    for (; --o >= 0;) {
        var s = e * this[t++] + n[i] + r;
        r = Math.floor(s / 67108864),
            n[i++] = 67108863 & s
    }
    return r
}
    ,
    C = 26) : ($.prototype.am = function (t, e, n, i, r, o) {
    for (var s = 16383 & e, a = e >> 14; --o >= 0;) {
        var l = 16383 & this[t]
            , c = this[t++] >> 14
            , u = a * l + c * s;
        r = ((l = s * l + ((16383 & u) << 14) + n[i] + r) >> 28) + (u >> 14) + a * c,
            n[i++] = 268435455 & l
    }
    return r
}
    ,
    C = 28),
    $.prototype.DB = C,
    $.prototype.DM = (1 << C) - 1,
    $.prototype.DV = 1 << C;
$.prototype.FV = Math.pow(2, 52),
    $.prototype.F1 = 52 - C,
    $.prototype.F2 = 2 * C - 52;
var R, N, z = [];
for (R = "0".charCodeAt(0),
         N = 0; N <= 9; ++N)
    z[R++] = N;
for (R = "a".charCodeAt(0),
         N = 10; N < 36; ++N)
    z[R++] = N;
for (R = "A".charCodeAt(0),
         N = 10; N < 36; ++N)
    z[R++] = N;

function V(t, e) {
    var n = z[t.charCodeAt(e)];
    return null == n ? -1 : n
}

function G(t) {
    var e = j();
    return e.fromInt(t),
        e
}

function H(t) {
    var e, n = 1;
    return 0 != (e = t >>> 16) && (t = e,
        n += 16),
    0 != (e = t >> 8) && (t = e,
        n += 8),
    0 != (e = t >> 4) && (t = e,
        n += 4),
    0 != (e = t >> 2) && (t = e,
        n += 2),
    0 != (e = t >> 1) && (t = e,
        n += 1),
        n
}

$.ZERO = G(0),
    $.ONE = G(1);
var U = function () {
    function t() {
        this.i = 0,
            this.j = 0,
            this.S = []
    }

    return t.prototype.init = function (t) {
        var e, n, i;
        for (e = 0; e < 256; ++e)
            this.S[e] = e;
        for (n = 0,
                 e = 0; e < 256; ++e)
            n = n + this.S[e] + t[e % t.length] & 255,
                i = this.S[e],
                this.S[e] = this.S[n],
                this.S[n] = i;
        this.i = 0,
            this.j = 0
    }
        ,
        t.prototype.next = function () {
            var t;
            return this.i = this.i + 1 & 255,
                this.j = this.j + this.S[this.i] & 255,
                t = this.S[this.i],
                this.S[this.i] = this.S[this.j],
                this.S[this.j] = t,
                this.S[t + this.S[this.i] & 255]
        }
        ,
        t
}();
var F, W, q = null;
if (null == q) {
    q = [],
        W = 0;
    var K = void 0;
    if (window.crypto && window.crypto.getRandomValues) {
        var X = new Uint32Array(256);
        for (window.crypto.getRandomValues(X),
                 K = 0; K < X.length; ++K)
            q[W++] = 255 & X[K]
    }
    var Y = 0
        , Z = function (t) {
        if ((Y = Y || 0) >= 256 || W >= 256)
            window.removeEventListener ? window.removeEventListener("mousemove", Z, !1) : window.detachEvent && window.detachEvent("onmousemove", Z);
        else
            try {
                var e = t.x + t.y;
                q[W++] = 255 & e,
                    Y += 1
            } catch (n) {
            }
    };
    window.addEventListener ? window.addEventListener("mousemove", Z, !1) : window.attachEvent && window.attachEvent("onmousemove", Z)
}

function Q() {
    if (null == F) {
        for (F = new U; W < 256;) {
            var t = Math.floor(65536 * Math.random());
            q[W++] = 255 & t
        }
        for (F.init(q),
                 W = 0; W < q.length; ++W)
            q[W] = 0;
        W = 0
    }
    return F.next()
}

var J = function () {
    function t() {
    }

    return t.prototype.nextBytes = function (t) {
        for (var e = 0; e < t.length; ++e)
            t[e] = Q()
    }
        ,
        t
}();
var tt = function () {
    function t() {
        this.n = null,
            this.e = 0,
            this.d = null,
            this.p = null,
            this.q = null,
            this.dmp1 = null,
            this.dmq1 = null,
            this.coeff = null
    }

    return t.prototype.doPublic = function (t) {
        return t.modPowInt(this.e, this.n)
    }
        ,
        t.prototype.doPrivate = function (t) {
            if (null == this.p || null == this.q)
                return t.modPow(this.d, this.n);
            for (var e = t.mod(this.p).modPow(this.dmp1, this.p), n = t.mod(this.q).modPow(this.dmq1, this.q); e.compareTo(n) < 0;)
                e = e.add(this.p);
            return e.subtract(n).multiply(this.coeff).mod(this.p).multiply(this.q).add(n)
        }
        ,
        t.prototype.setPublic = function (t, e) {
            null != t && null != e && t.length > 0 && e.length > 0 && (this.n = M(t, 16),
                this.e = parseInt(e, 16))
        }
        ,
        t.prototype.encrypt = function (t) {
            var e = this.n.bitLength() + 7 >> 3
                , n = function (t, e) {
                if (e < t.length + 11)
                    return null;
                for (var n = [], i = t.length - 1; i >= 0 && e > 0;) {
                    var r = t.charCodeAt(i--);
                    r < 128 ? n[--e] = r : r > 127 && r < 2048 ? (n[--e] = 63 & r | 128,
                        n[--e] = r >> 6 | 192) : (n[--e] = 63 & r | 128,
                        n[--e] = r >> 6 & 63 | 128,
                        n[--e] = r >> 12 | 224)
                }
                n[--e] = 0;
                for (var o = new J, s = []; e > 2;) {
                    for (s[0] = 0; 0 == s[0];)
                        o.nextBytes(s);
                    n[--e] = s[0]
                }
                return n[--e] = 2,
                    n[--e] = 0,
                    new $(n)
            }(t, e);
            if (null == n)
                return null;
            var i = this.doPublic(n);
            if (null == i)
                return null;
            for (var r = i.toString(16), o = r.length, s = 0; s < 2 * e - o; s++)
                r = "0" + r;
            return r
        }
        ,
        t.prototype.setPrivate = function (t, e, n) {
            null != t && null != e && t.length > 0 && e.length > 0 && (this.n = M(t, 16),
                this.e = parseInt(e, 16),
                this.d = M(n, 16))
        }
        ,
        t.prototype.setPrivateEx = function (t, e, n, i, r, o, s, a) {
            null != t && null != e && t.length > 0 && e.length > 0 && (this.n = M(t, 16),
                this.e = parseInt(e, 16),
                this.d = M(n, 16),
                this.p = M(i, 16),
                this.q = M(r, 16),
                this.dmp1 = M(o, 16),
                this.dmq1 = M(s, 16),
                this.coeff = M(a, 16))
        }
        ,
        t.prototype.generate = function (t, e) {
            var n = new J
                , i = t >> 1;
            this.e = parseInt(e, 16);
            for (var r = new $(e, 16); ;) {
                for (; this.p = new $(t - i, 1, n),
                       0 != this.p.subtract($.ONE).gcd(r).compareTo($.ONE) || !this.p.isProbablePrime(10);)
                    ;
                for (; this.q = new $(i, 1, n),
                       0 != this.q.subtract($.ONE).gcd(r).compareTo($.ONE) || !this.q.isProbablePrime(10);)
                    ;
                if (this.p.compareTo(this.q) <= 0) {
                    var o = this.p;
                    this.p = this.q,
                        this.q = o
                }
                var s = this.p.subtract($.ONE)
                    , a = this.q.subtract($.ONE)
                    , l = s.multiply(a);
                if (0 == l.gcd(r).compareTo($.ONE)) {
                    this.n = this.p.multiply(this.q),
                        this.d = r.modInverse(l),
                        this.dmp1 = this.d.mod(s),
                        this.dmq1 = this.d.mod(a),
                        this.coeff = this.q.modInverse(this.p);
                    break
                }
            }
        }
        ,
        t.prototype.decrypt = function (t) {
            var e = M(t, 16)
                , n = this.doPrivate(e);
            return null == n ? null : function (t, e) {
                var n = t.toByteArray()
                    , i = 0;
                for (; i < n.length && 0 == n[i];)
                    ++i;
                if (n.length - i != e - 1 || 2 != n[i])
                    return null;
                ++i;
                for (; 0 != n[i];)
                    if (++i >= n.length)
                        return null;
                var r = "";
                for (; ++i < n.length;) {
                    var o = 255 & n[i];
                    o < 128 ? r += String.fromCharCode(o) : o > 191 && o < 224 ? (r += String.fromCharCode((31 & o) << 6 | 63 & n[i + 1]),
                        ++i) : (r += String.fromCharCode((15 & o) << 12 | (63 & n[i + 1]) << 6 | 63 & n[i + 2]),
                        i += 2)
                }
                return r
            }(n, this.n.bitLength() + 7 >> 3)
        }
        ,
        t.prototype.generateAsync = function (t, e, n) {
            var i = new J
                , r = t >> 1;
            this.e = parseInt(e, 16);
            var o = new $(e, 16)
                , s = this
                , a = function () {
                var e = function () {
                    if (s.p.compareTo(s.q) <= 0) {
                        var t = s.p;
                        s.p = s.q,
                            s.q = t
                    }
                    var e = s.p.subtract($.ONE)
                        , i = s.q.subtract($.ONE)
                        , r = e.multiply(i);
                    0 == r.gcd(o).compareTo($.ONE) ? (s.n = s.p.multiply(s.q),
                        s.d = o.modInverse(r),
                        s.dmp1 = s.d.mod(e),
                        s.dmq1 = s.d.mod(i),
                        s.coeff = s.q.modInverse(s.p),
                        setTimeout((function () {
                                n()
                            }
                        ), 0)) : setTimeout(a, 0)
                }
                    , l = function () {
                    s.q = j(),
                        s.q.fromNumberAsync(r, 1, i, (function () {
                                s.q.subtract($.ONE).gcda(o, (function (t) {
                                        0 == t.compareTo($.ONE) && s.q.isProbablePrime(10) ? setTimeout(e, 0) : setTimeout(l, 0)
                                    }
                                ))
                            }
                        ))
                }
                    , c = function () {
                    s.p = j(),
                        s.p.fromNumberAsync(t - r, 1, i, (function () {
                                s.p.subtract($.ONE).gcda(o, (function (t) {
                                        0 == t.compareTo($.ONE) && s.p.isProbablePrime(10) ? setTimeout(l, 0) : setTimeout(c, 0)
                                    }
                                ))
                            }
                        ))
                };
                setTimeout(c, 0)
            };
            setTimeout(a, 0)
        }
        ,
        t.prototype.sign = function (t, e, n) {
            var i = function (t, e) {
                if (e < t.length + 22)
                    return null;
                for (var n = e - t.length - 6, i = "", r = 0; r < n; r += 2)
                    i += "ff";
                return M("0001" + i + "00" + t, 16)
            }((et[n] || "") + e(t).toString(), this.n.bitLength() / 4);
            if (null == i)
                return null;
            var r = this.doPrivate(i);
            if (null == r)
                return null;
            var o = r.toString(16);
            return 0 == (1 & o.length) ? o : "0" + o
        }
        ,
        t.prototype.verify = function (t, e, n) {
            var i = M(e, 16)
                , r = this.doPublic(i);
            return null == r ? null : function (t) {
                for (var e in et)
                    if (et.hasOwnProperty(e)) {
                        var n = et[e]
                            , i = n.length;
                        if (t.substr(0, i) == n)
                            return t.substr(i)
                    }
                return t
            }(r.toString(16).replace(/^1f+00/, "")) == n(t).toString()
        }
        ,
        t
}();
var et = {
    md2: "3020300c06082a864886f70d020205000410",
    md5: "3020300c06082a864886f70d020505000410",
    sha1: "3021300906052b0e03021a05000414",
    sha224: "302d300d06096086480165030402040500041c",
    sha256: "3031300d060960864801650304020105000420",
    sha384: "3041300d060960864801650304020205000430",
    sha512: "3051300d060960864801650304020305000440",
    ripemd160: "3021300906052b2403020105000414"
};
var nt = {};
nt.lang = {
    extend: function (t, e, n) {
        if (!e || !t)
            throw new Error("YAHOO.lang.extend failed, please check that all dependencies are included.");
        var i = function () {
        };
        if (i.prototype = e.prototype,
            t.prototype = new i,
            t.prototype.constructor = t,
            t.superclass = e.prototype,
        e.prototype.constructor == Object.prototype.constructor && (e.prototype.constructor = e),
            n) {
            var r;
            for (r in n)
                t.prototype[r] = n[r];
            var o = function () {
            }
                , s = ["toString", "valueOf"];
            try {
                /MSIE/.test(navigator.userAgent) && (o = function (t, e) {
                        for (r = 0; r < s.length; r += 1) {
                            var n = s[r]
                                , i = e[n];
                            "function" == typeof i && i != Object.prototype[n] && (t[n] = i)
                        }
                    }
                )
            } catch (a) {
            }
            o(t.prototype, n)
        }
    }
};
var it = {};
void 0 !== it.asn1 && it.asn1 || (it.asn1 = {}),
    it.asn1.ASN1Util = new function () {
        this.integerToByteHex = function (t) {
            var e = t.toString(16);
            return e.length % 2 == 1 && (e = "0" + e),
                e
        }
            ,
            this.bigIntToMinTwosComplementsHex = function (t) {
                var e = t.toString(16);
                if ("-" != e.substr(0, 1))
                    e.length % 2 == 1 ? e = "0" + e : e.match(/^[0-7]/) || (e = "00" + e);
                else {
                    var n = e.substr(1).length;
                    n % 2 == 1 ? n += 1 : e.match(/^[0-7]/) || (n += 2);
                    for (var i = "", r = 0; r < n; r++)
                        i += "f";
                    e = new $(i, 16).xor(t).add($.ONE).toString(16).replace(/^-/, "")
                }
                return e
            }
            ,
            this.getPEMStringFromHex = function (t, e) {
                return hextopem(t, e)
            }
            ,
            this.newObject = function (t) {
                var e = it.asn1
                    , n = e.DERBoolean
                    , i = e.DERInteger
                    , r = e.DERBitString
                    , o = e.DEROctetString
                    , s = e.DERNull
                    , a = e.DERObjectIdentifier
                    , l = e.DEREnumerated
                    , c = e.DERUTF8String
                    , u = e.DERNumericString
                    , h = e.DERPrintableString
                    , d = e.DERTeletexString
                    , f = e.DERIA5String
                    , p = e.DERUTCTime
                    , v = e.DERGeneralizedTime
                    , m = e.DERSequence
                    , g = e.DERSet
                    , b = e.DERTaggedObject
                    , y = e.ASN1Util.newObject
                    , w = Object.keys(t);
                if (1 != w.length)
                    throw "key of param shall be only one.";
                var x = w[0];
                if (-1 == ":bool:int:bitstr:octstr:null:oid:enum:utf8str:numstr:prnstr:telstr:ia5str:utctime:gentime:seq:set:tag:".indexOf(":" + x + ":"))
                    throw "undefined key: " + x;
                if ("bool" == x)
                    return new n(t[x]);
                if ("int" == x)
                    return new i(t[x]);
                if ("bitstr" == x)
                    return new r(t[x]);
                if ("octstr" == x)
                    return new o(t[x]);
                if ("null" == x)
                    return new s(t[x]);
                if ("oid" == x)
                    return new a(t[x]);
                if ("enum" == x)
                    return new l(t[x]);
                if ("utf8str" == x)
                    return new c(t[x]);
                if ("numstr" == x)
                    return new u(t[x]);
                if ("prnstr" == x)
                    return new h(t[x]);
                if ("telstr" == x)
                    return new d(t[x]);
                if ("ia5str" == x)
                    return new f(t[x]);
                if ("utctime" == x)
                    return new p(t[x]);
                if ("gentime" == x)
                    return new v(t[x]);
                if ("seq" == x) {
                    for (var _ = t[x], S = [], C = 0; C < _.length; C++) {
                        var E = y(_[C]);
                        S.push(E)
                    }
                    return new m({
                        array: S
                    })
                }
                if ("set" == x) {
                    for (_ = t[x],
                             S = [],
                             C = 0; C < _.length; C++) {
                        E = y(_[C]);
                        S.push(E)
                    }
                    return new g({
                        array: S
                    })
                }
                if ("tag" == x) {
                    var k = t[x];
                    if ("[object Array]" === Object.prototype.toString.call(k) && 3 == k.length) {
                        var O = y(k[2]);
                        return new b({
                            tag: k[0],
                            explicit: k[1],
                            obj: O
                        })
                    }
                    var T = {};
                    if (void 0 !== k.explicit && (T.explicit = k.explicit),
                    void 0 !== k.tag && (T.tag = k.tag),
                    void 0 === k.obj)
                        throw "obj shall be specified for 'tag'.";
                    return T.obj = y(k.obj),
                        new b(T)
                }
            }
            ,
            this.jsonToASN1HEX = function (t) {
                return this.newObject(t).getEncodedHex()
            }
    }
    ,
    it.asn1.ASN1Util.oidHexToInt = function (t) {
        for (var e = "", n = parseInt(t.substr(0, 2), 16), i = (e = Math.floor(n / 40) + "." + n % 40,
            ""), r = 2; r < t.length; r += 2) {
            var o = ("00000000" + parseInt(t.substr(r, 2), 16).toString(2)).slice(-8);
            if (i += o.substr(1, 7),
            "0" == o.substr(0, 1))
                e = e + "." + new $(i, 2).toString(10),
                    i = ""
        }
        return e
    }
    ,
    it.asn1.ASN1Util.oidIntToHex = function (t) {
        var e = function (t) {
            var e = t.toString(16);
            return 1 == e.length && (e = "0" + e),
                e
        }
            , n = function (t) {
            var n = ""
                , i = new $(t, 10).toString(2)
                , r = 7 - i.length % 7;
            7 == r && (r = 0);
            for (var o = "", s = 0; s < r; s++)
                o += "0";
            i = o + i;
            for (s = 0; s < i.length - 1; s += 7) {
                var a = i.substr(s, 7);
                s != i.length - 7 && (a = "1" + a),
                    n += e(parseInt(a, 2))
            }
            return n
        };
        if (!t.match(/^[0-9.]+$/))
            throw "malformed oid string: " + t;
        var i = ""
            , r = t.split(".")
            , o = 40 * parseInt(r[0]) + parseInt(r[1]);
        i += e(o),
            r.splice(0, 2);
        for (var s = 0; s < r.length; s++)
            i += n(r[s]);
        return i
    }
    ,
    it.asn1.ASN1Object = function () {
        this.getLengthHexFromValue = function () {
            if (void 0 === this.hV || null == this.hV)
                throw "this.hV is null or undefined.";
            if (this.hV.length % 2 == 1)
                throw "value hex must be even length: n=" + "".length + ",v=" + this.hV;
            var t = this.hV.length / 2
                , e = t.toString(16);
            if (e.length % 2 == 1 && (e = "0" + e),
            t < 128)
                return e;
            var n = e.length / 2;
            if (n > 15)
                throw "ASN.1 length too long to represent by 8x: n = " + t.toString(16);
            return (128 + n).toString(16) + e
        }
            ,
            this.getEncodedHex = function () {
                return (null == this.hTLV || this.isModified) && (this.hV = this.getFreshValueHex(),
                    this.hL = this.getLengthHexFromValue(),
                    this.hTLV = this.hT + this.hL + this.hV,
                    this.isModified = !1),
                    this.hTLV
            }
            ,
            this.getValueHex = function () {
                return this.getEncodedHex(),
                    this.hV
            }
            ,
            this.getFreshValueHex = function () {
                return ""
            }
    }
    ,
    it.asn1.DERAbstractString = function (t) {
        it.asn1.DERAbstractString.superclass.constructor.call(this);
        this.getString = function () {
            return this.s
        }
            ,
            this.setString = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.s = t,
                    this.hV = stohex(this.s)
            }
            ,
            this.setStringHex = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.s = null,
                    this.hV = t
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
            ,
        void 0 !== t && ("string" == typeof t ? this.setString(t) : void 0 !== t.str ? this.setString(t.str) : void 0 !== t.hex && this.setStringHex(t.hex))
    }
    ,
    nt.lang.extend(it.asn1.DERAbstractString, it.asn1.ASN1Object),
    it.asn1.DERAbstractTime = function (t) {
        it.asn1.DERAbstractTime.superclass.constructor.call(this);
        this.localDateToUTC = function (t) {
            return utc = t.getTime() + 6e4 * t.getTimezoneOffset(),
                new Date(utc)
        }
            ,
            this.formatDate = function (t, e, n) {
                var i = this.zeroPadding
                    , r = this.localDateToUTC(t)
                    , o = String(r.getFullYear());
                "utc" == e && (o = o.substr(2, 2));
                var s = o + i(String(r.getMonth() + 1), 2) + i(String(r.getDate()), 2) + i(String(r.getHours()), 2) + i(String(r.getMinutes()), 2) + i(String(r.getSeconds()), 2);
                if (!0 === n) {
                    var a = r.getMilliseconds();
                    if (0 != a) {
                        var l = i(String(a), 3);
                        s = s + "." + (l = l.replace(/[0]+$/, ""))
                    }
                }
                return s + "Z"
            }
            ,
            this.zeroPadding = function (t, e) {
                return t.length >= e ? t : new Array(e - t.length + 1).join("0") + t
            }
            ,
            this.getString = function () {
                return this.s
            }
            ,
            this.setString = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.s = t,
                    this.hV = stohex(t)
            }
            ,
            this.setByDateValue = function (t, e, n, i, r, o) {
                var s = new Date(Date.UTC(t, e - 1, n, i, r, o, 0));
                this.setByDate(s)
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
    }
    ,
    nt.lang.extend(it.asn1.DERAbstractTime, it.asn1.ASN1Object),
    it.asn1.DERAbstractStructured = function (t) {
        it.asn1.DERAbstractString.superclass.constructor.call(this);
        this.setByASN1ObjectArray = function (t) {
            this.hTLV = null,
                this.isModified = !0,
                this.asn1Array = t
        }
            ,
            this.appendASN1Object = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.asn1Array.push(t)
            }
            ,
            this.asn1Array = new Array,
        void 0 !== t && void 0 !== t.array && (this.asn1Array = t.array)
    }
    ,
    nt.lang.extend(it.asn1.DERAbstractStructured, it.asn1.ASN1Object),
    it.asn1.DERBoolean = function () {
        it.asn1.DERBoolean.superclass.constructor.call(this),
            this.hT = "01",
            this.hTLV = "0101ff"
    }
    ,
    nt.lang.extend(it.asn1.DERBoolean, it.asn1.ASN1Object),
    it.asn1.DERInteger = function (t) {
        it.asn1.DERInteger.superclass.constructor.call(this),
            this.hT = "02",
            this.setByBigInteger = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.hV = it.asn1.ASN1Util.bigIntToMinTwosComplementsHex(t)
            }
            ,
            this.setByInteger = function (t) {
                var e = new $(String(t), 10);
                this.setByBigInteger(e)
            }
            ,
            this.setValueHex = function (t) {
                this.hV = t
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
            ,
        void 0 !== t && (void 0 !== t.bigint ? this.setByBigInteger(t.bigint) : void 0 !== t.int ? this.setByInteger(t.int) : "number" == typeof t ? this.setByInteger(t) : void 0 !== t.hex && this.setValueHex(t.hex))
    }
    ,
    nt.lang.extend(it.asn1.DERInteger, it.asn1.ASN1Object),
    it.asn1.DERBitString = function (t) {
        if (void 0 !== t && void 0 !== t.obj) {
            var e = it.asn1.ASN1Util.newObject(t.obj);
            t.hex = "00" + e.getEncodedHex()
        }
        it.asn1.DERBitString.superclass.constructor.call(this),
            this.hT = "03",
            this.setHexValueIncludingUnusedBits = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.hV = t
            }
            ,
            this.setUnusedBitsAndHexValue = function (t, e) {
                if (t < 0 || 7 < t)
                    throw "unused bits shall be from 0 to 7: u = " + t;
                var n = "0" + t;
                this.hTLV = null,
                    this.isModified = !0,
                    this.hV = n + e
            }
            ,
            this.setByBinaryString = function (t) {
                var e = 8 - (t = t.replace(/0+$/, "")).length % 8;
                8 == e && (e = 0);
                for (var n = 0; n <= e; n++)
                    t += "0";
                var i = "";
                for (n = 0; n < t.length - 1; n += 8) {
                    var r = t.substr(n, 8)
                        , o = parseInt(r, 2).toString(16);
                    1 == o.length && (o = "0" + o),
                        i += o
                }
                this.hTLV = null,
                    this.isModified = !0,
                    this.hV = "0" + e + i
            }
            ,
            this.setByBooleanArray = function (t) {
                for (var e = "", n = 0; n < t.length; n++)
                    1 == t[n] ? e += "1" : e += "0";
                this.setByBinaryString(e)
            }
            ,
            this.newFalseArray = function (t) {
                for (var e = new Array(t), n = 0; n < t; n++)
                    e[n] = !1;
                return e
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
            ,
        void 0 !== t && ("string" == typeof t && t.toLowerCase().match(/^[0-9a-f]+$/) ? this.setHexValueIncludingUnusedBits(t) : void 0 !== t.hex ? this.setHexValueIncludingUnusedBits(t.hex) : void 0 !== t.bin ? this.setByBinaryString(t.bin) : void 0 !== t.array && this.setByBooleanArray(t.array))
    }
    ,
    nt.lang.extend(it.asn1.DERBitString, it.asn1.ASN1Object),
    it.asn1.DEROctetString = function (t) {
        if (void 0 !== t && void 0 !== t.obj) {
            var e = it.asn1.ASN1Util.newObject(t.obj);
            t.hex = e.getEncodedHex()
        }
        it.asn1.DEROctetString.superclass.constructor.call(this, t),
            this.hT = "04"
    }
    ,
    nt.lang.extend(it.asn1.DEROctetString, it.asn1.DERAbstractString),
    it.asn1.DERNull = function () {
        it.asn1.DERNull.superclass.constructor.call(this),
            this.hT = "05",
            this.hTLV = "0500"
    }
    ,
    nt.lang.extend(it.asn1.DERNull, it.asn1.ASN1Object),
    it.asn1.DERObjectIdentifier = function (t) {
        var e = function (t) {
            var e = t.toString(16);
            return 1 == e.length && (e = "0" + e),
                e
        }
            , n = function (t) {
            var n = ""
                , i = new $(t, 10).toString(2)
                , r = 7 - i.length % 7;
            7 == r && (r = 0);
            for (var o = "", s = 0; s < r; s++)
                o += "0";
            i = o + i;
            for (s = 0; s < i.length - 1; s += 7) {
                var a = i.substr(s, 7);
                s != i.length - 7 && (a = "1" + a),
                    n += e(parseInt(a, 2))
            }
            return n
        };
        it.asn1.DERObjectIdentifier.superclass.constructor.call(this),
            this.hT = "06",
            this.setValueHex = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.s = null,
                    this.hV = t
            }
            ,
            this.setValueOidString = function (t) {
                if (!t.match(/^[0-9.]+$/))
                    throw "malformed oid string: " + t;
                var i = ""
                    , r = t.split(".")
                    , o = 40 * parseInt(r[0]) + parseInt(r[1]);
                i += e(o),
                    r.splice(0, 2);
                for (var s = 0; s < r.length; s++)
                    i += n(r[s]);
                this.hTLV = null,
                    this.isModified = !0,
                    this.s = null,
                    this.hV = i
            }
            ,
            this.setValueName = function (t) {
                var e = it.asn1.x509.OID.name2oid(t);
                if ("" === e)
                    throw "DERObjectIdentifier oidName undefined: " + t;
                this.setValueOidString(e)
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
            ,
        void 0 !== t && ("string" == typeof t ? t.match(/^[0-2].[0-9.]+$/) ? this.setValueOidString(t) : this.setValueName(t) : void 0 !== t.oid ? this.setValueOidString(t.oid) : void 0 !== t.hex ? this.setValueHex(t.hex) : void 0 !== t.name && this.setValueName(t.name))
    }
    ,
    nt.lang.extend(it.asn1.DERObjectIdentifier, it.asn1.ASN1Object),
    it.asn1.DEREnumerated = function (t) {
        it.asn1.DEREnumerated.superclass.constructor.call(this),
            this.hT = "0a",
            this.setByBigInteger = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.hV = it.asn1.ASN1Util.bigIntToMinTwosComplementsHex(t)
            }
            ,
            this.setByInteger = function (t) {
                var e = new $(String(t), 10);
                this.setByBigInteger(e)
            }
            ,
            this.setValueHex = function (t) {
                this.hV = t
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
            ,
        void 0 !== t && (void 0 !== t.int ? this.setByInteger(t.int) : "number" == typeof t ? this.setByInteger(t) : void 0 !== t.hex && this.setValueHex(t.hex))
    }
    ,
    nt.lang.extend(it.asn1.DEREnumerated, it.asn1.ASN1Object),
    it.asn1.DERUTF8String = function (t) {
        it.asn1.DERUTF8String.superclass.constructor.call(this, t),
            this.hT = "0c"
    }
    ,
    nt.lang.extend(it.asn1.DERUTF8String, it.asn1.DERAbstractString),
    it.asn1.DERNumericString = function (t) {
        it.asn1.DERNumericString.superclass.constructor.call(this, t),
            this.hT = "12"
    }
    ,
    nt.lang.extend(it.asn1.DERNumericString, it.asn1.DERAbstractString),
    it.asn1.DERPrintableString = function (t) {
        it.asn1.DERPrintableString.superclass.constructor.call(this, t),
            this.hT = "13"
    }
    ,
    nt.lang.extend(it.asn1.DERPrintableString, it.asn1.DERAbstractString),
    it.asn1.DERTeletexString = function (t) {
        it.asn1.DERTeletexString.superclass.constructor.call(this, t),
            this.hT = "14"
    }
    ,
    nt.lang.extend(it.asn1.DERTeletexString, it.asn1.DERAbstractString),
    it.asn1.DERIA5String = function (t) {
        it.asn1.DERIA5String.superclass.constructor.call(this, t),
            this.hT = "16"
    }
    ,
    nt.lang.extend(it.asn1.DERIA5String, it.asn1.DERAbstractString),
    it.asn1.DERUTCTime = function (t) {
        it.asn1.DERUTCTime.superclass.constructor.call(this, t),
            this.hT = "17",
            this.setByDate = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.date = t,
                    this.s = this.formatDate(this.date, "utc"),
                    this.hV = stohex(this.s)
            }
            ,
            this.getFreshValueHex = function () {
                return void 0 === this.date && void 0 === this.s && (this.date = new Date,
                    this.s = this.formatDate(this.date, "utc"),
                    this.hV = stohex(this.s)),
                    this.hV
            }
            ,
        void 0 !== t && (void 0 !== t.str ? this.setString(t.str) : "string" == typeof t && t.match(/^[0-9]{12}Z$/) ? this.setString(t) : void 0 !== t.hex ? this.setStringHex(t.hex) : void 0 !== t.date && this.setByDate(t.date))
    }
    ,
    nt.lang.extend(it.asn1.DERUTCTime, it.asn1.DERAbstractTime),
    it.asn1.DERGeneralizedTime = function (t) {
        it.asn1.DERGeneralizedTime.superclass.constructor.call(this, t),
            this.hT = "18",
            this.withMillis = !1,
            this.setByDate = function (t) {
                this.hTLV = null,
                    this.isModified = !0,
                    this.date = t,
                    this.s = this.formatDate(this.date, "gen", this.withMillis),
                    this.hV = stohex(this.s)
            }
            ,
            this.getFreshValueHex = function () {
                return void 0 === this.date && void 0 === this.s && (this.date = new Date,
                    this.s = this.formatDate(this.date, "gen", this.withMillis),
                    this.hV = stohex(this.s)),
                    this.hV
            }
            ,
        void 0 !== t && (void 0 !== t.str ? this.setString(t.str) : "string" == typeof t && t.match(/^[0-9]{14}Z$/) ? this.setString(t) : void 0 !== t.hex ? this.setStringHex(t.hex) : void 0 !== t.date && this.setByDate(t.date),
        !0 === t.millis && (this.withMillis = !0))
    }
    ,
    nt.lang.extend(it.asn1.DERGeneralizedTime, it.asn1.DERAbstractTime),
    it.asn1.DERSequence = function (t) {
        it.asn1.DERSequence.superclass.constructor.call(this, t),
            this.hT = "30",
            this.getFreshValueHex = function () {
                for (var t = "", e = 0; e < this.asn1Array.length; e++) {
                    t += this.asn1Array[e].getEncodedHex()
                }
                return this.hV = t,
                    this.hV
            }
    }
    ,
    nt.lang.extend(it.asn1.DERSequence, it.asn1.DERAbstractStructured),
    it.asn1.DERSet = function (t) {
        it.asn1.DERSet.superclass.constructor.call(this, t),
            this.hT = "31",
            this.sortFlag = !0,
            this.getFreshValueHex = function () {
                for (var t = new Array, e = 0; e < this.asn1Array.length; e++) {
                    var n = this.asn1Array[e];
                    t.push(n.getEncodedHex())
                }
                return 1 == this.sortFlag && t.sort(),
                    this.hV = t.join(""),
                    this.hV
            }
            ,
        void 0 !== t && void 0 !== t.sortflag && 0 == t.sortflag && (this.sortFlag = !1)
    }
    ,
    nt.lang.extend(it.asn1.DERSet, it.asn1.DERAbstractStructured),
    it.asn1.DERTaggedObject = function (t) {
        it.asn1.DERTaggedObject.superclass.constructor.call(this),
            this.hT = "a0",
            this.hV = "",
            this.isExplicit = !0,
            this.asn1Object = null,
            this.setASN1Object = function (t, e, n) {
                this.hT = e,
                    this.isExplicit = t,
                    this.asn1Object = n,
                    this.isExplicit ? (this.hV = this.asn1Object.getEncodedHex(),
                        this.hTLV = null,
                        this.isModified = !0) : (this.hV = null,
                        this.hTLV = n.getEncodedHex(),
                        this.hTLV = this.hTLV.replace(/^../, e),
                        this.isModified = !1)
            }
            ,
            this.getFreshValueHex = function () {
                return this.hV
            }
            ,
        void 0 !== t && (void 0 !== t.tag && (this.hT = t.tag),
        void 0 !== t.explicit && (this.isExplicit = t.explicit),
        void 0 !== t.obj && (this.asn1Object = t.obj,
            this.setASN1Object(this.isExplicit, this.hT, this.asn1Object)))
    }
    ,
    nt.lang.extend(it.asn1.DERTaggedObject, it.asn1.ASN1Object);
var rt, ot = (rt = function (t, e) {
        return rt = Object.setPrototypeOf || {
                __proto__: []
            } instanceof Array && function (t, e) {
                t.__proto__ = e
            }
            || function (t, e) {
                for (var n in e)
                    Object.prototype.hasOwnProperty.call(e, n) && (t[n] = e[n])
            }
            ,
            rt(t, e)
    }
        ,
        function (t, e) {
            if ("function" != typeof e && null !== e)
                throw new TypeError("Class extends value " + String(e) + " is not a constructor or null");

            function n() {
                this.constructor = t
            }

            rt(t, e),
                t.prototype = null === e ? Object.create(e) : (n.prototype = e.prototype,
                    new n)
        }
), st = function (t) {
    function e(n) {
        var i = t.call(this) || this;
        return n && ("string" == typeof n ? i.parseKey(n) : (e.hasPrivateKeyProperty(n) || e.hasPublicKeyProperty(n)) && i.parsePropertiesFrom(n)),
            i
    }

    return ot(e, t),
        e.prototype.parseKey = function (t) {
            try {
                var e = 0
                    , n = 0
                    , i = /^\s*(?:[0-9A-Fa-f][0-9A-Fa-f]\s*)+$/.test(t) ? g(t) : b.unarmor(t)
                    , r = k.decode(i);
                if (3 === r.sub.length && (r = r.sub[2].sub[0]),
                9 === r.sub.length) {
                    e = r.sub[1].getHexStringValue(),
                        this.n = M(e, 16),
                        n = r.sub[2].getHexStringValue(),
                        this.e = parseInt(n, 16);
                    var o = r.sub[3].getHexStringValue();
                    this.d = M(o, 16);
                    var s = r.sub[4].getHexStringValue();
                    this.p = M(s, 16);
                    var a = r.sub[5].getHexStringValue();
                    this.q = M(a, 16);
                    var l = r.sub[6].getHexStringValue();
                    this.dmp1 = M(l, 16);
                    var c = r.sub[7].getHexStringValue();
                    this.dmq1 = M(c, 16);
                    var u = r.sub[8].getHexStringValue();
                    this.coeff = M(u, 16)
                } else {
                    if (2 !== r.sub.length)
                        return !1;
                    var h = r.sub[1].sub[0];
                    e = h.sub[0].getHexStringValue(),
                        this.n = M(e, 16),
                        n = h.sub[1].getHexStringValue(),
                        this.e = parseInt(n, 16)
                }
                return !0
            } catch (d) {
                return !1
            }
        }
        ,
        e.prototype.getPrivateBaseKey = function () {
            var t = {
                array: [new it.asn1.DERInteger({
                    int: 0
                }), new it.asn1.DERInteger({
                    bigint: this.n
                }), new it.asn1.DERInteger({
                    int: this.e
                }), new it.asn1.DERInteger({
                    bigint: this.d
                }), new it.asn1.DERInteger({
                    bigint: this.p
                }), new it.asn1.DERInteger({
                    bigint: this.q
                }), new it.asn1.DERInteger({
                    bigint: this.dmp1
                }), new it.asn1.DERInteger({
                    bigint: this.dmq1
                }), new it.asn1.DERInteger({
                    bigint: this.coeff
                })]
            };
            return new it.asn1.DERSequence(t).getEncodedHex()
        }
        ,
        e.prototype.getPrivateBaseKeyB64 = function () {
            return p(this.getPrivateBaseKey())
        }
        ,
        e.prototype.getPublicBaseKey = function () {
            var t = new it.asn1.DERSequence({
                array: [new it.asn1.DERObjectIdentifier({
                    oid: "1.2.840.113549.1.1.1"
                }), new it.asn1.DERNull]
            })
                , e = new it.asn1.DERSequence({
                array: [new it.asn1.DERInteger({
                    bigint: this.n
                }), new it.asn1.DERInteger({
                    int: this.e
                })]
            })
                , n = new it.asn1.DERBitString({
                hex: "00" + e.getEncodedHex()
            });
            return new it.asn1.DERSequence({
                array: [t, n]
            }).getEncodedHex()
        }
        ,
        e.prototype.getPublicBaseKeyB64 = function () {
            return p(this.getPublicBaseKey())
        }
        ,
        e.wordwrap = function (t, e) {
            if (!t)
                return t;
            var n = "(.{1," + (e = e || 64) + "})( +|$\n?)|(.{1," + e + "})";
            return t.match(RegExp(n, "g")).join("\n")
        }
        ,
        e.prototype.getPrivateKey = function () {
            var t = "-----BEGIN RSA PRIVATE KEY-----\n";
            return t += e.wordwrap(this.getPrivateBaseKeyB64()) + "\n",
                t += "-----END RSA PRIVATE KEY-----"
        }
        ,
        e.prototype.getPublicKey = function () {
            var t = "-----BEGIN PUBLIC KEY-----\n";
            return t += e.wordwrap(this.getPublicBaseKeyB64()) + "\n",
                t += "-----END PUBLIC KEY-----"
        }
        ,
        e.hasPublicKeyProperty = function (t) {
            return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e")
        }
        ,
        e.hasPrivateKeyProperty = function (t) {
            return (t = t || {}).hasOwnProperty("n") && t.hasOwnProperty("e") && t.hasOwnProperty("d") && t.hasOwnProperty("p") && t.hasOwnProperty("q") && t.hasOwnProperty("dmp1") && t.hasOwnProperty("dmq1") && t.hasOwnProperty("coeff")
        }
        ,
        e.prototype.parsePropertiesFrom = function (t) {
            this.n = t.n,
                this.e = t.e,
            t.hasOwnProperty("d") && (this.d = t.d,
                this.p = t.p,
                this.q = t.q,
                this.dmp1 = t.dmp1,
                this.dmq1 = t.dmq1,
                this.coeff = t.coeff)
        }
        ,
        e
}(tt), at = "3.2.1", lt = function () {
    function t(t) {
        void 0 === t && (t = {}),
            t = t || {},
            this.default_key_size = t.default_key_size ? parseInt(t.default_key_size, 10) : 1024,
            this.default_public_exponent = t.default_public_exponent || "010001",
            this.log = t.log || !1,
            this.key = null
    }

    return t.prototype.setKey = function (t) {
        this.log && this.key,
            this.key = new st(t)
    }
        ,
        t.prototype.setPrivateKey = function (t) {
            this.setKey(t)
        }
        ,
        t.prototype.setPublicKey = function (t) {
            this.setKey(t)
        }
        ,
        t.prototype.decrypt = function (t) {
            try {
                return this.getKey().decrypt(v(t))
            } catch (e) {
                return !1
            }
        }
        ,
        t.prototype.encrypt = function (t) {
            try {
                return p(this.getKey().encrypt(t))
            } catch (e) {
                return !1
            }
        }
        ,
        t.prototype.sign = function (t, e, n) {
            try {
                return p(this.getKey().sign(t, e, n))
            } catch (i) {
                return !1
            }
        }
        ,
        t.prototype.verify = function (t, e, n) {
            try {
                return this.getKey().verify(t, v(e), n)
            } catch (i) {
                return !1
            }
        }
        ,
        t.prototype.getKey = function (t) {
            if (!this.key) {
                if (this.key = new st,
                t && "[object Function]" === {}.toString.call(t))
                    return void this.key.generateAsync(this.default_key_size, this.default_public_exponent, t);
                this.key.generate(this.default_key_size, this.default_public_exponent)
            }
            return this.key
        }
        ,
        t.prototype.getPrivateKey = function () {
            return this.getKey().getPrivateKey()
        }
        ,
        t.prototype.getPrivateKeyB64 = function () {
            return this.getKey().getPrivateBaseKeyB64()
        }
        ,
        t.prototype.getPublicKey = function () {
            return this.getKey().getPublicKey()
        }
        ,
        t.prototype.getPublicKeyB64 = function () {
            return this.getKey().getPublicBaseKeyB64()
        }
        ,
        t.version = at.version,
        t
}();

function ct() {
    return function (t) {
        t = t || 32;
        let e = "abcdefhijkmnprstwxyz123456789"
            , n = e.length
            , i = "";
        for (let r = 0; r < t; r++)
            i += e.charAt(Math.floor(Math.random() * n));
        return i
    }(16)
}

function ut(t) {
    let e = new lt;
    return e.setPublicKey("MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDWMfZFtPVyDiYTVSqbNm8i4xjb\n4RVsveiUzTHaGIHRO2EXnn8GGOqofbQK+XCmY1SxNJhkh4iXY6wSTa3JFe27zG3f\n3o2BsWj/kX65s2TBHMKkOZ5qhko/9DVSKvK2VO7isT3p3V5TavrQgDp/brs5mnhH\nGCtNsOB1cAj4PPCT/QIDAQAB"),
    e.encrypt(t) || ""
}

function uut(t) {
    let e = new lt;
    return e.setPrivateKey("MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBANjLpuUMXeXll0L2\nqd/GaQWlpk3YtgmNGdZZzlgPREMLXoem9QJXH4F3RW8tD7hrurZZxCGmvaK+XNKd\n6TZlUZV0SG8VNDzoZGm2LOFI8M+DcHKjVXItUZWGPQeK/9mwZ6XVbMXG5wcpAtvf\nHc8gx8D0FsLA+gIP5tkLvGW4UpTnAgMBAAECgYAs+NoPK6iS1zSwnHCSzhrdJAbC\noVDp3E5ey9RlKg2UBti+NSEgMiiD99T8ghF/xUE/MJHiFS/Dgc/JlR5avVvVzkDK\n0bqY08iCdBHzw9l7ftzcgAg3Pq/kYg1bSecwX/+eSkSy9CKFlMa5K1ElbkfWIIT8\nr79hrYSTj92IKC4BEQJBAO6oakxkEBY5kmQXXmZaJd/+lxlFzf0rBENK07765Tu1\npex2iGPkJbcAx9z4p1q2SUYIt1B3xnVxqdmDIUcdvSkCQQDojIvwiaAwH/2ER0Ox\nn+u1QGu54IDm0oHIr1Q31WJKU7D5kg6/MjnKzopM7wqY6GP+0Qe3T1hNh9Mze8t/\n6POPAkAwjKozKBftrYCORAK8J5KU4qGyTnT9D4cqeUpiC4AeiXFbjTFpwLu7YrlF\nxn+lAHgfex5vjC4fLiQzT22xnechAkEAyXrD3/KNjESbNJk96E5jPNWEwDXn2JS4\nB3UIpZtGHpmmMoS+LB9K/RC3uHI/Hz3xLRxT8BlZq0qrzOZL6RWetwJALTr7sZvI\nmpZRPC+VADx4wn8E2t02459wr6zFyqF0WRnel3OF5bAIpDZNoDoA7gCCwmtU293l\npc6uixENXcmW5g=="),
    e.decrypt(t) || ""
}

function ht(t) {
    try {
        const e = ct();
        return {
            data: function (t, e) {
                let n = {
                    mode: r.a.mode.ECB,
                    padding: r.a.pad.Pkcs7
                }
                    , i = r.a.enc.Utf8.parse(e)
                    , o = r.a.AES.encrypt(t, i, n).toString().replace(/\//g, "_");
                return o = o.replace(/\+/g, "-"),
                    o
            }(JSON.stringify(t), e),
            encryptkey: ut(e)
        }
    } catch (e) {
        return !1
    }
}

function dt(t, e) {
    try {
        if (!t || !e)
            return !1;
        const n = function (t, e) {
            let n = t.replace(/\-/g, "+").replace(/_/g, "/")
                , i = {
                mode: r.a.mode.ECB,
                padding: r.a.pad.Pkcs7
            }
                , o = r.a.enc.Utf8.parse(e)
                , s = r.a.AES.decrypt(n, o, i);
            return r.a.enc.Utf8.stringify(s)
        }(t, function (t) {
            let e = new lt;
            return e.setPrivateKey("MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBANjLpuUMXeXll0L2\nqd/GaQWlpk3YtgmNGdZZzlgPREMLXoem9QJXH4F3RW8tD7hrurZZxCGmvaK+XNKd\n6TZlUZV0SG8VNDzoZGm2LOFI8M+DcHKjVXItUZWGPQeK/9mwZ6XVbMXG5wcpAtvf\nHc8gx8D0FsLA+gIP5tkLvGW4UpTnAgMBAAECgYAs+NoPK6iS1zSwnHCSzhrdJAbC\noVDp3E5ey9RlKg2UBti+NSEgMiiD99T8ghF/xUE/MJHiFS/Dgc/JlR5avVvVzkDK\n0bqY08iCdBHzw9l7ftzcgAg3Pq/kYg1bSecwX/+eSkSy9CKFlMa5K1ElbkfWIIT8\nr79hrYSTj92IKC4BEQJBAO6oakxkEBY5kmQXXmZaJd/+lxlFzf0rBENK07765Tu1\npex2iGPkJbcAx9z4p1q2SUYIt1B3xnVxqdmDIUcdvSkCQQDojIvwiaAwH/2ER0Ox\nn+u1QGu54IDm0oHIr1Q31WJKU7D5kg6/MjnKzopM7wqY6GP+0Qe3T1hNh9Mze8t/\n6POPAkAwjKozKBftrYCORAK8J5KU4qGyTnT9D4cqeUpiC4AeiXFbjTFpwLu7YrlF\nxn+lAHgfex5vjC4fLiQzT22xnechAkEAyXrD3/KNjESbNJk96E5jPNWEwDXn2JS4\nB3UIpZtGHpmmMoS+LB9K/RC3uHI/Hz3xLRxT8BlZq0qrzOZL6RWetwJALTr7sZvI\nmpZRPC+VADx4wn8E2t02459wr6zFyqF0WRnel3OF5bAIpDZNoDoA7gCCwmtU293l\npc6uixENXcmW5g=="),
            e.decrypt(t) || ""
        }(e));
        return JSON.parse(n || "{}")
    } catch (n) {
        return !1
    }
}

src = function (data, key) {
    key = CryptoJS.enc.Utf8.parse(key)
    encryptedData = CryptoJS.AES.encrypt(data, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    encryptedData = encryptedData.toString()
    encryptedData = encryptedData.replace(/\//g, "_")
    return encryptedData.replace(/\+/g, "-"), encryptedData
}
dec = function (data, key) {
    data = data.replace(/\-/g, "+").replace(/_/g, "/")
    key = CryptoJS.enc.Utf8.parse(key)
    decryptedData = CryptoJS.AES.decrypt(data, key, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    })
    decryptedData = decryptedData.toString(CryptoJS.enc.Utf8)
    return decryptedData
}

function get_key_and_encryptKey(ssss) {
    key = ct();     // "abcdefhijkmnprstwxyz123456789" 随机16选一
    // key = '993i6hxki49kci49'
    encryptkey = src(ssss, key)
    encryptdata = ut(key);
    data = {
        'data': encryptkey,
        'encryptKey': encryptdata
    }
    return JSON.stringify(data);

}

// out = get_key_and_encryptKey(ssss = '"{}"')
// console.log(out)


// data="Px7bVOLg8uAVWLArC7fPYVKzOkGaAT8OzeCtR8KinMGUS+X6/CPARAzWkxF/1abpd7uESleP30M7C/mhpyXT5gR6ZtIghTCr1H+lojxI/m8heUNMOY665qbvNMtZ9CewlqomVFrg+ne3dpk8NSgAjZYsmSBsRYLN9m/GTVS7vU1Ol1Dm0V936KNV7KfQT07OmZSMPZne9BXDkNW0RTfDqC5VcDWOnaihnmsgf7lix5em6l+JlbH/B1hJFfW85r5ZG8nBDbrobmYqT870n+6Ry/r5JcYgAvm1z473rq3cZV26NfhttwPF6KwXalyxTbLdHmB6NAHB2QTaU5eMBY0MS/8fn0nUxP+WWRSiWR2SuYf+uR0BSXrwAt5hXbEJvZA3ZwYwGUnGqzXMdZLE0tEINYRxPKZ2dBFaGYT5deqGesA1sj8+gR5ptH00GS2NGD9F6OjIzZXZfdzqz4RRYg2mGaBFacB2tfRgu1Um0wTedOxvT+ebasd/juvgAKUHSgr0GZ1lzWP70aZ9XgCZ9dyX5KEqRBkxdYmXLth1PG0PayEiRKMKQsGohc0js8rGiMg8vd3R/z61i8BBy3VvnYwFGhGQsUlTkrMamozxWQibPDhwLNuT8UKnXkppooTtxKnwB6Onypkk9yBMcHacnmiT/YqKXAhokQiGREFqVFKCm3/+u3etio0pjN4AOMogq1tG2QfDfwb5b3q2dTgHScgo9OVabpMM99Z3UW/0Gjqm2dMuOhhiICFl0LTCb9ZcaDEkldCOEfSlMz5x2tETTPmJIgUOoz2wIsxyI0y/C8ubY36RLWWkJqyPesknf4sczgMhdFU/Q13zeIHFOihEayON7VVrTe6PndgNXQg8fZXQh2gheUNMOY665qbvNMtZ9CewlqomVFrg+ne3dpk8NSgAjZ4AO5j25FtnzknsAzN7FFC9VOl+mOOk7WWuwF7QtQsGpQYzeYcYCwPQBp2I0ylQxDrxhS2QLIB8mhzzo5vRpEGdTMQ8Ctp4SpWDNj4c3Gmxoze7DQXdxGcloktJyMMrbJdspB7yxX6d5pzUOXshWMSDCpuR8AdY2n1j6gc9h1PFBQ7CtvoNPj+g35qJE8XYEF2RU+Q8d3Ie5swZlWMRk83l2Wh6kbqd9wYhancra5tHhzeB4V94452Nn0f0+nCfRtA8NEbq262Yfjc+MQYfFaRyNW79FMZEud1p8wVd/ldowzgB/yfuiRnBjxEU+Iqu1RPPCCz4e45cqNOqp4Hc8mXHzF6m4tccT7L3Aq6nX/d2xJCYjJojGAuo3OBeV0I14l09JCfvc/Zb5PL2SWxXNmwYdFpXJhjcey7dmbUI/CtlOUpTdDPKX/AhGbo0uSy8hGi1mT16lsl8uOs5UBfN29vPWAoyIMJhQP8luqpAHbV308/VCuoWD4HqPJsPee3UrTuwDVNfZA7qGadx4jrikWLuzp1f3R0HO7NYCqfMXqFUAGETFYnY9uP6zFdovqZ6TjZvknw32QhX0okt+E4+WJHSSMkzocWb7xOpHEKgO62GFRfTJGwycJfNkft0nRaCrqyJY8rckg4LdRlI6v76UhMs4VgCxnJgeV6sDkZ8gzHU4v6f+1XC6xX9jIA8t5l2bBs4AuxztAhjl+0EYVdWNXHhX28qMYm+OnlZAdsOYN5SYZBHCJTzx+j0Fy3Yg6FMCltWIp//7XUbqDyDdYTY57qhZSosYrqglMP9pcUFn8U4zAu6pC52F2kU+Yxi/u9M0Xv7o8mmSI7OT/0acWUQD1M9QPI6mGVxnr1eWRTeIx9quNCLZNU/qVyT8qqPmnwPRg=="
// encryptKey="jKkK+bJ7xXNwHnFh/EhBUoIk+fP8nTouTOWfs1F3ncG6kp36zjBJCkFa2TAZrZJnDpiJGt4T+xWpown7nDbOaPs7vwguI6fj39YBC7xkGJ4nSk8/eyxC9m+KSXR/HAw0ha2nXjgin/ikQkea0K0WbTUyKL6k064RIEBoEKYooNE="
// console.log(uut(encryptKey))
// console.log(dec(data, uut(encryptKey)))
// console.log(JSON.stringify(dec(data, uut(encryptKey))))


// data = process.argv[2];
// encryptKey = process.argv[3];
// console.log(dec(data, uut(encryptKey)))


// url = "https://gcaptcha4.geetest.com/load?captcha_id=32727fa8d208a82e46754c2e5055a679&challenge=34f8a9a4-eef4-4428-bc52-7e69555c803e&client_type=web&lang=zh-cn&callback=geetest_1668848675048"
// var uuid = function () {
//     return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function (c) {
//         var r = Math.random() * 16 | 0;
//         var v = c === 'x' ? r : (r & 0x3 | 0x8);
//         return v.toString(16);
//     });
// };
// callback = "geetest_" + (parseInt(Math.random() * 10000) + (new Date()).valueOf());
// console.log(uuid(), callback) // challenge参数


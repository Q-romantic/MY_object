// nn = [
//     function () {
//         n(1)(8)
//         console.log(123)
//
//     },
//     function (b) {
//         console.log(b)
//         return b
//     }
// ]
//
// window = this;
// var r = {}
//
// !function (i) {
//     function p(e) {
//         if (r[e])
//             return r[e].exports;
//         var t = r[e] = {
//             i: e,
//             l: !1,
//             exports: {}
//         };
//         return i[e].call(t.exports, t, t.exports, p),
//             t.l = !0,
//             t.exports
//     }
//
//     return p.m = i, window.xxx = p, p
// }(nn)
//
//
// n = function (i) {
//     return nn[i]
// }
// // console.log(nn[0]())
// // console.log(window.xxx(1))
// e = {}
// e.exports = function () {
//     function x() {
//         if (!(this instanceof x))
//             return new x();
//     }
//
//     return x.prototype.a = function (xxx) {
//         return xxx
//     },
//         x.prototype.b = function (xxx) {
//             return xxx
//         }
// }()
//
// console.log(e.exports.x.toString())
//
//


function W(e, t, n, r) {
    for (var i = 0; i < r && !(i + n >= t.length || i >= e.length); ++i)
        t[i + n] = e[i];
    return i
}

function H(e, t) {
    var n;
    t = t || 1 / 0;
    for (var r = e.length, i = null, a = [], o = 0; o < r; ++o) {
        if ((n = e.charCodeAt(o)) > 55295 && n < 57344) {
            if (!i) {
                if (n > 56319) {
                    (t -= 3) > -1 && a.push(239, 191, 189);
                    continue
                }
                if (o + 1 === r) {
                    (t -= 3) > -1 && a.push(239, 191, 189);
                    continue
                }
                i = n;
                continue
            }
            if (n < 56320) {
                (t -= 3) > -1 && a.push(239, 191, 189),
                    i = n;
                continue
            }
            n = 65536 + (i - 55296 << 10 | n - 56320)
        } else
            i && (t -= 3) > -1 && a.push(239, 191, 189);
        if (i = null,
        n < 128) {
            if ((t -= 1) < 0)
                break;
            a.push(n)
        } else if (n < 2048) {
            if ((t -= 2) < 0)
                break;
            a.push(n >> 6 | 192, 63 & n | 128)
        } else if (n < 65536) {
            if ((t -= 3) < 0)
                break;
            a.push(n >> 12 | 224, n >> 6 & 63 | 128, 63 & n | 128)
        } else {
            if (!(n < 1114112))
                throw new Error("Invalid code point");
            if ((t -= 4) < 0)
                break;
            a.push(n >> 18 | 240, n >> 12 & 63 | 128, n >> 6 & 63 | 128, 63 & n | 128)
        }
    }
    return a
}

function o() {
    return u.TYPED_ARRAY_SUPPORT ? 2147483647 : 1073741823
}

function s(e, t) {
    if (o() < t)
        throw new RangeError("Invalid typed array length");
    return u.TYPED_ARRAY_SUPPORT ? (e = new Uint8Array(t)).__proto__ = u.prototype : (null === e && (e = new u(t)),
        e.length = t),
        e
}

function u(e, t, n) {
    if (!(u.TYPED_ARRAY_SUPPORT || this instanceof u))
        return new u(e, t, n);
    if ("number" == typeof e) {
        if ("string" == typeof t)
            throw new Error("If encoding is specified then the first argument must be a string");
        return A(this, e)
    }
    return c(this, e, t, n)
}

function c(e, t, n, r) {
    if ("number" == typeof t)
        throw new TypeError('"value" argument must not be a number');
    return "undefined" != typeof ArrayBuffer && t instanceof ArrayBuffer ? function (e, t, n, r) {
        if (t.byteLength,
        n < 0 || t.byteLength < n)
            throw new RangeError("'offset' is out of bounds");
        if (t.byteLength < n + (r || 0))
            throw new RangeError("'length' is out of bounds");
        return t = void 0 === n && void 0 === r ? new Uint8Array(t) : void 0 === r ? new Uint8Array(t, n) : new Uint8Array(t, n, r),
            u.TYPED_ARRAY_SUPPORT ? (e = t).__proto__ = u.prototype : e = d(e, t),
            e
    }(e, t, n, r) : "string" == typeof t ? function (e, t, n) {
        if ("string" == typeof n && "" !== n || (n = "utf8"),
            !u.isEncoding(n))
            throw new TypeError('"encoding" must be a valid string encoding');
        var r = 0 | h(t, n)
            , i = (e = s(e, r)).write(t, n);
        return i !== r && (e = e.slice(0, i)),
            e
    }(e, t, n) : function (e, t) {
        if (u.isBuffer(t)) {
            var n = 0 | f(t.length);
            return 0 === (e = s(e, n)).length ? e : (t.copy(e, 0, 0, n),
                e)
        }
        if (t) {
            if ("undefined" != typeof ArrayBuffer && t.buffer instanceof ArrayBuffer || "length" in t)
                return "number" != typeof t.length || (r = t.length) != r ? s(e, 0) : d(e, t);
            if ("Buffer" === t.type && a(t.data))
                return d(e, t.data)
        }
        var r;
        throw new TypeError("First argument must be a string, Buffer, ArrayBuffer, Array, or array-like object.")
    }(e, t)
}

function l(e) {
    if ("number" != typeof e)
        throw new TypeError('"size" argument must be a number');
    if (e < 0)
        throw new RangeError('"size" argument must not be negative')
}

function A(e, t) {
    if (l(t),
        e = s(e, t < 0 ? 0 : 0 | f(t)),
        !u.TYPED_ARRAY_SUPPORT)
        for (var n = 0; n < t; ++n)
            e[n] = 0;
    return e
}

function d(e, t) {
    var n = t.length < 0 ? 0 : 0 | f(t.length);
    e = s(e, n);
    for (var r = 0; r < n; r += 1)
        e[r] = 255 & t[r];
    return e
}

function f(e) {
    if (e >= o())
        throw new RangeError("Attempt to allocate Buffer larger than maximum size: 0x" + o().toString(16) + " bytes");
    return 0 | e
}

function h(e, t) {
    if (u.isBuffer(e))
        return e.length;
    if ("undefined" != typeof ArrayBuffer && "function" == typeof ArrayBuffer.isView && (ArrayBuffer.isView(e) || e instanceof ArrayBuffer))
        return e.byteLength;
    "string" != typeof e && (e = "" + e);
    var n = e.length;
    if (0 === n)
        return 0;
    for (var r = !1; ;)
        switch (t) {
            case "ascii":
            case "latin1":
            case "binary":
                return n;
            case "utf8":
            case "utf-8":
            case void 0:
                return H(e).length;
            case "ucs2":
            case "ucs-2":
            case "utf16le":
            case "utf-16le":
                return 2 * n;
            case "hex":
                return n >>> 1;
            case "base64":
                return R(e).length;
            default:
                if (r)
                    return H(e).length;
                t = ("" + t).toLowerCase(),
                    r = !0
        }
}

function p(e, t, n) {
    var r = !1;
    if ((void 0 === t || t < 0) && (t = 0),
    t > this.length)
        return "";
    if ((void 0 === n || n > this.length) && (n = this.length),
    n <= 0)
        return "";
    if ((n >>>= 0) <= (t >>>= 0))
        return "";
    for (e || (e = "utf8"); ;)
        switch (e) {
            case "hex":
                return j(this, t, n);
            case "utf8":
            case "utf-8":
                return _(this, t, n);
            case "ascii":
                return S(this, t, n);
            case "latin1":
            case "binary":
                return x(this, t, n);
            case "base64":
                return E(this, t, n);
            case "ucs2":
            case "ucs-2":
            case "utf16le":
            case "utf-16le":
                return M(this, t, n);
            default:
                if (r)
                    throw new TypeError("Unknown encoding: " + e);
                e = (e + "").toLowerCase(),
                    r = !0
        }
}

function m(e, t, n) {
    var r = e[t];
    e[t] = e[n],
        e[n] = r
}

function g(e, t, n, r, i) {
    if (0 === e.length)
        return -1;
    if ("string" == typeof n ? (r = n,
        n = 0) : n > 2147483647 ? n = 2147483647 : n < -2147483648 && (n = -2147483648),
        n = +n,
    isNaN(n) && (n = i ? 0 : e.length - 1),
    n < 0 && (n = e.length + n),
    n >= e.length) {
        if (i)
            return -1;
        n = e.length - 1
    } else if (n < 0) {
        if (!i)
            return -1;
        n = 0
    }
    if ("string" == typeof t && (t = u.from(t, r)),
        u.isBuffer(t))
        return 0 === t.length ? -1 : b(e, t, n, r, i);
    if ("number" == typeof t)
        return t &= 255,
            u.TYPED_ARRAY_SUPPORT && "function" == typeof Uint8Array.prototype.indexOf ? i ? Uint8Array.prototype.indexOf.call(e, t, n) : Uint8Array.prototype.lastIndexOf.call(e, t, n) : b(e, [t], n, r, i);
    throw new TypeError("val must be string, number or Buffer")
}

function b(e, t, n, r, i) {
    var a, o = 1, s = e.length, u = t.length;
    if (void 0 !== r && ("ucs2" === (r = String(r).toLowerCase()) || "ucs-2" === r || "utf16le" === r || "utf-16le" === r)) {
        if (e.length < 2 || t.length < 2)
            return -1;
        o = 2,
            s /= 2,
            u /= 2,
            n /= 2
    }

    function c(e, t) {
        return 1 === o ? e[t] : e.readUInt16BE(t * o)
    }

    if (i) {
        var l = -1;
        for (a = n; a < s; a++)
            if (c(e, a) === c(t, -1 === l ? 0 : a - l)) {
                if (-1 === l && (l = a),
                a - l + 1 === u)
                    return l * o
            } else
                -1 !== l && (a -= a - l),
                    l = -1
    } else
        for (n + u > s && (n = s - u),
                 a = n; a >= 0; a--) {
            for (var A = !0, d = 0; d < u; d++)
                if (c(e, a + d) !== c(t, d)) {
                    A = !1;
                    break
                }
            if (A)
                return a
        }
    return -1
}

function v(e, t, n, r) {
    n = Number(n) || 0;
    var i = e.length - n;
    r ? (r = Number(r)) > i && (r = i) : r = i;
    var a = t.length;
    if (a % 2 != 0)
        throw new TypeError("Invalid hex string");
    r > a / 2 && (r = a / 2);
    for (var o = 0; o < r; ++o) {
        var s = parseInt(t.substr(2 * o, 2), 16);
        if (isNaN(s))
            return o;
        e[n + o] = s
    }
    return o
}

function y(e, t, n, r) {
    return W(H(t, e.length - n), e, n, r)
}

function w(e, t, n, r) {
    return W(function (e) {
        for (var t = [], n = 0; n < e.length; ++n)
            t.push(255 & e.charCodeAt(n));
        return t
    }(t), e, n, r)
}

function B(e, t, n, r) {
    return w(e, t, n, r)
}

function O(e, t, n, r) {
    return W(R(t), e, n, r)
}

function C(e, t, n, r) {
    return W(function (e, t) {
        for (var n, r, i, a = [], o = 0; o < e.length && !((t -= 2) < 0); ++o)
            r = (n = e.charCodeAt(o)) >> 8,
                i = n % 256,
                a.push(i),
                a.push(r);
        return a
    }(t, e.length - n), e, n, r)
}

function E(e, t, n) {
    return 0 === t && n === e.length ? r.fromByteArray(e) : r.fromByteArray(e.slice(t, n))
}

function _(e, t, n) {
    n = Math.min(e.length, n);
    for (var r = [], i = t; i < n;) {
        var a, o, s, u, c = e[i], l = null, A = c > 239 ? 4 : c > 223 ? 3 : c > 191 ? 2 : 1;
        if (i + A <= n)
            switch (A) {
                case 1:
                    c < 128 && (l = c);
                    break;
                case 2:
                    128 == (192 & (a = e[i + 1])) && (u = (31 & c) << 6 | 63 & a) > 127 && (l = u);
                    break;
                case 3:
                    a = e[i + 1],
                        o = e[i + 2],
                    128 == (192 & a) && 128 == (192 & o) && (u = (15 & c) << 12 | (63 & a) << 6 | 63 & o) > 2047 && (u < 55296 || u > 57343) && (l = u);
                    break;
                case 4:
                    a = e[i + 1],
                        o = e[i + 2],
                        s = e[i + 3],
                    128 == (192 & a) && 128 == (192 & o) && 128 == (192 & s) && (u = (15 & c) << 18 | (63 & a) << 12 | (63 & o) << 6 | 63 & s) > 65535 && u < 1114112 && (l = u)
            }
        null === l ? (l = 65533,
            A = 1) : l > 65535 && (l -= 65536,
            r.push(l >>> 10 & 1023 | 55296),
            l = 56320 | 1023 & l),
            r.push(l),
            i += A
    }
    return function (e) {
        var t = e.length;
        if (t <= k)
            return String.fromCharCode.apply(String, e);
        for (var n = "", r = 0; r < t;)
            n += String.fromCharCode.apply(String, e.slice(r, r += k));
        return n
    }(r)
}

t = {}
t.Buffer = u,
    t.SlowBuffer = function (e) {
        return +e != e && (e = 0),
            u.alloc(+e)
    }
    ,
    t.INSPECT_MAX_BYTES = 50,
    // u.TYPED_ARRAY_SUPPORT = void 0 !== e.TYPED_ARRAY_SUPPORT ? e.TYPED_ARRAY_SUPPORT : function () {
    function () {
        try {
            var e = new Uint8Array(1);
            return e.__proto__ = {
                __proto__: Uint8Array.prototype,
                foo: function () {
                    return 42
                }
            },
            42 === e.foo() && "function" == typeof e.subarray && 0 === e.subarray(1, 1).byteLength
        } catch (e) {
            return !1
        }
    }(),
    t.kMaxLength = o(),
    u.poolSize = 8192,
    u._augment = function (e) {
        return e.__proto__ = u.prototype,
            e
    }
    ,
    u.from = function (e, t, n) {
        return c(null, e, t, n)
    }
    ,
u.TYPED_ARRAY_SUPPORT && (u.prototype.__proto__ = Uint8Array.prototype,
    u.__proto__ = Uint8Array,
"undefined" != typeof Symbol && Symbol.species && u[Symbol.species] === u && Object.defineProperty(u, Symbol.species, {
    value: null,
    configurable: !0
})),
    u.alloc = function (e, t, n) {
        return function (e, t, n, r) {
            return l(t),
                t <= 0 ? s(e, t) : void 0 !== n ? "string" == typeof r ? s(e, t).fill(n, r) : s(e, t).fill(n) : s(e, t)
        }(null, e, t, n)
    }
    ,
    u.allocUnsafe = function (e) {
        return A(null, e)
    }
    ,
    u.allocUnsafeSlow = function (e) {
        return A(null, e)
    }
    ,
    u.isBuffer = function (e) {
        return !(null == e || !e._isBuffer)
    }
    ,
    u.compare = function (e, t) {
        if (!u.isBuffer(e) || !u.isBuffer(t))
            throw new TypeError("Arguments must be Buffers");
        if (e === t)
            return 0;
        for (var n = e.length, r = t.length, i = 0, a = Math.min(n, r); i < a; ++i)
            if (e[i] !== t[i]) {
                n = e[i],
                    r = t[i];
                break
            }
        return n < r ? -1 : r < n ? 1 : 0
    }
    ,
    u.isEncoding = function (e) {
        switch (String(e).toLowerCase()) {
            case "hex":
            case "utf8":
            case "utf-8":
            case "ascii":
            case "latin1":
            case "binary":
            case "base64":
            case "ucs2":
            case "ucs-2":
            case "utf16le":
            case "utf-16le":
                return !0;
            default:
                return !1
        }
    }
    ,
    u.concat = function (e, t) {
        if (!a(e))
            throw new TypeError('"list" argument must be an Array of Buffers');
        if (0 === e.length)
            return u.alloc(0);
        var n;
        if (void 0 === t)
            for (t = 0,
                     n = 0; n < e.length; ++n)
                t += e[n].length;
        var r = u.allocUnsafe(t)
            , i = 0;
        for (n = 0; n < e.length; ++n) {
            var o = e[n];
            if (!u.isBuffer(o))
                throw new TypeError('"list" argument must be an Array of Buffers');
            o.copy(r, i),
                i += o.length
        }
        return r
    }
    ,
    u.byteLength = h,
    u.prototype._isBuffer = !0,
    u.prototype.swap16 = function () {
        var e = this.length;
        if (e % 2 != 0)
            throw new RangeError("Buffer size must be a multiple of 16-bits");
        for (var t = 0; t < e; t += 2)
            m(this, t, t + 1);
        return this
    }
    ,
    u.prototype.swap32 = function () {
        var e = this.length;
        if (e % 4 != 0)
            throw new RangeError("Buffer size must be a multiple of 32-bits");
        for (var t = 0; t < e; t += 4)
            m(this, t, t + 3),
                m(this, t + 1, t + 2);
        return this
    }
    ,
    u.prototype.swap64 = function () {
        var e = this.length;
        if (e % 8 != 0)
            throw new RangeError("Buffer size must be a multiple of 64-bits");
        for (var t = 0; t < e; t += 8)
            m(this, t, t + 7),
                m(this, t + 1, t + 6),
                m(this, t + 2, t + 5),
                m(this, t + 3, t + 4);
        return this
    }
    ,
    u.prototype.toString = function () {
        var e = 0 | this.length;
        return 0 === e ? "" : 0 === arguments.length ? _(this, 0, e) : p.apply(this, arguments)
    }
    ,
    u.prototype.equals = function (e) {
        if (!u.isBuffer(e))
            throw new TypeError("Argument must be a Buffer");
        return this === e || 0 === u.compare(this, e)
    }
    ,
    u.prototype.inspect = function () {
        var e = ""
            , n = t.INSPECT_MAX_BYTES;
        return this.length > 0 && (e = this.toString("hex", 0, n).match(/.{2}/g).join(" "),
        this.length > n && (e += " ... ")),
        "<Buffer " + e + ">"
    }
    ,
    u.prototype.compare = function (e, t, n, r, i) {
        if (!u.isBuffer(e))
            throw new TypeError("Argument must be a Buffer");
        if (void 0 === t && (t = 0),
        void 0 === n && (n = e ? e.length : 0),
        void 0 === r && (r = 0),
        void 0 === i && (i = this.length),
        t < 0 || n > e.length || r < 0 || i > this.length)
            throw new RangeError("out of range index");
        if (r >= i && t >= n)
            return 0;
        if (r >= i)
            return -1;
        if (t >= n)
            return 1;
        if (this === e)
            return 0;
        for (var a = (i >>>= 0) - (r >>>= 0), o = (n >>>= 0) - (t >>>= 0), s = Math.min(a, o), c = this.slice(r, i), l = e.slice(t, n), A = 0; A < s; ++A)
            if (c[A] !== l[A]) {
                a = c[A],
                    o = l[A];
                break
            }
        return a < o ? -1 : o < a ? 1 : 0
    }
    ,
    u.prototype.includes = function (e, t, n) {
        return -1 !== this.indexOf(e, t, n)
    }
    ,
    u.prototype.indexOf = function (e, t, n) {
        return g(this, e, t, n, !0)
    }
    ,
    u.prototype.lastIndexOf = function (e, t, n) {
        return g(this, e, t, n, !1)
    }
    ,
    u.prototype.write = function (e, t, n, r) {
        if (void 0 === t)
            r = "utf8",
                n = this.length,
                t = 0;
        else if (void 0 === n && "string" == typeof t)
            r = t,
                n = this.length,
                t = 0;
        else {
            if (!isFinite(t))
                throw new Error("Buffer.write(string, encoding, offset[, length]) is no longer supported");
            t |= 0,
                isFinite(n) ? (n |= 0,
                void 0 === r && (r = "utf8")) : (r = n,
                    n = void 0)
        }
        var i = this.length - t;
        if ((void 0 === n || n > i) && (n = i),
        e.length > 0 && (n < 0 || t < 0) || t > this.length)
            throw new RangeError("Attempt to write outside buffer bounds");
        r || (r = "utf8");
        for (var a = !1; ;)
            switch (r) {
                case "hex":
                    return v(this, e, t, n);
                case "utf8":
                case "utf-8":
                    return y(this, e, t, n);
                case "ascii":
                    return w(this, e, t, n);
                case "latin1":
                case "binary":
                    return B(this, e, t, n);
                case "base64":
                    return O(this, e, t, n);
                case "ucs2":
                case "ucs-2":
                case "utf16le":
                case "utf-16le":
                    return C(this, e, t, n);
                default:
                    if (a)
                        throw new TypeError("Unknown encoding: " + r);
                    r = ("" + r).toLowerCase(),
                        a = !0
            }
    }
    ,
    u.prototype.toJSON = function () {
        return {
            type: "Buffer",
            data: Array.prototype.slice.call(this._arr || this, 0)
        }
    }
a = {
    isObject: function (e) {
        var t = typeof e;
        return !!e && ("object" == t || "function" == t)
    },
    isString: function (e) {
        return "string" == typeof e || e instanceof String
    },
    isNumber: function (e) {
        return "number" == typeof e || !isNaN(parseFloat(e)) && isFinite(e)
    },
    omit: function (e, t) {
        var n = {};
        for (var r in e)
            e.hasOwnProperty(r) && r !== t && (n[r] = e[r]);
        return n
    }
}
getDataForEncrypt = function (e, n) {
    if (a.isString(e) || a.isNumber(e))
        return u.from("" + e, n || "utf8");
    if (t.isBuffer(e))
        return e;
    if (a.isObject(e))
        return t.from(JSON.stringify(e));
    throw Error("Unexpected data type")
}

t_alloc = function(e, t, n) {
            return function(e, t, n, r) {
                return l(t),
                t <= 0 ? s(e, t) : void 0 !== n ? "string" == typeof r ? s(e, t).fill(n, r) : s(e, t).fill(n) : s(e, t)
            }(null, e, t, n)
        }
e_exports_eme_oaep_mgf1 = function(n, i, a) {
            a = a || "sha1";
            for (var o = e.exports.digestLength[a], s = Math.ceil(i / o), u = t.alloc(o * s), c = t.alloc(4), l = 0; l < s; ++l) {
                var A = r.createHash(a);
                A.update(n),
                c.writeUInt32BE(l, 0),
                A.update(c),
                A.digest().copy(u, l * o)
            }
            return u.slice(0, i)
        }
        e_exports_digestLength = {
            md4: 16,
            md5: 16,
            ripemd160: 20,
            rmd160: 20,
            sha1: 20,
            sha224: 28,
            sha256: 32,
            sha384: 48,
            sha512: 64
        }
e_encryptionScheme_encPad = function(n) {
                var i = "sha1"
                  , a = e_exports_eme_oaep_mgf1
                  , o = t_alloc(0)
                  , s = 256
                  , u = e_exports_digestLength[i];
                if (n.length > s - 2 * u - 2)
                    throw new Error("Message is too long to encode into an encoded message with a length of " + s + " bytes, increaseemLen to fix this error (minimum value for given parameters and options: " + (s - 2 * u - 2) + ")");
                var c = r.createHash(i);
                c.update(o),
                c = c.digest();
                var l = t.alloc(s - n.length - 2 * u - 1);
                l.fill(0),
                l[l.length - 1] = 1;
                for (var A = t.concat([c, l, n]), d = r.randomBytes(u), f = a(d, A.length, i), h = 0; h < A.length; h++)
                    A[h] ^= f[h];
                for (f = a(A, u, i),
                h = 0; h < d.length; h++)
                    d[h] ^= f[h];
                var p = t.alloc(1 + d.length + A.length);
                return p[0] = 0,
                d.copy(p, 1),
                A.copy(p, 1 + d.length),
                p
            }
function rr(e, n) {
            null != e && ("number" == typeof e ? this.fromNumber(e, n) : t.isBuffer(e) ? this.fromBuffer(e) : null == n && "string" != typeof e ? this.fromByteArray(e) : this.fromString(e, n))
        }
this_encryptEngine_encrypt = function(t, i) {
                var a, o;
                return i ? (a = new r(n.encPad(t, {
                    type: 1
                })),
                o = e.$doPrivate(a)) : (a = new rr(e_encryptionScheme_encPad(t)),
                o = e.$doPublic(a)),
                o.toBuffer(e.encryptedDataLength)
            }
encrypt = function (e, t) {
    var n = []
        , i = []
        , a = e.length
        , o = Math.ceil(a / this.maxMessageLength) || 1
        , s = Math.ceil(a / o || 1);
    if (1 == o)
        n.push(e);
    else
        for (var u = 0; u < o; u++)
            n.push(e.slice(u * s, (u + 1) * s));
    for (var c = 0; c < n.length; c++)
        i.push(this_encryptEngine_encrypt(n[c], t));
    return r.concat(i)
}

// t = '{"currency":"USD","departureDate":"2023-03-30","daysBeforeDeparture":0,"daysAfterDeparture":0,"departurePlace":"SGN","arrival":"HAN","oneway":1,"adultCount":1,"childCount":0,"infantCount":0,"requestId":"70F8HHFFANV5-1679839379143","sessionId":null,"x-power-web-s-d":"1729519188-9128518111-4ca0-9a7e-a32dd5b2900f","user-agent-ls-data":"b4cc1316-3188-413d-879a-95ec622c8d79-1679839078100","_signature":"9de02093f207765a64191c1d12eb6d79e1c39a446bccea25382e16e0ae490b32"}'
// t = '{"currency":"USD","departureDate":"2023-03-28","daysBeforeDeparture":0,"daysAfterDeparture":0,"departurePlace":"SGN","arrival":"HAN","oneway":1,"adultCount":1,"childCount":0,"infantCount":0,"requestId":"PAE27MFL6BD4-1679847523723","sessionId":null,"x-power-web-s-d":"1109511912-1410511344-49fa-bc52-5bb56f6e8645","user-agent-ls-data":"afc0efea-1208-4e9a-a498-ffee5ca9af13-1679845792038","_signature":"a7a13724fce0a647fb26c24e8c73d7fa226a102ba3427c419a24458eed2745d6"}'
t = '{"currency":"USD","departureDate":"2023-03-29","daysBeforeDeparture":0,"daysAfterDeparture":0,"departurePlace":"SGN","arrival":"HAN","oneway":1,"adultCount":1,"childCount":0,"infantCount":0,"returnDate":"","requestId":"EXIA4ZVCC3R3-1679847603427","sessionId":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImIwdjB3b2ZEMzQ3U1BaQURnR3ZjTFpUcklIYkZsZmVzRGxEeFpuZHhmMk5qSkJwdFQ3UnR4M1haWXVOellVVFEiLCJpc3MiOiJ2ai13ZWJzaXRlLW1vbml0b3JpbmciLCJpYXQiOjE2Nzk4NDc1OTQsImV4cCI6MTY3OTg0OTM5NH0.Xf96IlB7twCS1vjHiVXy8Z-2DnyVyjkAqvaNufttSymWhs-bl52qe1vN20-DCVMTch9Liu-Z3ZGpfLsD1XVfApeJFOz75KB0WyXKDsv-6amCzuIbxESix_gHQM4TGfeujOdijJzqn__KF2-vm0s10LQnqSeSNrby0IbZ3qX_GvPM-0MC3saBlg08EVjnuUKgoT-BEX7ZMuFSkTy0hf-NtS81z2UCksEsF2vWkMOk7s1iUeYtO7bRRYJ-8OKlmPrScKc35LG9bjuB-AHQEyHhqd05L49kcV5mqmW_KEsGWQXF-4m4_B8aL93XNH3u2nLAqfLh8zxPZL8ifqfhmUoD3w","x-power-web-s-d":"1109511912-1410511344-49fa-bc52-5bb56f6e8645","user-agent-ls-data":"afc0efea-1208-4e9a-a498-ffee5ca9af13-1679845792038","_signature":"2b82908bed7d0ecef500533470fc15365d00f48794bcd83cb86f0c9d6be352ec"}'
i = encrypt(getDataForEncrypt(t), false)
console.log(i)
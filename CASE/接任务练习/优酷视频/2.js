window = this
c = window

document = {};
u = document
navigator = {
    "appCodeName": "Mozilla",
    "appName": "Netscape",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
};


var d = 399, g = "isg", y = c


function pa() {
    return 4294967295 * Math.random() >>> 0
}

function ph(n) {
    for (var t = 0, r = n.length - 1; r >= 0; r--) {
        t = t << 1 | (0 | +n[r])
    }
    return t
}

function pb(n) {
    var t;
    switch (typeof n) {
        case "function":
            t = w.call(n);
            break;
        case "object":
            try {
                t = n + ""
            } catch (r) {
                return !1
            }
            break;
        default:
            return !1
    }
    return g.test(t)
}


var j;
!function (n) {
    function t() {
        if (sn) {
            var n = $ + ":" + ln + ":" + sn.join(",");
            k.D("", n, 4),
                sn = null
        }
    }

    function r(n) {
        K = n.clientX,
            Z = n.clientY,
            $++,
            nn = o(tn, rn)
    }

    function a(n) {
        N = n.isTrusted;
        var t = n.touches[0];
        K = t.clientX,
            Z = t.clientY,
            $++,
            nn = o(tn, rn)
    }

    function o(n, t) {
        return 0 <= n && n <= p.l() && 0 <= t && t <= p.m()
    }

    function e(n) {
        if (D = n.isTrusted,
            b) {
            var r = n.target
                , a = r.offsetWidth >> 1
                , o = r.offsetHeight >> 1;
            if (!(a < 10 && o < 10)) {
                var e = i.abs(n.offsetX - a)
                    , u = i.abs(n.offsetY - o)
                    , f = e < 2 && u < 2;
                if (f && ln++,
                ln >= 3 && (3 === ln && (s(t, 2e4),
                    p.i(c, "unload", t)),
                sn && sn.length < 20)) {
                    var l = (f ? "" : "!") + r.tagName;
                    sn.push(l)
                }
            }
        }
    }

    function m(n) {
        D = n.isTrusted,
            tn = n.clientX,
            rn = n.clientY,
            U++
    }

    function v(n) {
        N = n.isTrusted;
        var t = n.touches[0];
        tn = t.clientX,
            rn = t.clientY,
            U++
    }

    function d(n) {
        J++
    }

    function g(n) {
        V++
    }

    function w() {
        var n = h.availWidth
            , t = p.l();
        Y = n - t < 20,
            an = y.innerWidth,
            on = y.innerHeight
    }

    function x(n) {
        G = !0,
            en = !0
    }

    function z(n) {
        en = !1
    }

    function j() {
        var n = y.Gyroscope;
        if (n)
            try {
                var t = new n({
                    frequency: 2
                });
                return t.onreading = function () {
                    fn = t.z
                }
                    ,
                    void t.start()
            } catch (r) {
            }
        addEventListener("deviceorientation", function (n) {
            fn = n.gamma
        })
    }

    function A() {
        if ("ontouchmove" in u && (p.i(u, "touchmove", v, !0),
            p.i(u, "touchstart", a, !0)),
            p.i(u, "mousemove", m, !0),
            p.i(u, "mousedown", r, !0),
            p.i(u, "click", e, !0),
            p.i(u, "keydown", g, !0),
            p.i(c, "scroll", d, !0),
            p.i(c, "focus", x),
            p.i(c, "blur", z),
            p.i(c, "resize", w),
            w(),
            f.getBattery) {
            var n = f.getBattery();
            n && (n.then(function (n) {
                Q = n
            })["catch"](function (n) {
            }),
                cn = !0)
        }
        un && j()
    }

    function E() {
        return U
    }

    function F() {
        return J
    }

    function T() {
        return $
    }

    function M() {
        return V
    }

    function B() {
        var n = K
            , t = Z;
        n || t || (n = tn,
            t = rn);
        var r = D === undefined && N === undefined || !0 === D || !0 === N;
        return D = undefined,
            N = undefined,
            {
                K: n,
                L: t,
                M: r
            }
    }

    function L() {
        return [an, on]
    }

    function W() {
        return nn
    }

    function S() {
        var n = u.hidden;
        return null == n && (n = u.mozHidden),
            !n
    }

    function C() {
        return en
    }

    function O() {
        return G
    }

    function P() {
        return Y
    }

    function H() {
        return cn
    }

    function X() {
        return !Q || Q.charging
    }

    function I() {
        return Q ? 100 * Q.level : 127
    }

    function R() {
        return un && null != fn
    }

    function q() {
        return un && null != fn ? fn + 90 : 255
    }

    var D, N, Y, G, Q, U = 0, $ = 0, J = 0, V = 0, K = 0, Z = 0, nn = !0, tn = 0, rn = 0, an = 0, on = 0, en = !0, cn = !1, un = !!y.DeviceOrientationEvent;
    (/dingtalk|youku|uczzd\.cn|sm\.cn|uc\.cn/.test("www.youku.com") || /iPhone|iPad|Qianniu|DingTalk|Youku|SQREADER/.test(_)) && (un = !1);
    var fn = null
        , sn = []
        , ln = 0;
    n.F = A,
        n.G = E,
        n.H = F,
        n.I = T,
        n.J = M,
        n.N = B,
        n.O = L,
        n.P = W,
        n.Q = S,
        n.R = C,
        n.S = O,
        n.T = P,
        n.U = H,
        n.V = X,
        n.W = I,
        n.X = R,
        n.Y = q
}(j || (j = {}));
var A;
!function (n) {
    function r() {
        return "$cdc_asdjflasutopfhvcZLmcfl_" in u || f.webdriver
    }

    function i() {
        if (o())
            return !1;
        try {
            var n = u.createElement("canvas")
                , t = n.getContext("webgl");
            if (t) {
                var r = t.getExtension("WEBGL_lose_context");
                r && r.loseContext()
            }
            return !!t
        } catch (i) {
            return !1
        }
    }

    function o() {
        return "ontouchstart" in u
    }

    function e() {
        return /zh-cn/i.test(f.language || f.systemLanguage)
    }

    function s() {
        return -480 === (new a).getTimezoneOffset()
    }

    function l() {
        return j.P()
    }

    function m() {
        return j.X()
    }

    function h() {
        return j.U()
    }

    function v() {
        return j.V()
    }

    function d() {
        var n = 1920
            , t = 1032
            , r = j.O()
            , i = r[0]
            , a = r[1];
        if (null == i || null == a)
            return !1;
        var o = n - i
            , e = t - a;
        return o > 240 || e > 150
    }

    function g() {
        return A && ("complete" !== u.readyState || p.d() - E > 1e4 || j.G() || j.H() || j.I() || j.J()) && (A = !1),
            A
    }

    function k() {
        for (var n = 0; n < M.length; n++)
            F[T.length + n] = M[n]();
        return ph(F)
    }

    function x() {
        for (var n in O)
            if (O.hasOwnProperty(n)) {
                var t = O[n];
                if (t())
                    return +n.substr(1)
            }
        return 0
    }

    function z() {
        E = p.d();
        for (var n = 0; n < T.length; n++)
            F[n] = T[n]()
    }

    var A = !0
        , E = 0
        , F = Array(16)
        , T = [r, i, o, e, s]
        , M = [l, m, h, v, g, d];
    n.Z = g,
        n.$ = k;
    var B = "Google Inc."
        , L = {"maxHeight": ""}
        , W = "chrome" in c
        , S = "ActiveXObject" in c
        , C = pb(y.WeakMap)
        , O = {
        _13: function () {
            return "callPhantom" in y || /PhantomJS/i.test(_)
        },
        _14: function () {
            return /python/i.test(f.appVersion)
        },
        _15: function () {
            return "sgAppName" in f
        },
        _16: function () {
            return /Maxthon/i.test(B)
        },
        _17: function () {
            return "opr" in y
        },
        _18: function () {
            return W && /BIDUBrowser/i.test(_)
        },
        _19: function () {
            return W && /LBBROWSER/i.test(_)
        },
        _20: function () {
            return W && /QQBrowser/.test(_)
        },
        _21: function () {
            return W && /UBrowser/i.test(_)
        },
        _22: function () {
            return W && /2345Explorer/.test(_)
        },
        _23: function () {
            return W && /TheWorld/.test(_)
        },
        _24: function () {
            return W && "MSGesture" in y
        },
        _26: function () {
            return "aef" in y && /WW_IMSDK/.test(_)
        },
        _25: function () {
            return /Qianniu/.test(_)
        },
        _1: function () {
            return W
        },
        _2: function () {
            return "mozRTCIceCandidate" in y || "mozInnerScreenY" in y
        },
        _3: function () {
            return "safari" in y
        },
        _4: function () {
            return S && !("maxHeight" in L)
        },
        _5: function () {
            return S && !p.b(y.postMessage)
        },
        _6: function () {
            return S && !b
        },
        _7: function () {
            return S && !p.b(y.Uint8Array)
        },
        _8: function () {
            return S && !C
        },
        _9: function () {
            return S && C
        },
        _10: function () {
            return "Google Inc." === f.vendor
        },
        _11: function () {
            return "Apple Computer, Inc." === f.vendor
        },
        _12: function () {
            return S
        }
    };
    n._ = x,
        n.F = z
}(A || (A = {}));
var M, B = function () {
    function n(n) {
        this.ma = n;
        for (var t = 0, r = n.length; t < r; t++)
            this[t] = 0
    }

    return n.prototype.na = function () {
        for (var n = this.ma, t = [], r = -1, i = 0, a = n.length; i < a; i++)
            for (var o = this[i], e = n[i], c = r += e; t[c] = 255 & o,
            0 != --e;)
                --c,
                    o >>= 8;
        return t
    },
        n.prototype.oa = function (n) {
            for (var t = this.ma, r = 0, i = 0, a = t.length; i < a; i++) {
                var o = t[i],
                    e = 0;
                do {
                    e = e << 8 | n[r++]
                } while (--o > 0);
                this[i] = e >>> 0
            }
        },
        n
}();


!function (n) {
    function t(n) {
        for (var t = 0, r = 0, i = n.length; r < i; r++)
            t = (t << 5) - t + n[r];
        return 255 & t
    }

    function r(n, t, r, i, a) {
        for (var o = n.length; t < o;)
            r[i++] = n[t++] ^ 255 & a,
                a = ~(131 * a)
    }

    function i(n) {
        for (var t = [], r = n.length, i = 0; i < r; i += 3) {
            var a = n[i] << 16 | n[i + 1] << 8 | n[i + 2];
            t.push(f.charAt(a >> 18), f.charAt(a >> 12 & 63), f.charAt(a >> 6 & 63), f.charAt(63 & a))
        }
        return t.join("")
    }

    function a(n) {
        for (var t = [], r = 0; r < n.length; r += 4) {
            var i = s[n.charAt(r)] << 18 | s[n.charAt(r + 1)] << 12 | s[n.charAt(r + 2)] << 6 | s[n.charAt(r + 3)];
            t.push(i >> 16, i >> 8 & 255, 255 & i)
        }
        return t
    }

    function o() {
        for (var n = 0; n < 64; n++) {
            var t = f.charAt(n);
            s[t] = n
        }
    }

    function e(n) {
        var a = t(n)
            , o = [u, a];
        return r(n, 0, o, 2, a),
            i(o)
    }

    function c(n) {
        var i = a(n)
            , o = i[1]
            , e = [];
        if (r(i, 2, e, 0, o),
        t(e) == o)
            return e
    }

    var u = 4
        , f = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"
        , s = {};
    n.F = o,
        n.pa = e,
        n.qa = c
}(M || (M = {}));


var W;
!function (n) {
    function t() {
        return Date.now() / 1e3 >>> 0
    }

    function r(n) {
        if (j.F(),
            A.F(),
            n) {
            var t = M.qa(n);
            t && a.oa(t)
        }
        a[1] = p.a(),
            a[5] = A._(),
            a[6] = L.ra(),
            a[8] = p.c(f.userAgent),
            a[7] = 0
    }

    function i(n, r) {
        0 == a[4] && (a[4] = pa(),
            a[3] = t()),
            a[2] = t(),
            a[16] = A.$();
        var i = !1;
        if (!A.Z()) {
            a[9] = j.G(),
                a[10] = j.H(),
                a[11] = j.I(),
                a[12] = j.J();
            var e = j.N();
            a[13] = e.K,
                a[14] = e.L,
                i = e.M
        }
        a[17] = j.Y(),
            a[18] = j.W();
        var c = j.R(),
            u = j.T(),
            f = j.S(),
            s = [r, j.Q(), n, c, i, !0, f, u];
        n && o++,
            a[15] = ph(s),
            a[0] = o;
        var l = a.na(),
            m = M.pa(l);
        return m
    }

    var a = new B([2, 2, 4, 4, 4, 1, 1, 4, 4, 3, 2, 2, 2, 2, 2, 1, 2, 1, 1, 1, 1]),
        o = 0;
    n.F = r,
        n.sa = i
}(W || (W = {}));

function get_isg() {
    return W.sa(!1, !1)
}

isg = get_isg()
console.log(isg)


// cookie 中 tfstk 参数来源
// https://g.alicdn.com/AWSC/et/1.62.7/et_f.js

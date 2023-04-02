const crypto = require('crypto');

randomUUID = crypto.randomUUID.bind(crypto)
sessionStorage = {"ss-data-ga": randomUUID()}
localStorage = {"temp-data-ga": "".concat(randomUUID() + "-" + (new Date).getTime())}
P = {
    "b": "c3MtZGF0YS1nYQ==",
    "c": "dGVtcC1kYXRhLWdh",
    "f": "eC1wb3dlci13ZWItcy1k",
    "e": "dXNlci1hZ2VudC1scy1kYXRh",
    "d": "metaSearchKey",
    "a": {
        "Token": "token",
        "ExpireAt": "tokenExpireAt",
        "Provider": "auth_provider"
    }
}
var n = sessionStorage[atob(P.b)]
    , a = localStorage[atob(P.c)]
    , r = a
    , i = (null == r ? void 0 : r.split("-")) || [];
i.pop();
var o, c = null == n ? void 0 : n.split("-").slice(2).join("-");

function h_g(e) {
    for (var t = e.split("-").reduce((function (e, t) {
            return e + t[0] + t[t.length - 1]
        }
    ), ""), n = "", a = 0; a < t.length; a++)
        n += 1 ^ t[a];
    return n
}

function O_a(e, t, n) {
    return t in e ? Object.defineProperty(e, t, {
        value: n,
        enumerable: !0,
        configurable: !0,
        writable: !0
    }) : e[t] = n,
        e
}

get_requestid = function () {
    var n = (new Date).getTime()
    a = function () {
        for (var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : 12, t = "".concat("ABCDEFGHIJKLMNOPQRSTUVWXYZ").concat("0123456789"), n = "", a = 0; a < e; a++)
            n += t[Math.floor(Math.random() * t.length)];
        return n
    }(12)
    r = "".concat(a, "-").concat(n);
    return r
}

get_t = function () {
    t = {}
    Object(O_a)(t, atob(P.f), "".concat(Object(h_g)(i.join("-")) + "-" + Object(h_g)(n) + "-" + c))
    Object(O_a)(t, atob(P.e), a)
    t['requestId'] = get_requestid()
    return t
}

params = get_t()
console.log(params)
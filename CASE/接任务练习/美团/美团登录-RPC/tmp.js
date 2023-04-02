qn = function () {
    return Math.random()
}

function or() {
    return Math.floor(1 + 65535 * qn()).toString(16).substring(1)
}

function ar() {
    var t = []
        , e = +new Date;
    return t.push(e.toString(16)),
        t.push(or()),
        t.push(or()),
        t.push(or()),
        t.join("-")
}

get__lxsdk_s = function (x) {
    _lxsdk_s = [ar(), "%7C", "%7C", x].join("")
    return _lxsdk_s
}
console.log(get__lxsdk_s(0))


le = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"

function ir() {
    for (var t = +new Date, e = 0; t === +new Date && e < 200;)
        e++;
    return t.toString(16) + e.toString(16)
}

screen = {
    availHeight: 1032,
    availLeft: 0,
    availTop: 0,
    availWidth: 1920,
    colorDepth: 24,
    height: 1080,
    pixelDepth: 24,
    width: 1920,
}
r = (screen.height * screen.width).toString(16)
_lxsdk_cuid = "".concat(ir(), "-").concat(Math.random().toString(16).replace(".", ""), "-").concat(function () {
    var t, e, i = [], n = 0;

    function r(t, e) {
        for (var n = 0, r = 0; r < e.length; r++)
            n |= i[r] << 8 * r;
        return t ^ n
    }

    for (t = 0; t < le.length; t++)
        e = le.charCodeAt(t),
            i.unshift(255 & e),
        4 <= i.length && (n = r(n, i),
            i = []);
    return (n = 0 < i.length ? r(n, i) : n).toString(16)
}(), "-").concat(r, "-").concat(ir())
get__lxsdk_cuid = function (ua) {
    le = ua
    return _lxsdk_cuid
}
console.log(get__lxsdk_cuid(le))
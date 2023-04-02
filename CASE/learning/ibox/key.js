navigator = {
    "appCodeName": "Mozilla",
    "appName": "Netscape",
    "appVersion": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
    "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
}


Si = function () {
    function e() {
        return r = (9301 * r + 49297) % 233280,
        r / 233280
    }

    var t = new Date
        , r = t.getTime();
    return function (t) {
        return Math.ceil(e() * t)
    }
}();

function r(e) {
    return null != e && "[object Object]" == Object.prototype.toString.call(e)
}

function i() {
    if ("function" == typeof Uint32Array) {
        var e = "";
        if ("undefined" != typeof crypto ? e = crypto : "undefined" != typeof msCrypto && (e = msCrypto),
        r(e) && e.getRandomValues) {
            var t = new Uint32Array(1)
                , i = e.getRandomValues(t)[0]
                , n = Math.pow(2, 32);
            return i / n
        }
    }
    return Si(1e19) / 1e19
}

var ki = function () {
    var e = function () {
        for (var e = 1 * new Date, t = 0; e == 1 * new Date;)
            t++;
        return e.toString(16) + t.toString(16)
    }
        , t = function () {
        return i().toString(16).replace(".", "")
    }
        , r = function () {
        function e(e, t) {
            var r, i = 0;
            for (r = 0; r < t.length; r++)
                i |= n[r] << 8 * r;
            return e ^ i
        }

        var t, r, i = navigator.userAgent, n = [], a = 0;
        for (t = 0; t < i.length; t++)
            r = i.charCodeAt(t),
                n.unshift(255 & r),
            n.length >= 4 && (a = e(a, n),
                n = []);
        return n.length > 0 && (a = e(a, n)),
            a.toString(16)
    };
    return function () {
        screen_height = 1080
        screen_width = 1920
        var n = String(screen_height * screen_width);
        n = n && /\d{5,}/.test(n) ? n.toString(16) : String(31242 * i()).replace(".", "").slice(0, 8);
        var a = e() + "-" + t() + "-" + r() + "-" + n + "-" + e();
        return a ? a : (String(i()) + String(i()) + String(i())).slice(2, 15)
    }
}()

console.log(ki())
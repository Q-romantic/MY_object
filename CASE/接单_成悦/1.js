// https://deo.shopeemobile.com/shopee/shopee-pcmall-live-sg//assets/bundle.334209968403acb9.js
// "X-CSRFToken": V(r, n)
H_A8 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
csrftoken = function (e, t = H_A8) {
    let n = "";
    for (let r = 0; r < e; r++) {
        const e = Math.floor(Math.random() * t.length);
        n += t.substring(e, e + 1)
    }
    return n
}(32)
// console.log(csrftoken)

Ta = function () {
    return new Date(Date.now())
}
Ua = function () {
    return Ta().getTime()
}
b = Math.round(2147483647 * Math.random())
ts = Math.round(Ua() / 1E3)
_gcl_au = "1.1." + [String(b), ts].join(".")
// console.log(_gcl_au)

_ga_CB0044GVTM = "GS1.1." + ts + ".1.0." + ts + ".60.0.0"
// console.log(_ga_CB0044GVTM)

b = Math.round(2147483647 * Math.random())
_ga = "GA1.1." + [String(b), Math.round(Ua() / 1E3)].join(".")
// console.log(_ga)


get_cookies = function () {
    cookies = {
        "csrftoken": csrftoken,
        "_gcl_au": _gcl_au,
        "_ga_CB0044GVTM": _ga_CB0044GVTM,
        "_ga": _ga,
    }
    return cookies
}()
console.log(eval(get_cookies))
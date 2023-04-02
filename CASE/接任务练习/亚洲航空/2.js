const CryptoJS = require("crypto-js");
key = "5ff1783914a792c2322d51e4e30ed57eb9e76a44b14678f0b4b2087a6d579334"
iv = "c9ec6f6c062589a8d03fa6bdde729b4b"
aes_Encrypt_CFB = function (data, key, iv) {
    key = CryptoJS.enc.Hex.parse(key)
    iv = CryptoJS.enc.Hex.parse(iv)
    data = Buffer.from(decode_aes_utf8, 'utf8').toString()
    var ciphertext = CryptoJS.AES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CFB,
        // padding: CryptoJS.pad.Pkcs7,    // 这里填充方式貌似可有可无
    });
    // return ciphertext.ciphertext.toString() // 输出hex格式
    return ciphertext.toString()              // 输出base64格式
}

aes_Decrypt_CFB = function (ciphertext, key, iv) {
    key = CryptoJS.enc.Hex.parse(key)
    iv = CryptoJS.enc.Hex.parse(iv)
    ciphertext = CryptoJS.lib.CipherParams.create({
        ciphertext: CryptoJS.enc.Base64.parse(ciphertext)
    });
    var originalText = CryptoJS.AES.decrypt(ciphertext, key, {
        iv: iv,
        mode: CryptoJS.mode.CFB,
        // padding: CryptoJS.pad.Pkcs7,    // 这里填充方式貌似可有可无
    });
    originalText = originalText.toString(CryptoJS.enc.Utf8);
    return originalText
}
get_aes_Decrypt_CFB = function (t) {
    return aes_Decrypt_CFB(t, key, iv)
}

decode_aes = get_aes_Decrypt_CFB;

r = {
    "c": {
        "ALGO_ONE": [
            "AES_DECRYPT",
            "SPLIT_INTO_FOUR",
            "REVERSE"
        ],
        "ALGO_TWO": [
            "AES_DECRYPT",
            "SPLIT_INTO_THREE",
            "ADD_EXTRA_CHAR"
        ],
        "ALGO_THREE": [
            "AES_DECRYPT",
            "SPLIT_INTO_FOUR",
            "REVERSE",
            "INSERT_RANDOM_AT_3"
        ],
        "ALGO_FOUR": [
            "AES_DECRYPT",
            "SPLIT_INTO_FOUR",
            "REVERSE",
            "INSERT_ONLY_AT_3"
        ],
        "ALGO_FIVE": [
            "AES_DECRYPT",
            "SPLIT_INTO_THREE",
            "INSER_ONLY_AT_3_WITH_3_CHAR",
            "ADD_EXTRA_CHAR"
        ]
    },
    "b": "AES_DECRYPT",
    "e": "BASE64",
    "i": "REVERSE",
    "a": "ADD_EXTRA_CHAR",
    "n": "SPLIT_INTO_THREE",
    "m": "SPLIT_INTO_FOUR",
    "g": "INSERT_RANDOM_AT_3",
    "f": "INSERT_ONLY_AT_3",
    "h": "INSER_ONLY_AT_3_WITH_3_CHAR",
    "l": {
        "ADD_ONS_KEY": "addons",
        "SEAT_KEY": "seat",
        "CHECKOUT_KEY": "checkout",
        "SEARCH_KEY": "search",
        "AVAILABLE_DATES_KEY": "available_dates",
        "HOTEL_KEY": "hotel"
    },
    "j": "Shopping Website ",
    "k": "SHOWEBA",
    "d": 3
}

function t() {
}

function i_m(e, t) {
    var n = "function" == typeof Symbol && e[Symbol.iterator];
    if (!n)
        return e;
    var r, o, i = n.call(e), a = [];
    try {
        for (; (void 0 === t || t-- > 0) && !(r = i.next()).done;)
            a.push(r.value)
    } catch (l) {
        o = {
            error: l
        }
    } finally {
        try {
            r && !r.done && (n = i.return) && n.call(i)
        } finally {
            if (o)
                throw o.error
        }
    }
    return a
}

i__spread = function () {
    for (var e = [], t = 0; t < arguments.length; t++)
        e = e.concat(i_m(arguments[t]));
    return e
}
i__values = function (e) {
    var t = "function" == typeof Symbol && Symbol.iterator
        , n = t && e[t]
        , r = 0;
    if (n)
        return n.call(e);
    if (e && "number" == typeof e.length)
        return {
            next: function () {
                return e && r >= e.length && (e = void 0),
                    {
                        value: e && e[r++],
                        done: !e
                    }
            }
        };
    throw new TypeError(t ? "Object is not iterable." : "Symbol.iterator is not defined.")
}
t.identifyAlgorithm = function (t, e) {
    var n, r;
    if (t && e && e.synonyms) {
        var o = e.synonyms;
        try {
            for (var a = Object(i__values)(o), l = a.next(); !l.done; l = a.next()) {
                var s = l.value;
                if (s && s.value.find((function (e) {
                        return e === t
                    }
                )))
                    return s.name
            }
        } catch (u) {
            n = {
                error: u
            }
        } finally {
            try {
                l && !l.done && (r = a.return) && r.call(a)
            } finally {
                if (n)
                    throw n.error
            }
        }
    }
}
t.processSSRData = function (t, e) {
    var n = this;
    if (t && e) {
        var o = {
            "addons": "",
            "seat": "",
            "checkout": "",
            "search": "",
            "available_dates": "",
            "hotel": "",
        };
        return t.ssr_data.forEach((function (t) {
                if (t) {
                    var a = n.identifyAlgorithm(t.ssrgroup, e);
                    if (r.c[a]) {
                        var l = Object(i__spread)(r.c[a])
                            , s = n.reverseArray(l);
                        if (s) {
                            var u = n.executeAlgorithm(s, t.ssrlist);
                            if (u) {
                                var c = e.api_data.find((function (e) {
                                        return e.id === t.source
                                    }
                                ));
                                if (c) {
                                    var d = Object.keys(o).find((function (t) {
                                            return t === c.source
                                        }
                                    ));
                                    d && (o[d] = u)
                                }
                            }
                        }
                    }
                }
            }
        )),
            this.monitorJWTExpiration(o),
            o
    }
}
t.identifyAlgorithm = function (t, e) {
    var n, r;
    if (t && e && e.synonyms) {
        var o = e.synonyms;
        try {
            for (var a = Object(i__values)(o), l = a.next(); !l.done; l = a.next()) {
                var s = l.value;
                if (s && s.value.find((function (e) {
                        return e === t
                    }
                )))
                    return s.name
            }
        } catch (u) {
            n = {
                error: u
            }
        } finally {
            try {
                l && !l.done && (r = a.return) && r.call(a)
            } finally {
                if (n)
                    throw n.error
            }
        }
    }
}
t.getToken = function (t) {
    if (t) {
        var e = (t = t.reverse()).join("");
        return e = this.decode64(e),
        "" + o.i + e
    }
}
t.decode64 = function (t) {
    var e, n, i, r, o, a, l = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=", s = "", u = 0;
    /[^A-Za-z0-9\+\/\=]/g.exec(t) && alert("There were invalid base64 characters in the input text.\nValid base64 characters are A-Z, a-z, 0-9, '+', '/',and '='\nExpect errors in decoding."),
        t = t.replace(/[^A-Za-z0-9\+\/\=]/g, "");
    do {
        e = l.indexOf(t.charAt(u++)) << 2 | (r = l.indexOf(t.charAt(u++))) >> 4,
            n = (15 & r) << 4 | (o = l.indexOf(t.charAt(u++))) >> 2,
            i = (3 & o) << 6 | (a = l.indexOf(t.charAt(u++))),
            s += String.fromCharCode(e),
        64 != o && (s += String.fromCharCode(n)),
        64 != a && (s += String.fromCharCode(i)),
            e = n = i = "",
            r = o = a = ""
    } while (u < t.length);
    return unescape(s)
}
t.reverseArray = function (t) {
    if (t)
        return t.reverse()
}
t.concatArrayElements = function (t) {
    if (t)
        return t.join("")
}
t.removeExtraChar = function (t) {
    if (t) {
        var e = [];
        return t.forEach((function (t) {
                if (t) {
                    var n = t.substring(0, t.length - 1);
                    e.push(n)
                }
            }
        )),
            e
    }
}
t.removeRandomStringAtXPlace = function (t, e) {
    if (t) {
        for (var n = [], i = 0; i < t.length; i++)
            (i + 1) % e != 0 && n.push(t[i]);
        return n
    }
}
t.removeRandomOnlyAtXPlace = function (t, e) {
    if (t) {
        for (var n = [], i = 0; i < t.length; i++)
            (i + 1) % e == 0 && n.push(t[i]);
        return n
    }
}
t.executeAlgorithm = function (t, e) {
    var n = this;
    if (t && e) {
        var i = null
            , a = function (e, o) {
            switch (t[e]) {
                case r.b:
                    i = decode_aes(o);
                    break;
                case r.e:
                    i = n.decode64(o);
                    break;
                case r.i:
                    i = n.reverseArray(o);
                    break;
                case r.a:
                    i = n.removeExtraChar(o);
                    break;
                case r.n:
                case r.m:
                    i = n.concatArrayElements(o);
                    break;
                case r.g:
                    i = n.removeRandomStringAtXPlace(o, r.d);
                    break;
                case r.f:
                case r.h:
                    i = n.removeRandomOnlyAtXPlace(o, r.d)
            }
            e++,
            t.length > e && a(e, i)
        };
        return a(0, e),
        "" + "Bearer " + i
    }
}
t.getSSRTkn = function (t, e) {
    if (t && e) {
        var n;
        for (var i in t)
            i === e && (n = t[i]);
        return n
    }
}
t.verifySSRTknGlobals = function (t) {
    if (t) {
        var e = !0;
        for (var n in t)
            t[n].length <= 0 && n !== r.l.HOTEL_KEY && (e = !1);
        return e
    }
}
t.findShoppingHash = function (t, e, n) {
    if (void 0 === n && (n = ""),
    t && e) {
        var i = t.find((function (t) {
                return t.Platform === e
            }
        ));
        if (i || (i = t.find((function (t) {
                return t.ChannelId === n
            }
        ))))
            return i.ChannelHash
    }
}
t.monitorJWTExpiration = function (t) {
    return t
    // if (t) {
    //     var e, n = new l.a, i = s();
    //     for (var r in t) {
    //         if (!t[r])
    //             return;
    //         var o, a = n.getTokenExpirationDate(t[r]);
    //         o = s(a).diff(i, "milliseconds", !0),
    //         (!e || o < e) && (e = o)
    //     }
    //     clearInterval(this.jwtTimer),
    //         this.startJWTTimer(e)
    // }
}
t.startJWTTimer = function (t) {
    var e = this;
    t && (this.jwtTimer = setInterval((function () {
            t <= o.ab.ONE_MINUTE && (u.b.get(u.b.IsJWTExpired).emit(!0),
                clearInterval(e.jwtTimer)),
                t -= o.ab.ONE_SEC
        }
    ), o.ab.ONE_SEC))
}


_t = {
    "ssr_data": [
        {
            "source": "sdlkd2l3",
            "ssrlist": [
                "KAX2",
                "4DaJ",
                "jtzq",
                "JMTZ",
                "wFQ7",
                "byjl",
                "NiNs",
                "v4S7",
                "fbap",
                "fNeV",
                "Fy+V",
                "zavg",
                "6RXx",
                "ID7h",
                "ltsg",
                "v7Mo",
                "SXNb",
                "bckf",
                "EH6F",
                "YlTy",
                "wivl",
                "IxKw",
                "Tdgv",
                "gydk",
                "7l5E",
                "pmAE",
                "psqs",
                "5kpm",
                "SXZv",
                "exkm",
                "Ylm+",
                "orjQ",
                "gutb",
                "0nRg",
                "Tshl",
                "ykaj",
                "XTyw",
                "pX0O",
                "bixc",
                "fDTC",
                "+qxN",
                "ewhn",
                "1rzZ",
                "V2fm",
                "ysoe",
                "6ItY",
                "S9lr",
                "darm",
                "aAra",
                "pSTl",
                "sgoe",
                "LASR",
                "+/ZB",
                "jciv",
                "LXSO",
                "Y696",
                "ofbz",
                "Zpnm",
                "e8U2",
                "zqlj",
                "kOWy",
                "m2Z7",
                "jwqi",
                "9oSG",
                "uCT7",
                "oagq",
                "+MgS",
                "5TYW",
                "ndvc",
                "4M7l",
                "d1qQ",
                "rnob",
                "Uf+L",
                "ZOAo",
                "bkof",
                "0Z30",
                "+gyD",
                "nqeb",
                "tIDD",
                "M6zu",
                "kuca",
                "8cLL",
                "BlCU",
                "natb",
                "/6aM",
                "EHyZ",
                "qqgq",
                "66co",
                "CIxh",
                "myog",
                "vXcL",
                "AQbX",
                "hlej",
                "dHD7",
                "b8MH",
                "dqqk",
                "Tmik",
                "heF6",
                "gugy",
                "RhjN",
                "h5kR",
                "wnms",
                "ZOPT",
                "XKtu",
                "fgjn",
                "DN6F",
                "zvhm",
                "smty",
                "LA2x",
                "jVLV",
                "zxtb",
                "8Y7D",
                "XG1S",
                "hdkc",
                "pZLi",
                "vxMR",
                "wbno",
                "f8Qi",
                "H6v2",
                "hfgi",
                "aUw3",
                "5cTM",
                "lcbg",
                "ogfe",
                "YV6q",
                "fuhz",
                "mURN",
                "wMLx",
                "yttm",
                "wSVf",
                "9/BX",
                "bpev",
                "/gCw",
                "FWY+",
                "xdtk",
                "XaDl",
                "Ae9m",
                "djgn",
                "ATiX",
                "Vo1U",
                "woms",
                "izCm",
                "/tbP",
                "regv"
            ],
            "ssrgroup": "MDXT"
        },
        {
            "source": "eue3kds",
            "ssrlist": [
                "lSQP",
                "pEBh",
                "ljur",
                "B8RP",
                "KxQP",
                "flaa",
                "b576",
                "s98X",
                "gjjf",
                "Ed4S",
                "hO+M",
                "ipyd",
                "avlL",
                "2vOk",
                "pvzg",
                "7bfL",
                "ylUI",
                "rbbu",
                "xQmh",
                "2GRY",
                "mvus",
                "FbZR",
                "8Oz9",
                "pmhk",
                "k+6J",
                "Dj50",
                "frfx",
                "xsq1",
                "+L+C",
                "vykv",
                "HKrX",
                "4FL7",
                "jzlp",
                "t0Pn",
                "jtCp",
                "vbtl",
                "Ui3e",
                "ph0u",
                "hgwl",
                "KDUh",
                "9EPk",
                "dego",
                "CtEv",
                "EFee",
                "qipn",
                "n5Ce",
                "poAA",
                "bhka",
                "uIpO",
                "Ewr5",
                "sjty",
                "cb9+",
                "MK96",
                "odzx",
                "/lQo",
                "1Eqs",
                "wzqv",
                "kEpE",
                "49A5",
                "gqqv",
                "ZQ/4",
                "0ab0",
                "wlva",
                "9iRX",
                "1VAV",
                "pjkw",
                "4+gx",
                "HNuQ",
                "rxkt",
                "/93k",
                "dD8h",
                "ydgs",
                "Voxl",
                "4UAB",
                "nclb",
                "IjaL",
                "7UtF",
                "majk",
                "sjR9",
                "18tB",
                "fool",
                "VIO/",
                "eSRR",
                "hshe",
                "3+Z9",
                "b14b",
                "mnul",
                "feMv",
                "3Ny6",
                "maaj",
                "P1zm",
                "KsVR",
                "vbgi",
                "tD4v",
                "JghK",
                "ldsq",
                "gMfC",
                "+OUp",
                "mpcd",
                "EgEn",
                "YCcq",
                "qldr",
                "BO/N",
                "4Hsi",
                "hhrv",
                "LlvQ",
                "NCbL",
                "utvf",
                "5io2",
                "xD0L",
                "eyof",
                "264U",
                "I25m",
                "dbyt",
                "rcrt",
                "9wAv",
                "omxk",
                "UYUV",
                "PLDZ",
                "ltxd",
                "aUw3",
                "5cTM",
                "dmcy",
                "ogfe",
                "YV6q",
                "mdtg",
                "mURN",
                "wMLx",
                "ygts",
                "wSVf",
                "9/BX",
                "kuis",
                "/gCw",
                "FWY+",
                "kpha",
                "XaDl",
                "Ae9m",
                "evlx",
                "ATiX",
                "Vo1U",
                "rthn",
                "izCm",
                "/tbP",
                "ynnp"
            ],
            "ssrgroup": "MDXT"
        },
        {
            "source": "xmncx278",
            "ssrlist": [
                "khwZ",
                "bviW",
                "/tbG",
                "nqiH",
                "ekwE",
                "PizE",
                "jxpG",
                "hvyS",
                "CmVS",
                "itmU",
                "pedF",
                "o1UE",
                "fpfM",
                "ozxN",
                "ATiZ",
                "kywH",
                "mtzK",
                "XAeJ",
                "ljjC",
                "iemV",
                "9mXK",
                "ukhW",
                "yteV",
                "aDlD",
                "dboX",
                "azoO",
                "FWYE",
                "xcuJ",
                "xemQ",
                "+/gM",
                "zugW",
                "kfoN",
                "Cw9Q",
                "udvT",
                "sdiV",
                "/BXR",
                "txmT",
                "gukG",
                "wSVQ",
                "wieP",
                "thaI",
                "fwMJ",
                "jgfY",
                "vqdH",
                "LxmI",
                "agcS",
                "sahU",
                "URNT",
                "chaD",
                "tclG",
                "YV6H",
                "tdoW",
                "wbnC",
                "qogW",
                "uzxX",
                "upjP",
                "fe5M",
                "qyfE",
                "eedH",
                "cTMI",
                "yehB",
                "wvcY",
                "aUwB",
                "kymX",
                "yhgH",
                "3J7H",
                "ogqK",
                "qaaV",
                "SSeG",
                "flfN",
                "uyiA",
                "+EVU",
                "mufU",
                "vrnQ",
                "2jEM",
                "pmoP",
                "tqrD",
                "IqaK",
                "vafU",
                "xeoP",
                "/tJA",
                "bmoT",
                "ujaW",
                "Wp6Z",
                "btaE",
                "ibzE",
                "y5GB",
                "sizX",
                "lduI",
                "ezEY",
                "zbrO",
                "pryU",
                "9zcD",
                "nrqV",
                "kdpD",
                "lEKE",
                "sxaC",
                "skaX",
                "w3ZK",
                "dwpT",
                "mwoO",
                "hpmR",
                "uasR",
                "lwiA",
                "vfXK",
                "gsfC",
                "busM",
                "oXGE",
                "lexH",
                "eycM",
                "FC3V",
                "chkA",
                "nlyS",
                "fprA",
                "bdnL",
                "kjjQ",
                "VXAS",
                "xfaN",
                "rrnB",
                "oGuZ",
                "tdfX",
                "vkhC",
                "H33S",
                "zdtH",
                "siqV",
                "Ei7Z",
                "jrnS",
                "ploR",
                "1Q8B",
                "vcoU",
                "sxuI",
                "i43W",
                "qvuM",
                "exdT",
                "9hHB",
                "uzjN",
                "fzhK",
                "ukQM",
                "xmkP",
                "rayQ",
                "ub8V",
                "batI",
                "pvzF",
                "CGVJ",
                "rgzR",
                "zcwS",
                "nJAY",
                "epuX",
                "qhpY",
                "+etC",
                "wxiX",
                "afhR",
                "wEfG",
                "damU",
                "nelW",
                "1WzI",
                "viiX",
                "aceL",
                "wJrH",
                "apoA",
                "umkS",
                "OrBJ",
                "wvdB",
                "zggO",
                "YMAR",
                "gzpC",
                "whtM",
                "MZjY",
                "afxK",
                "dfdM",
                "qDlN",
                "htmS",
                "fruQ",
                "exyB",
                "hxlW",
                "gbaV",
                "rE6W",
                "dboU",
                "zhcL",
                "VkHR",
                "eydB",
                "ameF",
                "Ec7M",
                "wfsE",
                "eeuF",
                "aV4S",
                "wleG",
                "ksjL",
                "kY1E",
                "mnfO",
                "dwzS",
                "D69L",
                "nwcF",
                "qxyP",
                "ETQC",
                "kbvN",
                "uauV",
                "iVuF",
                "xojD",
                "lxdZ",
                "6DLL",
                "gcvW",
                "qsfO",
                "i50Z",
                "hdbX",
                "nvjX",
                "/YuA",
                "wrcL",
                "mzjO",
                "IJxC",
                "xglR",
                "ghpO",
                "JPdN",
                "jjgR",
                "zplO",
                "EziJ",
                "khgM",
                "vizD",
                "12gL",
                "cvjL",
                "rlhY",
                "HOVH",
                "xgwX",
                "zhaY",
                "IjrK",
                "ugeX",
                "worE",
                "FW0T",
                "bsbW",
                "uixP",
                "ETQN",
                "syxZ",
                "fhtV",
                "GtEY",
                "khcP",
                "rqvW",
                "pSCK",
                "cvgI",
                "flcL",
                "LtvE",
                "qvbW",
                "ivrE",
                "hhaK",
                "bpsA",
                "cuoG",
                "LZKX",
                "oviR",
                "mweA",
                "SLZH",
                "ubuR",
                "uxrL",
                "zvxR",
                "ybxI",
                "rhdV",
                "LnRT",
                "eqlA",
                "slsZ",
                "zXLS",
                "jsxC",
                "mwpV",
                "RaDT",
                "utyT",
                "vowP",
                "7X2G",
                "akvT",
                "bmzO",
                "k9iX",
                "vweR",
                "ibfG",
                "9y5T",
                "iquA",
                "mriC",
                "59YW",
                "wakC",
                "adqE",
                "b3OC",
                "gshM",
                "hphE",
                "PosQ",
                "nsvL",
                "afiQ",
                "qlPN",
                "nfgG",
                "bkqC",
                "UM8Q",
                "sjoS",
                "ofbQ",
                "p68X",
                "bhlJ",
                "utjH",
                "4J/N",
                "ofvT",
                "faxQ",
                "BMzH",
                "jjqP",
                "ploI",
                "vRVL",
                "glkF",
                "xrxV",
                "ILcR",
                "qlfA",
                "tikM",
                "DhqA",
                "tfzD",
                "xdyS",
                "jz4I",
                "plcG",
                "qnpR",
                "ts9P",
                "blkQ",
                "bgnI",
                "zqGJ",
                "xacH",
                "eobZ",
                "c+mM",
                "btfS",
                "juhH",
                "TvAV",
                "tseF",
                "xfaT",
                "X4LT",
                "autU",
                "wsxA",
                "gsLY",
                "jrmN",
                "tjxS",
                "ZO6M",
                "pisW",
                "ugvM",
                "bGvN",
                "qsgO",
                "ejjC",
                "RW7L",
                "gquJ",
                "bxrE",
                "zvwV",
                "mnsG",
                "vcaO",
                "jTqV",
                "cygM",
                "pnaT",
                "guCD",
                "qmwT",
                "ucmF",
                "7CrM",
                "cxqW",
                "hwyE",
                "m7TL",
                "xfpE",
                "cooI",
                "g+UC",
                "tqsT",
                "ewsM",
                "EbdR",
                "jdrS",
                "bhhC",
                "As2Y",
                "xtbH",
                "tsyY",
                "MJNZ",
                "trkU",
                "rhdH",
                "eVyC",
                "yxvJ",
                "ezlW",
                "4inF",
                "xpdI",
                "rnpR",
                "r+iC",
                "gayB",
                "hslK",
                "fwZJ",
                "atqA",
                "aomP",
                "oWSE",
                "nerV",
                "uzhW",
                "g1IZ",
                "icdO",
                "wknO",
                "iuKS",
                "xuiE",
                "jyrA",
                "TFEE"
            ],
            "ssrgroup": "MEFD"
        },
        {
            "source": "wiuwejk2",
            "ssrlist": [
                "jnhS",
                "grsA",
                "/tbQ",
                "cjzX",
                "hhiL",
                "PizK",
                "vuyR",
                "jsyH",
                "CmVO",
                "wccL",
                "hykR",
                "o1UC",
                "eviZ",
                "rseQ",
                "ATiU",
                "dniO",
                "shhK",
                "XAeG",
                "anpG",
                "xyfB",
                "9mXI",
                "tbnU",
                "lwlN",
                "aDlY",
                "qfcB",
                "cfiE",
                "FWYJ",
                "tyaY",
                "rtnV",
                "+/gR",
                "bopI",
                "lspR",
                "Cw9Q",
                "jpyI",
                "mmaV",
                "/BXY",
                "unuL",
                "zdtA",
                "wSVB",
                "jxaB",
                "buvD",
                "fwMI",
                "oalA",
                "pqrP",
                "LxmK",
                "vkoZ",
                "jipP",
                "URNB",
                "pukZ",
                "imsU",
                "YV6S",
                "vjjD",
                "yfdN",
                "qogJ",
                "qtrU",
                "ycjD",
                "fe5W",
                "rxaU",
                "oegT",
                "cTMV",
                "njkX",
                "nffD",
                "aUwM",
                "twhJ",
                "nujN",
                "0iNK",
                "jxrF",
                "gqqN",
                "4YdD",
                "pccH",
                "wttA",
                "KZYS",
                "rvvQ",
                "yfkI",
                "eE6B",
                "uhpJ",
                "bdqN",
                "7G8I",
                "vphS",
                "zpqH",
                "Fo9K",
                "vclH",
                "laoS",
                "8fOA",
                "hfuM",
                "hboD",
                "cApG",
                "zkvD",
                "ylhT",
                "jh7X",
                "gyaK",
                "qsxU",
                "yqeK",
                "acuD",
                "cykM",
                "+2IW",
                "ierX",
                "majB",
                "8yyY",
                "zyyE",
                "izbS",
                "19xP",
                "ifaE",
                "pctL",
                "Z5pQ",
                "fxbH",
                "csrP",
                "RJYU",
                "xveP",
                "eqxO",
                "SvgP",
                "zynE",
                "jmzW",
                "M3IG",
                "fxfY",
                "jngA",
                "SMcX",
                "ehhY",
                "uyoX",
                "McvX",
                "nguL",
                "upkR",
                "BgYD",
                "ysgQ",
                "jjxG",
                "erNG",
                "ytqE",
                "xyoF",
                "FnER",
                "hjrN",
                "hqdQ",
                "4pKX",
                "wkiX",
                "jpwV",
                "ifiN",
                "azhF",
                "ybtY",
                "PCJD",
                "gwsC",
                "jebY",
                "j6IU",
                "rrtA",
                "nytT",
                "A7hL",
                "bxlI",
                "iefL",
                "zopL",
                "fisK",
                "swfV",
                "QSOP",
                "civA",
                "bjiF",
                "OkAB",
                "csuK",
                "qloP",
                "uteV",
                "xzvQ",
                "stwR",
                "WLVA",
                "ojiN",
                "krlW",
                "VnuS",
                "phgP",
                "fjqF",
                "0lZU",
                "snoC",
                "rjwM",
                "9yiJ",
                "ohzR",
                "iviW",
                "0ToI",
                "bxjC",
                "iufF",
                "yuQW",
                "bzlO",
                "nyaN",
                "rtQU",
                "fdtY",
                "siqQ",
                "ij5X",
                "ushJ",
                "yraU",
                "mk9U",
                "hhcE",
                "wiaF",
                "7FRY",
                "jwlP",
                "cfqQ",
                "j1oK",
                "vgpN",
                "mvyC",
                "Sk9K",
                "sekS",
                "dtvD",
                "gCoD",
                "xesJ",
                "rozZ",
                "haNT",
                "uwsP",
                "jvmM",
                "nUWS",
                "gldZ",
                "pomM",
                "m6kO",
                "oadP",
                "nlbY",
                "WNpN",
                "cqtF",
                "ulnN",
                "EsHQ",
                "btrN",
                "mcuM",
                "rhwV",
                "dsrX",
                "wijZ",
                "xiuY",
                "ewyH",
                "ektP",
                "NvyR",
                "vgpF",
                "yxwH",
                "NqjW",
                "wsvU",
                "rbfA",
                "lvJL",
                "nsqK",
                "vebD",
                "DyEF",
                "fhzW",
                "pvzA",
                "r8zI",
                "hjsN",
                "iapH",
                "y9NN",
                "iheJ",
                "wseV",
                "YyuR",
                "gduZ",
                "pjzO",
                "WiqA",
                "bcjC",
                "bjhC",
                "f2qN",
                "wfnX",
                "neuW",
                "hTeR",
                "qkvF",
                "snyB",
                "LLjT",
                "dbqC",
                "qawQ",
                "ovHZ",
                "xnuA",
                "vzuX",
                "UgjI",
                "satO",
                "yfkZ",
                "MPCE",
                "jluW",
                "dovH",
                "PB1E",
                "sjtF",
                "fnkT",
                "8SZZ",
                "ccjT",
                "lcbO",
                "L3RO",
                "tvwW",
                "chqN",
                "z+/U",
                "xteG",
                "jfgY",
                "A2OQ",
                "qxaX",
                "pjnS",
                "e3vC",
                "ayjO",
                "vlyV",
                "C4uK",
                "dbtG",
                "pysC",
                "rXAY",
                "yvrF",
                "figA",
                "pkyO",
                "lgrR",
                "artO",
                "7OlV",
                "bmbX",
                "rwwQ",
                "shtY",
                "jxsZ",
                "nkcF",
                "IpVQ",
                "eubQ",
                "yjjO",
                "BzGG",
                "ohaK",
                "dkrA",
                "K34B",
                "oibX",
                "bhqR",
                "bYZH",
                "skxS",
                "ydbJ",
                "Of9U",
                "eklY",
                "wcaK",
                "S8dW",
                "iqmR",
                "goyL",
                "yneO",
                "xgyP",
                "yssQ",
                "Kj0Q",
                "nxrQ",
                "dxoR",
                "lBlW",
                "fqlL",
                "wnrM",
                "5xpO",
                "lseB",
                "vgdQ",
                "SeGP",
                "vqwR",
                "expS",
                "q2pB",
                "aicV",
                "kobU",
                "FsxE",
                "mluJ",
                "oqyJ",
                "KgmY",
                "gpqR",
                "lraW",
                "6hBV",
                "tzlO",
                "wjwE",
                "nyVV",
                "jgjO",
                "jkyA",
                "DVJF",
                "yzbM",
                "xftM",
                "SGzI",
                "bmrV",
                "hrlN",
                "7mhI",
                "emxF",
                "ypgL",
                "AkvF",
                "xzcW",
                "qauK",
                "M3bB",
                "fkkX",
                "wvvV",
                "qk0R",
                "vmcG",
                "pspW",
                "H+SE",
                "mlcC",
                "xotY",
                "dBnV",
                "vgiZ",
                "beeC",
                "tu/U",
                "ymcV",
                "thmG",
                "DFBH",
                "rzuC",
                "gmqL",
                "RepV",
                "deeC",
                "prjE",
                "qY6F",
                "ausS",
                "xipG",
                "4kGG",
                "yrsP",
                "cfdI",
                "A4GJ",
                "ytaO",
                "mshS",
                "V21S"
            ],
            "ssrgroup": "MCXJ"
        },
        {
            "source": "jksdkjsd2",
            "ssrlist": [
                "/tbD",
                "PizZ",
                "CmVI",
                "o1UQ",
                "ATiX",
                "XAeE",
                "9mXG",
                "aDlB",
                "FWYD",
                "+/gP",
                "Cw9I",
                "/BXL",
                "wSVC",
                "fwMD",
                "LxmM",
                "URNU",
                "YV6U",
                "qogX",
                "fe5I",
                "cTMQ",
                "aUwM",
                "0i8I",
                "pwIW",
                "qJuQ",
                "SmSR",
                "hL+Z",
                "oU7L",
                "8vDP",
                "ZGIC",
                "lPCJ",
                "QHlK",
                "3ATX",
                "ElXO",
                "SizB",
                "9Q9D",
                "9IrS",
                "qNQD",
                "i7hT",
                "hpjE",
                "WddL",
                "a9YL",
                "L4DC",
                "IP7C",
                "lk4M",
                "06QO",
                "UWUL",
                "sFMY",
                "18VY",
                "hVaI",
                "HPsN",
                "7hlX",
                "P30B",
                "EdAW",
                "8wAM",
                "nDWJ",
                "tQDW",
                "OUBD",
                "2wbZ",
                "jhHD",
                "UZ1W",
                "ZQ3I",
                "m2JA",
                "FjmV",
                "PKoU",
                "cMwA",
                "OSPS",
                "VqpK",
                "GNoE",
                "7gAN",
                "V6+X",
                "wIxZ",
                "ItjN",
                "LZ+I",
                "jnQH",
                "mlQV",
                "jQaV",
                "BYHV",
                "vooS",
                "S7LA",
                "9EvO",
                "bV1Q",
                "aQLC",
                "D96J",
                "PmnZ",
                "PopI",
                "94NX",
                "BlTI",
                "m0sL",
                "xCvA",
                "afHP",
                "xPGW",
                "H5IB",
                "doiE",
                "KmgE",
                "wGLS",
                "QCTD",
                "vWuG",
                "bq6T",
                "uG3G",
                "QSmD",
                "o7CK",
                "WtMU",
                "TCqF",
                "GvNY",
                "pNsQ",
                "hFWJ",
                "WJZJ",
                "wOZB",
                "eHAQ",
                "0clF",
                "8WWS",
                "5NGL",
                "bB2P",
                "jIvF",
                "7kxJ",
                "jKeC",
                "6x2U",
                "Eu3U",
                "eVoR",
                "SBbH",
                "4MAO",
                "=C"
            ],
            "ssrgroup": "MAZ2"
        },
        {
            "source": "hotel876",
            "ssrlist": [
                "Lj8J",
                "OJNf",
                "xfzp",
                "HSib",
                "7iAr",
                "pmdw",
                "dwSf",
                "Ksw6",
                "bogx",
                "acBS",
                "QDSx",
                "bxdb",
                "U8Lh",
                "Xuim",
                "wdmz",
                "JQ+b",
                "ORuM",
                "gfss",
                "vrEB",
                "fMkP",
                "gecb",
                "vo29",
                "aWzR",
                "ammk",
                "JHNa",
                "0mNj",
                "wfbk",
                "OTtW",
                "rnCk",
                "dosy",
                "1+oT",
                "EgZz",
                "xtlc",
                "Ym6q",
                "Lk4J",
                "ared",
                "rlDa",
                "zs2+",
                "lakt",
                "sAkE",
                "kDF1",
                "wprn",
                "UuU0",
                "MOYQ",
                "dybg",
                "OSM/",
                "5ZN0",
                "rfpl",
                "g3J3",
                "PnHz",
                "gnkh",
                "ujIQ",
                "OEAR",
                "bpaj",
                "et8p",
                "4e87",
                "hpgz",
                "k+O3",
                "Io+6",
                "vkdr",
                "6Pbk",
                "osWy",
                "zngi",
                "n1f0",
                "jF+g",
                "xhnk",
                "COnS",
                "aB+S",
                "vvzn",
                "sput",
                "7YWN",
                "nqdr",
                "Ej9e",
                "2j8F",
                "fana",
                "rJa5",
                "e7Ro",
                "hevv",
                "h7NA",
                "YhAO",
                "zuqz",
                "vr4v",
                "wPGW",
                "kzye",
                "EEUd",
                "fZq/",
                "iqka",
                "dphn",
                "Cy7b",
                "fxuo",
                "kt+z",
                "kGFy",
                "tqtb",
                "bvJU",
                "eXaT",
                "xykw",
                "ufvC",
                "P4qH",
                "imne",
                "CJcx",
                "7NoM",
                "fsqd",
                "NW7C",
                "whSC",
                "qhqr",
                "bYdD",
                "EzWG",
                "dars",
                "P3Mp",
                "hTdn",
                "neyy",
                "cLv6",
                "9sve",
                "tbvs",
                "APlo",
                "d1qu",
                "dhjq",
                "VcZs",
                "it0F",
                "duer",
                "aUw0",
                "5cTM",
                "hael",
                "ogfe",
                "YV6q",
                "jvyy",
                "mURN",
                "wMLx",
                "bapi",
                "wSVf",
                "9/BX",
                "uape",
                "/gCw",
                "FWY+",
                "rnst",
                "XaDl",
                "Ae9m",
                "mzou",
                "ATiX",
                "Vo1U",
                "sbja",
                "izCm",
                "/tbP",
                "hhdx"
            ],
            "ssrgroup": "MFXT"
        }
    ]
}
_e = {
    "synonyms": [
        {
            "name": "ALGO_ONE",
            "value": [
                "MCI5",
                "MLAK",
                "MBD7",
                "MKLB",
                "MCAI"
            ]
        },
        {
            "name": "ALGO_TWO",
            "value": [
                "MCX5",
                "MCDJ",
                "MEAK",
                "MDD7",
                "MAZ2"
            ]
        },
        {
            "name": "ALGO_THREE",
            "value": [
                "MEGR",
                "MEDJ",
                "MFXT",
                "MEQZ",
                "MDXT"
            ]
        },
        {
            "name": "ALGO_FOUR",
            "value": [
                "MBXT",
                "MEZ2",
                "MEXT",
                "MEI5",
                "MDI5"
            ]
        },
        {
            "name": "ALGO_FIVE",
            "value": [
                "MED7",
                "MCXJ",
                "MAXT",
                "MEFD",
                "MCXT"
            ]
        }
    ],
    "api_data": [
        {
            "source": "addons",
            "id": "sdlkd2l3"
        },
        {
            "source": "seat",
            "id": "eue3kds"
        },
        {
            "source": "checkout",
            "id": "xmncx278"
        },
        {
            "source": "search",
            "id": "wiuwejk2"
        },
        {
            "source": "available_dates",
            "id": "jksdkjsd2"
        },
        {
            "source": "hotel",
            "id": "hotel876"
        }
    ]
}
get_authorization = function (_t) {
    res = t.processSSRData(_t, _e)
    console.log(res)
    return res
}
get_authorization(_t, _e)
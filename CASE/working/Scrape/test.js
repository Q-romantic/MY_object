const CryptoJS = require('crypto-js');  // npm install crypto-js
// const CryptoJS = require('C:\\Y\\Case\\working\\猿人学\\crypto-js.js');

var ccc = 986876
var s = "qnbyzzwmdgghmcnm"
for (i = ccc; i < ccc + 100; i++) {
    var srcs = CryptoJS.enc.Utf8.parse(i);
    var k = CryptoJS.enc.Utf8.parse(s);
    var en = CryptoJS.AES.encrypt(srcs, k, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    var ddd = en.toString();
    ddd = ddd.replace(/\//g, "^");
    ddd = ddd.substring(0, ddd.length - 2);
    console.log(ddd)
}
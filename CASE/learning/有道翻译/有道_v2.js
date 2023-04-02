const crypto = require("crypto");


function m(e) {
    return crypto.createHash("md5").update(e).digest()
}

O = (t) => {
    decodeKey = "ydsecret://query/key/B*RGygVywfNBwpmBaZg*WT7SIOUP2T0C9WHMZN39j^DAdaZhAnxvGcCY6VYFwnHl"
    decodeIv = "ydsecret://query/iv/C@lZe2YzHtZ2CYgaXKSVfsb7Y4QWHjITPPZ0nQp87fBeJ!Iv6v^6fvi2WN@bYpJ4"

    if (!t)
        return null;
    const a = Buffer.alloc(16, m(decodeKey))
        , r = Buffer.alloc(16, m(decodeIv))
        , i = crypto.createDecipheriv("aes-128-cbc", a, r);
    let s = i.update(t, "base64", "utf-8");
    return s += i.final("utf-8"),
        s
};
sss = "Z21kD9ZK1ke6ugku2ccWu-MeDWh3z252xRTQv-wZ6jddVo3tJLe7gIXz4PyxGl73nSfLAADyElSjjvrYdCvEP4pfohVVEX1DxoI0yhm36ytQNvu-WLU94qULZQ72aml67Dyp8zwZ2zW2Woo1hUwGCAW7BxAMlElnObaSWlQ4SZQ3IMEsxScZWJkQjp1_Vu6xSOrWuIICC4CqQSF2rD-VbedbpCxFPsABU9oimbfHqHPLS6JM5PMR391ejG78hTE-CoKdXKFb4GY8rhwH6q_viiVVwcsMLKJnmuAAJYhRpxvFnE1bJ9YmChMzGQhH1iMsddh7bW1pKTrjkLKSAzprBlY_jCiaON2MjKTcL4YoQM-3CFnlABlMaG8JbUvNGhJ0l8p5hB8uvGyTX2wWpxH2Y_Wuljq2Bhu4UK_AClqdF4AMc0fp4mbcnfWgsO7qReA86MC4W7A4mmYuVTo5NyfyGg=="
res = O(sss)
console.log(res)

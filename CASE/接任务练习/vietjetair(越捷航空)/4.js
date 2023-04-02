//优化
deepClone2 = function (obj) {
    //判断传进来的参数类型不是对象数组 或者是null时 直接返回
    if (typeof obj !== "object" || obj == null) {
        return obj
    }
    //定义返回值result
    // 判断传进来的数据类型 是数组/对象 就给result一个数组/对象
    result = Array.isArray(obj) ? [] : {};
    //循环遍历方便拷贝
    for (key in obj) {
        //判读自有属性
        if (obj.hasOwnProperty(key)) {
            //函数递归实现深层拷贝
            result[key] = deepClone2(obj[key])
        }
    }
    //返回出去
    return result
}
// console 控制台使用 copy(deepClone(fun))
// 例如: copy(deepClone(H.encrypt))


deepClone = function (arr) {
    var obj = arr.constructor == Array ? [] : {};
    // 第二种方法 var obj = arr instanceof Array ? [] : {}
    // 第三种方法 var obj = Array.isArray(arr) ? [] : {}
    for (var item in arr) {
        if (typeof arr[item] === "object") {
            obj[item] = deepClone(arr[item]);
        } else {
            obj[item] = arr[item];
        }
    }
    return obj;
}


H_encrypt = function () {
    var e;
    if (!this._publicKey) throw new Error('"publicKey" is missing.');
    return (e = this._publicKey).encrypt.apply(e, arguments)
}


clone = function (obj) {
    if (typeof obj === "string", typeof obj === "number", typeof obj === "boolean", typeof obj === "undefined") {
        return obj;
    } else if (Array.isArray(obj)) {
        let arr = JSON.parse(JSON.stringify(obj));
        return arr;
    } else if (obj instanceof (obj)) {
        let obj2 = {};
        for (let k in obj) {
            obj2[k] = clone(obj[k]);
        }
        return obj2;
    }
}


function p(e) {
    if (r[e]) return r[e].exports;
    var t = r[e] = {i: e, l: !1, exports: {}};
    return i[e].call(t.exports, t, t.exports, p), t.l = !0, t.exports
}
console.log(p(163))




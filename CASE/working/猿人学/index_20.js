function Hlclient(wsURL) {
    this.wsURL = wsURL;
    this.handlers = {};
    this.socket = {};
    if (!wsURL) {
        throw new Error('wsURL can not be empty!!')
    }
    this.connect()
    this.handlers["_execjs"] = function (resolve, param) {
        var res = eval(param)
        if (!res) {
            resolve("没有返回值")
        } else {
            resolve(res)
        }

    }
}

Hlclient.prototype.connect = function () {
    console.log('begin of connect to wsURL: ' + this.wsURL);
    var _this = this;
    try {
        this.socket["ySocket"] = new WebSocket(this.wsURL);
        this.socket["ySocket"].onmessage = function (e) {
            try {
                let blob = e.data
                blob.text().then(data => {
                    _this.handlerRequest(data);
                })
            } catch {
                console.log("not blob")
                _this.handlerRequest(blob)
            }

        }
    } catch (e) {
        console.log("connection failed,reconnect after 10s");
        setTimeout(function () {
            _this.connect()
        }, 10000)
    }
    this.socket["ySocket"].onclose = function () {
        console.log("connection failed,reconnect after 10s");
        setTimeout(function () {
            _this.connect()
        }, 10000)
    }

};
Hlclient.prototype.send = function (msg) {
    this.socket["ySocket"].send(msg)
}

Hlclient.prototype.regAction = function (func_name, func) {
    if (typeof func_name !== 'string') {
        throw new Error("an func_name must be string");
    }
    if (typeof func !== 'function') {
        throw new Error("must be function");
    }
    console.log("register func_name: " + func_name);
    this.handlers[func_name] = func;
    return true

}

//收到消息后这里处理，
Hlclient.prototype.handlerRequest = function (requestJson) {
    var _this = this;
    var result = JSON.parse(requestJson);
    //console.log(result)
    if (!result['action']) {
        this.sendResult('', 'need request param {action}');
        return
    }
    var action = result["action"]
    var theHandler = this.handlers[action];
    if (!theHandler) {
        this.sendResult(action, 'action not found');
        return
    }
    try {
        if (!result["param"]) {
            theHandler(function (response) {
                _this.sendResult(action, response);
            })
        } else {
            var param = result["param"]
            try {
                param = JSON.parse(param)
            } catch (e) {
                console.log("")
            }
            theHandler(function (response) {
                _this.sendResult(action, response);
            }, param)
        }

    } catch (e) {
        console.log("error: " + e);
        _this.sendResult(action + e);
    }
}

Hlclient.prototype.sendResult = function (action, e) {
    this.send(action + atob("aGxeX14") + e);
}


// 连接通信
var client = new Hlclient("ws://127.0.0.1:12080/ws?group=group&name=name");

// 网页访问 http://localhost:12080/go?group=group&name=name&action=func_1&param=1

// 第二个参数为函数，resolve里面的值是想要的值(发送到服务器的)
// param是可传参参数，可以忽略，若为对象也需要转字符串处理
client.regAction("func_1", function (resolve, param) {
    console.log(resolve, param)
    t = Date.parse(new Date());
    var list = {
        "page": String(param),
        "sign": window.sign(String(param) + '|' + t.toString()),
        "t": t,
    }
    // resolve([list['page'], list['sign'], list['t']])
    resolve(JSON.stringify(list))     // resolve()函数只能输出一个字符串，故需要将对象处理转字符串
})



// promise = new Promise((resolve,reject)=>{
//     resolve({a:1,b:2,c:3}) 
// })
// promise.then(obj=>{
//     console.log(obj.a,obj.b,obj.c)
// })

(function () {
    var newElement = document.createElement("script");
    newElement.setAttribute("type", "text/javascript");
    newElement.setAttribute("src", "https://sekiro.virjar.com/sekiro-doc/assets/sekiro_web_client.js");
    document.body.appendChild(newElement);

    window.getH5fingerprint = utility.getH5fingerprint

    function guid() {
        function S4() {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        }

        return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }

    function startSekiro() {
        var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=rpc-test&clientId=" + guid());

        client.registerAction("action", function (request, resolve, reject) {
            resolve(window.getH5fingerprint(request["url"]));
        })
    }

    setTimeout(startSekiro, 2000)
})();


// 升级版
(function () {
    var newElement = document.createElement("script");
    newElement.setAttribute("type", "text/javascript");
    newElement.setAttribute("src", "https://sekiro.virjar.com/sekiro-doc/assets/sekiro_web_client.js");
    document.body.appendChild(newElement);

    window.getH5fingerprint = utility.getH5fingerprint;
    // 注意如下不能直接赋值函数方法，因为前面有对 encrypt 填充 publicKey。例如：window.getpassword = encrypt.encrypt 是不正确的;
    window.getpassword = encrypt;

    function guid() {
        function S4() {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        }

        return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }

    function startSekiro() {
        var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=rpc-test&clientId=" + guid());

        client.registerAction("action", function (request, resolve, reject) {
            resolve(
                {
                    "getH5fingerprint": window.getH5fingerprint(request["url"]),
                    "getpassword": window.getpassword.encrypt(request["password"]),
                }
            );
        })
    }

    setTimeout(startSekiro, 2000)
})();



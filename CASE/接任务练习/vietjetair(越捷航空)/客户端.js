// 升级版
(function () {
    var newElement = document.createElement("script");
    newElement.setAttribute("type", "text/javascript");
    newElement.setAttribute("src", "https://sekiro.virjar.com/sekiro-doc/assets/sekiro_web_client.js");
    document.body.appendChild(newElement);


    // window.getencrypted = H;

    function guid() {
        function S4() {
            return (((1 + Math.random()) * 0x10000) | 0).toString(16).substring(1);
        }

        return (S4() + S4() + "-" + S4() + "-" + S4() + "-" + S4() + "-" + S4() + S4() + S4());
    }

    function startSekiro() {
        var client = new SekiroClient("ws://127.0.0.1:5620/business-demo/register?group=rpc-test&clientId=" + guid());

        client.registerAction("action", function (request, resolve, reject) {
            console.log(request)
            resolve(
                {
                    "getencrypted": window.getencrypted.encrypt(request["data"], "base64"),
                }
            );
        })
    }

    setTimeout(startSekiro, 2000)
})();



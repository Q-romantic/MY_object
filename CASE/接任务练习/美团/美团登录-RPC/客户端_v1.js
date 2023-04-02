(function () {
    var ws = new WebSocket("ws://127.0.0.1:5620");  // 自定义端口

    ws.onmessage = function (evt) {
        console.log("Received Message: " + evt.data);
        if (evt.data == "exit") {
            ws.close();
        } else {
            ws.send(utility.getH5fingerprint(evt.data))
        }
    };
})();
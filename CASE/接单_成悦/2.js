(function () {
    'use strict';
    var cookieTemp = "";
    Object.defineProperty(document, 'cookie', {
        set: function (val) {
            console.log('Hook捕获到cookie设置->', val);
            if (val.indexOf('_QPWSDCXHZQA') != -1) {
                debugger;
            }
            cookieTemp = val;
            return val;
        },
        get: function () {
            return cookieTemp;
        }
    });
})();
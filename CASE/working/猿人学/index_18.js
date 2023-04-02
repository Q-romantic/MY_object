// var CryptoJS = CryptoJS || (function (Math, undefined) {
//     var C = {};
//     var C_lib = C.lib = {};
//     var Base = C_lib.Base = (function () {
//         function F() {};
//         return {
//             extend: function (overrides) {
//                 F.prototype = this;
//                 var subtype = new F();
//                 if (overrides) {
//                     subtype.mixIn(overrides);
//                 }
//                 if (!subtype.hasOwnProperty('init') || this.init === subtype.init) {
//                     subtype.init = function () {
//                         subtype.$super.init.apply(this, arguments);
//                     };
//                 }
//                 subtype.init.prototype = subtype;
//                 subtype.$super = this;
//                 return subtype;
//             }, create: function () {
//                 var instance = this.extend();
//                 instance.init.apply(instance, arguments);
//                 return instance;
//             }, init: function () {}, mixIn: function (properties) {
//                 for (var propertyName in properties) {
//                     if (properties.hasOwnProperty(propertyName)) {
//                         this[propertyName] = properties[propertyName];
//                     }
//                 }
//                 if (properties.hasOwnProperty('toString')) {
//                     this.toString = properties.toString;
//                 }
//             }, clone: function () {
//                 return this.init.prototype.extend(this);
//             }
//         };
//     }());
//     var WordArray = C_lib.WordArray = Base.extend({
//         init: function (words, sigBytes) {
//             words = this.words = words || [];
//             if (sigBytes != undefined) {
//                 this.sigBytes = sigBytes;
//             } else {
//                 this.sigBytes = words.length * 4;
//             }
//         }, toString: function (encoder) {
//             return (encoder || Hex).stringify(this);
//         }, concat: function (wordArray) {
//             var thisWords = this.words;
//             var thatWords = wordArray.words;
//             var thisSigBytes = this.sigBytes;
//             var thatSigBytes = wordArray.sigBytes;
//             this.clamp();
//             if (thisSigBytes % 4) {
//                 for (var i = 0; i < thatSigBytes; i++) {
//                     var thatByte = (thatWords[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
//                     thisWords[(thisSigBytes + i) >>> 2] |= thatByte << (24 - ((thisSigBytes + i) % 4) * 8);
//                 }
//             } else if (thatWords.length > 0xffff) {
//                 for (var i = 0; i < thatSigBytes; i += 4) {
//                     thisWords[(thisSigBytes + i) >>> 2] = thatWords[i >>> 2];
//                 }
//             } else {
//                 thisWords.push.apply(thisWords, thatWords);
//             }
//             this.sigBytes += thatSigBytes;
//             return this;
//         }, clamp: function () {
//             var words = this.words;
//             var sigBytes = this.sigBytes;
//             words[sigBytes >>> 2] &= 0xffffffff << (32 - (sigBytes % 4) * 8);
//             words.length = Math.ceil(sigBytes / 4);
//         }, clone: function () {
//             var clone = Base.clone.call(this);
//             clone.words = this.words.slice(0);
//             return clone;
//         }, random: function (nBytes) {
//             var words = [];
//             var r = (function (m_w) {
//                 var m_w = m_w;
//                 var m_z = 0x3ade68b1;
//                 var mask = 0xffffffff;
//                 return function () {
//                     m_z = (0x9069 * (m_z & 0xFFFF) + (m_z >> 0x10)) & mask;
//                     m_w = (0x4650 * (m_w & 0xFFFF) + (m_w >> 0x10)) & mask;
//                     var result = ((m_z << 0x10) + m_w) & mask;
//                     result /= 0x100000000;
//                     result += 0.5;
//                     return result * (Math.random() > .5 ? 1 : -1);
//                 }
//             });
//             for (var i = 0, rcache; i < nBytes; i += 4) {
//                 var _r = r((rcache || Math.random()) * 0x100000000);
//                 rcache = _r() * 0x3ade67b7;
//                 words.push((_r() * 0x100000000) | 0);
//             }
//             return new WordArray.init(words, nBytes);
//         }
//     });
//     var C_enc = C.enc = {};
//     var Hex = C_enc.Hex = {
//         stringify: function (wordArray) {
//             var words = wordArray.words;
//             var sigBytes = wordArray.sigBytes;
//             var hexChars = [];
//             for (var i = 0; i < sigBytes; i++) {
//                 var bite = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
//                 hexChars.push((bite >>> 4).toString(16));
//                 hexChars.push((bite & 0x0f).toString(16));
//             }
//             return hexChars.join('');
//         }, parse: function (hexStr) {
//             var hexStrLength = hexStr.length;
//             var words = [];
//             for (var i = 0; i < hexStrLength; i += 2) {
//                 words[i >>> 3] |= parseInt(hexStr.substr(i, 2), 16) << (24 - (i % 8) * 4);
//             }
//             return new WordArray.init(words, hexStrLength / 2);
//         }
//     };
//     var Latin1 = C_enc.Latin1 = {
//         stringify: function (wordArray) {
//             var words = wordArray.words;
//             var sigBytes = wordArray.sigBytes;
//             var latin1Chars = [];
//             for (var i = 0; i < sigBytes; i++) {
//                 var bite = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
//                 latin1Chars.push(String.fromCharCode(bite));
//             }
//             return latin1Chars.join('');
//         }, parse: function (latin1Str) {
//             var latin1StrLength = latin1Str.length;
//             var words = [];
//             for (var i = 0; i < latin1StrLength; i++) {
//                 words[i >>> 2] |= (latin1Str.charCodeAt(i) & 0xff) << (24 - (i % 4) * 8);
//             }
//             return new WordArray.init(words, latin1StrLength);
//         }
//     };
//     var Utf8 = C_enc.Utf8 = {
//         stringify: function (wordArray) {
//             try {
//                 return decodeURIComponent(escape(Latin1.stringify(wordArray)));
//             } catch (e) {
//                 throw new Error('Malformed UTF-8 data');
//             }
//         }, parse: function (utf8Str) {
//             return Latin1.parse(unescape(encodeURIComponent(utf8Str)));
//         }
//     };
//     var BufferedBlockAlgorithm = C_lib.BufferedBlockAlgorithm = Base.extend({
//         reset: function () {
//             this._data = new WordArray.init();
//             this._nDataBytes = 0;
//         }, _append: function (data) {
//             if (typeof data == 'string') {
//                 data = Utf8.parse(data);
//             }
//             this._data.concat(data);
//             this._nDataBytes += data.sigBytes;
//         }, _process: function (doFlush) {
//             var data = this._data;
//             var dataWords = data.words;
//             var dataSigBytes = data.sigBytes;
//             var blockSize = this.blockSize;
//             var blockSizeBytes = blockSize * 4;
//             var nBlocksReady = dataSigBytes / blockSizeBytes;
//             if (doFlush) {
//                 nBlocksReady = Math.ceil(nBlocksReady);
//             } else {
//                 nBlocksReady = Math.max((nBlocksReady | 0) - this._minBufferSize, 0);
//             }
//             var nWordsReady = nBlocksReady * blockSize;
//             var nBytesReady = Math.min(nWordsReady * 4, dataSigBytes);
//             if (nWordsReady) {
//                 for (var offset = 0; offset < nWordsReady; offset += blockSize) {
//                     this._doProcessBlock(dataWords, offset);
//                 }
//                 var processedWords = dataWords.splice(0, nWordsReady);
//                 data.sigBytes -= nBytesReady;
//             }
//             return new WordArray.init(processedWords, nBytesReady);
//         }, clone: function () {
//             var clone = Base.clone.call(this);
//             clone._data = this._data.clone();
//             return clone;
//         }, _minBufferSize: 0
//     });
//     var Hasher = C_lib.Hasher = BufferedBlockAlgorithm.extend({
//         cfg: Base.extend(),
//         init: function (cfg) {
//             this.cfg = this.cfg.extend(cfg);
//             this.reset();
//         }, reset: function () {
//             BufferedBlockAlgorithm.reset.call(this);
//             this._doReset();
//         }, update: function (messageUpdate) {
//             this._append(messageUpdate);
//             this._process();
//             return this;
//         }, finalize: function (messageUpdate) {
//             if (messageUpdate) {
//                 this._append(messageUpdate);
//             }
//             var hash = this._doFinalize();
//             return hash;
//         }, blockSize: 512 / 32,
//         _createHelper: function (hasher) {
//             return function (message, cfg) {
//                 return new hasher.init(cfg).finalize(message);
//             };
//         }, _createHmacHelper: function (hasher) {
//             return function (message, key) {
//                 return new C_algo.HMAC.init(hasher, key).finalize(message);
//             };
//         }
//     });
//     var C_algo = C.algo = {};
//     return C;
// }(Math));
//
// (function () {
//     var C = CryptoJS;
//     var C_lib = C.lib;
//     var WordArray = C_lib.WordArray;
//     var C_enc = C.enc;
//     var Base64 = C_enc.Base64 = {
//         stringify: function (wordArray) {
//             var words = wordArray.words;
//             var sigBytes = wordArray.sigBytes;
//             var map = this._map;
//             wordArray.clamp();
//             var base64Chars = [];
//             for (var i = 0; i < sigBytes; i += 3) {
//                 var byte1 = (words[i >>> 2] >>> (24 - (i % 4) * 8)) & 0xff;
//                 var byte2 = (words[(i + 1) >>> 2] >>> (24 - ((i + 1) % 4) * 8)) & 0xff;
//                 var byte3 = (words[(i + 2) >>> 2] >>> (24 - ((i + 2) % 4) * 8)) & 0xff;
//                 var triplet = (byte1 << 16) | (byte2 << 8) | byte3;
//                 for (var j = 0;
//                     (j < 4) && (i + j * 0.75 < sigBytes); j++) {
//                     base64Chars.push(map.charAt((triplet >>> (6 * (3 - j))) & 0x3f));
//                 }
//             }
//             var paddingChar = map.charAt(64);
//             if (paddingChar) {
//                 while (base64Chars.length % 4) {
//                     base64Chars.push(paddingChar);
//                 }
//             }
//             return base64Chars.join('');
//         }, parse: function (base64Str) {
//             var base64StrLength = base64Str.length;
//             var map = this._map;
//             var reverseMap = this._reverseMap;
//             if (!reverseMap) {
//                 reverseMap = this._reverseMap = [];
//                 for (var j = 0; j < map.length; j++) {
//                     reverseMap[map.charCodeAt(j)] = j;
//                 }
//             }
//             var paddingChar = map.charAt(64);
//             if (paddingChar) {
//                 var paddingIndex = base64Str.indexOf(paddingChar);
//                 if (paddingIndex !== -1) {
//                     base64StrLength = paddingIndex;
//                 }
//             }
//             return parseLoop(base64Str, base64StrLength, reverseMap);
//         }, _map: 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
//     };
//     function parseLoop(base64Str, base64StrLength, reverseMap) {
//         var words = [];
//         var nBytes = 0;
//         for (var i = 0; i < base64StrLength; i++) {
//             if (i % 4) {
//                 var bits1 = reverseMap[base64Str.charCodeAt(i - 1)] << ((i % 4) * 2);
//                 var bits2 = reverseMap[base64Str.charCodeAt(i)] >>> (6 - (i % 4) * 2);
//                 words[nBytes >>> 2] |= (bits1 | bits2) << (24 - (nBytes % 4) * 8);
//                 nBytes++;
//             }
//         }
//         return WordArray.create(words, nBytes);
//     }
// }());
//
// CryptoJS.lib.Cipher || (function (undefined) {
//     var C = CryptoJS;
//     var C_lib = C.lib;
//     var Base = C_lib.Base;
//     var WordArray = C_lib.WordArray;
//     var BufferedBlockAlgorithm = C_lib.BufferedBlockAlgorithm;
//     var C_enc = C.enc;
//     var Utf8 = C_enc.Utf8;
//     var Base64 = C_enc.Base64;
//     var C_algo = C.algo;
//     var EvpKDF = C_algo.EvpKDF;
//     var Cipher = C_lib.Cipher = BufferedBlockAlgorithm.extend({
//         cfg: Base.extend(),
//         createEncryptor: function (key, cfg) {
//             return this.create(this._ENC_XFORM_MODE, key, cfg);
//         }, createDecryptor: function (key, cfg) {
//             return this.create(this._DEC_XFORM_MODE, key, cfg);
//         }, init: function (xformMode, key, cfg) {
//             this.cfg = this.cfg.extend(cfg);
//             this._xformMode = xformMode;
//             this._key = key;
//             this.reset();
//         }, reset: function () {
//             BufferedBlockAlgorithm.reset.call(this);
//             this._doReset();
//         }, process: function (dataUpdate) {
//             this._append(dataUpdate);
//             return this._process();
//         }, finalize: function (dataUpdate) {
//             if (dataUpdate) {
//                 this._append(dataUpdate);
//             }
//             var finalProcessedData = this._doFinalize();
//             return finalProcessedData;
//         }, keySize: 128 / 32,
//         ivSize: 128 / 32,
//         _ENC_XFORM_MODE: 1,
//         _DEC_XFORM_MODE: 2,
//         _createHelper: (function () {
//             function selectCipherStrategy(key) {
//                 if (typeof key == 'string') {
//                     return PasswordBasedCipher;
//                 } else {
//                     return SerializableCipher;
//                 }
//             }
//             return function (cipher) {
//                 return {
//                     encrypt: function (message, key, cfg) {
//                         return selectCipherStrategy(key).encrypt(cipher, message, key, cfg);
//                     }, decrypt: function (ciphertext, key, cfg) {
//                         return selectCipherStrategy(key).decrypt(cipher, ciphertext, key, cfg);
//                     }
//                 };
//             };
//         }())
//     });
//     var StreamCipher = C_lib.StreamCipher = Cipher.extend({
//         _doFinalize: function () {
//             var finalProcessedBlocks = this._process(!!'flush');
//             return finalProcessedBlocks;
//         }, blockSize: 1
//     });
//     var C_mode = C.mode = {};
//     var BlockCipherMode = C_lib.BlockCipherMode = Base.extend({
//         createEncryptor: function (cipher, iv) {
//             return this.Encryptor.create(cipher, iv);
//         }, createDecryptor: function (cipher, iv) {
//             return this.Decryptor.create(cipher, iv);
//         }, init: function (cipher, iv) {
//             this._cipher = cipher;
//             this._iv = iv;
//         }
//     });
//     var CBC = C_mode.CBC = (function () {
//         var CBC = BlockCipherMode.extend();
//         CBC.Encryptor = CBC.extend({
//             processBlock: function (words, offset) {
//                 var cipher = this._cipher;
//                 var blockSize = cipher.blockSize;
//                 xorBlock.call(this, words, offset, blockSize);
//                 cipher.encryptBlock(words, offset);
//                 this._prevBlock = words.slice(offset, offset + blockSize);
//             }
//         });
//         CBC.Decryptor = CBC.extend({
//             processBlock: function (words, offset) {
//                 var cipher = this._cipher;
//                 var blockSize = cipher.blockSize;
//                 var thisBlock = words.slice(offset, offset + blockSize);
//                 cipher.decryptBlock(words, offset);
//                 xorBlock.call(this, words, offset, blockSize);
//                 this._prevBlock = thisBlock;
//             }
//         });
//
//         function xorBlock(words, offset, blockSize) {
//             var iv = this._iv;
//             if (iv) {
//                 var block = iv;
//                 this._iv = undefined;
//             } else {
//                 var block = this._prevBlock;
//             }
//             for (var i = 0; i < blockSize; i++) {
//                 words[offset + i] ^= block[i];
//             }
//         }
//         return CBC;
//     }());
//     var C_pad = C.pad = {};
//     var Pkcs7 = C_pad.Pkcs7 = {
//         pad: function (data, blockSize) {
//             var blockSizeBytes = blockSize * 4;
//             var nPaddingBytes = blockSizeBytes - data.sigBytes % blockSizeBytes;
//             var paddingWord = (nPaddingBytes << 24) | (nPaddingBytes << 16) | (nPaddingBytes << 8) | nPaddingBytes;
//             var paddingWords = [];
//             for (var i = 0; i < nPaddingBytes; i += 4) {
//                 paddingWords.push(paddingWord);
//             }
//             var padding = WordArray.create(paddingWords, nPaddingBytes);
//             data.concat(padding);
//         }, unpad: function (data) {
//             var nPaddingBytes = data.words[(data.sigBytes - 1) >>> 2] & 0xff;
//             data.sigBytes -= nPaddingBytes;
//         }
//     };
//     var BlockCipher = C_lib.BlockCipher = Cipher.extend({
//         cfg: Cipher.cfg.extend({
//             mode: CBC,
//             padding: Pkcs7
//         }),
//         reset: function () {
//             Cipher.reset.call(this);
//             var cfg = this.cfg;
//             var iv = cfg.iv;
//             var mode = cfg.mode;
//             if (this._xformMode == this._ENC_XFORM_MODE) {
//                 var modeCreator = mode.createEncryptor;
//             } else {
//                 var modeCreator = mode.createDecryptor;
//                 this._minBufferSize = 1;
//             } if (this._mode && this._mode.__creator == modeCreator) {
//                 this._mode.init(this, iv && iv.words);
//             } else {
//                 this._mode = modeCreator.call(mode, this, iv && iv.words);
//                 this._mode.__creator = modeCreator;
//             }
//         }, _doProcessBlock: function (words, offset) {
//             this._mode.processBlock(words, offset);
//         }, _doFinalize: function () {
//             var padding = this.cfg.padding;
//             if (this._xformMode == this._ENC_XFORM_MODE) {
//                 padding.pad(this._data, this.blockSize);
//                 var finalProcessedBlocks = this._process(!!'flush');
//             } else {
//                 var finalProcessedBlocks = this._process(!!'flush');
//                 padding.unpad(finalProcessedBlocks);
//             }
//             return finalProcessedBlocks;
//         }, blockSize: 128 / 32
//     });
//     var CipherParams = C_lib.CipherParams = Base.extend({
//         init: function (cipherParams) {
//             this.mixIn(cipherParams);
//         }, toString: function (formatter) {
//             return (formatter || this.formatter).stringify(this);
//         }
//     });
//     var C_format = C.format = {};
//     var OpenSSLFormatter = C_format.OpenSSL = {
//         stringify: function (cipherParams) {
//             var ciphertext = cipherParams.ciphertext;
//             var salt = cipherParams.salt;
//             if (salt) {
//                 var wordArray = WordArray.create([0x53616c74, 0x65645f5f]).concat(salt).concat(ciphertext);
//             } else {
//                 var wordArray = ciphertext;
//             }
//             return wordArray.toString(Base64);
//         }, parse: function (openSSLStr) {
//             var ciphertext = Base64.parse(openSSLStr);
//             var ciphertextWords = ciphertext.words;
//             if (ciphertextWords[0] == 0x53616c74 && ciphertextWords[1] == 0x65645f5f) {
//                 var salt = WordArray.create(ciphertextWords.slice(2, 4));
//                 ciphertextWords.splice(0, 4);
//                 ciphertext.sigBytes -= 16;
//             }
//             return CipherParams.create({
//                 ciphertext: ciphertext,
//                 salt: salt
//             });
//         }
//     };
//     var SerializableCipher = C_lib.SerializableCipher = Base.extend({
//         cfg: Base.extend({
//             format: OpenSSLFormatter
//         }),
//         encrypt: function (cipher, message, key, cfg) {
//             cfg = this.cfg.extend(cfg);
//             var encryptor = cipher.createEncryptor(key, cfg);
//             var ciphertext = encryptor.finalize(message);
//             var cipherCfg = encryptor.cfg;
//             return CipherParams.create({
//                 ciphertext: ciphertext,
//                 key: key,
//                 iv: cipherCfg.iv,
//                 algorithm: cipher,
//                 mode: cipherCfg.mode,
//                 padding: cipherCfg.padding,
//                 blockSize: cipher.blockSize,
//                 formatter: cfg.format
//             });
//         }, decrypt: function (cipher, ciphertext, key, cfg) {
//             cfg = this.cfg.extend(cfg);
//             ciphertext = this._parse(ciphertext, cfg.format);
//             var plaintext = cipher.createDecryptor(key, cfg).finalize(ciphertext.ciphertext);
//             return plaintext;
//         }, _parse: function (ciphertext, format) {
//             if (typeof ciphertext == 'string') {
//                 return format.parse(ciphertext, this);
//             } else {
//                 return ciphertext;
//             }
//         }
//     });
//     var C_kdf = C.kdf = {};
//     var OpenSSLKdf = C_kdf.OpenSSL = {
//         execute: function (password, keySize, ivSize, salt) {
//             if (!salt) {
//                 salt = WordArray.random(64 / 8);
//             }
//             var key = EvpKDF.create({
//                 keySize: keySize + ivSize
//             }).compute(password, salt);
//             var iv = WordArray.create(key.words.slice(keySize), ivSize * 4);
//             key.sigBytes = keySize * 4;
//             return CipherParams.create({
//                 key: key,
//                 iv: iv,
//                 salt: salt
//             });
//         }
//     };
//     var PasswordBasedCipher = C_lib.PasswordBasedCipher = SerializableCipher.extend({
//         cfg: SerializableCipher.cfg.extend({
//             kdf: OpenSSLKdf
//         }),
//         encrypt: function (cipher, message, password, cfg) {
//             cfg = this.cfg.extend(cfg);
//             var derivedParams = cfg.kdf.execute(password, cipher.keySize, cipher.ivSize);
//             cfg.iv = derivedParams.iv;
//             var ciphertext = SerializableCipher.encrypt.call(this, cipher, message, derivedParams.key, cfg);
//             ciphertext.mixIn(derivedParams);
//             return ciphertext;
//         }, decrypt: function (cipher, ciphertext, password, cfg) {
//             cfg = this.cfg.extend(cfg);
//             ciphertext = this._parse(ciphertext, cfg.format);
//             var derivedParams = cfg.kdf.execute(password, cipher.keySize, cipher.ivSize, ciphertext.salt);
//             cfg.iv = derivedParams.iv;
//             var plaintext = SerializableCipher.decrypt.call(this, cipher, ciphertext, derivedParams.key, cfg);
//             return plaintext;
//         }
//     });
// }());
//
// (function () {
//     var C = CryptoJS;
//     var C_lib = C.lib;
//     var BlockCipher = C_lib.BlockCipher;
//     var C_algo = C.algo;
//     var SBOX = [];
//     var INV_SBOX = [];
//     var SUB_MIX_0 = [];
//     var SUB_MIX_1 = [];
//     var SUB_MIX_2 = [];
//     var SUB_MIX_3 = [];
//     var INV_SUB_MIX_0 = [];
//     var INV_SUB_MIX_1 = [];
//     var INV_SUB_MIX_2 = [];
//     var INV_SUB_MIX_3 = [];
//     (function () {
//         var d = [];
//         for (var i = 0; i < 256; i++) {
//             if (i < 128) {
//                 d[i] = i << 1;
//             } else {
//                 d[i] = (i << 1) ^ 0x11b;
//             }
//         }
//         var x = 0;
//         var xi = 0;
//         for (var i = 0; i < 256; i++) {
//             var sx = xi ^ (xi << 1) ^ (xi << 2) ^ (xi << 3) ^ (xi << 4);
//             sx = (sx >>> 8) ^ (sx & 0xff) ^ 0x63;
//             SBOX[x] = sx;
//             INV_SBOX[sx] = x;
//             var x2 = d[x];
//             var x4 = d[x2];
//             var x8 = d[x4];
//             var t = (d[sx] * 0x101) ^ (sx * 0x1010100);
//             SUB_MIX_0[x] = (t << 24) | (t >>> 8);
//             SUB_MIX_1[x] = (t << 16) | (t >>> 16);
//             SUB_MIX_2[x] = (t << 8) | (t >>> 24);
//             SUB_MIX_3[x] = t;
//             var t = (x8 * 0x1010101) ^ (x4 * 0x10001) ^ (x2 * 0x101) ^ (x * 0x1010100);
//             INV_SUB_MIX_0[sx] = (t << 24) | (t >>> 8);
//             INV_SUB_MIX_1[sx] = (t << 16) | (t >>> 16);
//             INV_SUB_MIX_2[sx] = (t << 8) | (t >>> 24);
//             INV_SUB_MIX_3[sx] = t;
//             if (!x) {
//                 x = xi = 1;
//             } else {
//                 x = x2 ^ d[d[d[x8 ^ x2]]];
//                 xi ^= d[d[xi]];
//             }
//         }
//     }());
//     var RCON = [0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36];
//     var AES = C_algo.AES = BlockCipher.extend({
//         _doReset: function () {
//             if (this._nRounds && this._keyPriorReset === this._key) {
//                 return;
//             }
//             var key = this._keyPriorReset = this._key;
//             var keyWords = key.words;
//             var keySize = key.sigBytes / 4;
//             var nRounds = this._nRounds = keySize + 6;
//             var ksRows = (nRounds + 1) * 4;
//             var keySchedule = this._keySchedule = [];
//             for (var ksRow = 0; ksRow < ksRows; ksRow++) {
//                 if (ksRow < keySize) {
//                     keySchedule[ksRow] = keyWords[ksRow];
//                 } else {
//                     var t = keySchedule[ksRow - 1];
//                     if (!(ksRow % keySize)) {
//                         t = (t << 8) | (t >>> 24);
//                         t = (SBOX[t >>> 24] << 24) | (SBOX[(t >>> 16) & 0xff] << 16) | (SBOX[(t >>> 8) & 0xff] << 8) | SBOX[t & 0xff];
//                         t ^= RCON[(ksRow / keySize) | 0] << 24;
//                     } else if (keySize > 6 && ksRow % keySize == 4) {
//                         t = (SBOX[t >>> 24] << 24) | (SBOX[(t >>> 16) & 0xff] << 16) | (SBOX[(t >>> 8) & 0xff] << 8) | SBOX[t & 0xff];
//                     }
//                     keySchedule[ksRow] = keySchedule[ksRow - keySize] ^ t;
//                 }
//             }
//             var invKeySchedule = this._invKeySchedule = [];
//             for (var invKsRow = 0; invKsRow < ksRows; invKsRow++) {
//                 var ksRow = ksRows - invKsRow;
//                 if (invKsRow % 4) {
//                     var t = keySchedule[ksRow];
//                 } else {
//                     var t = keySchedule[ksRow - 4];
//                 } if (invKsRow < 4 || ksRow <= 4) {
//                     invKeySchedule[invKsRow] = t;
//                 } else {
//                     invKeySchedule[invKsRow] = INV_SUB_MIX_0[SBOX[t >>> 24]] ^ INV_SUB_MIX_1[SBOX[(t >>> 16) & 0xff]] ^ INV_SUB_MIX_2[SBOX[(t >>> 8) & 0xff]] ^ INV_SUB_MIX_3[SBOX[t & 0xff]];
//                 }
//             }
//         }, encryptBlock: function (M, offset) {
//             this._doCryptBlock(M, offset, this._keySchedule, SUB_MIX_0, SUB_MIX_1, SUB_MIX_2, SUB_MIX_3, SBOX);
//         }, decryptBlock: function (M, offset) {
//             var t = M[offset + 1];
//             M[offset + 1] = M[offset + 3];
//             M[offset + 3] = t;
//             this._doCryptBlock(M, offset, this._invKeySchedule, INV_SUB_MIX_0, INV_SUB_MIX_1, INV_SUB_MIX_2, INV_SUB_MIX_3, INV_SBOX);
//             var t = M[offset + 1];
//             M[offset + 1] = M[offset + 3];
//             M[offset + 3] = t;
//         }, _doCryptBlock: function (M, offset, keySchedule, SUB_MIX_0, SUB_MIX_1, SUB_MIX_2, SUB_MIX_3, SBOX) {
//             var nRounds = this._nRounds;
//             var s0 = M[offset] ^ keySchedule[0];
//             var s1 = M[offset + 1] ^ keySchedule[1];
//             var s2 = M[offset + 2] ^ keySchedule[2];
//             var s3 = M[offset + 3] ^ keySchedule[3];
//             var ksRow = 4;
//             for (var round = 1; round < nRounds; round++) {
//                 var t0 = SUB_MIX_0[s0 >>> 24] ^ SUB_MIX_1[(s1 >>> 16) & 0xff] ^ SUB_MIX_2[(s2 >>> 8) & 0xff] ^ SUB_MIX_3[s3 & 0xff] ^ keySchedule[ksRow++];
//                 var t1 = SUB_MIX_0[s1 >>> 24] ^ SUB_MIX_1[(s2 >>> 16) & 0xff] ^ SUB_MIX_2[(s3 >>> 8) & 0xff] ^ SUB_MIX_3[s0 & 0xff] ^ keySchedule[ksRow++];
//                 var t2 = SUB_MIX_0[s2 >>> 24] ^ SUB_MIX_1[(s3 >>> 16) & 0xff] ^ SUB_MIX_2[(s0 >>> 8) & 0xff] ^ SUB_MIX_3[s1 & 0xff] ^ keySchedule[ksRow++];
//                 var t3 = SUB_MIX_0[s3 >>> 24] ^ SUB_MIX_1[(s0 >>> 16) & 0xff] ^ SUB_MIX_2[(s1 >>> 8) & 0xff] ^ SUB_MIX_3[s2 & 0xff] ^ keySchedule[ksRow++];
//                 s0 = t0;
//                 s1 = t1;
//                 s2 = t2;
//                 s3 = t3;
//             }
//             var t0 = ((SBOX[s0 >>> 24] << 24) | (SBOX[(s1 >>> 16) & 0xff] << 16) | (SBOX[(s2 >>> 8) & 0xff] << 8) | SBOX[s3 & 0xff]) ^ keySchedule[ksRow++];
//             var t1 = ((SBOX[s1 >>> 24] << 24) | (SBOX[(s2 >>> 16) & 0xff] << 16) | (SBOX[(s3 >>> 8) & 0xff] << 8) | SBOX[s0 & 0xff]) ^ keySchedule[ksRow++];
//             var t2 = ((SBOX[s2 >>> 24] << 24) | (SBOX[(s3 >>> 16) & 0xff] << 16) | (SBOX[(s0 >>> 8) & 0xff] << 8) | SBOX[s1 & 0xff]) ^ keySchedule[ksRow++];
//             var t3 = ((SBOX[s3 >>> 24] << 24) | (SBOX[(s0 >>> 16) & 0xff] << 16) | (SBOX[(s1 >>> 8) & 0xff] << 8) | SBOX[s2 & 0xff]) ^ keySchedule[ksRow++];
//             M[offset] = t0;
//             M[offset + 1] = t1;
//             M[offset + 2] = t2;
//             M[offset + 3] = t3;
//         }, keySize: 256 / 32
//     });
//     C.AES = BlockCipher._createHelper(AES);
// }());
//
// // var key = CryptoJS.enc.Utf8.parse("0123456789abcdef");
// // var iv = CryptoJS.enc.Utf8.parse("0123456789abcdef");
// var key = CryptoJS.enc.Utf8.parse("620f38c8620f38c8");
// var iv = CryptoJS.enc.Utf8.parse("620f38c8620f38c8");
//
// function AES_Encrypt(word) {
//     var srcs = CryptoJS.enc.Utf8.parse(word);
//     var encrypted = CryptoJS.AES.encrypt(srcs, key, {
//         iv: iv,
//         mode: CryptoJS.mode.CBC,
//         padding: CryptoJS.pad.Pkcs7
//     });
//     return CryptoJS.enc.Hex.stringify(CryptoJS.enc.Base64.parse(encrypted.toString()));
// }
//
// function AES_Decrypt(word) {
//     var srcs = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Hex.parse(word));
//     var decrypt = CryptoJS.AES.decrypt(srcs, key, {
//         iv: iv,
//         mode: CryptoJS.mode.CBC,
//         padding: CryptoJS.pad.Pkcs7
//     });
//     return CryptoJS.enc.Utf8.stringify(decrypt).toString();
// }
//

//
// v: 'TPX1Cm7JNb419NS7+GYNvn2YUo2DQUxG6LoyujSBjNSSiW5vKX6BLXzSJcF9u4fx'
// console.log('00000')
// // console.log(AES_Decrypt("qvWc1ocST3u9jNjIZz+Fy/MvkA0bos29ctQ9I58osUGVMz+aOCtHzeSCoTCzckSv"))
// console.log(AES_Encrypt('2|800m312,800d312,800m312,800m312,800u312'))


const CryptoJS = require("crypto-js");  // npm install crypto-js

function AESencrypt(data, key, iv) { //key,iv：16位的字符串
    var key1 = CryptoJS.enc.Utf8.parse(key);
    var iv1 = CryptoJS.enc.Utf8.parse(iv);
    return CryptoJS.AES.encrypt(data, key1, {
        iv: iv1,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    }).toString();
}


// t：1645164744
// text：'2|800m312,800d312,800m312,800m312,800u312'
// key、iv：620f38c8620f38c8

function get_v(t, page) {
    var key = iv = t.toString(16) + t.toString(16)
    data = page.toString() + "|" + "800m312,800d312,800m312,800m312,800u312"
    res = AESencrypt(data, key, iv)
    return res
    // console.log(res) // -> TPX1Cm7JNb419NS7+GYNvn2YUo2DQUxG6LoyujSBjNSSiW5vKX6BLXzSJcF9u4fx
}


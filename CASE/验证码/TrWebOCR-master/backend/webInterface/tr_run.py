#!/usr/bin/env python
# encoding: utf-8
# author:alisen
# time: 2020/4/29 10:47

import time
import cv2
import numpy as np
from backend.tr import tr
import tornado.web
import tornado.gen
import tornado.httpserver
import base64
from PIL import Image, ImageDraw
from io import BytesIO
import datetime
import json

from backend.tools.np_encoder import NpEncoder
from backend.tools import log
import logging

logger = logging.getLogger(log.LOGGER_ROOT_NAME + '.' + __name__)


class TrRun(tornado.web.RequestHandler):
    '''
    使用 tr 的 run 方法
    '''

    def get(self):
        self.set_status(404)
        self.write("404 : Please use POST")

    @tornado.gen.coroutine
    def post(self):
        '''

        :return:
        报错：
        400 没有请求参数

        '''
        start_time = time.time()
        MAX_SIZE = 1600

        img_up = self.request.files.get('file', None)
        img_b64 = self.get_argument('img', None)
        compress_size = self.get_argument('compress', None)
        is_draw = self.get_argument("is_draw", None)

        # 判断是上传的图片还是base64
        self.set_header('content-type', 'application/json')
        up_image_type = None
        if img_up is not None and len(img_up) > 0:
            img_up = img_up[0]
            up_image_type = img_up.content_type
            up_image_name = img_up.filename
            img = Image.open(BytesIO(img_up.body))
        elif img_b64 is not None:
            raw_image = base64.b64decode(img_b64.encode('utf8'))
            img = Image.open(BytesIO(raw_image))
        else:
            self.set_status(400)
            logger.error(json.dumps({'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
            self.finish(json.dumps({'code': 400, 'msg': '没有传入参数'}, cls=NpEncoder))
            return

        # 旋转图片
        try:
            if hasattr(img, '_getexif') and img._getexif() is not None:
                orientation = 274
                exif = dict(img._getexif().items())
                if orientation in exif:
                    if exif[orientation] == 3:
                        img = img.rotate(180, expand=True)
                    elif exif[orientation] == 6:
                        img = img.rotate(270, expand=True)
                    elif exif[orientation] == 8:
                        img = img.rotate(90, expand=True)
        except Exception as ex:
            error_log = json.dumps({'code': 400, 'msg': '产生了一点错误，请检查日志', 'err': str(ex)}, cls=NpEncoder)
            logger.error(error_log, exc_info=True)
            self.finish(error_log)
            return
        img = img.convert("RGB")

        '''
        是否开启图片压缩
        默认为1600px
        值为 0 时表示不开启压缩
        非 0 时则压缩到该值的大小
        '''
        if compress_size is not None:
            try:
                compress_size = int(compress_size)
            except ValueError as ex:
                logger.error(exc_info=True)
                self.finish(json.dumps({'code': 400, 'msg': 'compress参数类型有误，只能是int类型'}, cls=NpEncoder))
                return

            if compress_size < 1:
                MAX_SIZE = max(img.height, img.width)
            else:
                MAX_SIZE = compress_size

        if img.height > MAX_SIZE or img.width > MAX_SIZE:
            scale = max(img.height / MAX_SIZE, img.width / MAX_SIZE)

            new_width = int(img.width / scale + 0.5)
            new_height = int(img.height / scale + 0.5)
            img = img.resize((new_width, new_height), Image.ANTIALIAS)

        # 进行ocr
        res = tr.run(img.copy().convert("L"), flag=tr.FLAG_ROTATED_RECT)

        response_data = {'code': 200, 'msg': '成功',
                         'data': {'raw_out': res,
                                  'speed_time': round(time.time() - start_time, 2)}}
        if is_draw != '0':
            img_detected = img.copy()
            img_draw = ImageDraw.Draw(img_detected)
            colors = ['red', 'green', 'blue', "purple"]

            for i, r in enumerate(res):
                rect, txt, confidence = r
                ''' 
                    cx: 中心点x
                    xy: 中心点y
                    w:  宽度
                    h:  高度
                    a:  旋转角度
                '''
                cx, cy, w, h, a = rect
                box = cv2.boxPoints(((cx, cy), (w, h), a))
                box = np.int0(np.round(box))

                for p1, p2 in [(0, 1), (1, 2), (2, 3), (3, 0)]:
                    img_draw.line(xy=(box[p1][0], box[p1][1], box[p2][0], box[p2][1]), fill=colors[i % len(colors)],
                                  width=2)

            output_buffer = BytesIO()
            img_detected.save(output_buffer, format='JPEG')
            byte_data = output_buffer.getvalue()
            img_detected_b64 = base64.b64encode(byte_data).decode('utf8')

            response_data['data']['img_detected'] = 'data:image/jpeg;base64,' + img_detected_b64
        log_info = {
            'ip': self.request.host,
            'return': response_data,
            'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        logger.info(json.dumps(log_info, cls=NpEncoder))
        self.finish(json.dumps(response_data,
                               cls=NpEncoder))
        return

import pprint
import time, requests, re, json, subprocess
from hashlib import md5
import execjs


class IQIYI:

    def __init__(self, cookie):
        self.cookie = cookie

    def get_vf(self, a):
        index = open('iqiyi.js', 'r', encoding='utf-8')
        js = execjs.compile(index.read())
        a = js.call('get_vf', a)
        return a

    def authKey_md5(self, tm, tvid):
        text = "d41d8cd98f00b204e9800998ecf8427e" + tm + tvid
        res = md5(text.encode()).hexdigest()
        return res

    def html_parser(self, url):
        resp = requests.get(url=url, headers={})
        data = resp.content.decode("utf-8")
        # print(data)
        playPageInfo = re.findall('window\..*?=(\{.*?\});', data)[0]
        playPageInfo = json.loads(playPageInfo)
        # pprint.pprint(playPageInfo)
        title = playPageInfo['shortTitle']
        tvid = playPageInfo['tvId']
        vid = playPageInfo['vid']

        return {"title": title, "tvid": str(tvid), "vid": vid}

    def play(self, x):
        text = 'ffplay -protocol_whitelist "file,http,https,rtp,udp,tcp,tls" -loglevel quiet -i "%s"' % x
        subprocess.call(text, shell=True)

    def m3u8_down(self, title, text):
        with open(f"m3u8_down\\{title}.m3u8.txt", "w") as f:
            f.write(text)

    def m3u8_url(self, tvid, vid, authkey, tm, vf):
        url = "https://cache.video.iqiyi.com/dash"
        params = {
            "tvid": tvid,  # 视频ID
            "bid": "600",  # 1080P 600  超清值为500，  高清值为300
            "vid": vid,  # 值可变，可为空，源码可得值
            "src": "01010031010000000000",
            "vt": "0",
            "rs": "1",
            "uid": "628184907449420",  # 未登陆是空
            "ori": "pcw",
            "ps": "0",  # 超清值为0，  高清值为 1
            "k_uid": "c55d485ee178762fe5e2135b9bddf52d",
            # 未登陆是 40828cdfb5dbdb55492bd373d1720881     c55d485ee178762fe5e2135b9bddf52d
            "pt": "0",
            "d": "0",
            "s": "",
            "lid": "",
            "cf": "",
            "ct": "",
            "authKey": authkey,  # 变化值 md5("d41d8cd98f00b204e9800998ecf8427e"+tm+tvid) 测试为真
            "k_tag": "1",
            "ost": "0",  # 超清值为 0 ， 高清值为 undefined
            "ppt": "0",  # 超清值为 0 ， 高清值为 undefined
            "dfp": "a0373263bc4e6a45538738180efbee117e17a685d4a066dc60d1c316825045623c",  # 可能固定，也可能变，待观察
            "locale": "zh_cn",
            "prio": '{"ff":"f4v","code":2}',
            "pck": "7beFNi8KSGasx94870BzsDHSKGhfCR6VFBGZt7QSgKsQ81m1yfqm1sKKm2u4B6KBwm3Am3ta3",
            "k_err_retries": "0",
            "up": "",
            "qd_v": "2",
            "tm": tm,  # 这个值还不能随便给时间戳，估计与其他值有联系， 这里一变，其他值也应要变
            "qdy": "a",
            "qds": "0",
            "k_ft1": "706436220846084",
            "k_ft4": "36283952406532",
            "k_ft5": "1",
            "bop": '{"version":"10.0","dfp":"a0373263bc4e6a45538738180efbee117e17a685d4a066dc60d1c316825045623c"}',
            "ut": "0",
            "vf": vf,  # 变化值
        }

        resp = requests.get(url=url, params=params)
        # print(resp.text)
        data = json.loads(resp.content.decode("utf-8"))
        video = data["data"]["program"]["video"]
        video_m3u8 = []
        for v in video:
            if v.get("m3u8"):
                m3u8 = v["m3u8"]  # m3u8文件源码
                scrsz = v["scrsz"]  # 视频分辨率
                vsize = v["vsize"]  # 视频大小
                v_url = re.compile("(http://.*?)#", re.S | re.M | re.I)
                video_url = v_url.findall(m3u8)[-1]  # 匹配到最后一段m3u8地址， 然后替换 start 开始位置为 0
                start = re.compile("(start=.*?)&")
                start = start.findall(video_url)[0]
                video_url = video_url.replace(start, "start=0")
                vsize = '{:.1f}'.format(float(vsize) / 1048576)  # 1048576 是 1024*1024的积， 是由bit,转换成M 经过两次转换
                video_m3u8.append({"video_url": video_url, "m3u8": m3u8, "scrsz": scrsz, "vsize": vsize})
        return video_m3u8

    def start(self, url):
        try:
            data = self.html_parser(url)
            # print(data)
            tm = str(int(time.time() * 1000))
            title = data["title"]
            tvid = data["tvid"]
            vid = data["vid"]
            authkey = self.authKey_md5(tm, tvid)
            url_vf = f"/dash?tvid={tvid}&bid=600&vid={vid}&src=01010031010000000000&vt=0&rs=1&uid=628184907449420&ori=pcw&ps=0&k_uid=c55d485ee178762fe5e2135b9bddf52d&pt=0&d=0&s=&lid=&cf=&ct=&authKey={authkey}&k_tag=1&ost=0&ppt=0&dfp=a0373263bc4e6a45538738180efbee117e17a685d4a066dc60d1c316825045623c&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&pck=7beFNi8KSGasx94870BzsDHSKGhfCR6VFBGZt7QSgKsQ81m1yfqm1sKKm2u4B6KBwm3Am3ta3&k_err_retries=0&up=&qd_v=2&tm={tm}&qdy=a&qds=0&k_ft1=706436220846084&k_ft4=36283952406532&k_ft5=1&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22a0373263bc4e6a45538738180efbee117e17a685d4a066dc60d1c316825045623c%22%7D&ut=0"
            vf = self.get_vf(url_vf)
            video_m3u8 = self.m3u8_url(tvid, vid, authkey, tm, vf)
            for video in video_m3u8:
                video_url = video["video_url"]
                m3u8 = video["m3u8"]
                scrsz = video["scrsz"]
                vsize = video["vsize"]
                name = f"{title}_分辨率-{scrsz}_视频大小-{vsize}M"
                # self.m3u8_down(name, m3u8)  # 保存m3u8文件
                print(f"{name}.m3u8 文件缓存完成，保存在m3u8_down文件夹中")
                print(f"m3u8播放地址 >>> {video_url}")
                # file_path = "./m3u8_down/" + name + ".m3u8"
                # self.play(file_path)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    # # 使用前，设置爱奇艺的cookie
    cookie = 'QC005=0cdeacebe253b1ad40190acf36ea6324; QC006=c427f7c430de6f8499b557345a035c6e; QP0030=1; QC173=0; P00004=.1625663848.c1b8b2ef98; user_type=web; QC170=1; SDKENTERTYPE=normal_login; GC_PCA=false; T00404=aed185152a4c04e518bcab8c1e8281f3; QIYUECK=qy_pc_71f21f31bc714f83a19df711fb53fa3f; TQC030=1; QP008=0; _ga=GA1.2.2116955020.1655029929; QC008=1632826003.1655029929.1656655373.11; QC175={"upd":true,"ct":""}; nu=0; QP0034={"v":1,"m":{"wm-vp9":1}}; QP0033=1; QC007=DIRECT; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1655029929,1656659677; __dfp=a1fc1f8bb5ba6b4f0fb19443be939cb8c2ccee677efaa53bd1f1523f48701c55b1@1657951374312@1656655375312; QP007=480; QP0036=202271|616.796; QP0035=2; QC159={"color":"FFFFFF","channelConfig":0,"hadTip":1,"isOpen":1,"speed":10,"density":40,"opacity":86,"isFilterColorFont":1,"isOpenMask":0,"proofShield":0,"forcedFontSize":24,"isFilterImage":1,"defaultSwitch":0,"isset":1,"openRecord":[1656655495449]}; Hm_lpvt_53b7374a63c37483e5dd97d78d9bb36e=1656668802; QC010=94019865; IMS=IggQARj_s_yVBiorCiBmOWNmZmRmZTIzMjExMmYxZmZlN2I3MGI0MzBlNjAzYxAAIgAo6AIwBXIkCiBmOWNmZmRmZTIzMjExMmYxZmZlN2I3MGI0MzBlNjAzYxAAggEAigEkCiIKIGY5Y2ZmZGZlMjMyMTEyZjFmZmU3YjcwYjQzMGU2MDNj; QP0027=17; T00700=EgcI9L-tIRABEgcI67-tIRAMEgcI58DtIRABEgcI8L-tIRABEgcIz7-tIRABEgcIkMDtIRABEgcIg8DtIRABEgcI0b-tIRABEgcI4b-tIRABEgcIhcDtIRABEgcIi8HtIRANEgcI87-tIRABEgcI7L-tIRABEgcImMDtIRABEgcI57-tIRABEgcIisHtIRAC; QP0037=575'
    iqiyi = IQIYI(cookie)
    url = 'https://www.iqiyi.com/v_1zo488bnv6s.html'  # 单集链接
    # url = 'https://www.iqiyi.com/v_20x944zloks.html'
    iqiyi.start(url)

    # url = 'https://hey05.cjkypo.com/20220329/1tMPxKtW/1100kb/hls/Lrw9oeSW.ts'
    # r = requests.get(url).content
    # with open(f"m3u8_down\\1.ts", "wb") as f:
    #     f.write(r)

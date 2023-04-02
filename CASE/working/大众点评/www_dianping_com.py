# -*- coding: utf-8 -*-
import requests
import base64
import zlib
import time
from jsonpath import jsonpath
import re
from lxml import etree
from PIL import ImageFont, Image, ImageDraw
from io import BytesIO
import ddddocr
from fontTools.ttLib import TTFont
from fontTools.ttLib.woff2 import decompress

# url = 'http://www.dianping.com/shop/l2zTH0M64V5o9our'
# url = 'http://www.dianping.com/shop/H3SyNUSShP5BYm87'
# url = 'http://www.dianping.com/shop/l3n4jWYuQPhDSKsE'
url = 'http://www.dianping.com/shop/ivbjaqnpAdOCsiY4'
url_i = 'http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo'
url_s = 'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar'
url_p = 'http://www.dianping.com/ajax/json/shopDynamic/allReview'

info = str(
    {"rId": "", "ts": int(time.time() * 1000), "cts": int(time.time() * 1000) + 100, "brVD": [], "brR": [], "bI": [],
     "mT": [], "kT": [], "aT": [], "tT": [], "sign": 'eJwDAAAAAAE='}).encode()
token = base64.b64encode(zlib.compress(info)).decode()

full_url = [
    'http://www.dianping.com/ajax/json/shopDynamic/fav',
    'http://www.dianping.com/ajax/json/shopDynamic/reviewAndStar',
    'http://www.dianping.com/ajax/json/shopDynamic/shopAlbum',
    'http://www.dianping.com/ajax/json/shopDynamic/searchPromo',
    'http://www.dianping.com/ajax/json/shopDynamic/shopTabs',
    'http://www.dianping.com/ajax/json/shopDynamic/addReview',
    'http://www.dianping.com/ajax/json/shopDynamic/myReview',
    'http://www.dianping.com/ajax/json/shopDynamic/friendReviews',
    'http://www.dianping.com/ajax/json/shopDynamic/allReview',
    'http://www.dianping.com/ajax/json/shopDynamic/basicHideInfo',
    'http://www.dianping.com/ajax/json/shopDynamic/shopAside',
    'http://www.dianping.com/ajax/json/shopDynamic/promoInfo',

]

full_data = {
    'shopId': url[-16:],  # 数据由字典source_data_2更新
    'uuid': 'd0bc69ea-087f-04f7-ca47-ca53213761fb.1637378507',
    'platform': '1',
    'partner': '150',
    'optimusCode': '10',
    'originUrl': 'http://www.dianping.com/shop/' + url[-16:],
    'cityId': '2',  # 数据由字典source_data_1更新
    'mainCategoryId': '114',  # 数据由字典source_data_2更新
    'defaultPic': '',  # 数据由字典source_data_2更新
    'power': '5',  # 数据由字典source_data_2更新
    'shopType': '10',  # 数据由字典source_data_2更新
    'shopName': '',  # 数据由字典source_data_2更新
    'shopCityId': '2',  # 数据由字典source_data_2更新
    'cityName': '北京',  # 数据由字典source_data_1更新
    'shopGroupId': '',  # 数据由字典source_data_2更新
    'pn': '1',
    'tcv': 'ro4xcqvykp',
    'mainRegionId': '1489',  # 数据由字典source_data_2更新
    'cityEnName': 'beijing',  # 数据由字典source_data_1更新
    '_token': token,
}

headers = {
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
}

proxy = '183.173.121.168:10080'

proxies = {
    "http": "http://" + proxy,
    "https": "http://" + proxy,
}

dic_data = {'shopdesc': {'x': '', 'unie004': '满', 'unie010': '养', 'unie015': '楼', 'unie02c': '教', 'unie030': '办',
                         'unie032': '限', 'unie03b': '皮', 'unie049': '木', 'unie04b': '饭', 'unie075': '体', 'unie076': '河',
                         'unie07e': '值', 'unie07f': '成', 'unie081': '置', 'unie087': '顺', 'unie096': '容', 'unie099': '着',
                         'unie0a2': '七', 'unie0a7': '管', 'unie0ae': '客', 'unie0b0': '房', 'unie0b2': '评', 'unie0bc': '热',
                         'unie0d3': '买', 'unie0d5': '厂', 'unie0df': '朋', 'unie0e4': '溪', 'unie0e8': '湾', 'unie0ef': '都',
                         'unie0f1': '厦', 'unie0f2': '一', 'unie0f5': '佳', 'unie0fe': '些', 'unie106': '恒', 'unie116': '设',
                         'unie128': '底', 'unie12c': '现', 'unie12d': '主', 'unie134': '年', 'unie13d': '知', 'unie140': '货',
                         'unie151': '看', 'unie153': '老', 'unie15a': '让', 'unie15e': '科', 'unie161': '活', 'unie175': '幢',
                         'unie17a': '陵', 'unie17e': '0', 'unie18e': '实', 'unie198': '会', 'unie1a6': '锦', 'unie1a7': '拍',
                         'unie1ac': '服', 'unie1ad': '宁', 'unie1af': '豆', 'unie1b4': '造', 'unie1bd': '味', 'unie1de': '还',
                         'unie1e1': '本', 'unie1ee': '红', 'unie1ef': '汤', 'unie1ff': '女', 'unie21b': '接', 'unie21c': '十',
                         'unie21f': '赞', 'unie221': '机', 'unie238': '凤', 'unie23a': '校', 'unie23f': '姐', 'unie240': '式',
                         'unie246': '们', 'unie24d': '尔', 'unie261': '进', 'unie269': '铺', 'unie276': '莲', 'unie278': '隆',
                         'unie299': '计', 'unie2b2': 'j', 'unie2b7': '杂', 'unie2c7': '用', 'unie2ce': '间', 'unie2f7': '他',
                         'unie2f9': '份', 'unie2fa': '宏', 'unie2fe': '全', 'unie304': '串', 'unie30b': '谷', 'unie310': '嘉',
                         'unie312': '鑫', 'unie315': '出', 'unie31b': '滨', 'unie31d': '干', 'unie32b': '弄', 'unie34c': '厅',
                         'unie370': '吉', 'unie373': '友', 'unie37c': '之', 'unie380': '到', 'unie383': '销', 'unie385': '快',
                         'unie387': '运', 'unie38d': '助', 'unie39d': '泰', 'unie3a4': '交', 'unie3af': '我', 'unie3dd': '区',
                         'unie3e4': '苑', 'unie3e9': '坊', 'unie405': '旁', 'unie424': '玉', 'unie42b': '材', 'unie433': '两',
                         'unie43b': '的', 'unie43c': '对', 'unie447': '料', 'unie449': '政', 'unie450': '刚', 'unie464': '与',
                         'unie479': '角', 'unie489': '原', 'unie4a2': '地', 'unie4a4': '龙', 'unie4a7': '重', 'unie4aa': '酸',
                         'unie4ba': '品', 'unie4c2': '汽', 'unie4c8': '别', 'unie4d1': '纪', 'unie4f0': '文', 'unie4fa': '行',
                         'unie4fd': '挺', 'unie50f': '内', 'unie543': '南', 'unie554': '样', 'unie557': '环', 'unie560': '斜',
                         'unie579': '京', 'unie57a': '欢', 'unie58e': '世', 'unie58f': '精', 'unie59d': '冥', 'unie59f': '跟',
                         'unie5a1': '己', 'unie5af': '清', 'unie5b6': '武', 'unie5b9': '片', 'unie5c9': '联', 'unie5cf': '网',
                         'unie5eb': '么', 'unie5f0': '居', 'unie5fe': '华', 'unie5ff': '种', 'unie615': '江', 'unie621': '哈',
                         'unie625': '团', 'unie62a': '庄', 'unie636': '专', 'unie662': '旗', 'unie66b': '州', 'unie67b': '像',
                         'unie691': '多', 'unie6a7': '井', 'unie6c7': '面', 'unie6cf': '记', 'unie6d7': '石', 'unie6de': '位',
                         'unie6e5': '屋', 'unie6e6': '粉', 'unie6e8': '单', 'unie709': '奶', 'unie70e': '大', 'unie71a': '蛋',
                         'unie72a': '而', 'unie72e': '茶', 'unie736': '室', 'unie741': '关', 'unie742': '再', 'unie759': '浦',
                         'unie767': '轩', 'unie76b': '紫', 'unie773': '富', 'unie783': '朝', 'unie785': '如', 'unie7a4': '产',
                         'unie7b3': '只', 'unie7bd': '牌', 'unie7c2': '童', 'unie7ca': '油', 'unie7e1': '个', 'unie7ec': '川',
                         'unie7ed': '上', 'unie7f7': '因', 'unie805': '双', 'unie82a': '但', 'unie830': '达', 'unie837': '万',
                         'unie838': '卫', 'unie84f': '庆', 'unie85f': '购', 'unie860': '药', 'unie865': '错', 'unie86a': '栋',
                         'unie86b': '振', 'unie87d': '四', 'unie897': '业', 'unie8a7': '第', 'unie8b2': '生', 'unie8c0': '乡',
                         'unie8c3': '棒', 'unie8cb': '嫩', 'unie8da': '便', 'unie8e7': '笑', 'unie8f9': '林', 'unie905': '西',
                         'unie909': '人', 'unie92a': '可', 'unie92e': '站', 'unie932': '商', 'unie940': '附', 'unie958': '喜',
                         'unie95d': '同', 'unie95f': '五', 'unie965': '好', 'unie97c': '很', 'unie990': '尝', 'unie993': '横',
                         'unie99b': '足', 'unie9b5': '酱', 'unie9cf': '是', 'unie9e3': '牛', 'unie9e9': '香', 'unie9ed': '央',
                         'unie9f6': '胜', 'unie9fe': '儿', 'uniea02': '缘', 'uniea07': '名', 'uniea15': '丰', 'uniea17': '周',
                         'uniea31': '整', 'uniea32': '福', 'uniea3e': '化', 'uniea5b': '白', 'uniea66': '每', 'uniea72': '家',
                         'uniea78': '城', 'uniea7f': '高', 'uniea86': '锅', 'uniea8e': '处', 'uniea96': '能', 'uniea97': '直',
                         'unieaad': '肉', 'unieac0': '昌', 'unieaca': '没', 'unieb02': '真', 'unieb04': '街', 'unieb05': '就',
                         'unieb17': '其', 'unieb1b': '培', 'unieb20': '部', 'unieb28': '算', 'unieb32': '度', 'unieb37': '段',
                         'unieb4f': '影', 'unieb51': '排', 'unieb5b': '民', 'unieb68': '走', 'unieb71': '海', 'unieb98': '鲜',
                         'unieba0': '济', 'unieba4': '泉', 'unieba8': '格', 'uniebae': '堂', 'uniebb4': '公', 'uniebb9': '幼',
                         'uniebc5': '电', 'uniebd4': '烟', 'uniebdc': '有', 'uniebdd': '物', 'uniebf8': '向', 'uniec01': '临',
                         'uniec02': '最', 'uniec0a': '兴', 'uniec0b': '中', 'uniec1b': '王', 'uniec20': '康', 'uniec23': '院',
                         'uniec2b': '园', 'uniec2c': '停', 'uniec37': '荣', 'uniec40': '安', 'uniec41': '试', 'uniec45': '7',
                         'uniec47': '座', 'uniec5f': '桂', 'uniec76': '市', 'uniec78': '光', 'uniec84': '子', 'uniec87': '你',
                         'uniec88': '啊', 'uniec97': '吧', 'unieca6': '东', 'uniecb4': '美', 'uniecbe': '于', 'uniecc3': '古',
                         'uniecc7': '羊', 'uniecce': '午', 'uniece0': '队', 'uniecec': '洗', 'uniecf2': '马', 'unied01': '差',
                         'unied07': '加', 'unied14': '湖', 'unied17': '乐', 'unied1a': '烤', 'unied26': '鞋', 'unied36': '甲',
                         'unied3c': '晚', 'unied52': '带', 'unied5e': '旅', 'unied6a': '际', 'unied72': '田', 'unied79': '特',
                         'unied7b': '国', 'unied85': '八', 'unied8d': '鸿', 'unied95': '制', 'uniedb0': '次', 'uniedc6': '以',
                         'uniedc8': '台', 'uniedcc': '秀', 'uniedd4': '饰', 'uniedd7': '喝', 'uniedd9': '府', 'uniede4': '门',
                         'uniedee': '态', 'uniedf1': '6', 'uniedfa': '饼', 'uniee08': '1', 'uniee13': '黄', 'uniee15': '阳',
                         'uniee17': '不', 'uniee18': '钢', 'uniee22': '斯', 'uniee45': '馆', 'uniee4a': '想', 'uniee51': '修',
                         'uniee53': '性', 'uniee59': '调', 'uniee5b': '气', 'uniee7f': '衣', 'uniee91': '阿', 'uniee93': '讯',
                         'unieeb1': '连', 'unieeb2': '洲', 'unieebc': '巷', 'unieec9': '集', 'unieeca': '妆', 'unieed4': '解',
                         'unieeeb': '经', 'unieef9': '提', 'unief0c': '批', 'unief0d': '元', 'unief21': '在', 'unief29': '头',
                         'unief35': '里', 'unief6b': '层', 'unief6c': '说', 'unief6d': '装', 'unief79': '更', 'unief85': '感',
                         'unief8b': '意', 'uniefb0': '前', 'uniefb2': '比', 'uniefc1': '风', 'uniefd5': '适', 'uniefd8': '常',
                         'uniefd9': '拉', 'uniefdc': '宝', 'uniefdf': '境', 'uniefe5': '窗', 'unieff0': '建', 'unieff1': '明',
                         'unieff6': '觉', 'unif009': '一', 'unif00a': '时', 'unif022': '花', 'unif051': '售', 'unif05a': '营',
                         'unif084': '3', 'unif085': '博', 'unif08b': '什', 'unif096': '非', 'unif09f': '艺', 'unif0a9': '8',
                         'unif0af': '器', 'unif0b4': '酒', 'unif0b9': '六', 'unif0c1': '丽', 'unif0ca': '型', 'unif0cd': '岛',
                         'unif0d8': '外', 'unif0e8': '辣', 'unif0f0': '鸭', 'unif0f8': '无', 'unif0fa': '等', 'unif0fc': '号',
                         'unif10a': '块', 'unif113': '给', 'unif131': '梅', 'unif141': '张', 'unif147': '后', 'unif166': '工',
                         'unif16a': '又', 'unif16c': '日', 'unif17d': '5', 'unif19a': '铁', 'unif1a6': '峰', 'unif1b6': '师',
                         'unif1b8': '具', 'unif1d6': '彩', 'unif1e1': '桥', 'unif1e6': '桌', 'unif1ee': '学', 'unif1ef': '理',
                         'unif1f9': '得', 'unif1fc': '动', 'unif202': '县', 'unif204': 'j', 'unif213': '级', 'unif217': '育',
                         'unif21a': '新', 'unif21d': '作', 'unif224': '广', 'unif227': '甜', 'unif24b': '放', 'unif251': '社',
                         'unif257': '话', 'unif268': '吃', 'unif272': '术', 'unif279': '道', 'unif27b': '岭', 'unif27d': '边',
                         'unif290': '手', 'unif2af': '健', 'unif2b2': '这', 'unif2be': '青', 'unif2c2': '鸡', 'unif2c6': '来',
                         'unif2ce': '虹', 'unif2d2': '才', 'unif2e3': '祥', 'unif2e9': '心', 'unif2f4': '松', 'unif2fe': '入',
                         'unif312': '食', 'unif337': '方', 'unif344': '副', 'unif349': '九', 'unif357': '春', 'unif35b': '卖',
                         'unif35e': '合', 'unif361': '量', 'unif36a': '那', 'unif37a': '山', 'unif37c': '农', 'unif386': '板',
                         'unif38f': '氏', 'unif390': '为', 'unif394': '包', 'unif3a4': '太', 'unif3a6': '推', 'unif3ba': '烫',
                         'unif3c7': '点', 'unif3c8': '价', 'unif3dd': '店', 'unif3e9': '然', 'unif3f0': '去', 'unif402': '寓',
                         'unif404': '贝', 'unif40b': '起', 'unif410': '4', 'unif43f': '几', 'unif452': '技', 'unif457': '强',
                         'unif459': '代', 'unif461': '路', 'unif469': '场', 'unif484': '米', 'unif487': '分', 'unif494': '镇',
                         'unif49a': '保', 'unif4a6': '叉', 'unif4ba': '通', 'unif4d3': '小', 'unif4db': '开', 'unif4fb': '爱',
                         'unif50a': '德', 'unif50d': '发', 'unif50e': '近', 'unif519': '盛', 'unif51d': '少', 'unif520': '力',
                         'unif521': '凯', 'unif52a': '定', 'unif53b': '员', 'unif541': '烧', 'unif55e': '菜', 'unif561': '配',
                         'unif563': '医', 'unif565': '维', 'unif56b': '事', 'unif572': '星', 'unif575': '务', 'unif58d': '迎',
                         'unif592': '果', 'unif5b1': '自', 'unif5b9': '了', 'unif5c0': '汉', 'unif5e1': '费', 'unif5e7': '杨',
                         'unif5fa': '糕', 'unif604': '火', 'unif606': '过', 'unif60d': '长', 'unif614': '北', 'unif631': '柳',
                         'unif638': '塘', 'unif649': '景', 'unif664': '司', 'unif666': '完', 'unif669': '正', 'unif685': '兰',
                         'unif6ae': '微', 'unif6b1': '港', 'unif6c7': '也', 'unif6cb': '永', 'unif6dc': '宾', 'unif6e5': '所',
                         'unif6e8': '汇', 'unif6ec': '百', 'unif6fc': '和', 'unif701': '沿', 'unif707': '麻', 'unif70e': '村',
                         'unif71f': '要', 'unif722': '打', 'unif72b': '餐', 'unif733': '云', 'unif736': '银', 'unif757': '口',
                         'unif758': '金', 'unif75a': '9', 'unif75b': '诚', 'unif768': '训', 'unif76d': '找', 'unif770': '岗',
                         'unif77b': '局', 'unif77e': '荐', 'unif78c': '鱼', 'unif78e': '般', 'unif79d': '沙', 'unif7a3': '三',
                         'unif7a6': '水', 'unif7ab': '当', 'unif7ae': '贸', 'unif7bf': '雅', 'unif7c4': '瑞', 'unif7ec': '且',
                         'unif7ee': '步', 'unif7ef': '回', 'unif804': '惠', 'unif806': '总', 'unif812': '车', 'unif816': '天',
                         'unif82b': '选', 'unif835': '塔', 'unif845': '厨', 'unif854': '津', 'unif85e': '布', 'unif85f': '下',
                         'unif868': '尚', 'unif869': '色', 'unif86a': '虾', 'unif871': '做', 'unif873': '较', 'unif878': '候',
                         'unif883': '情', 'unif884': '平', 'unif888': '侧', 'unif892': '源', 'unif8a8': '2', 'unif8b0': '字',
                         'unif8c3': '利', 'unif8c6': '超', 'unif8c7': '珠', 'unif8e3': '啦', 'unif8e6': '线', 'unif8f2': '期',
                         'unif8fb': '省', 'unif8fc': '信'},
            'review': {'x': '', 'unie006': '字', 'unie00a': '办', 'unie024': '村', 'unie031': '也', 'unie03a': '烟',
                       'unie03f': '线', 'unie059': '名', 'unie061': '油', 'unie086': '隆', 'unie08e': '满',
                       'unie094': '洗',
                       'unie0a0': '糕', 'unie0a3': '医', 'unie0ac': '乡', 'unie0ad': '岛', 'unie0af': '般',
                       'unie0bc': '外',
                       'unie0c4': '但', 'unie0e1': '布', 'unie0ff': '石', 'unie101': '之', 'unie104': '吧',
                       'unie10a': '口',
                       'unie115': '福', 'unie120': '柳', 'unie129': '成', 'unie133': '等', 'unie13b': '起',
                       'unie13e': '木',
                       'unie158': '回', 'unie162': '院', 'unie163': '女', 'unie167': '物', 'unie16b': '附',
                       'unie194': '推',
                       'unie19b': '锅', 'unie19c': '养', 'unie19e': '价', 'unie19f': '格', 'unie1a9': '几',
                       'unie1ae': '奶',
                       'unie1b0': '一', 'unie1b1': '政', 'unie1b4': '0', 'unie1b5': '昌', 'unie1c0': '河',
                       'unie1c2': '博',
                       'unie1f1': '银', 'unie1f2': '度', 'unie201': '连', 'unie213': '清', 'unie217': '梅',
                       'unie21e': '房',
                       'unie236': '平', 'unie238': '员', 'unie240': '道', 'unie24f': '楼', 'unie251': '食',
                       'unie262': '林',
                       'unie263': '面', 'unie265': '蛋', 'unie291': '秀', 'unie2d1': '坊', 'unie2d7': '阳',
                       'unie2e9': '只',
                       'unie2ed': '欢', 'unie2f2': '到', 'unie301': '材', 'unie304': '童', 'unie310': '州',
                       'unie311': '用',
                       'unie314': '汤', 'unie33d': '理', 'unie358': '一', 'unie361': '务', 'unie365': '烫',
                       'unie368': '辣',
                       'unie36f': '能', 'unie372': '种', 'unie381': '助', 'unie38e': '具', 'unie390': '给',
                       'unie391': '幢',
                       'unie3a6': '你', 'unie3af': '贝', 'unie3b1': '没', 'unie3bd': '态', 'unie3d0': '因',
                       'unie3d2': '就',
                       'unie3d4': '评', 'unie3de': '佳', 'unie3e3': '临', 'unie3e5': '品', 'unie3f2': '斯',
                       'unie3f4': '园',
                       'unie405': '自', 'unie42f': '里', 'unie436': '干', 'unie442': '现', 'unie447': '份',
                       'unie44d': '朝',
                       'unie44e': '旁', 'unie450': '兰', 'unie454': '晚', 'unie466': '所', 'unie485': '中',
                       'unie48f': '饰',
                       'unie49d': '7', 'unie4a6': '当', 'unie4a7': '塔', 'unie4ae': '尔', 'unie4af': '四',
                       'unie4b1': '市',
                       'unie4b4': '式', 'unie4c4': '紫', 'unie4d5': '体', 'unie4e5': '丰', 'unie4fc': '文',
                       'unie510': '酸',
                       'unie512': '近', 'unie51b': '点', 'unie541': '红', 'unie54a': '强', 'unie54d': '人',
                       'unie55d': '设',
                       'unie566': '冥', 'unie571': '氏', 'unie57e': '米', 'unie5a4': '兴', 'unie5a5': '如',
                       'unie5a6': '串',
                       'unie5ba': '门', 'unie5ef': '区', 'unie5f8': '尚', 'unie60a': '虹', 'unie61f': '十',
                       'unie623': '觉',
                       'unie625': '友', 'unie62d': '总', 'unie62e': '说', 'unie632': '西', 'unie64c': '在',
                       'unie653': '铁',
                       'unie654': '康', 'unie658': '接', 'unie65b': '大', 'unie66c': '城', 'unie67d': '挺',
                       'unie680': '六',
                       'unie682': '泰', 'unie68d': '差', 'unie698': '更', 'unie69c': '药', 'unie6a6': '茶',
                       'unie6ad': '子',
                       'unie6af': '香', 'unie6b4': '滨', 'unie6bb': '9', 'unie6be': '站', 'unie6c3': '包',
                       'unie6d4': '县',
                       'unie6d6': '训', 'unie6df': '鸿', 'unie6e1': '微', 'unie6e6': '午', 'unie6eb': '三',
                       'unie6ee': '姐',
                       'unie700': '店', 'unie71a': '边', 'unie71d': '技', 'unie727': '定', 'unie72f': '富',
                       'unie742': '电',
                       'unie743': '牛', 'unie757': '做', 'unie758': '局', 'unie772': '内', 'unie774': '王',
                       'unie79c': '彩',
                       'unie7a2': '健', 'unie7a8': '迎', 'unie7b8': '真', 'unie7c6': '足', 'unie7c9': '北',
                       'unie7dc': '洲',
                       'unie7eb': '桥', 'unie7ef': '本', 'unie801': '井', 'unie807': '谷', 'unie814': '街',
                       'unie816': '艺',
                       'unie818': '美', 'unie827': '发', 'unie839': '岗', 'unie857': '造', 'unie85c': '跟',
                       'unie867': '侧',
                       'unie869': '全', 'unie876': '于', 'unie88a': '向', 'unie895': '样', 'unie89f': '张',
                       'unie8a0': '厦',
                       'unie8da': '庆', 'unie8e1': '诚', 'unie8ec': '黄', 'unie8ed': '泉', 'unie8f1': '锦',
                       'unie916': '肉',
                       'unie91b': '我', 'unie922': '达', 'unie923': '司', 'unie927': '开', 'unie92b': '关',
                       'unie936': '农',
                       'unie93d': '很', 'unie93e': '丽', 'unie946': '间', 'unie98a': '水', 'unie99c': '鲜',
                       'unie9a4': '还',
                       'unie9a9': '销', 'unie9ac': '走', 'unie9c0': '高', 'unie9d8': '队', 'unie9eb': '轩',
                       'unie9f6': '货',
                       'uniea00': '的', 'uniea1e': '加', 'uniea21': '田', 'uniea22': '己', 'uniea2a': '阿',
                       'uniea2c': '镇',
                       'uniea31': '直', 'uniea43': '胜', 'uniea4b': '环', 'uniea4e': '座', 'uniea53': '整',
                       'uniea54': '双',
                       'uniea5c': '6', 'uniea65': '集', 'uniea6d': '入', 'uniea82': '行', 'uniea84': '好',
                       'unieaaf': '算',
                       'unieab1': '鱼', 'unieab3': '影', 'unieacf': '下', 'unieadb': '卫', 'unieadc': '纪',
                       'unieaea': '东',
                       'unieaed': '打', 'unieaef': '这', 'unieaf0': '且', 'unieaf1': '爱', 'unieb07': '两',
                       'unieb17': '化',
                       'unieb1a': '最', 'unieb1f': '横', 'unieb2d': '么', 'unieb3d': '主', 'unieb41': '寓',
                       'unieb42': '酒',
                       'unieb45': '运', 'unieb4d': '营', 'unieb53': '副', 'unieb54': '鸭', 'unieb6b': '笑',
                       'unieb7a': '菜',
                       'unieb7b': '钢', 'unieb80': '气', 'unieb9b': '业', 'uniebb8': '饼', 'uniebbf': '着',
                       'uniebc6': '可',
                       'uniebd8': '皮', 'uniebec': '都', 'uniebef': '些', 'uniebf2': '装', 'uniebf4': '情',
                       'uniebfa': '小',
                       'uniec01': '带', 'uniec02': '津', 'uniec0d': '出', 'uniec20': '产', 'uniec22': '龙',
                       'uniec26': '凤',
                       'uniec2c': '乐', 'uniec2e': '与', 'uniec35': '宾', 'uniec40': '后', 'uniec44': '次',
                       'uniec63': '信',
                       'uniec6b': '保', 'uniec6c': '景', 'uniec76': '万', 'uniec78': '快', 'uniec79': '沿',
                       'uniec85': '祥',
                       'uniec86': '豆', 'uniec8b': '利', 'uniec8c': '买', 'uniec8f': '选', 'uniecbe': '特',
                       'uniecc3': '候',
                       'uniecde': '汉', 'uniece2': '朋', 'uniece4': '桂', 'uniecf1': '术', 'uniecf9': '限',
                       'unied08': '步',
                       'unied11': '讯', 'unied3d': '再', 'unied3f': '制', 'unied48': '代', 'unied5d': '玉',
                       'unied73': '甜',
                       'unied78': '民', 'unied7b': '机', 'unied82': '分', 'unied85': '号', 'unied93': '味',
                       'uniedc1': '湖',
                       'uniedc3': '马', 'uniedd0': '科', 'uniedd8': '置', 'unieddc': '铺', 'uniede4': '斜',
                       'uniedea': '过',
                       'uniedee': '山', 'uniedf3': '地', 'uniedf4': '知', 'uniee01': '哈', 'uniee08': '喝',
                       'uniee17': '沙',
                       'uniee27': '世', 'uniee28': '教', 'uniee2c': '找', 'uniee34': '元', 'uniee45': '九',
                       'uniee47': '才',
                       'uniee52': '餐', 'uniee53': '庄', 'uniee58': '川', 'uniee5f': 'j', 'uniee6e': '容',
                       'uniee70': '窗',
                       'uniee99': '心', 'uniee9d': '型', 'unieea7': '烤', 'unieecd': '管', 'unieed7': '荣',
                       'unieedb': '吉',
                       'unieedc': '话', 'unieee0': '育', 'unief1f': '试', 'unief27': '杨', 'unief2b': '师',
                       'unief3a': '旗',
                       'unief49': '桌', 'unief4a': '意', 'unief4b': '巷', 'unief58': '明', 'unief5a': '社',
                       'unief5d': '又',
                       'unief6b': '峰', 'unief97': '府', 'unief9a': '凯', 'unief9c': '尝', 'uniefa6': '和',
                       'uniefa8': '南',
                       'uniefab': '们', 'uniefad': '盛', 'uniefc8': '个', 'uniefe6': '汇', 'unieff8': 'j',
                       'unif004': '客',
                       'unif005': '然', 'unif006': '馆', 'unif013': '广', 'unif015': '羊', 'unif018': '顺',
                       'unif01d': '配',
                       'unif01e': '让', 'unif021': '莲', 'unif02f': '车', 'unif032': '培', 'unif035': '宏',
                       'unif03d': '松',
                       'unif050': '学', 'unif05a': '浦', 'unif05d': '部', 'unif065': '央', 'unif06a': '振',
                       'unif081': '境',
                       'unif08d': '对', 'unif091': '感', 'unif094': '儿', 'unif0a6': '少', 'unif0ab': '比',
                       'unif0ce': '生',
                       'unif0d2': '鸡', 'unif0d9': '购', 'unif0de': '鑫', 'unif0e7': '3', 'unif0ec': '太',
                       'unif0fe': '厅',
                       'unif111': '位', 'unif143': '衣', 'unif14d': '5', 'unif14f': '汽', 'unif154': '酱',
                       'unif183': '别',
                       'unif187': '第', 'unif19c': '块', 'unif1a3': '前', 'unif1c3': '片', 'unif1c7': '会',
                       'unif1ca': '单',
                       'unif216': '鞋', 'unif21e': '甲', 'unif22c': '火', 'unif23a': '青', 'unif23d': '想',
                       'unif240': '校',
                       'unif24c': '京', 'unif25a': '年', 'unif26d': '看', 'unif289': '级', 'unif28b': '常',
                       'unif291': '日',
                       'unif29f': '底', 'unif2a2': '错', 'unif2aa': '每', 'unif2ab': '宝', 'unif2b6': '正',
                       'unif2b7': '那',
                       'unif2b8': '2', 'unif2c5': '网', 'unif2db': '超', 'unif2df': '旅', 'unif2e5': '武',
                       'unif2f3': '栋',
                       'unif2f5': '雅', 'unif307': '维', 'unif30a': '处', 'unif326': '层', 'unif338': '拍',
                       'unif342': '要',
                       'unif34b': '七', 'unif367': '果', 'unif36c': '停', 'unif37b': '五', 'unif37c': '是',
                       'unif37d': '力',
                       'unif37f': '通', 'unif386': '国', 'unif39b': '提', 'unif39f': '头', 'unif3b5': '得',
                       'unif3c4': '弄',
                       'unif3d1': '八', 'unif3d6': '进', 'unif3d7': '放', 'unif3d8': '场', 'unif3de': '周',
                       'unif3e4': '段',
                       'unif3ec': '实', 'unif3f8': '港', 'unif40d': '动', 'unif428': '啊', 'unif431': '厂',
                       'unif437': '方',
                       'unif44c': '贸', 'unif45a': '费', 'unif45c': '天', 'unif467': '妆', 'unif47a': '百',
                       'unif498': '金',
                       'unif4a2': '1', 'unif4a3': '器', 'unif4a4': '来', 'unif4ab': '刚', 'unif4b3': '喜',
                       'unif4b6': '长',
                       'unif4c3': '白', 'unif4c5': '工', 'unif4dc': '料', 'unif4de': '荐', 'unif4ea': '售',
                       'unif4f3': '便',
                       'unif4fa': '吃', 'unif509': '合', 'unif50c': '完', 'unif52a': '8', 'unif52f': '安',
                       'unif535': '星',
                       'unif537': '上', 'unif539': '修', 'unif53c': '公', 'unif542': '粉', 'unif548': '作',
                       'unif54f': '堂',
                       'unif550': '江', 'unif55b': '春', 'unif571': '塘', 'unif576': '角', 'unif578': '事',
                       'unif595': '花',
                       'unif59f': '啦', 'unif5ad': '赞', 'unif5b3': '较', 'unif5b4': '同', 'unif5b8': '宁',
                       'unif5bc': '源',
                       'unif5be': '饭', 'unif5c6': '色', 'unif5cf': '记', 'unif5d0': '瑞', 'unif5d1': '以',
                       'unif5d2': '缘',
                       'unif5dd': '交', 'unif5df': '风', 'unif5e1': '烧', 'unif5e3': '重', 'unif5e5': '居',
                       'unif5ed': '批',
                       'unif5f2': '活', 'unif5fa': '联', 'unif60c': '云', 'unif612': '性', 'unif617': '台',
                       'unif625': '他',
                       'unif626': '服', 'unif628': '期', 'unif638': '珠', 'unif63c': '专', 'unif644': '湾',
                       'unif647': '路',
                       'unif649': '济', 'unif64e': '手', 'unif650': '德', 'unif651': '像', 'unif660': '卖',
                       'unif667': '有',
                       'unif678': '值', 'unif67c': '不', 'unif686': '牌', 'unif698': '无', 'unif6b8': '拉',
                       'unif6bf': '虾',
                       'unif6ce': '时', 'unif6d1': '苑', 'unif6d5': '为', 'unif6db': '热', 'unif6dc': '溪',
                       'unif6e1': '陵',
                       'unif6f3': '经', 'unif6f5': '团', 'unif70e': '恒', 'unif70f': '精', 'unif71d': '而',
                       'unif72e': '解',
                       'unif73f': '去', 'unif754': '嫩', 'unif759': '省', 'unif76c': '建', 'unif76e': '永',
                       'unif781': '惠',
                       'unif783': '古', 'unif78a': '幼', 'unif78b': '板', 'unif78d': '多', 'unif7b7': '华',
                       'unif7c8': '岭',
                       'unif7ca': '际', 'unif7d2': '其', 'unif7e8': '4', 'unif7fe': '叉', 'unif802': '什',
                       'unif808': '屋',
                       'unif80e': '杂', 'unif826': '排', 'unif827': '原', 'unif836': '量', 'unif845': '非',
                       'unif851': '光',
                       'unif858': '海', 'unif86f': '嘉', 'unif878': '了', 'unif87d': '麻', 'unif88d': '调',
                       'unif8a4': '室',
                       'unif8a6': '新', 'unif8b4': '厨', 'unif8bb': '商', 'unif8bc': '适', 'unif8c7': '老',
                       'unif8ca': '计',
                       'unif8ea': '棒', 'unif8f4': '家'},
            'num': {'x': '', 'unie003': '地', 'unie013': '太', 'unie017': '跟', 'unie01e': '当', 'unie02c': '场',
                    'unie037': '鸿', 'unie040': '很', 'unie044': '事', 'unie048': '林', 'unie04c': '且', 'unie065': '巷',
                    'unie075': '头', 'unie08c': '四', 'unie09c': '喝', 'unie0a7': '丽', 'unie0bf': '武', 'unie0d3': '话',
                    'unie0d6': '部', 'unie0db': '湾', 'unie0de': '七', 'unie0eb': '才', 'unie0ee': '走', 'unie109': '技',
                    'unie11d': '湖', 'unie121': '记', 'unie12e': '铺', 'unie133': '特', 'unie137': '之', 'unie143': '式',
                    'unie145': '的', 'unie14b': '尝', 'unie151': '货', 'unie156': '屋', 'unie15d': '牛', 'unie15e': '本',
                    'unie161': '央', 'unie166': '知', 'unie170': '少', 'unie180': '单', 'unie189': '强', 'unie19a': '务',
                    'unie1b1': '福', 'unie1b4': '香', 'unie1bd': '欢', 'unie1cc': '饰', 'unie1d6': '港', 'unie1e5': '衣',
                    'unie1f6': '洗', 'unie1f7': '块', 'unie202': '做', 'unie216': '师', 'unie229': '乐', 'unie22f': '说',
                    'unie237': '评', 'unie246': '去', 'unie248': '局', 'unie255': '昌', 'unie263': '还', 'unie267': '康',
                    'unie270': '都', 'unie284': '艺', 'unie288': '岭', 'unie28e': '牌', 'unie290': '运', 'unie294': '井',
                    'unie297': '错', 'unie2a1': '城', 'unie2a4': '解', 'unie2a8': '方', 'unie2bb': '栋', 'unie2bc': '车',
                    'unie2c4': '看', 'unie2da': '作', 'unie2e9': '活', 'unie2fa': '瑞', 'unie305': '烤', 'unie30e': '六',
                    'unie30f': '副', 'unie321': '如', 'unie322': '晚', 'unie323': '好', 'unie324': '南', 'unie339': '外',
                    'unie33b': '花', 'unie33c': '意', 'unie33e': '旗', 'unie343': '每', 'unie35d': '带', 'unie369': '直',
                    'unie36f': '助', 'unie386': '打', 'unie395': '就', 'unie39d': '拍', 'unie3a8': '名', 'unie3b1': '种',
                    'unie3b4': '市', 'unie3ed': '豆', 'unie3fa': '岗', 'unie41e': '浦', 'unie426': '计', 'unie433': '常',
                    'unie440': '2', 'unie447': '字', 'unie44a': '健', 'unie45c': '横', 'unie45e': '6', 'unie462': '平',
                    'unie46b': '纪', 'unie4a3': '站', 'unie4ad': '精', 'unie4c5': '连', 'unie4ce': '业', 'unie4cf': '超',
                    'unie4de': '哈', 'unie4df': '到', 'unie4e3': '我', 'unie4e8': '同', 'unie4ec': '津', 'unie501': '阿',
                    'unie505': '厅', 'unie508': '油', 'unie50e': '友', 'unie51e': '全', 'unie523': '松', 'unie53e': '古',
                    'unie542': '马', 'unie546': '装', 'unie547': '对', 'unie562': '想', 'unie56c': '药', 'unie57f': '云',
                    'unie591': '姐', 'unie59e': '永', 'unie5a8': '足', 'unie5ac': '料', 'unie5b3': 'j', 'unie5ba': '虹',
                    'unie5c0': '茶', 'unie5ca': '面', 'unie5d2': '处', 'unie5d6': '甜', 'unie5d7': '高', 'unie5dc': '紫',
                    'unie5dd': '岛', 'unie5e2': '7', 'unie5e4': '明', 'unie5eb': '商', 'unie5f0': '青', 'unie5fc': '宏',
                    'unie5fd': '凤', 'unie602': '房', 'unie606': '斯', 'unie60b': '客', 'unie60d': '顺', 'unie614': '旅',
                    'unie620': '道', 'unie623': '接', 'unie62f': '但', 'unie643': '河', 'unie646': '气', 'unie649': '制',
                    'unie653': '汉', 'unie65a': '在', 'unie679': '彩', 'unie682': '再', 'unie69d': '提', 'unie6a5': '奶',
                    'unie6bc': '购', 'unie6c0': '关', 'unie6ce': '态', 'unie6d3': '嘉', 'unie6fd': '像', 'unie708': '泉',
                    'unie70d': '几', 'unie718': '红', 'unie71c': '堂', 'unie721': '楼', 'unie72b': '定', 'unie73d': '板',
                    'unie753': '试', 'unie763': '桂', 'unie767': '家', 'unie770': '赞', 'unie772': '祥', 'unie774': '教',
                    'unie784': '卖', 'unie7a5': '专', 'unie7af': '江', 'unie7b1': '销', 'unie7c0': '培', 'unie7ca': '烟',
                    'unie7d0': '儿', 'unie7e8': '幢', 'unie803': '座', 'unie806': '寓', 'unie807': '你', 'unie80e': '光',
                    'unie80f': '济', 'unie81c': '以', 'unie825': '会', 'unie826': '吧', 'unie82c': '近', 'unie83f': '配',
                    'unie854': '珠', 'unie865': '着', 'unie879': '厂', 'unie885': '心', 'unie8a1': '布', 'unie8a5': '叉',
                    'unie8a9': '电', 'unie8ab': '下', 'unie8bc': '重', 'unie8c8': '联', 'unie8f8': '情', 'unie901': '般',
                    'unie906': '尔', 'unie92b': '弄', 'unie92d': '多', 'unie932': '比', 'unie934': '盛', 'unie940': '洲',
                    'unie94c': '幼', 'unie958': '火', 'unie95a': '陵', 'unie968': '谷', 'unie987': '果', 'unie996': '工',
                    'unie997': '凯', 'unie99e': '世', 'unie9ae': '雅', 'unie9cc': '汇', 'unie9d4': '4', 'unie9e3': '真',
                    'unie9f4': '鸭', 'uniea0a': '其', 'uniea0d': '起', 'uniea14': '喜', 'uniea26': '北', 'uniea29': '科',
                    'uniea33': '佳', 'uniea3d': '育', 'uniea43': '次', 'uniea5d': '底', 'uniea65': '山', 'uniea69': '信',
                    'uniea6a': '三', 'uniea76': '午', 'uniea79': '中', 'uniea81': '皮', 'uniea85': '角', 'uniea89': '王',
                    'uniea8c': '恒', 'uniea8e': '串', 'uniea9e': '理', 'unieaa4': '食', 'unieaad': '县', 'unieac7': '糕',
                    'unieacd': '后', 'unieae7': '农', 'unieaf6': '过', 'unieafd': '兴', 'unieafe': '网', 'unieb23': '饼',
                    'unieb2d': '街', 'unieb31': '星', 'unieb33': '实', 'unieb3b': '汽', 'unieb49': '府', 'unieb4d': '万',
                    'unieb56': '要', 'unieb5a': '主', 'unieb60': '力', 'unieb75': '便', 'unieb7c': '现', 'unieb7d': '童',
                    'unieb81': '修', 'unieb8b': '个', 'uniebae': '虾', 'uniebb7': '贝', 'uniebc8': '美', 'uniebce': '可',
                    'uniebef': '位', 'uniebf8': '桌', 'uniebfb': '买', 'uniebfd': '么', 'uniec0e': '品', 'uniec11': '术',
                    'uniec14': '政', 'uniec1a': '总', 'uniec33': '卫', 'uniec3b': '境', 'uniec48': '前', 'uniec4c': '推',
                    'uniec62': '人', 'uniec6b': '让', 'uniec77': '溪', 'uniec7a': '小', 'uniec89': '博', 'uniecbd': '一',
                    'uniecc2': '京', 'uniecdb': '塔', 'uniecee': '店', 'uniecf8': '嫩', 'uniecf9': '设', 'uniecfb': '具',
                    'unied08': '里', 'unied27': '轩', 'unied45': '养', 'unied5e': '笑', 'unied71': '更', 'unied8b': '正',
                    'unied8e': '算', 'unied91': '队', 'unied92': '了', 'unied9b': '德', 'unied9c': '加', 'unieda1': '附',
                    'unieda9': '天', 'uniedaa': '柳', 'uniedb1': '路', 'uniedba': '得', 'uniedc2': '室', 'uniedc6': '体',
                    'uniedc8': '旁', 'uniedd3': '5', 'uniedd9': '氏', 'unieddb': '价', 'uniedfd': '宁', 'uniedff': '鸡',
                    'uniee07': '缘', 'uniee0c': '荣', 'uniee10': '影', 'uniee30': '滨', 'uniee31': '热', 'uniee55': '蛋',
                    'uniee56': '进', 'uniee60': '刚', 'uniee80': '女', 'uniee86': '保', 'uniee8c': '非', 'uniee8e': '自',
                    'uniee8f': '调', 'uniee9d': '停', 'uniee9f': '又', 'unieea6': '快', 'unieeb4': '临', 'unieeb6': '厦',
                    'unieedf': '水', 'unieee1': '是', 'unieee3': '医', 'unieef7': '度', 'unieefe': '整', 'unief01': '日',
                    'unief0d': '候', 'unief0e': '型', 'unief17': '学', 'unief20': '朋', 'unief27': '庄', 'unief3c': '木',
                    'unief41': '窗', 'uniefa3': '村', 'uniefa4': '校', 'uniefa8': 'j', 'uniefad': '费', 'uniefb0': '段',
                    'uniefb8': '妆', 'uniefbe': '隆', 'uniefc0': '侧', 'uniefcc': '梅', 'uniefd6': '荐', 'uniefde': '诚',
                    'uniefe0': '和', 'uniefed': '期', 'uniefee': '一', 'unieff0': '也', 'unieff4': '色', 'unieffd': '台',
                    'unif000': '东', 'unif00f': '机', 'unif010': '化', 'unif011': '通', 'unif012': '辣', 'unif013': '餐',
                    'unif01d': '己', 'unif029': '州', 'unif02a': '放', 'unif02d': '行', 'unif02f': '生', 'unif04d': '际',
                    'unif061': '8', 'unif086': '院', 'unif099': '公', 'unif0b6': '材', 'unif0c0': '内', 'unif0df': '苑',
                    'unif0e7': '坊', 'unif0e8': '冥', 'unif0f1': '振', 'unif0f4': '新', 'unif104': '银', 'unif106': '排',
                    'unif107': '门', 'unif10e': '清', 'unif122': '能', 'unif124': '交', 'unif128': '惠', 'unif132': '烧',
                    'unif13f': '老', 'unif140': '迎', 'unif143': '给', 'unif145': '九', 'unif155': '差', 'unif157': '员',
                    'unif179': '份', 'unif180': '宝', 'unif1b2': '甲', 'unif1c0': '斜', 'unif1c4': '锦', 'unif1dd': '景',
                    'unif1ee': '味', 'unif1fc': '宾', 'unif208': '石', 'unif210': '饭', 'unif219': '铁', 'unif221': '区',
                    'unif238': '容', 'unif23a': '周', 'unif241': '9', 'unif248': '只', 'unif24f': '时', 'unif25e': '向',
                    'unif261': '园', 'unif26b': '粉', 'unif275': '峰', 'unif28e': '微', 'unif290': '玉', 'unif294': '维',
                    'unif295': '级', 'unif2aa': '团', 'unif2d1': '钢', 'unif2e7': '那', 'unif2ea': '十', 'unif2fd': '沿',
                    'unif31c': '步', 'unif322': '成', 'unif336': '无', 'unif33f': '爱', 'unif34c': '民', 'unif34e': '桥',
                    'unif353': '回', 'unif357': '棒', 'unif359': '龙', 'unif35b': '上', 'unif363': '田', 'unif36d': '因',
                    'unif370': '厨', 'unif373': '干', 'unif37c': '汤', 'unif388': '尚', 'unif3b1': '贸', 'unif3c7': '杂',
                    'unif3d2': '八', 'unif3d3': '羊', 'unif3f1': '黄', 'unif423': '胜', 'unif428': '乡', 'unif433': '开',
                    'unif45b': '间', 'unif45d': '五', 'unif461': '不', 'unif46e': '利', 'unif47c': '来', 'unif47e': '庆',
                    'unif48b': '镇', 'unif490': '满', 'unif493': '司', 'unif498': '华', 'unif4a4': '选', 'unif4b7': '风',
                    'unif4ba': '张', 'unif4be': '训', 'unif4c2': '营', 'unif4c6': '与', 'unif4d9': '大', 'unif4e6': '然',
                    'unif4ec': '挺', 'unif4f7': '口', 'unif4f8': '所', 'unif4f9': '杨', 'unif51a': '没', 'unif51b': '产',
                    'unif521': '找', 'unif524': '啊', 'unif525': '居', 'unif526': '1', 'unif53d': '物', 'unif53f': '性',
                    'unif55a': '阳', 'unif562': '文', 'unif563': '泰', 'unif566': '米', 'unif56a': '第', 'unif57b': '鲜',
                    'unif57f': '烫', 'unif588': '发', 'unif58e': '菜', 'unif592': '他', 'unif598': '鑫', 'unif59d': '麻',
                    'unif5b7': '鞋', 'unif5e4': '子', 'unif5ef': '合', 'unif5f8': '感', 'unif5fe': '点', 'unif604': '金',
                    'unif610': '值', 'unif618': '置', 'unif619': '鱼', 'unif61a': '广', 'unif634': '适', 'unif640': '售',
                    'unif652': '环', 'unif654': '批', 'unif655': '片', 'unif65a': '兰', 'unif65b': '什', 'unif674': '锅',
                    'unif678': '元', 'unif67f': '酱', 'unif686': '限', 'unif68e': '社', 'unif69c': '这', 'unif6b2': '别',
                    'unif6bc': '样', 'unif6d0': '朝', 'unif6db': '线', 'unif6e6': '拉', 'unif6f9': '觉', 'unif6fc': '双',
                    'unif703': '动', 'unif704': '长', 'unif70b': '原', 'unif710': '入', 'unif712': '沙', 'unif71d': '为',
                    'unif72d': '最', 'unif730': '较', 'unif732': '春', 'unif734': '管', 'unif73c': '酒', 'unif745': '安',
                    'unif75a': '号', 'unif763': '建', 'unif76d': '用', 'unif76f': '国', 'unif775': '3', 'unif78a': '分',
                    'unif7a2': '办', 'unif7ad': '塘', 'unif7ae': '达', 'unif7b5': '量', 'unif7ba': '0', 'unif7d6': '讯',
                    'unif7e2': '酸', 'unif7e4': '器', 'unif7fd': '格', 'unif800': '源', 'unif824': '西', 'unif82d': '服',
                    'unif836': '有', 'unif838': '肉', 'unif83e': '手', 'unif847': '等', 'unif859': '莲', 'unif85a': '省',
                    'unif85e': '川', 'unif869': '馆', 'unif86b': '吉', 'unif877': '于', 'unif87c': '经', 'unif882': '们',
                    'unif88e': '丰', 'unif88f': '吃', 'unif899': '年', 'unif89b': '代', 'unif8ae': '包', 'unif8af': '秀',
                    'unif8b5': '百', 'unif8be': '造', 'unif8c3': '集', 'unif8c6': '富', 'unif8c7': '层', 'unif8c8': '出',
                    'unif8c9': '完', 'unif8cc': '些', 'unif8d5': '两', 'unif8e6': '而', 'unif8ed': '边', 'unif8f4': '海',
                    'unif8f6': '啦', 'unif8fa': '白'},
            'hours': {'x': '', 'unie001': '滨', 'unie002': '务', 'unie015': '上', 'unie031': '走', 'unie03e': '专',
                      'unie03f': '量', 'unie086': '发', 'unie0b3': '且', 'unie0b9': '沿', 'unie0bd': '侧', 'unie0cc': '得',
                      'unie0ce': '好', 'unie0d0': '饰', 'unie0d6': '林', 'unie0df': '爱', 'unie0e6': '局', 'unie0f4': '味',
                      'unie101': '城', 'unie11e': '隆', 'unie165': '有', 'unie16d': '鸭', 'unie171': '跟', 'unie18d': '做',
                      'unie195': '妆', 'unie19b': '棒', 'unie19e': '9', 'unie1bb': '镇', 'unie1c8': '子', 'unie1d0': '代',
                      'unie1d4': '宾', 'unie1d8': '喝', 'unie1dd': '部', 'unie1fd': '信', 'unie205': '岛', 'unie214': '吧',
                      'unie223': '赞', 'unie224': '附', 'unie22f': '迎', 'unie236': '万', 'unie242': '买', 'unie24c': '适',
                      'unie252': '第', 'unie25f': '满', 'unie274': '货', 'unie279': '喜', 'unie284': '山', 'unie287': '都',
                      'unie295': '紫', 'unie2ae': '放', 'unie2b0': '色', 'unie2ca': '辣', 'unie2d6': '百', 'unie2d9': '配',
                      'unie2db': '童', 'unie2ea': '在', 'unie2eb': '常', 'unie2ec': '化', 'unie2f7': '术', 'unie2fc': '牌',
                      'unie306': '物', 'unie30d': '精', 'unie329': '雅', 'unie33b': '布', 'unie340': '段', 'unie36e': '产',
                      'unie371': '同', 'unie388': '桌', 'unie391': '联', 'unie394': '停', 'unie397': '古', 'unie3a3': '市',
                      'unie3a7': '师', 'unie3b4': '因', 'unie3b5': '家', 'unie3c0': '世', 'unie3c7': '菜', 'unie3ca': '试',
                      'unie3d3': '才', 'unie3eb': '光', 'unie3f4': '室', 'unie418': '心', 'unie422': '境', 'unie431': '华',
                      'unie442': '陵', 'unie447': '要', 'unie44a': '川', 'unie44b': '口', 'unie44e': '庄', 'unie44f': '训',
                      'unie455': '话', 'unie459': '省', 'unie470': '挺', 'unie472': '红', 'unie482': '算', 'unie483': '微',
                      'unie489': '号', 'unie4a3': '向', 'unie4a7': '而', 'unie4c1': '意', 'unie4c4': '四', 'unie4d2': '料',
                      'unie4df': '汽', 'unie4e1': '岭', 'unie4e3': '我', 'unie4e7': '春', 'unie4eb': '合', 'unie4ec': '松',
                      'unie4ef': '大', 'unie501': '横', 'unie507': '饼', 'unie50c': '银', 'unie517': '什', 'unie536': '品',
                      'unie539': '堂', 'unie54b': '朝', 'unie556': '北', 'unie55c': '桥', 'unie55d': '吉', 'unie575': '像',
                      'unie576': '鱼', 'unie57f': '所', 'unie585': '工', 'unie587': '选', 'unie58c': '州', 'unie59b': '记',
                      'unie5ab': '高', 'unie5b1': '装', 'unie5c1': '通', 'unie5d8': '道', 'unie5d9': '全', 'unie5e9': '分',
                      'unie5eb': '济', 'unie5ec': '不', 'unie5ed': '1', 'unie60f': '经', 'unie615': '你', 'unie619': '健',
                      'unie61d': '到', 'unie62a': '甜', 'unie62d': '源', 'unie630': '限', 'unie639': '们', 'unie641': '铺',
                      'unie643': '便', 'unie651': '昌', 'unie652': '服', 'unie661': '丽', 'unie66c': '面', 'unie670': '能',
                      'unie676': '黄', 'unie67f': '小', 'unie681': '校', 'unie689': '强', 'unie68d': '景', 'unie690': '马',
                      'unie692': '推', 'unie6a0': '内', 'unie6ac': '车', 'unie6b5': '一', 'unie6b8': '长', 'unie6c4': '明',
                      'unie6cc': '白', 'unie6d6': '觉', 'unie6e7': '场', 'unie6ee': '感', 'unie6f8': '知', 'unie706': '湾',
                      'unie70b': '管', 'unie71b': '性', 'unie723': '湖', 'unie72c': '度', 'unie731': '计', 'unie73a': '边',
                      'unie74e': '着', 'unie75b': '解', 'unie75f': '笑', 'unie769': '宁', 'unie775': '动', 'unie785': '会',
                      'unie794': '日', 'unie79d': '找', 'unie79e': '海', 'unie7a9': '浦', 'unie7b1': '影', 'unie7b9': '豆',
                      'unie7cd': '瑞', 'unie7e2': '园', 'unie7e5': '酒', 'unie7f8': '米', 'unie7ff': '时', 'unie803': '提',
                      'unie804': '纪', 'unie80a': '排', 'unie81d': '与', 'unie831': '来', 'unie84d': '热', 'unie855': '材',
                      'unie862': '食', 'unie871': '维', 'unie88f': '双', 'unie89c': '美', 'unie8aa': '环', 'unie8ad': '候',
                      'unie8be': '干', 'unie8c2': '杂', 'unie8d5': '衣', 'unie8d8': '青', 'unie8e0': '星', 'unie8e4': '次',
                      'unie8f4': '学', 'unie905': '烫', 'unie908': '教', 'unie916': '么', 'unie91b': '5', 'unie923': '比',
                      'unie92b': '玉', 'unie92f': '梅', 'unie934': '武', 'unie93b': '东', 'unie947': '际', 'unie94f': '九',
                      'unie969': '批', 'unie96e': '冥', 'unie97d': '富', 'unie990': '块', 'unie9a1': '又', 'unie9af': '凤',
                      'unie9b1': '份', 'unie9cc': '井', 'unie9d3': '凯', 'unie9d9': '元', 'unie9e8': '实', 'unie9f3': '体',
                      'unie9f5': '再', 'unie9fb': '台', 'unie9ff': '旅', 'uniea03': '塘', 'uniea1d': '了', 'uniea2c': '保',
                      'uniea36': '线', 'uniea3f': '员', 'uniea44': '社', 'uniea49': '盛', 'uniea4d': '制', 'uniea64': '想',
                      'uniea65': '贸', 'uniea69': '鲜', 'uniea71': '就', 'uniea8b': '门', 'uniea95': '近', 'unieaaf': '啊',
                      'unieab1': '营', 'unieabf': '于', 'unieace': '永', 'uniead6': '整', 'unieadf': '广', 'unieae7': '午',
                      'unieaf6': '天', 'unieb09': '王', 'unieb0d': '设', 'unieb28': '4', 'unieb50': '博', 'unieb5b': '龙',
                      'unieb5e': '坊', 'unieb62': '事', 'unieb68': '文', 'unieb69': '德', 'unieb75': '宏', 'unieb92': '谷',
                      'unieb94': '虹', 'unieb9a': '足', 'unieba1': '恒', 'uniebab': '字', 'uniebb6': '叉', 'uniebb8': '的',
                      'uniebbb': '讯', 'uniebc1': '厂', 'uniebdd': '奶', 'uniebfc': '诚', 'uniec00': '几', 'uniec0c': '态',
                      'uniec11': '公', 'uniec15': '石', 'uniec17': '很', 'uniec18': '人', 'uniec3d': '间', 'uniec4f': '清',
                      'uniec51': '进', 'uniec55': '方', 'uniec5f': '弄', 'uniec64': '网', 'uniec66': '果', 'uniec6e': '蛋',
                      'uniec70': '氏', 'uniec81': '生', 'uniec90': '溪', 'uniec98': '泰', 'unieca0': '步', 'uniecb1': '其',
                      'uniecb6': '莲', 'uniecb7': '回', 'uniecce': '当', 'unieccf': '般', 'uniecd2': '更', 'uniecda': '外',
                      'uniece6': '3', 'uniecea': '幼', 'uniecee': '7', 'unied2e': '成', 'unied36': '培', 'unied3d': '去',
                      'unied43': '厨', 'unied51': '村', 'unied53': '加', 'unied54': '油', 'unied58': '里', 'unied5b': '可',
                      'unied5f': '别', 'unied60': '南', 'unied65': '气', 'unied7d': '丰', 'unied83': '荐', 'unied84': '两',
                      'unied8f': '总', 'uniedc9': '六', 'uniedd0': '洗', 'uniedd3': 'j', 'unieddd': '名', 'uniedff': '购',
                      'uniee0d': '前', 'uniee21': '八', 'uniee30': '0', 'uniee4c': '嘉', 'uniee5f': '助', 'uniee62': '最',
                      'uniee64': '医', 'uniee79': '个', 'uniee8f': '厦', 'uniee9b': '业', 'unieea4': '院', 'unieec1': '顺',
                      'unieed2': '尚', 'unieed9': '锅', 'unieeda': '运', 'unieee6': '作', 'unieee7': '较', 'unieeed': '单',
                      'unief19': '街', 'unief2f': '8', 'unief34': '中', 'unief36': '造', 'unief3c': '他', 'unief3d': '艺',
                      'unief4a': '费', 'unief5d': '云', 'unief5f': '卫', 'unief72': '秀', 'unief73': '阳', 'unief7a': '这',
                      'unief7c': '祥', 'unief88': '洲', 'unief9e': '商', 'uniefab': '欢', 'uniefaf': '岗', 'uniefb0': '行',
                      'uniefb9': '杨', 'uniefba': '锦', 'uniefd5': '那', 'uniefde': '电', 'uniefe4': '铁', 'uniefe8': '佳',
                      'unieff9': '区', 'unif002': '站', 'unif009': '真', 'unif018': '座', 'unif021': '处', 'unif029': '河',
                      'unif02b': '哈', 'unif032': '快', 'unif035': '接', 'unif057': '多', 'unif059': '皮', 'unif05b': '福',
                      'unif05d': '宝', 'unif086': '无', 'unif08f': '三', 'unif0aa': '头', 'unif0ac': '烟', 'unif0c0': '让',
                      'unif0ea': '糕', 'unif0ec': '县', 'unif0f1': '乡', 'unif102': '饭', 'unif11b': '活', 'unif11d': '康',
                      'unif121': '五', 'unif124': '烤', 'unif13e': '出', 'unif143': '打', 'unif149': '桂', 'unif14a': '屋',
                      'unif150': '6', 'unif151': '西', 'unif16a': '楼', 'unif17e': '荣', 'unif17f': '对', 'unif181': '型',
                      'unif184': '塔', 'unif189': '粉', 'unif18a': '一', 'unif191': '片', 'unif194': '香', 'unif1a1': '十',
                      'unif1af': '七', 'unif1b2': '己', 'unif1ba': '汤', 'unif1c7': '羊', 'unif1ce': '置', 'unif1d0': '情',
                      'unif1da': '窗', 'unif1e7': '还', 'unif1ec': '肉', 'unif1fe': '木', 'unif202': '机', 'unif207': '样',
                      'unif208': '修', 'unif20d': '层', 'unif213': '麻', 'unif217': '理', 'unif227': '鸡', 'unif235': '给',
                      'unif237': '育', 'unif23a': '起', 'unif243': '刚', 'unif271': '缘', 'unif278': '田', 'unif281': '儿',
                      'unif29e': '格', 'unif2a3': '津', 'unif2ae': '风', 'unif2be': '乐', 'unif2c0': '路', 'unif2c1': '后',
                      'unif2c2': '司', 'unif2c7': '平', 'unif2ce': '副', 'unif2db': 'j', 'unif2eb': '药', 'unif2ef': '旁',
                      'unif315': '办', 'unif318': '水', 'unif31e': '具', 'unif325': '居', 'unif388': '集', 'unif394': '太',
                      'unif39b': '连', 'unif3ad': '入', 'unif3b0': '江', 'unif3cc': '式', 'unif3e1': '开', 'unif3fc': '花',
                      'unif3fe': '京', 'unif3ff': '少', 'unif403': '包', 'unif411': '等', 'unif445': '烧', 'unif448': '之',
                      'unif44c': '手', 'unif462': '定', 'unif469': '政', 'unif47e': '安', 'unif483': '牛', 'unif489': '是',
                      'unif4a3': '巷', 'unif4b1': '非', 'unif4cf': '养', 'unif4d8': '2', 'unif4df': '级', 'unif4e6': '年',
                      'unif4ea': '下', 'unif4ec': '以', 'unif4ed': '带', 'unif4fb': '拉', 'unif4ff': '庆', 'unif513': '点',
                      'unif51a': '胜', 'unif525': '新', 'unif531': '位', 'unif536': '技', 'unif545': '角', 'unif546': '鞋',
                      'unif547': '团', 'unif548': '朋', 'unif551': '值', 'unif568': '周', 'unif578': '为', 'unif579': '国',
                      'unif583': '关', 'unif595': '调', 'unif596': '酸', 'unif5a7': '错', 'unif5b5': '完', 'unif5b7': '轩',
                      'unif5bc': '甲', 'unif5bf': '原', 'unif5cf': '厅', 'unif5d4': '虾', 'unif5d6': '种', 'unif5df': '只',
                      'unif5e8': '店', 'unif5ee': '底', 'unif5fb': '馆', 'unif5ff': '看', 'unif605': '售', 'unif608': '鑫',
                      'unif60e': '茶', 'unif611': '柳', 'unif614': '汉', 'unif624': '房', 'unif632': '过', 'unif646': '张',
                      'unif647': '容', 'unif653': '晚', 'unif65a': '民', 'unif686': '临', 'unif68f': '苑', 'unif694': '沙',
                      'unif699': '期', 'unif69c': '珠', 'unif6a8': '达', 'unif6a9': '拍', 'unif6c5': '销', 'unif6c7': '姐',
                      'unif6d8': '直', 'unif6da': '老', 'unif6eb': '金', 'unif6fb': '斜', 'unif703': '评', 'unif710': '也',
                      'unif717': '地', 'unif718': '火', 'unif72d': '吃', 'unif72e': '力', 'unif733': '器', 'unif737': '串',
                      'unif742': '女', 'unif747': '特', 'unif748': '每', 'unif749': '兴', 'unif757': '斯', 'unif75a': '重',
                      'unif76d': '主', 'unif773': '用', 'unif77c': '惠', 'unif77d': '正', 'unif791': '啦', 'unif795': '如',
                      'unif79d': '尝', 'unif79f': '队', 'unif7a2': '峰', 'unif7a8': '说', 'unif7af': '超', 'unif7b0': '幢',
                      'unif7b2': '彩', 'unif7b8': '泉', 'unif7d1': '科', 'unif7da': '餐', 'unif7ed': '栋', 'unif7f7': '友',
                      'unif7f8': '尔', 'unif7fb': '府', 'unif7fd': '旗', 'unif7fe': '价', 'unif807': '些', 'unif822': '但',
                      'unif82d': '港', 'unif82e': '嫩', 'unif831': '兰', 'unif83b': '利', 'unif83e': '振', 'unif842': '和',
                      'unif865': '现', 'unif86e': '没', 'unif875': '寓', 'unif877': '酱', 'unif87c': '鸿', 'unif88e': '汇',
                      'unif89e': '差', 'unif8a9': '然', 'unif8ae': '交', 'unif8af': '贝', 'unif8b5': '央', 'unif8b9': '阿',
                      'unif8c2': '本', 'unif8d2': '卖', 'unif8d7': '钢', 'unif8e0': '客', 'unif8f1': '板', 'unif8f4': '自',
                      'unif8f5': '建', 'unif8ff': '农'},
            'dishname': {'x': '', 'unie001': '平', 'unie007': '斯', 'unie00f': '公', 'unie010': '板', 'unie011': '代',
                         'unie015': '用', 'unie02a': '2', 'unie036': '祥', 'unie047': '设', 'unie04d': '客',
                         'unie05a': '旁',
                         'unie05d': '肉', 'unie05e': '提', 'unie06d': '青', 'unie075': '调', 'unie077': '其',
                         'unie079': '较',
                         'unie082': '七', 'unie083': '前', 'unie0b3': '经', 'unie0b8': '泉', 'unie0bb': '胜',
                         'unie0ca': '便',
                         'unie0d3': '产', 'unie0da': '乐', 'unie0e9': '如', 'unie0ee': '屋', 'unie0ff': '口',
                         'unie109': '层',
                         'unie116': '华', 'unie117': '物', 'unie11b': '滨', 'unie11d': '5', 'unie120': '副',
                         'unie134': '高',
                         'unie139': '满', 'unie151': '小', 'unie154': '批', 'unie15a': '盛', 'unie173': '实',
                         'unie17d': '井',
                         'unie1a1': '机', 'unie1a8': '六', 'unie1ab': '发', 'unie1ad': '线', 'unie1b7': '限',
                         'unie1b8': '一',
                         'unie1be': '费', 'unie1c2': '的', 'unie1cc': '友', 'unie1d4': '本', 'unie1ec': '停',
                         'unie1fa': '厦',
                         'unie201': '入', 'unie204': '旅', 'unie209': '加', 'unie221': '恒', 'unie22f': '那',
                         'unie241': '重',
                         'unie262': '元', 'unie263': '振', 'unie264': '城', 'unie26a': '集', 'unie26f': '马',
                         'unie270': '完',
                         'unie27d': '济', 'unie27f': '北', 'unie2ac': '好', 'unie2ad': '才', 'unie2c8': '话',
                         'unie2eb': '境',
                         'unie2f5': '销', 'unie2fb': '试', 'unie307': '大', 'unie316': '汽', 'unie317': '体',
                         'unie31f': '处',
                         'unie320': '梅', 'unie323': '非', 'unie354': '虹', 'unie370': '津', 'unie374': '关',
                         'unie37c': '值',
                         'unie37d': '笑', 'unie394': '镇', 'unie39f': '片', 'unie3a3': '我', 'unie3aa': '红',
                         'unie3b4': '与',
                         'unie3b6': '置', 'unie3d8': '油', 'unie3e7': '7', 'unie3ed': '塔', 'unie3f1': '营',
                         'unie3f4': '尔',
                         'unie429': '社', 'unie42b': '宏', 'unie433': '麻', 'unie43b': '去', 'unie43c': '1',
                         'unie43e': '缘',
                         'unie447': '地', 'unie457': '办', 'unie45d': '博', 'unie45f': '色', 'unie461': '着',
                         'unie462': '坊',
                         'unie468': '整', 'unie47c': '医', 'unie47d': '车', 'unie493': '真', 'unie49e': '鞋',
                         'unie4a2': '售',
                         'unie4a3': '冥', 'unie4af': '窗', 'unie4b2': '位', 'unie4b5': '横', 'unie4c6': '原',
                         'unie4cb': '全',
                         'unie4cc': '专', 'unie4e3': '货', 'unie4e4': '湖', 'unie505': '行', 'unie506': '河',
                         'unie512': '他',
                         'unie513': '3', 'unie518': '石', 'unie51d': '双', 'unie51e': '司', 'unie542': '辣',
                         'unie548': '厅',
                         'unie54b': '起', 'unie555': '也', 'unie56d': '还', 'unie589': '为', 'unie59b': '角',
                         'unie5a7': '台',
                         'unie5ab': '中', 'unie5bf': '部', 'unie5c0': '晚', 'unie5c2': '轩', 'unie5ca': '0',
                         'unie5cb': '进',
                         'unie5d0': '惠', 'unie5d2': '银', 'unie5d8': '山', 'unie5dd': '无', 'unie5e1': '排',
                         'unie5e2': '气',
                         'unie5e9': '田', 'unie5ea': '都', 'unie5f2': '方', 'unie601': '吧', 'unie604': '吉',
                         'unie60d': '莲',
                         'unie627': '有', 'unie62d': '昌', 'unie634': '生', 'unie641': '度', 'unie646': '文',
                         'unie651': '味',
                         'unie655': '同', 'unie666': '出', 'unie667': '底', 'unie681': '拉', 'unie688': '武',
                         'unie690': '雅',
                         'unie695': '了', 'unie697': '粉', 'unie6a8': '糕', 'unie6b2': '洲', 'unie6b8': '顺',
                         'unie6c4': '路',
                         'unie6c8': '合', 'unie6cf': '过', 'unie6f2': '啦', 'unie6f3': '务', 'unie6fd': '妆',
                         'unie701': '放',
                         'unie703': '微', 'unie70c': '要', 'unie719': '玉', 'unie725': '培', 'unie72b': '主',
                         'unie739': '沿',
                         'unie741': '荐', 'unie749': '岛', 'unie74f': '鲜', 'unie751': '午', 'unie756': '朝',
                         'unie75a': '推',
                         'unie763': '没', 'unie76b': '两', 'unie77c': '接', 'unie78a': '黄', 'unie797': '长',
                         'unie7b2': '信',
                         'unie7c2': '酸', 'unie7d2': '药', 'unie7d4': '4', 'unie7e1': '饰', 'unie7e7': '在',
                         'unie7eb': '一',
                         'unie7f5': '维', 'unie7fa': '厂', 'unie814': '贸', 'unie81f': '农', 'unie828': '热',
                         'unie837': '四',
                         'unie847': '国', 'unie848': '羊', 'unie853': '纪', 'unie85c': '心', 'unie866': '快',
                         'unie868': '康',
                         'unie878': '哈', 'unie87e': '个', 'unie883': '甲', 'unie8aa': '喜', 'unie8bb': '德',
                         'unie8bf': '嘉',
                         'unie8dd': '跟', 'unie8df': '幼', 'unie8e6': '现', 'unie8ea': '情', 'unie8f5': '给',
                         'unie8f6': '叉',
                         'unie901': '环', 'unie907': '只', 'unie90a': '就', 'unie913': '侧', 'unie92b': 'j',
                         'unie956': '巷',
                         'unie966': '央', 'unie973': '连', 'unie980': '算', 'unie983': '场', 'unie99e': '凯',
                         'unie9a1': '太',
                         'unie9a2': '精', 'unie9a8': '觉', 'unie9ac': '氏', 'unie9ae': '下', 'unie9af': '永',
                         'unie9b3': '东',
                         'unie9b4': '配', 'unie9b5': '汇', 'unie9c2': '星', 'unie9ca': '面', 'unie9d5': '动',
                         'unie9db': '王',
                         'unie9dd': '点', 'unie9f7': '八', 'uniea11': '己', 'uniea17': '老', 'uniea20': '弄',
                         'uniea2e': '直',
                         'uniea3b': '奶', 'uniea44': '格', 'uniea46': '锦', 'uniea4f': '张', 'uniea63': '朋',
                         'uniea70': '尝',
                         'uniea80': '技', 'uniea83': '秀', 'uniea8c': '外', 'unieaa1': '可', 'unieab6': '政',
                         'unieabc': '什',
                         'uniead0': '汉', 'unieaed': '谷', 'unieaf2': '座', 'unieaf4': '南', 'unieaf8': '串',
                         'unieafb': '足',
                         'unieb07': '评', 'unieb10': '鱼', 'unieb23': '尚', 'unieb2b': '豆', 'unieb30': '分',
                         'unieb3d': '京',
                         'unieb49': '讯', 'unieb4b': '安', 'unieb4e': '常', 'unieb54': '很', 'unieb99': '多',
                         'unieb9b': '错',
                         'uniebbe': '火', 'uniebc8': '佳', 'uniebca': '旗', 'uniebcd': '料', 'uniebde': '得',
                         'uniebec': '内',
                         'uniebed': '带', 'uniebfe': '水', 'uniec10': '街', 'uniec15': '助', 'uniec20': '强',
                         'uniec2d': '房',
                         'uniec58': '嫩', 'uniec59': '队', 'uniec60': '岭', 'uniec64': '荣', 'uniec65': '管',
                         'uniec84': '十',
                         'uniec8d': '能', 'unieca6': '馆', 'uniecc1': '木', 'uniecc3': '交', 'uniecd4': '港',
                         'uniece3': '买',
                         'uniece4': '龙', 'uniecf6': '吃', 'unied0a': '金', 'unied0f': '特', 'unied17': '期',
                         'unied20': '烧',
                         'unied2e': '钢', 'unied2f': '训', 'unied3c': '赞', 'unied3e': '像', 'unied44': '子',
                         'unied4b': '理',
                         'unied59': '影', 'unied63': '容', 'unied6b': '术', 'unied7f': '铁', 'unied90': '食',
                         'unied95': '几',
                         'unied9b': '汤', 'unied9d': '儿', 'unieda4': '走', 'unieda6': '花', 'uniedb1': '凤',
                         'uniedbb': '斜',
                         'uniedcb': '再', 'uniedce': '达', 'uniedd0': '单', 'uniedd7': '阳', 'unieddf': '商',
                         'uniedfa': '林',
                         'uniee01': '女', 'uniee02': '里', 'uniee03': '景', 'uniee0a': '鸭', 'uniee22': '府',
                         'uniee28': '养',
                         'uniee36': '对', 'uniee3b': '桌', 'uniee41': '迎', 'uniee44': '铺', 'uniee47': '香',
                         'uniee49': '业',
                         'uniee67': '湾', 'uniee6a': '且', 'uniee75': '阿', 'uniee88': '时', 'uniee9e': '瑞',
                         'unieeb6': '甜',
                         'unieebf': '联', 'unieec5': '近', 'unieece': '说', 'unieee4': '计', 'unieee6': '宝',
                         'unieeec': '西',
                         'unieef0': '福', 'unieef3': '堂', 'unieefa': '五', 'unief00': '而', 'unief0a': '茶',
                         'unief14': '清',
                         'unief25': '么', 'unief37': '啊', 'unief39': '们', 'unief4a': '源', 'unief4f': '县',
                         'unief5c': '桂',
                         'unief67': '周', 'unief68': '艺', 'unief75': '彩', 'unief77': '刚', 'unief7f': '让',
                         'unief99': '以',
                         'unief9a': '号', 'uniefa5': '然', 'uniefb4': '兰', 'uniefb9': '布', 'uniefba': '家',
                         'uniefd3': '价',
                         'uniefd8': '局', 'uniefeb': '酒', 'unif010': '光', 'unif01b': '乡', 'unif023': '后',
                         'unif058': '皮',
                         'unif05d': '事', 'unif06b': '量', 'unif07a': '泰', 'unif07e': '最', 'unif087': '居',
                         'unif09a': '比',
                         'unif0c2': '万', 'unif0c7': '世', 'unif0c8': '候', 'unif0d6': '活', 'unif0e1': '丰',
                         'unif0e2': '看',
                         'unif0e5': '人', 'unif0e7': '酱', 'unif0f6': '每', 'unif101': '烤', 'unif11e': '份',
                         'unif11f': '隆',
                         'unif13c': '鑫', 'unif14e': '健', 'unif154': '白', 'unif163': '和', 'unif16a': '你',
                         'unif16b': '解',
                         'unif176': '种', 'unif189': '站', 'unif18b': '利', 'unif19a': '手', 'unif19c': '做',
                         'unif1cf': '边',
                         'unif1d7': '向', 'unif1ea': '科', 'unif1f4': '年', 'unif20f': '百', 'unif22e': '厨',
                         'unif230': '建',
                         'unif235': '春', 'unif23a': '江', 'unif23c': '适', 'unif23d': '米', 'unif241': '鸡',
                         'unif242': '员',
                         'unif246': '岗', 'unif24f': '正', 'unif255': '会', 'unif25a': '装', 'unif264': '保',
                         'unif269': '名',
                         'unif272': '日', 'unif292': '打', 'unif296': '九', 'unif29d': '包', 'unif2d0': '少',
                         'unif2d5': '姐',
                         'unif2df': '柳', 'unif2e7': '州', 'unif2e8': '牌', 'unif2ec': '块', 'unif2f1': '服',
                         'unif2f6': '川',
                         'unif304': '村', 'unif309': '级', 'unif30f': '喝', 'unif310': '更', 'unif319': '别',
                         'unif321': '院',
                         'unif32c': 'j', 'unif32f': '材', 'unif330': '态', 'unif358': '宾', 'unif36d': '爱',
                         'unif392': '电',
                         'unif399': '桥', 'unif3b6': '8', 'unif3c5': '具', 'unif3d0': '楼', 'unif3dc': '峰',
                         'unif3de': '不',
                         'unif3e4': '意', 'unif3e9': '欢', 'unif3f6': '烫', 'unif403': '杨', 'unif408': '团',
                         'unif40c': '风',
                         'unif40d': '想', 'unif40f': '松', 'unif441': '型', 'unif452': '师', 'unif459': '知',
                         'unif45f': '富',
                         'unif47e': '际', 'unif485': '力', 'unif48e': '选', 'unif490': '菜', 'unif498': '杂',
                         'unif4ab': '兴',
                         'unif4ad': '蛋', 'unif4af': '次', 'unif4bb': '器', 'unif4cf': '制', 'unif4d6': '找',
                         'unif4ff': '是',
                         'unif50d': '记', 'unif50f': '门', 'unif52a': '感', 'unif534': '教', 'unif54a': '庄',
                         'unif54e': '化',
                         'unif552': '沙', 'unif558': '回', 'unif55f': '云', 'unif56a': '性', 'unif574': '定',
                         'unif575': '样',
                         'unif57c': '临', 'unif58a': '丽', 'unif58d': '天', 'unif596': '饭', 'unif5a3': '间',
                         'unif5a6': '作',
                         'unif5b1': '等', 'unif5b7': '字', 'unif5b8': '些', 'unif5bc': '贝', 'unif5c9': '挺',
                         'unif5ce': '陵',
                         'unif5cf': '虾', 'unif5e2': '差', 'unif5e3': '步', 'unif5e5': '开', 'unif5ee': '总',
                         'unif5f1': '学',
                         'unif605': '古', 'unif611': '幢', 'unif61d': '通', 'unif624': '附', 'unif62f': '之',
                         'unif631': '道',
                         'unif638': '餐', 'unif63a': '苑', 'unif642': '但', 'unif66f': '童', 'unif683': '自',
                         'unif69a': '运',
                         'unif69c': '三', 'unif6b4': '上', 'unif6b9': '栋', 'unif6ba': '拍', 'unif6c2': '校',
                         'unif6d0': '民',
                         'unif6d9': '这', 'unif6ea': '寓', 'unif6ec': '超', 'unif6f2': '因', 'unif6f3': '果',
                         'unif6f6': '卖',
                         'unif702': '鸿', 'unif708': '品', 'unif718': '所', 'unif73f': '塘', 'unif743': '室',
                         'unif745': '段',
                         'unif74e': '紫', 'unif75e': '广', 'unif765': '式', 'unif772': '9', 'unif773': '海',
                         'unif787': '育',
                         'unif78b': '诚', 'unif78d': '美', 'unif790': '衣', 'unif794': '成', 'unif797': '烟',
                         'unif79b': '溪',
                         'unif7a8': '珠', 'unif7aa': '到', 'unif7b3': '头', 'unif7b7': '饼', 'unif7c9': '店',
                         'unif7e1': '工',
                         'unif7f2': '第', 'unif7f8': '市', 'unif7ff': '于', 'unif80e': '区', 'unif812': '新',
                         'unif81c': '明',
                         'unif81f': '洗', 'unif824': '省', 'unif828': '又', 'unif839': '般', 'unif845': '网',
                         'unif846': '购',
                         'unif84d': '6', 'unif851': '浦', 'unif855': '棒', 'unif85e': '修', 'unif86b': '锅',
                         'unif872': '造',
                         'unif883': '宁', 'unif88b': '庆', 'unif8a8': '当', 'unif8b1': '来', 'unif8c8': '园',
                         'unif8d3': '牛',
                         'unif8f3': '卫', 'unif8fe': '干'},
            'address': {'x': '', 'unie000': '技', 'unie026': '好', 'unie02f': '推', 'unie033': '门', 'unie03f': '那',
                        'unie049': '工', 'unie04c': '厅', 'unie04e': '的', 'unie04f': '尔', 'unie051': '双',
                        'unie056': '城',
                        'unie06d': '电', 'unie082': '乡', 'unie094': '健', 'unie097': '通', 'unie098': '买',
                        'unie099': '太',
                        'unie09f': '前', 'unie0a2': '再', 'unie0b3': '两', 'unie0b9': '内', 'unie0dd': '儿',
                        'unie0e1': '烫',
                        'unie0e5': '原', 'unie0f8': '岗', 'unie0f9': '维', 'unie107': '且', 'unie10b': '是',
                        'unie114': '寓',
                        'unie115': '车', 'unie125': '商', 'unie132': '春', 'unie143': '烟', 'unie156': '附',
                        'unie159': '童',
                        'unie160': '物', 'unie162': '他', 'unie165': '吉', 'unie16d': '要', 'unie17f': '斜',
                        'unie18f': '强',
                        'unie193': '才', 'unie19d': '也', 'unie1ac': '培', 'unie1af': '市', 'unie1b2': '房',
                        'unie1c5': '宏',
                        'unie1ce': '古', 'unie1d4': '多', 'unie1d9': '科', 'unie1e3': '给', 'unie1f1': '田',
                        'unie201': '以',
                        'unie20b': '境', 'unie214': '学', 'unie22d': '态', 'unie232': '务', 'unie23c': '幢',
                        'unie242': '政',
                        'unie252': '般', 'unie25b': '隆', 'unie25d': '计', 'unie26f': '快', 'unie274': '营',
                        'unie277': '妆',
                        'unie279': '味', 'unie28b': '横', 'unie29a': '非', 'unie2a6': '王', 'unie2a9': '女',
                        'unie2aa': '鸭',
                        'unie2bc': '和', 'unie2c0': '塔', 'unie2c2': '运', 'unie2ca': '单', 'unie2fa': '喜',
                        'unie302': '费',
                        'unie31b': '街', 'unie328': '豆', 'unie329': '州', 'unie32d': '七', 'unie339': '们',
                        'unie33c': '吃',
                        'unie347': '会', 'unie34a': '无', 'unie360': '斯', 'unie362': '外', 'unie379': '足',
                        'unie37e': '力',
                        'unie388': '凯', 'unie39a': '蛋', 'unie3a4': '洲', 'unie3ac': '7', 'unie3b6': '样',
                        'unie3b8': '可',
                        'unie3ba': '向', 'unie3de': '珠', 'unie3ec': '信', 'unie3f7': '特', 'unie408': '我',
                        'unie423': '更',
                        'unie437': '加', 'unie43d': '际', 'unie440': '心', 'unie44c': '制', 'unie465': '常',
                        'unie475': '又',
                        'unie47e': '宝', 'unie480': '度', 'unie48d': '还', 'unie4ac': '3', 'unie4d6': '窗',
                        'unie4e4': '汉',
                        'unie4ec': '边', 'unie4fb': '少', 'unie500': '居', 'unie50c': '育', 'unie513': '鸡',
                        'unie51c': '调',
                        'unie52a': '文', 'unie53e': '总', 'unie558': '沙', 'unie55d': '别', 'unie57a': '康',
                        'unie584': '湾',
                        'unie586': '限', 'unie594': '钢', 'unie5a6': '吧', 'unie5b3': '整', 'unie5f5': '成',
                        'unie5f8': '专',
                        'unie5f9': '9', 'unie5fd': '话', 'unie602': '小', 'unie603': '评', 'unie608': '河',
                        'unie618': '西',
                        'unie619': '容', 'unie627': '自', 'unie641': '助', 'unie64a': '阿', 'unie64b': '永',
                        'unie659': '厦',
                        'unie667': '方', 'unie67e': '其', 'unie68c': '2', 'unie68d': 'j', 'unie69c': '日',
                        'unie6a5': '红',
                        'unie6a7': '完', 'unie6ac': '宾', 'unie6ae': '有', 'unie6af': '巷', 'unie6b0': '正',
                        'unie6b2': '连',
                        'unie6bb': '走', 'unie6bc': '料', 'unie6c0': '爱', 'unie6c7': '因', 'unie6d2': '机',
                        'unie6e1': '不',
                        'unie6ec': '期', 'unie6f2': '影', 'unie6f4': '停', 'unie6f9': '高', 'unie6fe': '格',
                        'unie708': '甲',
                        'unie70e': '利', 'unie727': '桥', 'unie732': '华', 'unie743': '过', 'unie747': '哈',
                        'unie750': '林',
                        'unie762': '食', 'unie765': '满', 'unie78e': '近', 'unie795': '解', 'unie796': '湖',
                        'unie7a1': '活',
                        'unie7a9': '晚', 'unie7ac': '乐', 'unie7c0': '中', 'unie7cb': '喝', 'unie7d3': '海',
                        'unie7db': '养',
                        'unie7e5': '网', 'unie7e6': '字', 'unie7f5': '设', 'unie7f8': '一', 'unie801': '油',
                        'unie811': '代',
                        'unie819': '氏', 'unie86b': '发', 'unie872': '同', 'unie882': '松', 'unie891': '花',
                        'unie89a': '找',
                        'unie8ab': '修', 'unie8be': '没', 'unie8cd': '铁', 'unie8d5': '木', 'unie8d8': '衣',
                        'unie8df': '彩',
                        'unie8e4': '甜', 'unie8f0': '泉', 'unie8fc': '馆', 'unie901': '得', 'unie909': '八',
                        'unie92a': '饼',
                        'unie935': '时', 'unie938': '清', 'unie939': '皮', 'unie93b': '杂', 'unie947': '品',
                        'unie948': '拉',
                        'unie954': '像', 'unie95c': '对', 'unie964': '周', 'unie966': '县', 'unie967': '三',
                        'unie96c': '赞',
                        'unie976': '校', 'unie97f': '觉', 'unie984': '叉', 'unie986': '缘', 'unie987': '荐',
                        'unie99d': '出',
                        'unie9aa': '口', 'unie9b0': '贸', 'unie9ba': '艺', 'unie9ce': '里', 'unie9cf': '友',
                        'unie9da': '泰',
                        'unie9e8': '0', 'unie9f9': '头', 'uniea02': '酸', 'uniea18': '虾', 'uniea2d': '底',
                        'uniea32': '昌',
                        'uniea37': '来', 'uniea3a': '比', 'uniea4d': '化', 'uniea4f': '区', 'uniea50': '子',
                        'uniea5b': '社',
                        'uniea77': '提', 'uniea7a': '笑', 'uniea7b': '茶', 'uniea7d': '理', 'uniea81': '姐',
                        'uniea92': '白',
                        'unieaa1': '庆', 'unieab4': '临', 'unieabc': '员', 'unieabd': '级', 'unieac1': '厨',
                        'unieac3': '排',
                        'unieac7': '候', 'uniead7': '京', 'unieada': '恒', 'unieae4': '上', 'unieae7': '装',
                        'unieaed': '省',
                        'unieafb': '事', 'unieb06': '放', 'unieb0b': '饭', 'unieb13': '但', 'unieb19': '洗',
                        'unieb3b': '块',
                        'unieb3e': '如', 'unieb59': '为', 'unieb60': '秀', 'unieb65': '桌', 'unieb67': '份',
                        'unieb6d': '香',
                        'unieb74': '司', 'unieb77': '汇', 'unieb7a': '线', 'unieb7b': '鱼', 'unieb80': '啊',
                        'unieb8e': '南',
                        'unieb9e': '段', 'unieba6': '购', 'uniebaf': '汤', 'uniebb9': '集', 'uniebba': '德',
                        'uniebc9': '一',
                        'uniebcf': '惠', 'uniebd2': '室', 'uniebe0': '嫩', 'uniebf4': '关', 'uniec01': '算',
                        'uniec0c': '黄',
                        'uniec12': '步', 'uniec33': '着', 'uniec3d': '分', 'uniec41': '主', 'uniec5a': '动',
                        'uniec68': '景',
                        'uniec69': '售', 'uniec7a': '进', 'uniec88': '风', 'uniec99': '错', 'unieca1': '部',
                        'uniecab': '货',
                        'uniecb9': '置', 'uniecc3': '山', 'uniecd2': '路', 'uniece2': '真', 'uniecee': '具',
                        'uniecf2': '定',
                        'unied00': '现', 'unied17': '鑫', 'unied2a': '生', 'unied2d': '楼', 'unied2f': '第',
                        'unied41': '知',
                        'unied4b': '座', 'unied4c': '配', 'unied61': '与', 'unied65': '十', 'unied6a': '鞋',
                        'unied6f': '民',
                        'unied71': '江', 'unied72': '石', 'unied79': '名', 'unied82': '值', 'unied85': '粉',
                        'unied86': '尝',
                        'unied87': '用', 'unied98': '术', 'uniedb5': '溪', 'uniedc7': '马', 'uniedc8': '8',
                        'unieddd': '经',
                        'uniede4': '北', 'uniedf4': '入', 'uniedf8': '你', 'uniee01': '次', 'uniee04': '龙',
                        'uniee20': '顺',
                        'uniee28': '金', 'uniee3b': '园', 'uniee4e': '佳', 'uniee51': '轩', 'uniee52': '酒',
                        'uniee5f': '拍',
                        'uniee60': '能', 'uniee68': '队', 'uniee75': '饰', 'uniee7c': '国', 'uniee7e': '银',
                        'uniee84': '串',
                        'uniee8d': '包', 'uniee8f': '紫', 'uniee97': '星', 'unieea4': '鲜', 'unieea6': '达',
                        'unieea9': '局',
                        'unieeac': '兰', 'unieebd': '东', 'unieed0': '微', 'unieee0': '米', 'unieef3': '旅',
                        'unieefc': '阳',
                        'unieefd': '试', 'unief08': '肉', 'unief10': '去', 'unief13': '九', 'unief36': '世',
                        'unief44': '贝',
                        'unief46': '厂', 'unief4f': '朝', 'unief53': '万', 'unief60': '陵', 'unief6f': '镇',
                        'unief70': '棒',
                        'unief76': '团', 'unief7e': '副', 'unief80': '柳', 'unief86': '打', 'unief87': '府',
                        'unief8d': '胜',
                        'uniefa3': '麻', 'uniefb8': '型', 'uniefc8': '欢', 'uniefd5': '到', 'uniefe4': '做',
                        'unif013': '火',
                        'unif020': '嘉', 'unif023': '平', 'unif037': 'j', 'unif03e': '锅', 'unif040': '餐',
                        'unif050': '后',
                        'unif054': '岭', 'unif069': '然', 'unif06f': '师', 'unif080': '牌', 'unif081': '开',
                        'unif08f': '农',
                        'unif090': '环', 'unif092': '地', 'unif094': '色', 'unif0aa': '客', 'unif0ba': '沿',
                        'unif0bb': '庄',
                        'unif0d7': '个', 'unif0d8': '水', 'unif0da': '站', 'unif0eb': '公', 'unif0f1': '布',
                        'unif0f8': '之',
                        'unif100': '只', 'unif130': '合', 'unif140': '交', 'unif151': '间', 'unif164': '滨',
                        'unif169': '百',
                        'unif16d': '弄', 'unif170': '羊', 'unif185': '服', 'unif188': '烧', 'unif18e': '塘',
                        'unif199': '层',
                        'unif1a5': '峰', 'unif1a7': '富', 'unif1a8': '台', 'unif1a9': '点', 'unif1b2': '业',
                        'unif1cb': '式',
                        'unif1d3': '午', 'unif1db': '挺', 'unif1e6': '虹', 'unif1eb': '场', 'unif1ec': '张',
                        'unif1ee': '手',
                        'unif1ef': '些', 'unif1f5': '精', 'unif20f': '医', 'unif241': '栋', 'unif245': '看',
                        'unif249': '作',
                        'unif254': '大', 'unif261': '当', 'unif26a': '美', 'unif26c': '铺', 'unif26e': '道',
                        'unif271': '热',
                        'unif276': '堂', 'unif28e': '荣', 'unif2a2': '六', 'unif2b0': '么', 'unif2b2': '感',
                        'unif2b3': '辣',
                        'unif2c1': '五', 'unif2c6': '超', 'unif2c7': '店', 'unif2c8': '玉', 'unif2d6': '己',
                        'unif2f9': '丰',
                        'unif317': '最', 'unif318': '都', 'unif330': '果', 'unif33a': '鸿', 'unif33b': '材',
                        'unif340': '老',
                        'unif350': '桂', 'unif35b': '武', 'unif374': '说', 'unif37f': '院', 'unif394': '而',
                        'unif3c5': '干',
                        'unif3d1': '牛', 'unif3d7': '丽', 'unif3ec': '处', 'unif3f1': '直', 'unif3f2': '莲',
                        'unif3f7': '下',
                        'unif40d': '情', 'unif42b': '浦', 'unif42f': '兴', 'unif432': '片', 'unif436': '川',
                        'unif442': '杨',
                        'unif445': '央', 'unif44b': '安', 'unif44c': '村', 'unif456': '位', 'unif47e': '旗',
                        'unif490': '本',
                        'unif499': '青', 'unif49a': '重', 'unif4a7': '谷', 'unif4b4': '这', 'unif4ba': '适',
                        'unif4bb': '训',
                        'unif4c9': '福', 'unif4cf': '于', 'unif4ea': '保', 'unif4ee': '管', 'unif4ff': '朋',
                        'unif500': '种',
                        'unif52d': '雅', 'unif539': '盛', 'unif541': '济', 'unif54e': '人', 'unif54f': '产',
                        'unif556': '刚',
                        'unif55f': '元', 'unif560': '诚', 'unif564': '6', 'unif572': '长', 'unif575': '板',
                        'unif579': '造',
                        'unif57d': '全', 'unif581': '井', 'unif58c': '量', 'unif591': '行', 'unif5a1': '起',
                        'unif5a5': '带',
                        'unif5a6': '幼', 'unif5b0': '跟', 'unif5b7': '号', 'unif5c8': '实', 'unif5d4': '苑',
                        'unif5f2': '云',
                        'unif5fa': '1', 'unif61d': '坊', 'unif620': '家', 'unif62e': '便', 'unif63d': '教',
                        'unif659': '酱',
                        'unif65d': '卖', 'unif666': '博', 'unif668': '差', 'unif66e': '较', 'unif693': '体',
                        'unif6b5': '四',
                        'unif6c0': '几', 'unif6ce': '等', 'unif6d5': '药', 'unif6df': '祥', 'unif6ff': '纪',
                        'unif706': '所',
                        'unif708': '建', 'unif716': '屋', 'unif71a': '糕', 'unif725': '烤', 'unif726': '卫',
                        'unif727': '选',
                        'unif728': '锦', 'unif72a': '源', 'unif73d': '接', 'unif73e': '联', 'unif750': '岛',
                        'unif756': '销',
                        'unif758': '梅', 'unif75c': '气', 'unif75d': '汽', 'unif767': '办', 'unif769': '广',
                        'unif770': '性',
                        'unif776': '光', 'unif77c': '新', 'unif785': '迎', 'unif78c': '意', 'unif78d': '5',
                        'unif796': '记',
                        'unif7a5': '振', 'unif7a7': '想', 'unif7ba': '明', 'unif7bc': '器', 'unif7c9': '4',
                        'unif7cd': '旁',
                        'unif7de': '尚', 'unif7fc': '批', 'unif802': '在', 'unif807': '面', 'unif830': '菜',
                        'unif831': '凤',
                        'unif834': '啦', 'unif83f': '什', 'unif843': '津', 'unif844': '回', 'unif84d': '角',
                        'unif855': '讯',
                        'unif858': '很', 'unif868': '宁', 'unif86d': '奶', 'unif870': '年', 'unif877': '侧',
                        'unif885': '港',
                        'unif893': '价', 'unif8a5': '了', 'unif8a9': '瑞', 'unif8cc': '就', 'unif8d5': '让',
                        'unif8df': '天',
                        'unif8e9': '每', 'unif8fe': '冥'}}


def str_to_dic_data(s):
    s1 = s.replace('<e class="address">&#x', '|address_uni').replace(';</e>', '|') \
        .replace('<d class="num">&#x', '|num_uni').replace(';</d>', '|') \
        .replace('<svgmtsi class="review">&#x', '|review_uni').replace(';</svgmtsi>', '|') \
        .replace('<svgmtsi class="shopdesc">&#x', '|shopdesc_uni').replace(';</svgmtsi>', '|') \
        .replace('<svgmtsi class="hours">&#x', '|hours_uni').replace(';</svgmtsi>', '|') \
        .replace('<br />', '\n').replace('&nbsp;', '') \
        .split('|')
    li = []
    for i in s1:
        if '_' in i:
            try:
                k = i.split('_')
                i = dic_data[k[0]][k[-1]]
            except:
                pass
            else:
                pass
        li.append(i)
    s = ''.join(li)
    return s


def visit_url():
    resp = requests.get(url, headers=headers)
    # print(resp.text)
    xml = etree.HTML(resp.text)
    # link_css_font = 'http:' + xml.xpath('/html/head/link[10]/@href')[0]
    # print(link_css_font)  # 获取字体编码文件链接
    source_s = xml.xpath('/html/head/script[3]/text()')[0][24:-1]
    source_data_1 = eval(source_s)  # 字典形式字符串转字典
    # print(source_data_1)
    source_s = xml.xpath('//*[@id="top"]/script[1]/text()')[0][21:-1]
    source_data_2 = {}
    for i in source_s.replace(': "', ':').replace('",', ',').replace(": '", ":").replace("',", ",").replace(':"',
                                                                                                            ':').replace(
            ', ', ',').replace(':{ ', ':"{').replace('" }', '}"').split(','):
        li = i.split(':')
        source_data_2[li[0]] = li[1]
    # print(source_data_2)
    full_data.update(source_data_1), full_data.update(source_data_2)  # 更新full_data字典
    # print(full_data)
    obj = re.compile('<span class="info-name">营业时间：</span>.*?<span class="item">(?P<li>.*?)</span>', re.S)
    T = obj.search(resp.text).group('li')
    T = str_to_dic_data(T)
    print('营业时间：' + T)
    # return link_css_font


def get_url_css_font():
    resp = requests.get(url, headers=headers)
    xml = etree.HTML(resp.text)
    # print(resp.text)
    link_css_font = 'http:' + xml.xpath('/html/head/link[10]/@href')[0]
    print(link_css_font)
    return link_css_font


def get_url_font():
    resp = requests.get(get_url_css_font(), headers=headers).text
    obj1 = re.compile(',url(?P<url>.*?);', re.S)
    urls = obj1.findall(resp)
    obj2 = re.compile("font-family: 'PingFangSC-Regular-(?P<name>.*?)';", re.S)
    names = obj2.findall(resp)
    dic = {}
    for i in range(len(names)):
        print(names[i], urls[i])
        font_url = 'http:' + urls[i][2:-2]
        dic[names[i]] = get_dic(font_url)
    # print(dic)
    # return dic


def font_to_img(_code, filename):
    """将字体画成图片"""
    img_size = 1024
    img = Image.new('1', (img_size, img_size), 255)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(filename, int(img_size * 0.7))
    txt = chr(_code)
    x, y = draw.textsize(txt, font=font)
    draw.text(((img_size - x) // 2, (img_size - y) // 2), txt, font=font, fill=0)
    return img


def identify_word(_ttf_path):
    """识别ttf字体结果"""
    dic = {}
    font = TTFont(_ttf_path)
    ocr = ddddocr.DdddOcr()
    for cmap_code, glyph_name in font.getBestCmap().items():
        bytes_io = BytesIO()
        pil = font_to_img(cmap_code, _ttf_path)
        pil.save(bytes_io, format="PNG")
        word = ocr.classification(bytes_io.getvalue())  # 识别字体
        # print(cmap_code, glyph_name, word)
        # dic.update({glyph_name: word})
        dic[glyph_name] = word
    # print(dic)
    return dic


def get_dic(url):
    resp = requests.get(url)
    name = url[-13:]
    # print(resp.content)
    with open(name, mode='wb') as f:
        f.write(resp.content)
    dic = identify_word(name)
    return dic


def get_info():
    print(url_i)
    resp = requests.get(url_i, headers=headers, params=full_data)
    # print(resp.text)
    shopInfo = resp.json()['msg']['shopInfo']
    shopName = shopInfo['shopName']
    branchName = shopInfo['branchName']
    address = shopInfo['address']
    crossRoad = shopInfo['crossRoad']
    phoneNo = shopInfo['phoneNo']
    # print(phoneNo)
    print('店名：' + shopName, branchName)
    address = str_to_dic_data(address)
    print('地址：' + address)
    crossRoad = str_to_dic_data(crossRoad)
    print('十字路口：' + crossRoad)
    phoneNo = str_to_dic_data(phoneNo)
    print('电话：' + phoneNo)
    resp2 = requests.get(url_s, headers=headers, params=full_data)
    # print(resp2.text)
    avgPrice = resp2.json()['avgPrice']
    avgPrice = str_to_dic_data(avgPrice)
    print('人均：' + avgPrice + '元')
    defaultReviewCount = resp2.json()['defaultReviewCount']
    defaultReviewCount = str_to_dic_data(defaultReviewCount)
    print('评论量：' + defaultReviewCount)
    shopRefinedScoreValueList = resp2.json()['shopRefinedScoreValueList']
    shopRefinedScoreValueList[0] = str_to_dic_data(shopRefinedScoreValueList[0])
    shopRefinedScoreValueList[1] = str_to_dic_data(shopRefinedScoreValueList[1])
    shopRefinedScoreValueList[2] = str_to_dic_data(shopRefinedScoreValueList[2])
    print('口味：' + shopRefinedScoreValueList[0])
    print('环境：' + shopRefinedScoreValueList[1])
    print('服务：' + shopRefinedScoreValueList[2])


def get_pinglun():
    print(url_p)
    resp = requests.get(url_p, headers=headers, params=full_data)
    # print(resp.json())
    reviewAllDOList = resp.json()['reviewAllDOList']
    for i in reviewAllDOList:
        reviewBody = i['reviewDataVO']['reviewBody']
        userNickName = i['user']['userNickName']
        userId = i['user']['userId']
        userId_url = 'http://www.dianping.com/member/' + str(userId)
        print('评论用户网名：' + userNickName + ' ' + userId_url)
        reviewBody = str_to_dic_data(reviewBody)
        print(reviewBody)
        print('----' * 40)
    print('单页评论量：', len(reviewAllDOList))


print(url)
visit_url()
# # print(full_data)
get_info()
get_pinglun()
# print(dic_data.keys())
#
# for i in full_url:
#     print(i)
#     print(full_data)
#     resp = requests.get(i, headers=headers, params=full_data)
#     print(resp.text)
#     print('====='*20)

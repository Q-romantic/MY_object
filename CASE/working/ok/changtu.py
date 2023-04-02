import requests
from PIL import Image
from io import BytesIO
from os import listdir


def get_changtu_urls(urls: list, title: str):  # 通过url直接获取图片并合并成长图，减少走磁盘IO，直接内存处理，快
    ims = []
    for url in urls:
        resp = requests.get(url)
        # print(resp.content)
        img = Image.open(BytesIO(resp.content))  # 二进制转PIL
        ims.append(img)
    width, height = ims[0].size
    result = Image.new(ims[0].mode, (width, height * len(ims)))
    for j, im in enumerate(ims):
        result.paste(im, box=(0, j * height))
    result.save(f'{title}.jpg')


def get_picture_dir(cut_pictures: dir, title: str):  # 通过指定图片所在目录合并成长图
    ims = [Image.open(cut_pictures + '\\' + fn) for fn in listdir(cut_pictures) if fn.endswith('.jpg')]
    width, height = ims[0].size
    result = Image.new(ims[0].mode, (width, height * len(ims)))
    for j, im in enumerate(ims):
        result.paste(im, box=(0, j * height))
    result.save(cut_pictures + f'\\{title}.jpg')


if __name__ == '__main__':
    urls = [
        'https://content.mkzcdn.com/image/20220420/625f89023027b-800x1182.jpg!page-800-x?auth_key=1654598586-0-0-92145a5c201bf7be3f3ff1ca85000d3e',
        'https://content.mkzcdn.com/image/20220420/625f890266def-800x1182.jpg!page-800-x?auth_key=1654598586-0-0-26431c702db69f6abbb655d7099c21f0',
        'https://content.mkzcdn.com/image/20220420/625f8902b145e-800x1182.jpg!page-800-x?auth_key=1654598586-0-0-f74cc22cef473b87b35589f238e70e68',
        'https://content.mkzcdn.com/image/20220420/625f8902ef253-800x1182.jpg!page-800-x?auth_key=1654598586-0-0-b8318efccc436cc8979bdb5dee12cb03'
    ]
    # get_changtu_urls(urls, 'changtu')

    # cut_pictures = 'C:\\Y\\Case\\working\\ok'
    # get_picture_dir(cut_pictures, 'changtu2')


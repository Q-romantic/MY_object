# -*- coding: utf-8 -*-
import pprint
import time
import requests

poiId = '527645'
url = 'https://bj.meituan.com/meishi/api/poi/getMerchantComment'
headers = {
    "Cookie": "uuid=300f1676c1a641409e64.1655864783.1.0.0; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=181893b7455c8-0b237ed6c0e96f-623e5653-1fa400-181893b7455c8; ci=1; __mta=176003613.1655864792730.1655864792730.1655864792730.1; client-id=4a68a2e3-023c-44c2-8acb-fb1ae88bd455; mtcdn=K; userTicket=HNPNLsLemxEVOnZIknZgTvwVnzumHHRnHLmdmLHf; _yoda_verify_resp=WIclpfM1v%2Fr7dFX4l7fs%2FW3sMlpJEsKq8PAgWNX3KBaC1d6HNKXSOLt1R9HW%2BBxzJX6SMLeKn1cdEca4afzaL%2F0UEEc9mOsTEYycifrmAxtAmFBB9rgi2YGUDRfb7GOm%2FtTFTkVxun8hziKsCI0DasWdlsV742P3M%2Fj2tarJPWdgYKrRU9ygYGdg6qadYgrqt%2FSzd%2BDo9982yRvT1crP%2B%2FKbyrxy279r6OYGLFpUIzGd1srOjCsRQQSJtalp95BSKYZ522Zncrtvpgzh%2FvAI8ea5L9H7CQvDX3%2Fnt2S49KcSHqzPGmm5wkVT80Lo%2BLZIfW0SiWkQRnWed4nc3dx5wyGvLUcdG6sfISYmR72FwZS89TMpTvrwUTCMVGvCM%2BJa; _yoda_verify_rid=155d2bf145026048; u=913901191; n=gAC776427767; lt=j_KVZzUfkf71KqIOdDpHU0a8iMkAAAAAexIAAPIZSxwfQ5UvV_SZsSYIv4DyB0SVD45bkNV9ZL0d_9JctXCjBL4PFo-JtUfHkJ3KTQ; mt_c_token=j_KVZzUfkf71KqIOdDpHU0a8iMkAAAAAexIAAPIZSxwfQ5UvV_SZsSYIv4DyB0SVD45bkNV9ZL0d_9JctXCjBL4PFo-JtUfHkJ3KTQ; token=j_KVZzUfkf71KqIOdDpHU0a8iMkAAAAAexIAAPIZSxwfQ5UvV_SZsSYIv4DyB0SVD45bkNV9ZL0d_9JctXCjBL4PFo-JtUfHkJ3KTQ; token2=j_KVZzUfkf71KqIOdDpHU0a8iMkAAAAAexIAAPIZSxwfQ5UvV_SZsSYIv4DyB0SVD45bkNV9ZL0d_9JctXCjBL4PFo-JtUfHkJ3KTQ; unc=gAC776427767; _lxsdk=181893b7455c8-0b237ed6c0e96f-623e5653-1fa400-181893b7455c8; _hc.v=7399ea34-7a0c-a1a2-3e5b-cb55eddd14ee.1655864906; lat=39.889507; lng=116.655757; firstTime=1655866113771; _lxsdk_s=181893b7456-5db-512-71b%7C%7C35",
    "Host": "bj.meituan.com",
    "Referer": "https://bj.meituan.com/meishi/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36"
}
for page in range(1, 6):
    params = {
        "uuid": "300f1676c1a641409e64.1655864783.1.0.0",
        "platform": "1",
        "partner": "126",
        "originUrl": f"https://bj.meituan.com/meishi/{poiId}/",
        "riskLevel": "1",
        "optimusCode": "10",
        "id": poiId,
        "userId": "913901191",
        "offset": (page - 1) * 10,
        "pageSize": "10",
        "sortType": "1",
        "tag": ""
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    # pprint.pprint(data)
    comments_list = data['data']['comments']
    for comments in comments_list:
        commentTime = comments['commentTime']
        comment_time = time.strftime("%Y-%m-%d", time.localtime(int(commentTime) / 1000))
        # comment_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(commentTime)/1000))
        userId = comments['userId']
        userName = comments['userName']
        comment = comments['comment']
        print(comment_time, userName, comment)
        print("-----" * 15)
    print("-----" * 30)
    # break

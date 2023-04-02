import random
import hashlib
# from SubFunction import SubFunction
from collections import Counter  # 引入Counter

player_name_big_list = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13',
                        'A14', 'A15', 'A16', 'A17']  # 参与玩家名字大列表，最多17人


def generate_pokers():
    """生成52张牌，并对牌号赋计算值"""
    poke_types = ['♣-1', '♦-1', '♥-1', '♠-1']  # 按照英文开头字母的顺序排列而成，即梅花 (Club)为C，方块(Diamond)为D，红心(Hearts)为H，黑桃(Spade)为S
    # poke_types = ['1-1', '1-1', '1-1', '1-1']  # 按照英文开头字母的顺序排列而成，即梅花 (Club)为C，方块(Diamond)为D，红心(Hearts)为H，黑桃(Spade)为S
    poke_nums = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
    poke_list = []
    for p_type in poke_types:
        n = 2
        for p_num in poke_nums:
            cord = [f'{p_type}-{p_num}', n]
            n += 1
            poke_list.append(cord)
    return poke_list


def issue_cards(p_names, card_list):
    """发牌"""
    player_dict = {}
    for p in p_names:
        p_cards = random.sample(card_list, 3)
        p_cards = sorted(p_cards, key=lambda x: x[1])  # 排序，默认升序
        player_dict[p] = p_cards
        for card in p_cards:
            card_list.remove(card)
    return player_dict


def get_name_by_equal_pokers(a):
    a1 = {}
    # for k, v in a.items():
    #     data = str(v).replace('♠', '').replace('♣', '').replace('♥', '').replace('♦', '')
    #     a1[k] = hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()
    for k, v in a.items():
        data = str(v).replace('♠', '').replace('♣', '').replace('♥', '').replace('♦', '')
        a1[k] = hash(data)
    list1 = list(a1.values())
    b = dict(Counter(list1))
    c = [key for key, value in b.items() if value > 1]  # 只展示重复元素
    # d = {key: value for key, value in b.items() if value > 1}  # 展现重复元素和重复次数
    for v in c:
        key = [i for i, j in a1.items() if j == v]
        return key


d = set()

# print(p_card_list)
if __name__ == '__main__':
    for n in range(1, 18):
        for j in range(1, 10 + 1):
            # play(n)
            player_names = random.sample(player_name_big_list, n)
            p_card_list = generate_pokers()  # 生成52张牌
            player_dic = issue_cards(player_names, p_card_list)  # 发牌
            # print(player_dic)
            key = get_name_by_equal_pokers(player_dic)
            # print(key)
            if key != None:
                if len(key) > 0:
                    for i in key:
                        print(i, player_dic[i], n)
                d.add(len(key))
            print('---' * 20, f'第 {j} 局')
        print('---' * 22, f'参与人数： {n}')
    print(d)

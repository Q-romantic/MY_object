import random
# from SubFunction import SubFunction
from collections import Counter  # 引入Counter

player_name_big_list = ['A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A07', 'A08', 'A09', 'A10', 'A11', 'A12', 'A13',
                        'A14', 'A15', 'A16', 'A17']  # 参与玩家名字大列表，最多17人
poker_type_count_total = {
    'people_11': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_12': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_13': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_14': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_15': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_16': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_17': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_18': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_19': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_20': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_21': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_22': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_23': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_24': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_25': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_26': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
    'people_27': {'single': 0, 'pair': 0, 'straight': 0, 'same_color': 0, 'color_striaght': 0, 'baozi': 0},
}


def generate_pokers():
    """生成52张牌，并对牌号赋计算值"""
    poke_types = ['♣-8', '♦-4', '♥-2', '♠-1']  # 按照英文开头字母的顺序排列而成，即梅花 (Club)为C，方块(Diamond)为D，红心(Hearts)为H，黑桃(Spade)为S
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


def compare_single(n, p_name, p_cards, score):
    """单三张，先加权、再求和"""
    # 普通最小： [['♦-4-2', 2], ['♥-2-3', 3], ['♠-1-5', 5]] == 53.2 + 7 == 60.2
    # 普通最大： [['♥-2-J', 11], ['♦-4-K', 13], ['♣-8-A', 14]] == 154.1 + 14 == 168.1
    weights = [0.1, 1, 10]  # 给三张牌加权重
    for index, p in enumerate(p_cards):
        score += p[1] * weights[index]
    for p in p_cards:
        score += int(p[0][2])  # 给花色加权重，避免相同牌计算值相等情况
    print(f"玩家-{p_name}-杂牌：".rjust(12, '-'), p_cards, score)
    poker_type_count_total['people_' + str(n + 10)]['single'] += 1
    return score


'''加权后放大倍数对比
		0.1	1	10					权重	0.1,1,10	1,10,100	10,1,0.1	1,1,1	0.1,1,10	min	max
		4	2	1		2	4	8								
普通	min	2	3	5	max	11	13	14	普通	1	1	1	1	1	60.2	168.1
对子	min	2	2	3	max	13	14	14	对子	5	5	6	6	5	196	846.5
顺子	min	2	3	4	max	12	13	14	顺子	17	18	40	29	18	853.4	2859.4
同花	min	2	3	5	max	11	13	14	同花	48	53	228	114	53	2889.6	8068.8
同顺	min	2	3	4	max	12	13	14	同顺	816	954	9120	3306	954	40963.2	137251.2
豹子	min	2	2	2	max	14	14	14	豹子	4701	6627	55213	21490	6627	137269.2	796349.4
'''


def compare_pair(n, p_name, p_cards, score):
    """对子"""
    # 最小对子：[['♦-4-2', 2], ['♥-2-2', 2], ['♠-1-3', 3]] == 32.2 + 7 == 39.2
    # 最大对子：[['♥-2-K', 13], ['♦-4-A', 14], ['♣-8-A', 14]] == 155.3 + 14 == 169.3
    p_nums = {i[1] for i in p_cards}
    if len(p_nums) == 2:
        score *= 5  # 最大普通/最小对子 ~= 4.2883
        print(f"玩家-{p_name}-对子：".rjust(15, '-'), p_cards, score)
        poker_type_count_total['people_' + str(n + 10)]['pair'] += 1
        poker_type_count_total['people_' + str(n + 10)]['single'] -= 1
    return score


def compare_straight(n, p_name, p_cards, score):
    """顺子"""
    # 最小顺子：[['♦-4-2', 2], ['♥-2-3', 3], ['♠-1-4', 4]] == 43.2 + 7 == 50.2
    # 最大顺子：[['♥-2-Q', 12], ['♦-4-K', 13], ['♣-8-A', 14]] == 154.2 + 14 == 168.2
    a, b, c = p_cards
    if c[1] - b[1] == 1 and b[1] - a[1] == 1:
        score *= 20  # 最大对子/最小顺子 ~= 16.86255
        print(f"玩家-{p_name}-顺子：".rjust(15, '-'), p_cards, score)
        poker_type_count_total['people_' + str(n + 10)]['straight'] += 1
        poker_type_count_total['people_' + str(n + 10)]['single'] -= 1
    return score


def compare_same_color(n, p_name, p_cards, score):
    """同花"""
    # 最小同花：[['♦-4-2', 2], ['♥-2-3', 3], ['♠-1-5', 5]] == 53.2 + 7 == 60.2
    # 最大同花：[['♥-2-J', 11], ['♦-4-K', 13], ['♣-8-A', 14]] == 154.1 + 14 == 168.1
    color_set = {i[0][0] for i in p_cards}
    if len(color_set) == 1:
        score *= 60  # 最大顺子/最小同花 ~= 55.8804
        print(f"玩家-{p_name}-同花：".rjust(15, '-'), p_cards, score)
        poker_type_count_total['people_' + str(n + 10)]['same_color'] += 1
        poker_type_count_total['people_' + str(n + 10)]['single'] -= 1
    return score


def compare_color_striaght(n, p_name, p_cards, score):
    """即是顺子又是同花"""
    # 最小同花顺：[['♦-4-2', 2], ['♥-2-3', 3], ['♠-1-4', 4]] == 50.2*20*60 == 60240
    # 最大同花顺：[['♥-2-Q', 12], ['♦-4-K', 13], ['♣-8-A', 14]] == 168.2*20*60 == 201840
    a, b, c = p_cards
    if c[1] - b[1] == 1 and b[1] - a[1] == 1:
        color_set = {i[0][0] for i in p_cards}
        if len(color_set) == 1:
            score *= 1  # 最大同花/最小同花顺 ~= 0.1674303
            print(f"玩家-{p_name}-同花顺：".rjust(19, '-'), p_cards, score)
            poker_type_count_total['people_' + str(n + 10)]['color_striaght'] += 1
            poker_type_count_total['people_' + str(n + 10)]['straight'] -= 1
            poker_type_count_total['people_' + str(n + 10)]['same_color'] -= 1
            poker_type_count_total['people_' + str(n + 10)]['single'] += 1
    return score


def compare_baozi(n, p_name, p_cards, score):
    """豹子"""
    # 最小豹子：[['♦-4-2', 2], ['♥-2-2', 2], ['♠-1-2', 2]] == 22.2 + 7 == 29.2
    # 最大豹子：[['♥-2-A', 14], ['♦-4-A', 14], ['♣-8-A', 14]] == 155.4 + 14 == 169.4
    p_nums = {i[1] for i in p_cards}
    if len(p_nums) == 1:
        score *= 9000  # 最大同花顺/最小豹子 ~= 8335.135
        print(f"玩家-{p_name}-豹子：".rjust(15, '-'), p_cards, score)
        poker_type_count_total['people_' + str(n + 10)]['baozi'] += 1
        poker_type_count_total['people_' + str(n + 10)]['single'] -= 1
    return score


exec_order_list = [
    compare_single,
    compare_pair,
    compare_straight,
    compare_same_color,
    compare_color_striaght,
    compare_baozi
]


def play(n):
    # player_names = ['Alex', 'Peigi', 'blackGirl', 'xiaowu6', 'boldLee']  # 参与玩家
    player_names = random.sample(player_name_big_list, n)
    p_card_list = generate_pokers()  # 生成52张牌
    player_dic = issue_cards(player_names, p_card_list)  # 发牌
    # print(player_dic)
    tmp_dic = {}
    for p_name, p_cards in player_dic.items():
        # print(f"玩家{p_name}".rjust(12, '-'), p_cards)
        score = 0
        for func_name in exec_order_list:
            score = func_name(n, p_name, p_cards, score)
        # print(score)
        tmp_dic[p_name] = score
    # [print(i) for i in tmp_dic.items()]
    poker_max = max(tmp_dic.values())

    def get_dict_key(dic, value):
        key = list(dic.keys())[list(dic.values()).index(value)]
        return key

    name = get_dict_key(tmp_dic, poker_max)
    print(f'{"-" * 80}玩家{name}牌最大')


# @SubFunction().clock
def start(num, count, mode=0):
    def run(a):
        for j in range(1, count + 1):  # 控制重复玩的次数
            play(a)
            print('----' * 20, f'第 {j} 局')
        print('----' * 23, f'本次参与人数： {a} 人')

    if mode == 0:
        run(num)
        get_poker_type_count_probability(num, count)
    else:
        for i in range(1, num + 1):  # 控制参与人数，可1~17人
            run(i)
            get_poker_type_count_probability(i, i * count)


def get_poker_type_count_probability(n, t):
    s = 'people_' + str(n + 10)
    x = 5
    poker_type_count_probability[s]['single'] = round(poker_type_count_total[s]['single'] / t, x)
    poker_type_count_probability[s]['pair'] = round(poker_type_count_total[s]['pair'] / t, x)
    poker_type_count_probability[s]['straight'] = round(poker_type_count_total[s]['straight'] / t, x)
    poker_type_count_probability[s]['same_color'] = round(poker_type_count_total[s]['same_color'] / t, x)
    poker_type_count_probability[s]['color_striaght'] = round(poker_type_count_total[s]['color_striaght'] / t, x)
    poker_type_count_probability[s]['baozi'] = round(poker_type_count_total[s]['baozi'] / t, x)


poker_type_count_probability = {
    "people_11": {},
    "people_12": {},
    "people_13": {},
    "people_14": {},
    "people_15": {},
    "people_16": {},
    "people_17": {},
    "people_18": {},
    "people_19": {},
    "people_20": {},
    "people_21": {},
    "people_22": {},
    "people_23": {},
    "people_24": {},
    "people_25": {},
    "people_26": {},
    "people_27": {},
}
if __name__ == '__main__':
    start(17, 1000, 1)  # 参与人数最多17人   玩的次数   调试模式（默认0）
    for i in poker_type_count_total:
        print(poker_type_count_total[i])
    print('----' * 25)
    for i in poker_type_count_probability:
        print(poker_type_count_probability[i])

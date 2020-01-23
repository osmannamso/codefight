# coding=utf-8
def calc_prizes(prev_results, last_results):
    res = []

    # принтанем места
    ret_str = u'места:\n'
    for i, p in enumerate(last_results[::-1]):
        ret_str += f'{i+1}, {p}\n'

    ex_msg = ''
    if len(set(prev_results)) != len(prev_results):
        ex_msg += 'Players in prev_results must be unique!\n'
    if len(set(last_results)) != len(last_results):
        ex_msg += 'Players in last_results must be unique!\n'
    if not prev_results:
        ex_msg += 'No players in prev_results!\n'
    if not last_results:
        ex_msg += 'No players in last_results!\n'
    if ex_msg != '':
        ret_str += f'{ex_msg}\n'
        raise ValueError(ex_msg)

    # Новенькие (показываем кому должен и убираем)
    for player_last in last_results:
        if player_last not in prev_results:
            if last_results.index(player_last) == len(last_results) - 1:
                res.append(u'%s первое место, но не получает приз и '
                           u'не должен потому что не участвовал в прошлый раз' % player_last)
            else:
                player_to = last_results[last_results.index(player_last) + 1]
                res.append(u'%s получает приз от %s потому что '
                           u'%s не участвовал в прошлый раз и стоит ниже %s' % (player_to, player_last, player_last, player_to))

    for player_last in last_results:
        if player_last not in prev_results:
            last_results.pop(last_results.index(player_last))

    # Те кто не участвовал в этот раз (убираем из анализа)
    for player_prev in prev_results:
        if player_prev not in last_results:
            prev_results.pop(prev_results.index(player_prev))

    # Обгоны
    for i in range(1, len(prev_results)):
        p_lower = prev_results[i-1]
        p_upper = prev_results[i]

        # обогнал
        if last_results.index(p_lower) > last_results.index(p_upper):
            res.append(u'%s получает приз от %s потому что '
                       u'обогнал его' % (p_lower, p_upper))
        # не обогнал
        elif last_results.index(p_upper) > last_results.index(p_lower):
            res.append(u'%s получает приз от %s потому что %s '
                       u'не смог обогнать' % (p_upper, p_lower, p_lower))
    ret_str += '\n'
    ret_str += f'призы:\n'
    for s in res:
        ret_str += f'- {s}\n'

    return ret_str


# игроки
marhabbat = u'marhabbat'
nurbossynov = u'nurbossynov'
suleimenoff = u'suleimenoff'
shyngys_s = u'шыңғыс_с'
bsybanov = u'bsybanov'
osmannamso_ = u'osmannamso_'
chyna_j = u'chyna_j'
pynur = u'pynur'
temirlan_s = u'Temirlan_S'
askhatb = u'асхат_б2'

# результаты турниров
# заносим результаты от последнего к первому месту по возрастанию индекса в массиве
results = [
    [temirlan_s, suleimenoff, marhabbat, nurbossynov, chyna_j,pynur, osmannamso_, shyngys_s, bsybanov],
    # november 19
    [marhabbat, nurbossynov, suleimenoff, shyngys_s, bsybanov, osmannamso_, chyna_j, pynur],
    [marhabbat, chyna_j, pynur, shyngys_s, osmannamso_, suleimenoff, temirlan_s, bsybanov],
    [shyngys_s, suleimenoff, temirlan_s, chyna_j, bsybanov, osmannamso_, pynur],
    [marhabbat, osmannamso_, pynur, shyngys_s, chyna_j, temirlan_s],
    # december 19
    [marhabbat, osmannamso_, chyna_j, bsybanov, shyngys_s, pynur],      # pynur - 3; shyngys_s - 2; bsybanov - 1
    [marhabbat, shyngys_s, pynur, suleimenoff, chyna_j, bsybanov],      # bsybanov - 4, pynur - 3, chyna_j - 2, shyngys_s - 2, suleimenoff - 1
    [pynur, nurbossynov, marhabbat, bsybanov, chyna_j, shyngys_s, osmannamso_], # chyna_j 3, shyngys_s 4, osmannamso_ 3, bsybanov 4, pynur 3, suleimenoff 1
    [pynur, chyna_j, shyngys_s, osmannamso_, marhabbat, nurbossynov, bsybanov], # bsybanov 7, shyngys_s 4, chyna_j 3, osmannamso_ 3, pynur 3, nurbossynov 2, marhabbat 1, suleimenoff 1,
    [suleimenoff, marhabbat, bsybanov, askhatb, osmannamso_, nurbossynov, pynur, shyngys_s], # shyngys_s 7, bsybanov 7, pynur 5, nurbossynov 3, chyna_j 3, marhabbat 1, suleimenoff 1
    # january 2020
    # pynur 3, bsybanov 2, osmannamso_ 1
    [marhabbat, suleimenoff, chyna_j, osmannamso_, bsybanov, pynur],
    # pynur 6, osmannamso_ 3, bsybanov 3
    [marhabbat, nurbossynov, suleimenoff, chyna_j, shyngys_s, bsybanov, osmannamso_, pynur],
]

# calc_prizes(results[-2], results[-1])

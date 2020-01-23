from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from counter import calc_prizes


def parse(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path='./chromedriver', chrome_options=chrome_options)
    driver.get(url)
    print(url)
    sleep(10)
    ours = ['shyngys_s', 'pynur', 'nurbossynov', 'osmannamso_', 'askhat_b2', 'bsybanov', 'marhabbat', 'suleimenoff',
            'chyna_j']
    users = []

    table = driver.find_element_by_css_selector('.card .table')
    for tr in table.find_elements_by_css_selector('.table--body-row'):
        user = {'username': tr.find_element_by_css_selector('.user-info').get_attribute('href').split('/')[-1]}
        if user['username'] == '%D1%88%D1%8B%D2%A3%D2%93%D1%8B%D1%81_%D1%81':
            user['username'] = 'shyngys_s'
        if user['username'] == '%D0%B0%D1%81%D1%85%D0%B0%D1%82_%D0%B12':
            user['username'] = 'askhat_b2'
        if user['username'] not in ours:
            continue
        user['count'] = 0
        user['max'] = ''
        for task in tr.find_elements_by_css_selector('.-layout.-vertical.-center'):
            if len(task.find_elements_by_css_selector('.-bold.-green')) > 0:
                t = task.find_element_by_css_selector('.-font-size-12').get_attribute('innerHTML')
                user['count'] += 1
                if user['max'] == '' or user['max'] < t:
                    user['max'] = t
        users.append(user)
    driver.close()

    for i in range(0, len(users)):
        for j in range(0, len(users)):
            if users[i]['count'] > users[j]['count']:
                users[i], users[j] = users[j], users[i]
            elif users[i]['count'] == users[j]['count']:
                if users[i]['max'] < users[j]['max']:
                    users[i], users[j] = users[j], users[i]

    s = ''
    for i in users:
        s += i['username'] + ' '

    g = open('turnir.txt', 'r')
    ll = g.read()

    s = s[:-1]
    f = open('turnir.txt', 'w')
    f.write(s)
    f.close()

    old_u = ll.split(' ')[::-1]
    new_u = s.split(' ')[::-1]

    return calc_prizes(old_u, new_u)

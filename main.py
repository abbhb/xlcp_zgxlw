import random
import time
from urllib.parse import urlencode
from bs4 import BeautifulSoup
import requests

base_url = "https://api.psy.com.cn"
listjiekou = base_url+"/member/to-test-list"
# 需要 Authorization get
tijiao = base_url+"/test"
login_url = base_url+"/login"


import hashlib

select_ke = 0

'''
howlong 秒
lb 项id
answer |分割，一般都是1为没事
attach LOGIN的key isdistrictadmin逗号分隔
'''

user_info = {}




def password_md5(password:str):
    input_name = hashlib.md5()
    input_name.update(password.encode("utf-8"))
    return (input_name.hexdigest()).lower()
def login():
    loginsuccess = False
    while loginsuccess!=True:
        username = input("请输入用户名\n")
        password = input("请输入密码\n")
        school_name = input("请输入学校名\n")
        school_id = ''
        while school_id=='' :
            try:
                a = int(time.time_ns()/1000000)+10
                t = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=8))
                # l 值不变
                l = "/table/13"
                # 构造字符串
                str_to_hash = str(a) + t + 'get' + l + "6WgczxsGIO2RPkLN"

                Sign = str(a)+'.'+t+'.'+password_md5(str_to_hash)

                # 搜索学校
                hearder = {
                    'Accept-Encoding':'gzip, deflate',
                    'Accept-Language':'zh-CN,zh;q=0.9',
                    'Content-Type':'application/json',
                    'Sec-Fetch-Mode':'cors',
                    'Sec-Fetch-Site':'cross-site',
                    'Sec-Fetch-Dest':'empty',
                    'Accept':'*/*',
                    'Sign':Sign,
                    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x6309092b) XWEB/8555',
                }
                search_school_url = base_url + "/table/13"

                response = requests.get(search_school_url+"?f=a.id%20as%20id%2Cb.name%20as%20label%2Ca.mp_student_expiredate%20as%20isDue&j=%7B%2211%22%3A%22id%22%2C%22a%22%3A%22id%22%7D&w=%7B%22b.name%22%3A%5B%22like%22%2C%22"+school_name+"%22%5D%7D&l=10",headers=hearder)
                # 解析 JSON 数据

                data = response.json()
                if (data['code']!=0):
                    print("请重新输入，异常")
                # 提取需要的信息
                iasd = 0
                for item in data['data']:
                    iasd+=1
                    print('No.'+str(iasd))
                    print(' ID:', item['id'])
                    print(' 学校名:', item['label'])
                    print(' 过期时间:', item['isDue'])
                    print("\n")
                xuhao = int(input("输入序号选择(No.后面的那个数字！！)"))
                if(xuhao>len(data['data'])):
                    input("输入任意值回车重新选择")
                    continue
                school_id = data['data'][iasd-1]['id']
                print("选择的项为:")
                print(' ID:', data['data'][iasd-1]['id'])
                print(' 学校名:', data['data'][iasd-1]['label'])
                print("\n")

            except Exception as e:
                print(e)
                print("\n")
                input("输入任意值回车重新选择")
        # 定义请求参数
        data = {
            'p': password_md5(password),
            'r': 'student',
            'u': username,
            's': school_id
        }
        response = requests.post(login_url, data=data)
        # 解析 JSON 数据
        data = response.json()
        if int(data['code'])==0:
            loginsuccess = True
            user_info = data['data']
            print("登录成功,欢迎您,"+user_info["realname"]+"\n")
            return data['data']
            break

        input("登录失败,回车后重试!\n")

def select_wenjuan():
    datalist = []
    success = False
    while success!=True:
        try:

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                'Authorization': user_info["token"]
            }
            response = requests.get(listjiekou,headers=headers)
            # 解析 JSON 数据
            data = response.json()
            if int(data['code'])==0:
                success = True
            else:
                print("请求异常\n")

                print("\n")
                print("重请求开始\n")
            if len(data['data'])>0:
                datalist = data['data']
        except Exception as e:
            print(e)
            print("\n")
            input("请求失败，是否需要重新请求")
    iasd = 0
    for item in datalist:
        iasd += 1
        print('No.' + str(iasd))
        print(' |ID:', item['id'])
        print(' |问卷名:', item['name'])
        print(' |介绍:', item['intro'])
        print("\n")
    select_ke_temp = ''
    while select_ke_temp =='':
        try:
            nos = int(input("请输入需要自动答的问卷(No.后面的数字即可)"))
            if nos<=len(datalist):
                select_ke = datalist[(nos-1)]['id']
                select_ke_temp = datalist[(nos-1)]['id']
                print("选择成功\n")
                print(datalist[(nos-1)]['name'])
                return datalist[(nos-1)]['id']
                print("\n")
        except Exception as e:
            print(e)
            print("\n")
print("欢迎使用自动心理问卷答题程序 V1.0\n")
print("Power by abbhb\n")
print("Date:2024.3.21\n")
print("Github: https://github.com/abbhb\n")
print('注意：网络不佳的情况可能某次回车会卡顿没有反应，不要多次回车，否则会导致后面的选择被误碰！等待5-6s没反应可尝试再次回车!\n')


ye_s = ''
while ye_s !='yes':
    ye_s = input("阅读完说明后请输入yes正式开始!\n")

print("第一步 登录\n")
user_info = login()
print("第二步 选择问卷\n")
select_ke = select_wenjuan()
print("第三步 判读正确答案是最前面还是最后面(暂时只支持这两种)\n")
xsurl = f'https://www.psy.com.cn/lb/html/{str(select_ke)}.htm'
response = requests.get(xsurl)
response.encoding = 'utf-8'

# 解析 JSON 数据
data = response.text




soup = BeautifulSoup(data,'lxml',from_encoding='utf-8')
qid = 0
divs = soup.select('div.q.am-panel.am-panel-default')
total= 0

show_line_max = 3
all_question= []
print("展示3个题已经选项，判断选最前面的还是选最后的！\n")
# 打印匹配结果
for div in divs:
    item_question = {}
    qid +=1

    sdiv = soup.find('div', id='q_' + str(qid))
    if sdiv!=None:
        total += 1
        # print(sdiv)
        lis = sdiv.select('div.am-panel-hd > span')
        # print('q_' + str(qid)+':')
        names = ''
        for li in lis:
            names += li.text.strip()  # 输出每个li标签的文本内容（去除首尾空格）
        item_question["name"] = names
        item_question["id"] = qid
        daans = []
        # 或者使用 select() 方法直接访问下级标签内容
        lis = sdiv.select('div.q-answer > ul > li')
        answer = 0
        # 遍历所有的li标签，获取里面的文本内容
        for li in lis:
            answer +=1
            daans.append(str(answer)+'.'+li.text.strip())  # 输出每个li标签的文本内容（去除首尾空格）

        item_question["answer"] = daans
        all_question.append(item_question)
print("-------\n")
if show_line_max>=len(all_question):
    show_line_max = len(all_question)-1
for i in range(show_line_max):
    print(str(all_question[i]["id"]) + ".题目:" + all_question[i]["name"])
    print("\n")
    print("答案选项为\n")
    daaas = 0
    for ix in all_question[i]["answer"]:
        daaas += 1
        print(str(daaas)+"."+ix+"\n")
    print("-------------------")
mode = 0
while mode==0:
    xuanze = str(input("请选择最前面的还是最后面的答案，输入q就是前面的，l就是最后面的"))
    if xuanze=='q':
        mode = 1
    elif xuanze == 'l':
        mode = 2
    else:
        print("错误,请重新选择\n")
#构造答案字符串
answer_string = ''
for i in all_question:
    if mode==1:
        asdasdasfq = str(1) + '|'
    else:
        asdasdasfq = str(len(i["answer"])) + '|'
    answer_string += asdasdasfq
answer_string = answer_string[:-1]

def submit():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Authorization': user_info["token"]
    }
    data = {
        'lb': str(select_ke),
        'attach': str(user_info["key"])+','+str(user_info["isdistrictadmin"]),
        'howlong': random.randint(1000, 5000),
        'answer': answer_string
    }

    response = requests.post(tijiao, data=data,headers=headers)
    data = response.json()
    if(data["code"]==0):
        print("提交成功!\n")
    else:
        print(response.text)

submit()
input("按任意键退出!\n")
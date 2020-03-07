import requests
import json

def get_translate():
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 77.0.3865.120 Safari / 537.36'
    }
    words = input('请输入要翻译的内容：')
    format_data = {'i': words,
                   'from': 'AUTO',
                   'to': 'AUTO',
                   'smartresult': 'dict',
                   'client': 'fanyideskweb',
                   'salt': '15834933552030',
                   'sign': 'cd975d4857c13ed9d20331ac9c87a3b4',
                   'ts': '1583493355203',
                   'bv': 'e218a051a7336600dfed880d272c7d6f',
                   'doctype': 'json',
                   'version': '2.1',
                   'keyfrom': 'fanyi.web',
                   'action': 'FY_BY_CLICKBUTTION',
                   'typoResult': 'false'
                   }
    response = requests.post(url, data=format_data, headers=headers)
    content = json.loads(response.text)
    print('返回的content内容是：\n', content)
    print('您翻译的结果是：\n', content['translateResult'][0][0]['tgt'])

if __name__ == "__main__":
    get_translate()

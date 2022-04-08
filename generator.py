# ------------------------------------------- #
# NikitaBeloglazov Software Foundation        #
# (https://vk.com/nikita.beloglazov)          #
#                                             #
# Генератор текстов с bash.im                 #
# ------------------------------------------- #

import requests

response = requests.get("https://bash.im/forweb/?u").text # получаем виджет с рандомным постом ( https://bash.im/webmaster )
data = response[response.find('ding: 15px 15px 12px">')+22:response.find("<' + '/span><' + '/header>")] # получаем дату поста
link = response[response.find('one" href="/quote/')+11:response.find('">#')] # получаем ссылку на пост
text = response[response.find('lor: #21201e">')+14:response.find("<' + '/div><' + 'fo")] # получаем сам текст
# 🠗 обрабатываем текст, заменяем мусор (&quot; на кавычку, br на \n (перенос строки))
text = text.replace("<' + 'br>", "\n").replace("<' + '\\br>", "\n").replace("<' + 'br \\>", "\n").replace("<' + 'br />", "\n").replace("&quot;", '"').replace("&lt;", '<').replace("&gt;", '>')

print(f"{text}\n\n{data} | https://bash.im{link}") # генерируем читаемый и красивый формат для чтения человеком (✨СТИЛЬ✨)

""" # Не знаю, нужно это кому-нибудь вообще или нет, но вот кусок кода, который подчищает после этого переменные для оптимизации
del response
del data
del link
del text
"""

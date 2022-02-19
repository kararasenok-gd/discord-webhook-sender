from discord_webhook import DiscordWebhook
import os
import time

url = input('Введите URL вебхука: ')

os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)
print('checking url...')
os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(1)


if url == "":
    print('ОШИБКА! URL Вебхука не указан!')
    input('Нажмите ENTER для заверщения')
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)
    print('checking url...')
    os.system('cls' if os.name == 'nt' else 'clear')
    time.sleep(1)

DiscordWebhook(url=url, content=f"WebHook Conected by **WebHook Sender by KararasenokApps Inc.**").execute()

while True:

    print('''__          __  _     _                 _    
\ \        / / | |   | |               | |   
 \ \  /\  / /__| |__ | |__   ___   ___ | | __
  \ \/  \/ / _ \ '_ \| '_ \ / _ \ / _ \| |/ /
   \  /\  /  __/ |_) | | | | (_) | (_) |   < 
    \/  \/ \___|_.__/|_| |_|\___/ \___/|_|\_\ 
                                             
        by KararasenokApps Inc.                                     
  _____                _           
 / ____|              | |          
| (___   ___ _ __   __| | ___ _ __ 
 \___ \ / _ \ '_ \ / _` |/ _ \ '__|
 ____) |  __/ | | | (_| |  __/ |   
|_____/ \___|_| |_|\__,_|\___|_|  ''')

    print('''    Подсказка: Введите "changewebhook" для замены вебхука
    Подсказка: Введите quit для выхода из приложения''')
    message = input('Введите сообщение для отправки: ')

    if message == 'changewebhook':
        DiscordWebhook(url=url, content='app conected to new webhook. This webhook is disconected')
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
        url = input('Введите URL другого вебхука: ')
        oldwebhookname = input('Введите название старого вебхука: ')
        oldwebhookservername = input('Введите название сервера на котором находился старый вебхук: ')

        if oldwebhookname == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            oldwebhookname = input('ОШИБКА! Введите название старого вебхука: ')
        elif oldwebhookservername == '':
            os.system('cls' if os.name == 'nt' else 'clear')
            time.sleep(1)
            oldwebhookservername = input('ОШИБКА! Введите название сервера на котором находился старый вебхук: ')

        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)

        if oldwebhookname == '':
            oldwebhookname = 'Unknown WebHook Name'
        elif oldwebhookservername == '':
            oldwebhookservername = 'Unknown WebHook Server'

        #DiscordWebhook(url=url, content=f"WebHook Conected by **WebHook Sender by KararasenokApps Inc.**").execute()
        #time.sleep(2)
        DiscordWebhook(url=url, content=f"Вебхук был заменён на этот! \n **Название старого вебхука: {oldwebhookname}** \n **Название сервера со старым вебхуком: {oldwebhookservername}**").execute()
    elif message == 'quit':
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
        input('Press ENTER')
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)
        DiscordWebhook(url=url, content='Webhook Disconected').execute()
        quit()
    else:
        DiscordWebhook(url=url, content=f"{message}").execute()
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Отправлено!')
        time.sleep(3)
        os.system('cls' if os.name == 'nt' else 'clear')
        time.sleep(1)

        message = '_ _'


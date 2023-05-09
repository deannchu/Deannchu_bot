# Ниже представлен код для однократного запуска

import requests
from bs4 import BeautifulSoup
import json

# Функция для получения первых Всех и Главных новостей и сохранения их в словарь
def All_main_news():
    # Устанавливаем заголовки, чтобы сайт не видел, что парсер - это питон программа
    headers = {
        # Находится в Show Page Source - Network - Headers
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    }
    # Извлекаем новости с сайта Лента ру
    url = "https://lenta.ru/"
    r = requests.get(url = url, headers = headers)
    soup = BeautifulSoup(r.text, "lxml")

    # ---- Все последние новости ----
    topnews =  soup.find_all("a",class_ = "card-mini _topnews") # достаю все статьи из верхнего контейнера основного блока
    all_news_dict = {} #словарь всех последних новостей
    for top in topnews:
        # Находим заголовок
        top_title = top.find("span",class_ = "card-mini__title").text.strip()
        # Находим ссылку на статью
        top_url = f'https://lenta.ru{top.get("href")}'
        # Находим время публикации
        top_time = top.find("time", class_ = "card-mini__date").text
        
        #Ключи для словаря
        top_id = top_url.split("/")[-2]#забираем предпоследний элемент

        all_news_dict[top_id]={
            "title": top_title,
            "url": top_url,
            "time": top_time
        }
    # Сохраняем результат работы в json файл
    with open("all_news_dict.json","w") as file:
        json.dump(all_news_dict, file, indent = 4, ensure_ascii = False)

    # ---- Главные новости ----
    mainnews = soup.find_all("a",class_ = "card-mini _compact") 
    main_news_dict = {} #словарь главных новостей
    for main in mainnews:
        # Находим заголовок
        main_title = main.find("span",class_ = "card-mini__title").text.strip()
        # Находим ссылку на статью
        main_url = f'https://lenta.ru{main.get("href")}'
        
        # Ключи для словаря
        main_id = main_url.split("/")[-2]#забираем предпоследний элемент

        main_news_dict[main_id]={
            "title": main_title,
            "url": main_url
        }
    # Сохраняем результат работы в json файл
    with open("main_news_dict.json","w") as file:
        json.dump(main_news_dict, file, indent = 4, ensure_ascii = False)

# Функция получает первые новости Санкт-Петербурга и сохраняет их в словарь
def SPB_news():
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/region/saint_petersburg?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    spb_news_dict = {} #словарь новостей Санкт-Петербурга
    for card in cards:
        # Находим заголовок
        card_title = card.find("h2", class_ = "mg-card__title").text.strip()
        # Находим аннотацию
        card_annotation = card.find("div", class_ = "mg-card__annotation").text.strip()
        # Находим ссылку на статью
        card_url = card.find("a", class_ = "mg-card__link").get("href")
        # Находим время публикации статьи
        source_time = card.find("span", class_ = "mg-card-source__time").text

        # Создаём ключи для словаря
        card_id = card_url.split("/")[5].split("&")[-3].split("=")[-1] #достаю постоянный ID

        spb_news_dict[card_id]={
            "title": card_title,
            "annotation": card_annotation,
            "url": card_url,
            "time": source_time
        }
    #Сохраняем результат в json файл
    with open("spb_news_dict.json","w") as file:
        json.dump(spb_news_dict, file, indent=4, ensure_ascii = False)

# Функция получает первые новости категории "Интересное" и сохраняет их в словарь
def Interesting_news():
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/rubric/personal_feed?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    interesting_news_dict = {} #словарь новостей категории "Интересное"
    for card in cards:
        # Находим заголовок
        card_title = card.find("h2", class_ = "mg-card__title").text.strip()
        # Находим аннотацию
        card_annotation = card.find("div", class_ = "mg-card__annotation").text.strip()
        # Находим ссылку на статью
        card_url = card.find("a", class_ = "mg-card__link").get("href")
        # Находим время публикации статьи
        source_time = card.find("span", class_ = "mg-card-source__time").text

        # Создаём ключи для словаря
        card_id = card_url.split("/")[5].split("&")[-3].split("=")[-1] #достаю постоянный ID

        interesting_news_dict[card_id]={
            "title": card_title,
            "annotation": card_annotation,
            "url": card_url,
            "time": source_time
        }
    # Сохраняем результат в json файл
    with open("interesting_news_dict.json","w") as file:
        json.dump(interesting_news_dict, file, indent=4, ensure_ascii = False)

# Функция получает первые новости категории "Политика" и сохраняет их в словарь
def Politics_news():
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/rubric/politics?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    political_news_dict = {} #словарь новостей категории "Политика"
    for card in cards:
        # Находим заголовок
        card_title = card.find("h2", class_ = "mg-card__title").text.strip()
        # Находим аннотацию
        card_annotation = card.find("div", class_ = "mg-card__annotation").text.strip()
        # Находим ссылку на статью
        card_url = card.find("a", class_ = "mg-card__link").get("href")
        # Находим время публикации статьи
        source_time = card.find("span", class_ = "mg-card-source__time").text

        # Создаём ключи для словаря
        card_id = card_url.split("/")[5].split("&")[-3].split("=")[-1] #достаю постоянный ID

        political_news_dict[card_id]={
            "title": card_title,
            "annotation": card_annotation,
            "url": card_url,
            "time": source_time
        }
    # Сохраняем результат в json файл
    with open("political_news_dict.json","w") as file:
        json.dump(political_news_dict, file, indent=4, ensure_ascii = False)

# Функция получает первые новости категории "Экономика" и сохраняет их в словарь
def Economics_news():
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/rubric/business?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    econ_news_dict = {} #словарь новостей категории "Экономика"
    for card in cards:
        # Находим заголовок
        card_title = card.find("h2", class_ = "mg-card__title").text.strip()
        # Находим аннотацию
        card_annotation = card.find("div", class_ = "mg-card__annotation").text.strip()
        # Находим ссылку на статью
        card_url = card.find("a", class_ = "mg-card__link").get("href")
        # Находим время публикации статьи
        source_time = card.find("span", class_ = "mg-card-source__time").text

        # Создаём ключи для словаря
        card_id = card_url.split("/")[5].split("&")[-3].split("=")[-1] #достаю постоянный ID

        econ_news_dict[card_id]={
            "title": card_title,
            "annotation": card_annotation,
            "url": card_url,
            "time": source_time
        }
    # Сохраняем результат в json файл
    with open("econ_news_dict.json","w") as file:
        json.dump(econ_news_dict, file, indent=4, ensure_ascii = False)

def main():
    All_main_news()
    SPB_news()
    Interesting_news()
    Politics_news()
    Economics_news()
 
if __name__== '__main__':
    main()
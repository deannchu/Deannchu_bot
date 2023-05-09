import requests
from bs4 import BeautifulSoup
import json

#Функция для добавления новых Всех новостей в словарь, если такие имеются
def all_news_update():
    with open("all_news_dict.json") as file:
        all_news_dict = json.load(file)
   
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    }
    url = "https://lenta.ru/"
    r = requests.get(url = url, headers = headers)

    soup = BeautifulSoup(r.text, "lxml")

    # ---- Все новости ----
    topnews =  soup.find_all("a",class_ = "card-mini _topnews") # достаю все статьи из верхнего контейнера основного блока
    
    all_fresh_news = {} #словарь всех свежих новостей
    for top in topnews:
        # Находим ссылку на статью
        top_url = f'https://lenta.ru{top.get("href")}'
        #Ключи для словаря
        top_id = top_url.split("/")[-2]

        if top_id in all_news_dict:
            continue
        else:
            # Находим заголовок
            top_title = top.find("span",class_ = "card-mini__title").text.strip()
            # Находим ссылку на статью
            top_url = f'https://lenta.ru{top.get("href")}'
            # Находим время публикации
            top_time = top.find("time", class_ = "card-mini__date").text
            #Ключи для словаря
            top_id = top_url.split("/")[-2]
            
            all_news_dict[top_id]={
                "title": top_title,
                "url": top_url,
                "time": top_time
                }
            
            all_fresh_news[top_id]={
                "title": top_title,
                "url": top_url,
                "time": top_time
                }
    #Сохраняем результат работы в json файл
    with open("all_news_dict.json", "w") as file:
        json.dump(all_news_dict, file, indent=4, ensure_ascii=False)
    
    return all_fresh_news

#Функция для добавления новых Главных новостей в словарь, если такие имеются
def main_news_update():
    with open("main_news_dict.json") as file:
        main_news_dict = json.load(file)
   
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15"
    }
    url = "https://lenta.ru/"
    r = requests.get(url = url, headers = headers)

    soup = BeautifulSoup(r.text, "lxml")
    mainnews =  soup.find_all("a",class_ = "card-mini _topnews") # достаю все статьи из верхнего контейнера основного блока
    
    main_fresh_news = {} #словарь всех последних новостей
    for main in mainnews:
        # Находим ссылку на статью
        main_url = f'https://lenta.ru{main.get("href")}'
        #Ключи для словаря
        main_id = main_url.split("/")[-2]

        if main_id in main_news_dict:
            continue
        else:
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

            main_fresh_news[main_id]={
                "title": main_title,
                "url": main_url
                }
    #Сохраняем результат работы в json файл
    with open("main_news_dict.json", "w") as file:
        json.dump(main_news_dict, file, indent=4, ensure_ascii=False)
    
    return main_fresh_news

#Функция для добавления новых новостей Санкт-Петербурга в словарь, если такие имеются
def spb_news_update():
    with open("spb_news_dict.json") as file:
        spb_news_dict = json.load(file)
    
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/region/saint_petersburg?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    spb_fresh_news = {} #словарь всех последних новостей
    for card in cards:
        # Находим ссылку на статью
        card_url = f'https://lenta.ru{card.get("href")}'
        #Ключи для словаря
        card_id = card_url.split("/")[-2]

        if card_id in spb_news_dict:
            continue
        else:
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
            
            spb_fresh_news[card_id]={
                "title": card_title,
                "annotation": card_annotation,
                "url": card_url,
                "time": source_time
                }
    #Сохраняем результат работы в json файл
    with open("spb_news_dict.json", "w") as file:
        json.dump(spb_news_dict, file, indent=4, ensure_ascii=False)
    
    return spb_fresh_news

#Функция для добавления новых новостей категории "Интересное" в словарь, если такие имеются
def interesting_news_update():
    with open("interesting_news_dict.json") as file:
        interesting_news_dict = json.load(file)
    
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/rubric/personal_feed?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    int_fresh_news = {} #словарь всех последних новостей
    for card in cards:
        # Находим ссылку на статью
        card_url = f'https://lenta.ru{card.get("href")}'
        #Ключи для словаря
        card_id = card_url.split("/")[-2]

        if card_id in interesting_news_dict:
            continue
        else:
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
            
            int_fresh_news[card_id]={
                "title": card_title,
                "annotation": card_annotation,
                "url": card_url,
                "time": source_time
                }
    #Сохраняем результат работы в json файл
    with open("interesting_news_dict.json", "w") as file:
        json.dump(interesting_news_dict, file, indent=4, ensure_ascii=False)
    
    return int_fresh_news

#Функция для добавления новых новостей категории "Политика" в словарь, если такие имеются
def political_news_update():
    with open("political_news_dict.json") as file:
        political_news_dict = json.load(file)
    
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/rubric/politics?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    political_fresh_news = {} #словарь всех последних новостей
    for card in cards:
        # Находим ссылку на статью
        card_url = f'https://lenta.ru{card.get("href")}'
        #Ключи для словаря
        card_id = card_url.split("/")[-2]

        if card_id in political_news_dict:
            continue
        else:
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
            
            political_fresh_news[card_id]={
                "title": card_title,
                "annotation": card_annotation,
                "url": card_url,
                "time": source_time
                }
    #Сохраняем результат работы в json файл
    with open("political_news_dict.json", "w") as file:
        json.dump(political_news_dict, file, indent=4, ensure_ascii=False)
    
    return political_fresh_news

#Функция для добавления новых новостей категории "Экономика" в словарь, если такие имеются
def economics_news_update():
    with open("econ_news_dict.json") as file:
        econ_news_dict = json.load(file)
    
    headers = { 
        "Cookie": "news_lang=ru; KIykI=1; _ym_d=1682621706; _ym_isad=1; _ym_uid=1681293551884608471; gdpr=0; tmr_lvid=d1e8956ba6d68b78144405633ce79e44; tmr_lvidTS=1681293549993; tmr_detect=1%7C1682621706395; _yasc=XAT8YWnTVulc5BdobgVLDxubNlzj5KZB5K+2jcpQuvh2EYihXDe2+Fo7zEMHPg==; bltsr=1; Zen-User-Data={%22zen-theme%22:%22light%22}; Session_id=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.CnqOTA2wRMMsDUk2jbPO3p08rNY; sessionid2=3:1681572383.5.0.1681293547923:MJFDsg:bfe4.1.2:1|1246965227.0.2.0:3.3:1680727009|64:10008870.767689.fakesign0000000000000000000; yandex_login=Deannchu; zen_sso_checked=1; mda2_beacon=1681293547962; yandexuid=6693970021680466951; ys=udn.cDpEZWFubmNodQ%3D%3D#c_chck.3913848329",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.1 Safari/605.1.15",      
    }
    # Извлекаем новости с сайта Яндекс Дзен
    url = "https://dzen.ru/news/rubric/business?issue_tld=ru"
    r = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    cards = soup.find_all("div", class_="mg-card")
    
    econ_fresh_news = {} #словарь всех последних новостей
    for card in cards:
        # Находим ссылку на статью
        card_url = f'https://lenta.ru{card.get("href")}'
        #Ключи для словаря
        card_id = card_url.split("/")[-2]

        if card_id in econ_news_dict:
            continue
        else:
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
            
            econ_fresh_news[card_id]={
                "title": card_title,
                "annotation": card_annotation,
                "url": card_url,
                "time": source_time
                }
    #Сохраняем результат работы в json файл
    with open("econ_news_dict.json", "w") as file:
        json.dump(econ_news_dict, file, indent=4, ensure_ascii=False)
    
    return econ_fresh_news

def main():
    all_news_update()
    main_news_update()
    spb_news_update()
    interesting_news_update()
    political_news_update()
    economics_news_update()
    
if __name__== '__main__':
    main()
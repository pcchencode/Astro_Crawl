import re
import requests as rs
import datetime
from bs4 import BeautifulSoup
import random
import time
import pandas as pd


def get_astro_info(url):
    req = rs.get(url)
    if req.status_code==200:
        web_content = req.text
        soup = BeautifulSoup(web_content, 'lxml')
        
        date_content = soup.find('select', id='iAcDay')
        date_content = soup.find('option', selected='selected')
        tday_date = date_content.text
        
        aname_content = soup.find('a', href='javascript:void(0);')
        astro_name = aname_content.text[-3:]
        
        today_content = soup.find('div', class_='TODAY_CONTENT')
        today_content = today_content.find_all('p')
        
        total_trend_rate = today_content[0].text[-6:-1] # 整體運勢評分
        total_trend_desc = today_content[1].text # 整體運勢說明
        love_trend_rate = today_content[2].text[-6:-1] # 愛情運勢評分
        love_trend_desc = today_content[3].text # 愛情運勢說明
        work_trend_rate = today_content[4].text[-6:-1] #事業運勢評分
        work_trend_desc = today_content[5].text # 事業運勢說明
        money_trend_rate = today_content[6].text[-6:-1] # 財運運勢評分
        money_trend_desc = today_content[7].text # 財運運勢說明
        
        astro_info = []
        astro_info.append({'DATE':tday_date, 'ASTRO':astro_name, 'TOTAL_TREND_RATE':total_trend_rate, 'TOTAL_TREND_DESC':total_trend_desc
                          , 'LOVE_TREND_RATE':love_trend_rate, 'LOVE_TREND_DESC':love_trend_desc
                          , 'WORK_TREND_RATE':work_trend_rate, 'WORK_TREND_DESC':work_trend_desc
                          , 'MONEY_TREND_RATE':money_trend_rate, 'MONEY_TREND_DESC':money_trend_desc})
        astro_info = pd.DataFrame(astro_info)
        astro_info = astro_info[['DATE', 'ASTRO', 'TOTAL_TREND_RATE', 'TOTAL_TREND_DESC'
                           , 'LOVE_TREND_RATE', 'LOVE_TREND_DESC'
                           , 'WORK_TREND_RATE', 'WORK_TREND_DESC'
                           , 'MONEY_TREND_RATE', 'MONEY_TREND_DESC']]
        
        return astro_info
    
    else:
        return 404


def main():
    data = get_astro_info(url='http://astro.click108.com.tw/daily_9.php?iAstro=0')
    for i in range(1, 12):
        time.sleep(random.uniform(0,2))
        data = data.append(get_astro_info(url='http://astro.click108.com.tw/daily_9.php?iAstro='+str(i)))
	    
    return data



if __name__ == '__main__':
    main().to_csv('astro_info_'+str(datetime.datetime.today().strftime('%Y%m%d'))+'.csv', index=False)
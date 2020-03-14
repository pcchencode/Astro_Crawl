# Astro_Crawl
* 目標網址：[科技紫微網](http://astro.click108.com.tw)
* 需求：請參考檔案 [需求.pdf](https://github.com/pcchencode/Astro_Crawl/blob/master/需求.pdf)

## 使用方法
* 排程：每日早上 9 點執行一次
```
* 09 * * * python3 \path\to\the\file\astro.py
```
* 資料輸出：csv.file, 檔名依照執行日期
  - 後續可利用套件 `pymssql` 將輸出的檔案每日 insert value into database

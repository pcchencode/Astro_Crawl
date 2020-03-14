# Astro_Crawl
* 目標網址：[科技紫微網](http://astro.click108.com.tw)
* 需求：請參考檔案 [需求.pdf](https://github.com/pcchencode/Astro_Crawl/blob/master/需求.pdf)

## 使用方法
* Docker:
1. download and install Docker desktop  [Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/) or [Windows](https://hub.docker.com/editions/community/docker-ce-desktop-windows)

2. clone this repo and cd into this as working directory

3. build image from `Dockerfile` and run `astro.py` in container:
```
docker build -t my_image .
docker run --mount type=bind,source={/YOUR/PATH/OF/LOCAL/WORKING/DIRECTORY},target=/work_dir my_image python3 /work_dir/astro.py 
```

* linux or terminal:
1. clone this repo and cd into this as working directory

2. install the required packages in [requirements.txt](https://github.com/pcchencode/Astro_Crawl/blob/master/requirements.txt)

3. command
```
python3 astro.py 
```



## 排程：每日早上 9 點執行一次
* 使用 `crontab` 建置排程
  ```
  * 09 * * * python3 \path\to\the\file\astro.py
  ```

* 資料輸出：csv.file, 檔名依照執行日期, EX. [astro_info_20200314.csv](https://github.com/pcchencode/Astro_Crawl/blob/master/astro_info_20200314.csv)
  - 後續可利用套件 [pymssql](https://pypi.org/project/pymssql/) 將輸出的檔案每日 insert value into database

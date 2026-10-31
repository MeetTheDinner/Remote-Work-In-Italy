import requests


url2023 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2023%2F4%2F4.zip&filename=RCFL_2023_Quarto_trimestre_IT.zip"
url2022 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2022%2F4%2F4.zip&filename=RCFL_2022_Quarto_trimestre_IT.zip"
url2021 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2021%2F4%2F4.zip&filename=RCFL_2021_Quarto_trimestre_IT.zip"
url2020 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2020%2F4%2F4.zip&filename=RCFL_2020_Quarto_trimestre_IT.zip"
url2019 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2019%2F4%2F4.zip&filename=RCFL_2019_Quarto_trimestre_IT.zip"
url2018 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2018%2F4%2F4.zip&filename=RCFL_2018_Quarto_trimestre_IT.zip"
url2017 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2017%2F4%2F4.zip&filename=RCFL_2017_Quarto_trimestre_IT.zip"
url2016 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2016%2F4%2F4.zip&filename=RCFL_2016_Quarto_trimestre_IT.zip"
url2015 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2015%2F4%2F4.zip&filename=RCFL_2015_Quarto_trimestre_IT.zip"
url2014 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2014%2F4%2F4.zip&filename=RCFL_2014_Quarto_trimestre_IT.zip"

url_list = ["url2014", "url2015", "url2016", "url2017", "url2018", "url2019", "url2020", "url2021", "url2022", "url2023"]

url_dict = {
            url2014: "RCFL_2014_Q4.zip", 
            url2015: "RCFL_2015_Q4.zip", 
            url2016: "RCFL_2016_Q4.zip", 
            url2017: "RCFL_2017_Q4.zip", 
            url2018: "RCFL_2018_Q4.zip", 
            url2019: "RCFL_2019_Q4.zip", 
            url2020: "RCFL_2020_Q4.zip", 
            url2021: "RCFL_2021_Q4.zip", 
            url2022: "RCFL_2022_Q4.zip", 
            url2023: "RCFL_2023_Q4.zip" 
            }

headers = {
    "User-Agent": "Mozilla/5.0"
}

for url in url_dict.keys():

    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(url_dict[url.value()], "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
    """

    with requests.get(url2023, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open("RCFL_2023_Q4.zip", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)

    with requests.get(url2021, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open("RCFL_2021_Q4.zip", "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
    """

print("Download completed")
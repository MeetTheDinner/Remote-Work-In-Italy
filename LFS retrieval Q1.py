import requests
 

url2023 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2023%2F1%2F1.zip&filename=RCFL_2023_Primo_trimestre_IT.zip"
url2022 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2022%2F1%2F1.zip&filename=RCFL_2022_Primo_trimestre_IT.zip"
url2021 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2021%2F1%2F1.zip&filename=RCFL_2021_Primo_trimestre_IT.zip"
url2020 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2020%2F1%2F1.zip&filename=RCFL_2020_Primo_trimestre_IT.zip"
url2019 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2019%2F1%2F1.zip&filename=RCFL_2019_Primo_trimestre_IT.zip"
url2018 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2018%2F1%2F1.zip&filename=RCFL_2018_Primo_trimestre_IT.zip"
url2017 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2017%2F1%2F1.zip&filename=RCFL_2017_Primo_trimestre_IT.zip"
url2016 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2016%2F1%2F1.zip&filename=RCFL_2016_Primo_trimestre_IT.zip"
url2015 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2015%2F1%2F1.zip&filename=RCFL_2015_Primo_trimestre_IT.zip"
url2014 = "https://www.istat.it/wp-content/themes/EGPbs5-child/microdata/download.php?file=%2F2%2F2014%2F1%2F1.zip&filename=RCFL_2014_Primo_trimestre_IT.zip"

url_dict = {
            url2014: "RCFL_2014_Q1.zip", 
            url2015: "RCFL_2015_Q1.zip", 
            url2016: "RCFL_2016_Q1.zip", 
            url2017: "RCFL_2017_Q1.zip", 
            url2018: "RCFL_2018_Q1.zip", 
            url2019: "RCFL_2019_Q1.zip", 
            url2020: "RCFL_2020_Q1.zip", 
            url2021: "RCFL_2021_Q1.zip", 
            url2022: "RCFL_2022_Q1.zip", 
            url2023: "RCFL_2023_Q1.zip" 
            }

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Iterate through dictionary items (url, filename pairs)
for url, filename in url_dict.items():
    print(f"Downloading {filename}...")
    with requests.get(url, headers=headers, stream=True) as r:
        r.raise_for_status()
        with open(filename, "wb") as f:
            for chunk in r.iter_content(chunk_size=1024*1024):
                if chunk:
                    f.write(chunk)
    print(f"✓ {filename} downloaded")

print("Download completed")
from bs4 import BeautifulSoup as BS
import urllib.request as req
import urllib.parse as pa
import pandas as pd
from tqdm import tqdm_notebook
import time
import re
import math


# 평점 url 얻기 위한 url_open

url = 'https://cdn.class101.net/videos/12ab0679-2e47-4410-b45f-8e26dbc3e03f/hls/master_HLS-1080p.m3u8'
url_open = req.urlopen(url).read()


with open('01.m3u8', 'wb') as f:
    f.write(url_open)
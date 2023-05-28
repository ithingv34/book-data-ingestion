import os
import time
import json
import pandas as pd

from utils.http_message import HTTPMessage
from core.base_scraper import BaseScraper

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_PATH = os.path.dirname(CURRENT_PATH)
SAVE_DIR = os.path.join(PROJECT_PATH, 'data')

class OreillyScraper(BaseScraper):
    def __init__(self):
        super().__init__()

    def get_book_data(self):
        
        book_data = []
        curr_page = 1

        while True:
        
            url = 'https://learning.oreilly.com/search/api/search/'
        
            params = {
                "q": "*",
                "type": ["book"],
                "publishers": "O'Reilly Media, Inc.",
                "rows": 100,
                "user_language": "en",
                "enableLiveCoursesInCoursesSearch": False,
                "report": True,
                "page": curr_page
            }

            headers = {
                'Accept': '*/*',
                'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
                'Connection': 'keep-alive',
                'Cookie': '_vwo_uuid_v2=D690F3DE3ECB1A26C0B015CE672D6D284|eefbc1769e4dfa2e273816043dbdc36f; _mkto_trk=id:107-FMS-070&token:_mch-oreilly.com-1671280105241-94558; fs_uid=#SAVCH#4922918881808384:6207216643035136:::#/1703128408; _gcl_au=1.1.1601706592.1679221297; _uetvid=4d08e4a07e0611ed96922f87197dfca3; orm-rt=bd6947e5d0e44855b125d07e806dae3d; _ga_092EL089CH=GS1.1.1684739202.10.1.1684740038.30.0.0; akaalb_LearningALB=~op=learning_oreilly_com_GCP_ALB:learning_oreilly_com_gcp1|~rv=67~m=learning_oreilly_com_gcp1:0|~os=3284f997983d0bd4e10a6b83f3b25a7c~id=ad743a232fa79be7ed123ec13da3de5c; AMP_MKTG_49f7a68a85=JTdCJTdE; _gid=GA1.2.1928118655.1685092505; ak_bmsc=489B16D49D554030205EBA45D95E7A33~000000000000000000000000000000~YAAQjaUrF5IszBGIAQAAoJ3GVxPj7sK3oX4oiOlKZ8jkbGpm3nuR8BfYGnxd3YvQ/FCtnmfMOiKtkGa03fEdCcm3TnT2USygDL8o34aNUY/UMUV78QMxh9YhDpw2sWYEYsDsYyaEvGR9t+7InC3ICN5cHQTIbN24zWWL7HVbjXuacAbfwe2rblGYU1/VTUsRfKkCmwGRnffNLO+NqRwKhWOauzQncdE0DJDjkoRueFWBPh6/kWe4aQY3a4TLCT5d5EQjMiDvnzHiVhYW4bF8X0/X/K0Y4QQZ4Fu74y9yA79uMYyx4LUa9YnhB+EZEFrkWDJQ5ldzJy1d7QNHUbyMGpnDaCmm3XBovdnHlz+WBUa7YMMid8aVzCe97XpK3V/Z; orm-jwt=eyJhbGciOiAiUlMyNTYiLCAia2lkIjogImI1ZjliMGU1YzM1ZDRiY2NjYjY1YzZkOGQxYzQ2MWI5In0.eyJhY2N0cyI6IFsiNjgxZWU1MzEtNzAxZi00NDkzLTliMzEtMDU0ZDA2MWI3ZTU4Il0sICJlaWRzIjogeyJleGFjdHRhcmdldCI6ICJwbGF0Zm9ybV9wcm9kXzhiODhmM2Y1LTVmNDEtNGY5Ny1iMDE0LTA4OTEwM2JkNzk3OSIsICJoZXJvbiI6ICI4Yjg4ZjNmNS01ZjQxLTRmOTctYjAxNC0wODkxMDNiZDc5NzkifSwgImVudiI6ICJwcm9kdWN0aW9uIiwgImV4cCI6IDE2ODUxMDI3MTEsICJpbmRpdmlkdWFsIjogdHJ1ZSwgInBlcm1zIjogeyJhY2FkbSI6ICJ2IiwgImNuZnJjIjogInYiLCAiY3ByZXgiOiAidiIsICJjc3N0ZCI6ICJ2IiwgImVwdWJzIjogInYiLCAibHJwdGgiOiAidiIsICJsdnRyZyI6ICJ2IiwgIm50YmtzIjogInYiLCAib3Jpb2wiOiAidiIsICJwbHlscyI6ICJjZXYiLCAic2JzY3AiOiAiY2V2IiwgInNjbnJpbyI6ICJ2IiwgInVzYWdlIjogImMiLCAidXNycGYiOiAiZXYiLCAidmlkZW8iOiAidiJ9LCAic3ViIjogIjhiODhmM2Y1LTVmNDEtNGY5Ny1iMDE0LTA4OTEwM2JkNzk3OSJ9.GVRy_5CQG7BrOjVcA8BydpWFyNqnl5HU5dP_R8biAfZoXuELg_W4cToa0MhL0UJFxtnYn6wDV8E9n5X_OuhwbPLcqm0MZChCs-OJR_zgy0UY61YjuGOva9jlhQsGlDHnoC2gunRebXWS-3mH0O-2i0A4cnS22hQeoxZk3aCx2g8; AMP_49f7a68a85=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjJWZV9rSkUwQzQ2cWhoeGgxN1FiN2FwJTIyJTJDJTIydXNlcklkJTIyJTNBJTIyOGI4OGYzZjUtNWY0MS00Zjk3LWIwMTQtMDg5MTAzYmQ3OTc5JTIyJTJDJTIyc2Vzc2lvbklkJTIyJTNBMTY4NTA5OTAxODM0NyUyQyUyMm9wdE91dCUyMiUzQWZhbHNlJTJDJTIybGFzdEV2ZW50VGltZSUyMiUzQTE2ODUxMDE4NjYyNjglMkMlMjJsYXN0RXZlbnRJZCUyMiUzQTg4JTdE; _gat_UA-112091926-1=1; _ga=GA1.1.2144888109.1671280105; OptanonConsent=isIABGlobal=false&datestamp=Fri+May+26+2023+20%3A51%3A07+GMT%2B0900+(%ED%95%9C%EA%B5%AD+%ED%91%9C%EC%A4%80%EC%8B%9C)&version=6.25.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&AwaitingReconsent=false&geolocation=KR%3B11; OptanonAlertBoxClosed=2023-05-26T11:51:07.018Z; bm_sv=677C58A7676314609B8BD5273589EA83~YAAQ1DMsF21y/A2IAQAAWAPmVxO90hJWTU+pcJOtfzwvRy58ZL573sh2R5GCsrteYrg/Y6O942KM0foNQ8jcb/j8L5xd9NfV6b2CbHMwfTE2Ca2M0e8JbykTVam6ZKC1DeFie84s1GBVIORYd22qFSIOBogWJkD1Q4iqvrRUqMwfqa2IUESSJ3bTU0A+LOX0zG4hHunf6Bn1C8P/0oNsX35VDYTYiJtUSzkdIzY8WD8nO7ywQZ2wuk6wOsb9mdKI7Jc=~1; _ga_4WZYL59WMV=GS1.1.1685099018.35.1.1685101872.53.0.0; _dd_s=logs=1&id=29e36564-0ed9-4548-8624-a77244545aac&created=1685099017533&expire=1685102772607&rum=0',
                'If-None-Match': 'W/"807b6-+qpTt8AyVLkl9ZPTa9+4b+GRDis"',
                'Referer': 'https://learning.oreilly.com/search/?q=*&type=article&type=book&type=journal&publishers=O%27Reilly%20Media%2C%20Inc.&rows=100',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            message = HTTPMessage(url=url, headers=headers, params=params)
            code = f'book_{curr_page}'
            content = self.check_and_load_data(code=code, message=message)
            
            book_list = json.loads(content)['data']['products']
            
            if len(book_list) == 0:
                self.logger.info("Book data no longer exists.")
                break

            book_data.extend(book_list)
            curr_page += 1
            
            # time.sleep(3)
            
        return book_data

    def scape_book_data(self) -> None:
        
        books = self.get_book_data()
        book_info_list = []

        for book in books:
            book_info = {
                'id': book['product_id'],
                'title': book['title'],
                'url': book['url'],
                'author': book['authors'],
                'categories': book['categories'],
                'cover_image': book['cover_image'],
                'description': book['description'],
                'publication_date': book['custom_attributes']['publication_date'],
                'page_count': book['custom_attributes']['page_count'],
                'publisher': book['custom_attributes']['publishers'],
                'topics': [topic['name'] for topic in book['custom_attributes']['topic__topic_hierarchy']],
                'average_rating': book['custom_attributes']['average_rating']
            }

            book_info_list.append(book_info)

        file_path = os.path.join(SAVE_DIR, 'oreilly_book.csv')
        book_df = pd.DataFrame(book_info_list)
        book_df.to_csv(file_path, index=False)
        self.logger.info(f"Save book data to: {file_path}")

    def save_review_data(self):
        pass

    def parse_review_data(self):
        pass

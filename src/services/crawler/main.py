from src.drives.kafka import Kafka
from src.drives.enums import Topics
from src.drives.kafka_template import AbsctractKafka
from src.services.crawler.mock_notices import NOTICES
import json
import requests
from bs4 import BeautifulSoup

url = 'https://portal.ifba.edu.br/conquista/noticias-2/noticias-campus-vitoria-da-conquista'

def get_dat_publish(article):
    data_modification = article.header.find(class_='documentByLine').getText().replace("  ", "").replace('\n', "")
    date = data_modification[data_modification.find('modificação') + 11:]
    return date

def crawler(page_url: str, verify: bool):
    page = requests.get(page_url, verify=verify)
    soup = BeautifulSoup(page.text, 'html.parser').find_all('article', class_='entry')
    posts = []
    for article in soup:
        summary = article.header.find(class_='summary')
        article = {
            'title': summary.a.getText(),
            'link': summary.a['href'],
            'date': get_dat_publish(article)
        }
        posts.append(article)
        # print(article)
    return posts


def get_posts(start=1) -> list:
    b_start = 0 if start == 1 else 30 * (start - 1)
    page_url = '{}?b_start:int={}'.format(url, b_start)
    posts = crawler(page_url, verify=True)
    return posts

def send_to_queue(queue: AbsctractKafka, posts):
    queue.send_message(Topics.NEWS, str(posts))


def handler(queue: AbsctractKafka):
    
    posts = get_posts()
    for post in posts:
        print(post)
        send_to_queue(queue, post)
    # for notice in NOTICES:
    #     queue.send_message(Topics.NEWS, str(notice))


if __name__ == '__main__':
    handler(Kafka())

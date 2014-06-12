# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import lxml
from lxml.html.clean import Cleaner
#import json
#import codecs
from peewee import *

cleaner = Cleaner()
cleaner.javascript = True
cleaner.style = True
cleaner.comments = True
cleaner.allow_tags = False
cleaner.links = False
cleaner.page_structure = False

db = MySQLDatabase('scrap', user='scrap', passwd='')

class BaseModel(Model):
    """
    Base peewee DB model
    """

    class Meta:
        database = db


class Texts(BaseModel):
    title = CharField()
    link = CharField()
    date = CharField()
    description = TextField()


class DelfiPipeline(object):
    def __init__(self):
        # self.file = codecs.open('scraped_data_utf8.json', 'w', encoding='utf-8')
        db.connect()

    def process_item(self, item, spider):
        if item['description']:
            item['description'] = cleaner.clean_html(lxml.html.fromstring(''.join(item['description']))).text_content() \
                .replace('\n', '').replace('\r', '').replace('\t', '').strip()

        Texts.create(title=item['title'][0], link=item['link'], date="2014-12-12", description=item['description'])

        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        #self.file.write(line)

        return item

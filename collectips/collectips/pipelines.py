# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class CollectipsPipeline(object):

    def __init__(self):                            #初始化连接mysql的数据库相关信息  
    	self.dbpool = adbapi.ConnectionPool('MySQLdb',  
            db = 'ip_db',  
            user = 'root',  
            passwd = 'michael',  
            cursorclass = MySQLdb.cursors.DictCursor,  
            charset = 'utf8',  
            use_unicode = False  
    )  


    def process_item(self, item, spider):
		query = self.dbpool.runInteraction(self._conditional_insert, item)
		return item

   # insert the data to databases                 #把数据插入到数据库中  
    def _conditional_insert(self, tx, item):  
        sql = ("insert into ip_info(IP,PORT,TYPE,POSITION,SPEED,LAST_CHECK_TIME)" "values(%s,%s,%s,%s,%s,%s)")

        lis = (item["IP"],item["PORT"],item["TYPE"],item["POSITION"],item["SPEED"],item["LAST_CHECK_TIME"])

        tx.execute(sql,lis)  

'''       
		DBKWARGS = spider.settings.get('DBKWARGS')
		con = MySQLdb.connect(**DBKWARGS)
		cur = con.cursor()
		sql = ("insert into proxy(IP,PORT,TYPE,POSITION,SPEED,LAST_CHECK_TIME)" "values(%s,%s,%s,%s,%s,%s)")
		lis = (item["IP"],item["PORT"],item["TYPE"],item["POSITION"],item["SPEED"],item["LAST_CHECK_TIME"],)

		try:
			cur.execute(sql,lis)
		except Exception,e:
			print "Insert error:",e
			con.rollback()
		else:
			con.commit()
		cur.close()
		con.close()

		return item
'''

import mysql.connector


class mysql_operate(object):
    db_name = "taobao"
    table_name="shop"
    def connect_mysql(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456",
            database=self.db_name
        )

    def create_db(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="123456"
        )
        mycursor = mydb.cursor()
        sql = "CREATE DATABASE {}".format(self.db_name)
        mycursor.execute(sql)

    def create_table(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "CREATE TABLE {}(id INT AUTO_INCREMENT PRIMARY KEY,item_id VARCHAR(255),price VARCHAR(255)" \
              ",sold VARCHAR(255),title VARCHAR(255),store_name VARCHAR(255),address VARCHAR(255))".format(self.table_name)
        mycursor.execute(sql)

    def drop_table(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "drop table if exists {}".format(self.table_name)
        mycursor.execute(sql)

    def insert_data(self,item):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "INSERT INTO {} (item_id,title,price,sold,store_name,address) VALUES (%s,%s,%s,%s,%s,%s)".format(self.table_name)
        val = (item['item_id'], item['title'],item['price'], item['sold'],item['store_name'], item['address'])
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.lastrowid, "记录插入成功！")

    def update_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "update {} set name=%s where name=%s".format(self.table_name)
        val = ("zhuliyi", "zhuly")
        mycursor.execute(sql, val)
        self.mydb.commit()
        print(mycursor.rowcount, " 条记录被修改")

    def del_date(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        sql = "delete from {} where id=5".format(self.table_name)
        mycursor.execute(sql)
        self.mydb.commit()
        print(mycursor.rowcount, " 条记录删除成功")

    def query_data(self):
        self.connect_mysql()
        mycursor = self.mydb.cursor()
        # sql = "select * from user where name='zhuly' order by age desc limit 2"
        sql = "select * from {}".format(self.table_name)
        mycursor.execute(sql)
        result = mycursor.fetchall()

        for item in result:
            print(item)

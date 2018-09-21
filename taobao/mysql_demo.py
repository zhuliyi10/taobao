from taobao.mysql_operate import mysql_operate

if __name__ == "__main__":
    operate = mysql_operate()
    operate.create_table()
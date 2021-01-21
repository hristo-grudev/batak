import sqlite3


class BatakPipeline:
    conn = sqlite3.connect('batak.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `batak` (post text)''')
        self.conn.commit()

    def process_item(self, item, spider):
        post = item['post'][0]
        print(f"""select * from batak where post = '{post}'""")
        self.cursor.execute(f"""select * from batak where post = '{post}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `batak` (`post`) values ('{post}')""")
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()

import sqlite3

class BotDB:
    def __init__(self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def user_exists(self,user_id):
        print(user_id)
    #Проверяем есть ли юзер в базе
        result = self.cursor.execute("SELECT 'id' FROM 'users' WHERE 'user_id' = ?",(user_id,))
        return bool(len(result.fetchall()))

    def get_user_id(self,user_id):
        print(user_id)
        #Достаем id юзера в базе по его user_id
        result = self.cursor.execute("SELECT `id` FROM `users` WHERE `user_id` = ?", (user_id,))
        return result.fetchone()[0]

    def add_user(self,user_id):
        print(user_id)
        print("add")
        #Добавляем юзера в базу
        self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
        return self.conn.commit()

    def get_date(self,user_id):
        date = self.cursor.execute("select join_date from users where user_id = ?",(user_id,)).fetchall()
        return date

    def add_notifications(self,user_id):
        self.cursor.execute("insert into notifications (user_id,state) select users.id,'1' from users where users.user_id = ?",(user_id,))
        print("notif")
        return self.conn.commit()

    def update_notifications(self,user_id,check = None):
        if (check == False):
            self.cursor.execute("update notifications set state = '1' where notifications.user_id = (select users.id from users where users.user_id = ?)",(user_id,))
        else:
            self.cursor.execute("update notifications set state = '0' where notifications.user_id = (select users.id from users where users.user_id = ?)",(user_id,))
        return self.conn.commit()

    def check_notifications(self,user_id):
        state = self.cursor.execute("select state from notifications inner join users on notifications.user_id = users.id where users.user_id = ?",(user_id,)).fetchall()
        return state[0][0]

    def stock_exists(self,user_id,stock_name):
        self.cursor.execute("SELECT id FROM users WHERE user_id = ?",(user_id,))
        user_stock_id = self.cursor.fetchall()
        self.cursor.execute("select id from stock where stock_name = ?",(stock_name,))
        stock_id = self.cursor.fetchall()
        result = self.cursor.execute("select id from portfolio where user_stock_id = ? and stock_id = ?",(user_stock_id[0][0],stock_id[0][0],))
        return bool(len(result.fetchall()))

    def add_stock(self,user_id,stock_name,amount):
        print("add")
        self.cursor.execute("insert into portfolio (stock_id,user_stock_id,number_of_shares) select stock.id,users.id, ? from stock,users where stock.stock_name = ? and users.user_id = ?",(amount,stock_name,user_id,))
        return self.conn.commit()

    def update_stock(self,user_id,stock_name,amount):
        print("update")
        self.cursor.execute("update portfolio set number_of_shares = ? WHERE user_stock_id =(select id from users where user_id = ?) and stock_id =(select id from stock where stock_name = ?)",(amount,user_id,stock_name,))
        return self.conn.commit()

    def delete_stock(self,user_id,stock_name):
        print("delete")
        self.cursor.execute("delete from portfolio where user_stock_id = (select id from users where user_id = ?) and stock_id = (select id from stock where stock_name = ?)",(user_id,stock_name,))
        return self.conn.commit()

    def get_stock_user(self,user_id):
        self.cursor.execute("SELECT stock_name,number_of_shares  FROM stock INNER JOIN portfolio ON stock.id = portfolio.stock_id INNER JOIN users ON portfolio.user_stock_id = users.id WHERE users.user_id = ?",(user_id,))
        result = self.cursor.fetchall()
        I = {}
        for i in result:
            I[i[0]] = i[1]
            # I.append(i[0])
        # I = ', '.join(I)
        # print(I[0])
        return I
    #         channels = ', '.join(channels)
    def get_users(self):
        return self.cursor.execute("SELECT user_id FROM users").fetchall()

    def get_stock(self):
        return self.cursor.execute("select stock_name from stock INNER JOIN portfolio on"
                            " stock.id = stock_id GROUP BY stock_name").fetchall()

    def push(self,stock_name):
        # self.cursor.execute("select user_id,portfolio.number_of_shares from users inner join portfolio on users.id = user_stock_id where stock_id = (select id from stock  where stock_name = ?)",(stock_name,))
        # a = self.cursor.fetchall()
        # print(a)
        return self.cursor.execute("select user_id,portfolio.number_of_shares from users inner join portfolio on "
                                   "users.id = user_stock_id where stock_id = "
                                   "(select id from stock  where stock_name = ?)",(stock_name,)).fetchall()


    def close(self):
        """Закрываем соединение с БД"""
        self.conn.close()
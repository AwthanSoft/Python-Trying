
import peewee


db = peewee.SqliteDatabase("D:\\Users\\CPBLK\\Desktop\\proj\\PyCharm\\07\\sqliteStores\\01\\people.db")



db.connect()


class TempUser(peewee.Model):
    id = peewee.AutoField(primary_key=True)
    name = peewee.CharField(null=True)







    class Meta:
        database = db
        db_table = 'at_temp_users'




db.create_tables([TempUser])





if __name__ == '__main__':


    user = TempUser(name = "ali")



    print("db.connection() : " + str(db.connection()))

    user.save()


    pass
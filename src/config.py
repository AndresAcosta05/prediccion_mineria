import psycopg2

class Conecction:

    def getConecction():
        try:
            con = psycopg2.connect(
            host = 'db.jfotbibxfuazvztupgny.supabase.co',
            user = 'postgres',
            password = 'Postgres123457',
            port = 5432,
            database = 'postgres'
            )
            return con
        except Exception as ex:
            print(ex)
            return False

if __name__ == '__main__':
    con = Conecction.getConecction()
    print(con)
        
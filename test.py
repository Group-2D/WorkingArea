import databaseConnection


def main():
    session = databaseConnection

    session.test()

    print(session.cursor.fetchall())

    session.cursor.close()


#driver 
if "__name__" == "__main__":
    main()
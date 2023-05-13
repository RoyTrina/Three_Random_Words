from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# print(QSqlDatabase.drivers())   #This shows me the available database drivers that I can use
# The result is an array containing the drivers : ['QSQLITE', 'QODBC', 'QODBC3', 'QPSQL', 'QPSQL7']

DB = QSqlDatabase.addDatabase("QODBC3")
DB.setDatabaseName("three_random_words_data.db")

if DB.open():
    statement = QSqlQuery()
    statement.exec_('SELECT * FROM users')
    while statement.next():
        pass
    DB.close()
    print("Database has been connected.")
else:
    print("Database is not connected. Please try again.")


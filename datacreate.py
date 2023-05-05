import mysql.connector, csv, os, os.path
filepath = os.path.dirname(__file__)

with open(os.path.join(filepath, 'gamedata.txt'), 'r') as file:
    data = csv.reader(file)
    data_login = list(data)
game_host = data_login[0][0]
game_pass = data_login[0][1]
game_user = data_login[0][2]
game_db = data_login[0][3]
mydb = mysql.connector.connect(host=game_host, password=game_pass, user=game_user, database=game_db)
mycursor = mydb.cursor()
try:
    mycursor.execute('INSERT INTO scores VALUES(0,0,0,0,0,0)')
except:
    mycursor.execute(
        'CREATE TABLE scores (lvl1 integer, lvl2 integer, lvl3 integer, lvl4 integer, lvl5 integer, lvl6 integer)')
    mycursor.execute('INSERT INTO scores VALUES(0,0,0,0,0,0)')
mydb.commit()

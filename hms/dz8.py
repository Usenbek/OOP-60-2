import sqlite3
connect = sqlite3.connect('games.db')
cursor = connect.cursor()

def create_game():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS games(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(15) NOT NULL
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS players(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    score INTEGER NOT NULL,
    players_score INTEGER NOT NULL,
    FOREIGN KEY(players_score) REFERENCES games(id)
    )
    ''')
    connect.commit()

create_game()
def insert_game_scoredb():

    # cursor.execute(
        # 'INSERT INTO games(name) VALUES (?)',
        # ('Batyr',)
        # [
        #     ("john",),
        #     ("Kana",),
        #     ("Batyr")
        # ]
    # )

    # cursor.execute(
    #     'INSERT INTO players(score,players_score) VALUES(?,?)',
    #     (75,3)
        # [
        #     (70,1),
        #     (90,2),
        #     (80,2)
        # ]
    # )
    connect.commit()
    print('Данные сохранены')

# insert_game_scoredb()

def get_players_score():
    cursor.execute('''
    SELECT games.name, players.score
    FROM games 
    LEFT JOIN players ON games.id = players.players_score
                            ''')
    users = cursor.fetchall()
    print(users)
# get_players_score()

def get_player_hh_score():
    cursor.execute('''
    SELECT games.name,  MAX(players.score) FROM games INNER JOIN players ON games.id = players.players_score
    ''')
    users = cursor.fetchall()
    print(users)

# get_player_hh_score()

def get_my_view():
    cursor.execute('''
    CREATE VIEW IF NOT EXISTS my_view AS
    SELECT games.name,  players.score
    FROM games LEFT JOIN players ON games.id = players.players_score
    ''')
    connect.commit()
# get_my_view()
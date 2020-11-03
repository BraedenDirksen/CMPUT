import sqlite3,sys
#braeden dirksen

def init_sql(db_path):
    global connection, cursor

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    

def question_one():
    query = """
    select name, age, breed
    cats
    where gender = ?
    """
    gender = input('what is the gender? ')
    cursor.execute(query, (gender),)
    outputs = cursor.fetchall()
    for output in outputs:
        print(output)

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <database_path>")
        exit()
    db_path = sys.argv[1]
    init_sql(db_path)
    question_one()

main()
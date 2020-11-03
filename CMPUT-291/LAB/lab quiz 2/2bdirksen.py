import sqlite3,sys
#braeden dirksen

def init_sql(db_path):
    global connection, cursor

    connection = sqlite3.connect(db_path)
    cursor = connection.cursor()
    cursor.execute(' PRAGMA foreign_keys=ON; ')
    connection.commit()
    

def question_two():
    query_drop = """
    drop table if exists ?
    """
    query_get_columns = """
    select *
    from favourite
    """
    query_create_table = """
    create table ?(
    ?     TEXT,
    ?   TEXT,
    PRIMARY KEY (?, ?),
    FOREIGN KEY (?) REFERENCES cats(name),
    FOREIGN KEY (?) REFERENCES food(?) 
    )
    """
    query_insert = """
    insert into ? 
    select *
    from favourite
    where favourite.productID in (select food.productID from food where doos.brand = ?)
    """ 
    query_getrows = """
    select * from ?
    """

    brand = input("what is the brand?")
    cursor.execute(query_drop,(brand,))

    cursor.execute(query_get_columns)
    columns = []
    for i in range(len(cursor.description)):
        columns.append(cursor.description[i][0])

    cursor.execute(query_create_table,(brand,columns[0],columns[1],columns[0],columns[1],columns[0],columns[1]))
    
    cursor.execute(query_insert,(brand,brand))
    connection.commit()

    cursor.execute(query_getrows,(brand,))

    output = cursor.fetchall()
    for item in output:
        print(item)


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <database_path>")
        exit()
    db_path = sys.argv[1]
    init_sql(db_path)
    question_two()

main()
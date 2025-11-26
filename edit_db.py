import sqlite3

date_input, menu_input = input().split(maxsplit=1)
conn = sqlite3.connect("/workspaces/DaegunDinnerAPI/dinner.db")
cur = conn.cursor()
cur.execute("""
        UPDATE dinner SET menu = ? WHERE date == ?
    """, (menu_input, date_input))
conn.commit()
conn.close()
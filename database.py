import sqlite3

def ensure_connection(func):
	def inner(*args, **kwargs):
		with sqlite3.connect("database.db") as conn:
			kwargs["conn"] = conn
			res = func(*args, **kwargs)
		return res
	return inner

@ensure_connection
def check_db(conn, force: bool = False):
	c = conn.cursor()
	if force:
		c.execute("DROP TABLE IF EXISTS user_language")
	c.execute("""
		CREATE TABLE IF NOT EXISTS user_language (
			id           INTEGER PRIMARY KEY,
			user_id      INTEGER NOT NULL,
			language     TEXT NOT NULL
		)
	""")
	conn.commit()

@ensure_connection
def choice_language(conn, user_id: int, language: str):
	c = conn.cursor()
	c.execute("INSERT INTO user_language (user_id, language) VALUES (?, ?)", (user_id, language))
	conn.commit()
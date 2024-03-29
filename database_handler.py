from os import path
import sqlite3
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash

class DatabaseHandler():
	def __init__(self, database_name):
		self.con = sqlite3.connect(f"{path.dirname(path.abspath(__file__))}/{database_name}", check_same_thread=False)
		self.con.row_factory = sqlite3.Row

	def add_user(self, username: str, password: str, email : str, grade : str | None = None, admin : bool = False) -> tuple[bool, str]:
		if not self.exist(username):
			cursor = self.con.cursor()
			if admin:
				query = f"INSERT INTO OmegaUsers (username, password, email, grade) VALUES (?, ?, ?, ?);"
				password = generate_password_hash(password)
				cursor.execute(query, (username, password, email, grade))
			else:
				query = f"INSERT INTO OmegaUsers (username, password, email) VALUES (?, ?, ?);"
				password = generate_password_hash(password)
				cursor.execute(query, (username, password, email))
			cursor.close()
			self.con.commit()
			return (True, str(self.get_id(username)))
		else:
			return (False, "The name is already taken .")

	def show(self):
		cursor = self.con.cursor()
		query = f"SELECT * FROM OmegaUsers;"
		cursor.execute(query)
		result = cursor.fetchall()
		result = map(dict, result,)
		cursor.close()
		for i in result:
			print(i)
		
	def check_login(self, username, password):
		if self.exist(username):
			cursor = self.con.cursor()
			query = 'SELECT username, password FROM OmegaUsers WHERE username=?'
			cursor.execute(query, (username,))
			result = cursor.fetchall()
			cursor.close()
			if check_password_hash(dict(result[0])["password"], password):
				return (True, str(self.get_id(username)))
			else:
				return  (False, 'Wrong password')
		else:
			return (False, 'Wrong username')

	def exist(self, username: str) -> bool:
		cursor = self.con.cursor()
		query = f"SELECT * FROM OmegaUsers WHERE username = ?;"
		cursor.execute(query, (username,))
		result = cursor.fetchall()
		cursor.close()

		return len(result) == 1

	def get_id(self, username):
		cursor = self.con.cursor()
		query = f"SELECT id FROM OmegaUsers WHERE username = ?;"
		cursor.execute(query, (username,))
		result = cursor.fetchall()
		cursor.close()
		return dict(result[0])["id"]

	def get_data(self, id):
		cursor = self.con.cursor()
		query = f"SELECT id, username, email, grade FROM OmegaUsers WHERE id = ?;"
		cursor.execute(query, (id,))
		result = cursor.fetchall()
		cursor.close()
		return dict(result[0])

	def get_username(self, id):
		cursor = self.con.cursor()
		query = f"SELECT username FROM OmegaUsers WHERE id = ?;"
		cursor.execute(query, (id,))
		result = cursor.fetchall()
		cursor.close()
		if len(result) > 0:
			return dict(result[0])['user_name']
		else:
			return None

class DatabaseHandler_Game():
	def __init__(self, database_name, table_name):
		self.con = sqlite3.connect(f"{path.dirname(path.abspath(__file__))}/{database_name}", check_same_thread=False)
		self.con.row_factory = sqlite3.Row
		self.table_name = table_name
  
	def add_time(self, id_user : int, time : int):
		cursor = self.con.cursor()
		day =  str(date.today())
		if self.id_still_play(id_user):
			add_time = self.get_time(id_user)+time
			query = f"UPDATE {self.table_name} SET time = {add_time} WHERE id_user = ? AND day == ? ;"
			cursor.execute(query, (id_user, day,))
		else:
			query = f"INSERT INTO {self.table_name} (id_user, day, time) VALUES (?, ?, ?);"
			cursor.execute(query, (id_user, day, time))
		self.con.commit()
		cursor.close()
  
	def id_still_play(self, id_user : int):
		day = str(date.today())
		cursor = self.con.cursor()
		query = f"SELECT * FROM {self.table_name} WHERE id_user = ? AND day == ? ;"
		cursor.execute(query, (id_user, day,))
		result = cursor.fetchall()
		cursor.close()
		return len(result) == 1

	def get_time(self, id_user : int):
		day = str(date.today())
		cursor = self.con.cursor()
		query = f"SELECT time FROM {self.table_name} WHERE id_user = ? AND day == ? ;"
		cursor.execute(query, (id_user, day,))
		result = cursor.fetchall()
		cursor.close()
		return dict(result[0])['time']
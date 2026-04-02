import sqlite3
from config import DATABASE

class DB_Manager:
    def __init__(self, database):
        self.database = database

    def create_tables(self):
        # Veri tabanına bir bağlantı kurulması
        conn = sqlite3.connect(self.database)

        with conn:
            # projects tablosunu oluşturma
            conn.execute('''CREATE TABLE projects (
                            project_id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            project_name TEXT NOT NULL,
                            description TEXT,
                            url TEXT,
                            status_id INTEGER,
                            FOREIGN KEY(status_id) REFERENCES status(status_id)
                        )''') # görüntü

            # skills tablosunu oluşturma
            conn.execute('''CREATE TABLE skills (
                            skill_id INTEGER PRIMARY KEY,
                            skill_name TEXT
                        )''')

            # Bağlantı tablosu oluşturma - project_skills
            conn.execute('''CREATE TABLE project_skills (
                            project_id INTEGER,
                            skill_id INTEGER,
                            FOREIGN KEY(project_id) REFERENCES projects(project_id),
                            FOREIGN KEY(skill_id) REFERENCES skills(skill_id)
                        )''')
            
            conn.execute('''CREATE TABLE status (
                            status_id INTEGER PRIMARY KEY,
                            status_name TEXT
                        )''')

            # Değişiklikleri kaydetme ve bağlantıyı kapatma
            conn.commit()

        print("Veri tabanı başarılı bir şekilde oluşturuldu!")

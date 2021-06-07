import sqlite3

conn = sqlite3.connect('competition_submissions.db')

setup = '''
CREATE TABLE IF NOT EXISTS Submissions
(submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
first_name TEXT NOT NULL,
email TEXT NOT NULL,
recipe_title TEXT NOT NULL,
recipe_type TEXT NOT NULL,
recipe_content TEXT NOT NULL)
'''

conn.execute(setup)

conn.close()

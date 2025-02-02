import json
import searching
import os 
import pytest
import sqlite3

conn = sqlite3.connect("../database/database.sqlite")
cursor = conn.cursor()
rows = cursor.execute("SELECT Stored_Location, Name FROM songs").fetchall()
song_files = [[f"../{row[0]}", row[1]] for row in rows]
print(song_files)

@pytest.mark.parametrize("test_file,test_expected", song_files)
def test_1(test_file, test_expected):
    file = os.path.join(test_file)
    file_name = os.path.basename(file)
    file_directory = os.path.dirname(file)
    # print(file_name, file_directory)
    searchers = searching.searching(file_name, file_directory)
    assert json.loads(searchers)["Name"] == test_expected


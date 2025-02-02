import uuid
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
def test_2(test_file, test_expected):
    # trimming the audio down to 30 second
    new_file = f"{uuid.uuid4()}.wav"
    new_format = os.path.join("/tmp", new_file)
    os.system(f"ffmpeg -loglevel quiet -y -to 30 -i '{test_file}' '{new_format}'")

    file = os.path.join(new_format)
    file_name = os.path.basename(file)
    file_directory = os.path.dirname(file)

    searchers = searching.searching(file_name, file_directory)
    assert json.loads(searchers)["Name"] == test_expected


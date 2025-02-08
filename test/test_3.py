import noised
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
def test_3(test_file, test_expected):
    file = os.path.join(test_file)
    file_name = os.path.basename(file)
    file_directory = os.path.dirname(file)

    new_file = f"{uuid.uuid4()}.wav"
    new_format = os.path.join("/tmp", new_file)
    os.system(f"ffmpeg -loglevel quiet -y -i '{test_file}' '{new_format}'")

    new_noised_file = f"{uuid.uuid4()}.wav"
    noised.basic_noise(new_file, "/tmp", new_noised_file)

    searchers = searching.searching(new_noised_file, "/tmp")
    assert json.loads(searchers)["Name"] == test_expected

# @pytest.mark.parametrize("test_file,test_expected", song_files)
# def test_3_1(test_file, test_expected):
#     file = os.path.join(test_file)
#     file_name = os.path.basename(file)
#     file_directory = os.path.dirname(file)
# 
#     new_file = f"{uuid.uuid4()}.wav"
#     new_format = os.path.join("/tmp", new_file)
#     os.system(f"ffmpeg -loglevel quiet -y -i '{test_file}' '{new_format}'")
# 
#     new_noised_file = f"{uuid.uuid4()}.wav"
#     noised.random_noise(new_file, "/tmp", new_noised_file)
# 
#     searchers = searching.searching(new_noised_file, "/tmp")
#     assert json.loads(searchers)["Name"] == test_expected
# 

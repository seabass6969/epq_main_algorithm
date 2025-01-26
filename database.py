import json
import settings
import sqlite3
import spectrogram_analysis
import uuid
import os
import tqdm


def connection():
    return sqlite3.connect("../database/database.sqlite")


def write_points(items):
    conn = connection()
    cursor = conn.cursor()
    cursor.executemany('INSERT INTO "points" VALUES (?, ?, ?)', items)
    conn.commit()
    conn.close()

def search_points(searchPairs):
    """
        :params searchPairs pairs from the searchPairs function with all the (deltas, hashes)
    """
    conn = connection()
    time = {}
    conn.execute("VACUUM;")
    conn.execute("PRAGMA synchronous = NORMAL;")
    # create a temp table to accomdiate the searching 
    # It's statistically faster
    # 10 minutes -> 4 seconds (approximately depanding on which hardware it uses) (tested with the test file "test/new_test/27_tapping.wav")
    table_UUID_temp = str(uuid.uuid1()).replace("-", "_")
    conn.execute(f"CREATE TABLE IF NOT EXISTS TEMP_READ_{table_UUID_temp} (data TEXT);")
    conn.executemany(f"INSERT INTO TEMP_READ_{table_UUID_temp} VALUES(?)", searchPairs)
    conn.commit()
    # r_1 = conn.execute("SELECT COUNT(*) FROM TEMP_READ;").fetchone() 
    # print(r_1)
    result = conn.execute(f'SELECT Song_ID, Time_Offset FROM points WHERE Hash IN (SELECT TEMP_READ_{table_UUID_temp}.data FROM TEMP_READ_{table_UUID_temp});').fetchall()
    for r in result:
        if r[0] not in time:
            time[r[0]] = []
        time[r[0]].append(r[1])
    conn.execute(f"DROP TABLE TEMP_READ_{table_UUID_temp};")
    conn.commit()
    conn.close()

    return time


def new_song_entry(song_name, song_author, song_file, License, song_url, genre):
    uuid_song = str(uuid.uuid4())
    sqlstr = f"""
        INSERT INTO "songs" VALUES 
        (
            '{uuid_song}',
            '{song_name}',
            '{song_author}',
            '{song_file}',
            '{License}',
            '{song_url}',
            "{genre}"
        );
    """

    conn = connection()
    cursor = conn.cursor()
    cursor.execute(sqlstr)

    conn.commit()
    conn.close()
    return uuid_song


def adding_entry(song_name, song_author, song_file, song_start_directory, License, song_url, genre):
    uuids = new_song_entry(song_name, song_author, os.path.join(song_start_directory, song_file), License, song_url, genre)
    pairs = list(spectrogram_analysis.getPairs(song_file, song_start_directory, uuids))
    #unique = []
    #for pair in pairs:
    #    if pair not in unique:
    #        unique.append(pair)
    write_points(pairs)
    # if settings.DEBUG:
    print("I wrote {} points".format(len(pairs)))


def get_entry(ID):
    SQL_COMMAND = f'SELECT Name, Author, Stored_Location, License, Original_location, Genre FROM songs WHERE Song_ID="{ID}";'

    conn = connection()
    conn.row_factory = sqlite3.Row 
    curs = conn.cursor()
    item = curs.execute(SQL_COMMAND).fetchone()
    conn.close()
    return json.dumps(dict(item))
    # return dict(item)

def create_queue_request():
    requester_id = str(uuid.uuid1())
    conn = connection()
    conn.execute(f'INSERT INTO queue_requests VALUES ("{requester_id}")')
    conn.commit()
    conn.close()
    return requester_id

if __name__ == "__main__":
    # print(item["Name"])
    entry = get_entry("f84be331-e4bd-4479-afef-993a93ecf09e")
    print(entry)
    pass

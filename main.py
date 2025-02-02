import sys
import os
args = sys.argv
if len(args) == 2 and args[1] == "--queue-request":
    # import database
    # queue_id = database.create_queue_request()
    import uuid
    queue_id = str(uuid.uuid1())
    os.mkdir(f"/tmp/{queue_id}")
    print(queue_id)

elif len(args) == 3 and args[1] == "--test":
    import searching
    import json
    file = os.path.join(args[2])
    file_name = os.path.basename(file)
    file_directory = os.path.dirname(file)
    # print(file_name, file_directory)
    searchers = searching.searching(file_name, file_directory)
    print(json.loads(searchers)["Stored_Location"])

elif len(args) == 3 and args[1] == "--pure-test":
    import searching
    import json
    import settings
    settings.DEBUG = True
    file = os.path.join(args[2])
    file_name = os.path.basename(file)
    file_directory = os.path.dirname(file)
    # print(file_name, file_directory)
    searchers = searching.searching(file_name, file_directory)
    print(searchers)

elif len(args) == 3:
    import searching
    searchers = searching.searching(f"{args[1]}.wav", f"/tmp/{args[2]}")
    print(searchers)

else:
    print("Error: No arguments given.")
    print("Usage: [queue_number_on] [queue_id] or --queue-request or --test [paths_to_file]")

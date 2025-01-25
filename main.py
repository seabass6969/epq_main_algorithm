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
elif len(args) == 3:
    import searching
    searchers = searching.searching(f"{args[1]}.wav", f"/tmp/{args[2]}")
    print(searchers)
else:
    print("Error: No arguments given.")
    print("Usage: [queue_number_on] [queue_id] or --queue-request")

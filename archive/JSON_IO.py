import json
import datetime
import glob
import os


new_tasks = [
    {'id':1,'task':'sleep','status':'Not started'},
    {'id':2,'task':'nap','status':'Not started'},
    {'id':12,'task':'do dishes','status':'Not started'},
    {'id':4,'task':'clean the car','status':'Not started'}
]


original_tasks = [{'id':0,
                     'task':'wake up',
                     'status':'Not started'}]

#this dumps a json with a filename prefix and a timestamp into a directory of your choice.

def dump_json_with_timestamp(data, filename_prefix, directory="."):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{directory}/{filename_prefix}_{timestamp}.json"
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)  # Use indent for readability
        print(f"JSON data dumped to: {filename}")
    except Exception as e:
        print(f"Error dumping JSON data: {e}")


#this function needs to loop through all the filenames, find the most recent (timedelta) and save to memory(variable)
#works - need to append to todo_list variable
def read_latest_json(list_to_update, directory):
    json_files = glob.glob(os.path.join(directory, '*.json'))
    if not json_files:
        return None

    latest_file = max(json_files, key=os.path.getmtime)

    with open(latest_file, 'r') as f:
        list_to_update = json.load(f)

    return list_to_update

# Example usage:
directory_path = '/Users/will_tang/Documents/GitHub/task_tracker/task_logs' # Replace with the actual directory path

#json_data = read_latest_json(output_todo_list, directory_path)

print(f'pre-updated tasks {original_tasks}')
#we want to add new tasks to original tasks
for task in new_tasks:
    original_tasks.append(task)

print(f'updated tasks {original_tasks}')

            






import json
import datetime

def dump_json_with_timestamp(data, filename_prefix, directory="."):
    """Dumps JSON data to a file with a timestamp in the filename.

    Args:
        data: The Python object to be serialized to JSON.
        filename_prefix: The prefix for the filename.
        directory: The directory to save the file in (default: current directory).
    """

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{directory}/{filename_prefix}_{timestamp}.json"
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)  # Use indent for readability
        print(f"JSON data dumped to: {filename}")
    except Exception as e:
        print(f"Error dumping JSON data: {e}")

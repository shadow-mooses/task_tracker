from flask import Flask, request, session, render_template
import datetime, json, glob, os


app = Flask(__name__)
app.secret_key = "secretkey" #this is the session cookie

#------------ VARIABLES ---------------

#this is the example todo list
todo_list = [
    {'id':1,'task':'sleep','status':'Not started'},
    {'id':2,'task':'nap','status':'Not started'},
    {'id':12,'task':'do dishes','status':'Not started'},
    {'id':4,'task':'clean the car','status':'Not started'}
]

#this is the base todo list that all future tasks will be appended to
empty_list = [
    {'id':0, 'task':None, 'status':'Not started'}
]

#these are the registered users
users = [{"username":"William","password":"test"}]


#------------ FUNCTIONS ---------------

#this function returns the highest task 'id' (integer) in the todo list and adds 1 for the new task.
def new_max_key(list) -> list:
    key_list = []
    for dict in list:
        for value in dict.values():
            if type(value) == int:
                key_list.append(value)
            else:
                break
    return max(key_list) + 1

#this checks the login/password of the user against the defined list of users
def checkUser(username, password):
    for user in users:
        if username in user["username"] and password in user["password"]:
            return True
    return False

#this dumps a json in the task_logs directory with a timestamp as the filename
def dump_json_with_timestamp(data, filename_prefix, directory="."):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{directory}/{filename_prefix}_{timestamp}.json"
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)  # Use indent for readability
        print(f"JSON data dumped to: {filename}")
    except Exception as e:
        print(f"Error dumping JSON data: {e}")

#this marks the 'status' key as 'complete' and raises errors if a user tries to update an 'id' that is of range or if someone tries to delete the zero index:
def task_completer(task_num, list):
    int_task = int(task_num)
    if int_task <= 0:
        raise KeyError('you entered a task number that is out of range')
    elif type(int_task) == int:
        task_list_dict = {}
        task_list_index = 0
        for dict in list: #loop through the todo list and create a dictionary of the task ids and the index in the list
            for value in dict.values():
                if type(value) == int:
                    task_list_dict[value] = task_list_index
                    task_list_index += 1
                else:
                    break
        if int_task in task_list_dict:
            updated_dict = list[task_list_dict[int_task]]
            updated_dict['status'] = 'completed'
            return updated_dict
        raise KeyError('you entered a task number that is out of range')
    raise TypeError('task_num is not an integer')


#------------ ROUTES ---------------


#this first route checks registration
@app.route("/", methods=["GET"])
def first_route():
    return render_template("register.html")

#the user will register and take them to the add task page
@app.route("/login", methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if checkUser(username,password):
            session["username"] = username    
            return render_template("index.html", username=session['username'])
        else:
            return render_template("register.html")
    elif request.method == "GET":
        return render_template("register.html")
    
#this route will remove the session cookie, dump a json file to disk and logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    dump_json_with_timestamp(todo_list, 'task_log','task_logs')
    return "Logged out and saved your tasks."

#this displays the task history that is saved to memeory (empty_list)
@app.route("/task_history", methods=["GET"])
def get_history():
    try:
        username = session['username']
        if len(empty_list) == 1:
            return render_template('empty_task_list.html')
        else:
            return render_template("task_history.html", username=username, empty_list=empty_list)
    except:
        return render_template ('register.html')
    
#this adds adds a new task with the new_max_key function
@app.route("/task_add", methods=["GET","POST"])
def task_add():
    try:
        username = session['username']
        if request.method == 'GET':
            return render_template('task_add.html')
        if request.method == 'POST':
            add_task = request.form.get('add_task')
            max_key = new_max_key(empty_list)
            new_task = {'id':max_key,'task':add_task, 'status':'Not started'}
            empty_list.append(new_task)
            return render_template("task_history.html", username=username, add_task=add_task,empty_list=empty_list)
    except:
        return render_template ('register.html')

#update needed - completing a task that doesn't exit brings back to login
@app.route('/task_complete', methods=['POST','GET'])
def remove_task():
    try:
        username = session['username']
        if request.method == 'GET':
            return render_template('task_complete.html')
        elif request.method == 'POST':
            complete_task_id = request.form.get('complete_task_id')
            task_completer(complete_task_id,empty_list)
            return render_template('task_updated.html', username=username, complete_task_id=complete_task_id)
    except:
        return "There was an error completing the task, you entered a task id that was out of range."    

#this addes previous tasks to the original list.
@app.route('/task_load', methods = ['GET','POST'])
def load_tasks():
    try:
        username = session['username']
        if request.method == 'GET':
            return render_template('task_load.html')
        if request.method == 'POST':
            directory_path = '/Users/will_tang/Documents/GitHub/task_tracker/task_logs'#static directory for loading jsons
            json_files = glob.glob(os.path.join(directory_path, '*.json'))
            latest_file = max(json_files, key=os.path.getmtime)

            with open(latest_file, 'r') as f:
                new_tasks = json.load(f)

            for task in new_tasks:
                empty_list.append(task)#this loops through the new tasks and adds to the empty_list
            
            return render_template('task_loaded.html', empty_list=empty_list)
        else:
            return "Saved tasks not found!"

    except:
        return "error loading tasks"
    

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2050)


  

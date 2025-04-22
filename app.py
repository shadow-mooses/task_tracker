from flask import Flask, request, session, render_template
import datetime, json

app = Flask(__name__)
app.secret_key = "secretkey" #this is the session cookie

#------------ VARIABLES ---------------

#this is the example todo list  has been updated from a list -> a dictionary to work with the functions iteration
todo_list = [
    {'id':1,'task':'sleep','status':'Not started'},
    {'id':2,'task':'nap','status':'Not started'},
    {'id':12,'task':'do dishes','status':'Not started'},
    {'id':4,'task':'clean the car','status':'Not started'}
]

#these are the registered users
users = [{"username":"William","password":"test"}]


#------------ FUNCTIONS ---------------


#this function returns the highest key (integer) in the list of dictionaries in the todo list and adds 1 for the new task.
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

#this dumps a json in the task_logs directory with a timestamp in the filename
def dump_json_with_timestamp(data, filename_prefix, directory="."):
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{directory}/{filename_prefix}_{timestamp}.json"
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)  # Use indent for readability
        print(f"JSON data dumped to: {filename}")
    except Exception as e:
        print(f"Error dumping JSON data: {e}")


#works - loops through the tasks, creates a dictionary with the task id and the list index. Then pops the index in the todo list.
#unused since delete API calls can't be done with flask?
def delete_task(task_num, list):
    task_list_dict = {}
    task_list_index = 0
    for dict in list: #loop through the todo list and create a dictionary of the task ids and the index in the list
        for value in dict.values():
            if type(value) == int:
                task_list_dict[value] = task_list_index
                task_list_index += 1
            else:
                break
    list.pop(task_list_dict[task_num])



#works - need to add an out of range raise def task_completer(task_num, list):
def task_completer(task_num, list):
    if type(task_num) == int:
        task_list_dict = {}
        task_list_index = 0
        for dict in list: #loop through the todo list and create a dictionary of the task ids and the index in the list
            for value in dict.values():
                if type(value) == int:
                    task_list_dict[value] = task_list_index
                    task_list_index += 1
                else:
                    break
        if task_num in task_list_dict:
            updated_dict = list[task_list_dict[task_num]]
            updated_dict['status'] = 'completed'
            return updated_dict
        raise KeyError('task_num is out of range')
    raise TypeError('task_num is not an integer')

#------------ ROUTES ---------------


#this first route checks registration
@app.route("/", methods=["GET"])
def first_route():
    return render_template("register.html")

#works - the user will register and take them to the add task page
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
    
#works - this route will remove the session cookie, dump (save) a json file to disk and logout
@app.route("/logout")
def logout():
    session.pop("username", None)
    dump_json_with_timestamp(todo_list, 'task_log','task_logs')
    return "Saved and logged out of the task tracker"


#works - displays the tasks
@app.route("/task_history", methods=["GET"])
def get_history():
    try:
        user = session['username'] #check user
        return render_template("task_history.html", username=user, todo_list=todo_list)
    except:
        return render_template ('register.html')
    


#works - adds new task and max task id to todo-list variable and naviages to task history
@app.route("/task_add", methods=["GET","POST"])
def task_add():
    username = session['username'] #this could be wrong
    if request.method == 'GET':
        return render_template('task_add.html')
    if request.method == 'POST':
        add_task = request.form.get("add_task")
        max_key = new_max_key(todo_list)
        new_task = {'id':max_key,'task':add_task, 'status':'Not started'}
        todo_list.append(new_task)
        return render_template("task_history.html", username=username, add_task=add_task,todo_list=todo_list)
    else:
        return 400


#remove tasks - this will display the list of tasks with a field (task_key) to remove with a 
#bootstrap list below to reference

@app.route('/task_complete', methods=['POST','GET'])
def remove_task():
    if request.method == 'GET':
        return render_template('task_complete.html')
    elif request.method == 'POST':
        complete_task_id = request.form.get('complete_task_id')
        task_completer(complete_task_id,todo_list)
        return f"{complete_task_id} is completed"
    else:
        return 'Id not found'



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=2050)


  

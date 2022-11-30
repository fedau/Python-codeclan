from flask import render_template, Blueprint
from repositories import task_repository, user_repository

task_blueprint = Blueprint("tasks", __name__)

#INDEX
#GET '/tasks'
@task_blueprint.route('/tasks')
def tasks():
    all_tasks_list = task_repository.select_all()
    return render_template('tasks/index.html', all_tasks_key = all_tasks_list)

# NEW
#GET '/tasks/new'
@task_blueprint.route('/tasks/new')
def new_task():
    users = user_repository.select_all()
    return render_template('tasks/new.html', all_users = users)


#CREATE (save)
#POST '/tasks'




#SHOW
#GET '/tasks/<id>'



#EDIT (display form in edit mode) 
#GET '/tasks/<id>/edit'

#UPDATE
#PUT '/tasks/<id>'
# PUT indicates updating an existing resource

#DELETE
#DELETE '/tasks/<id>'

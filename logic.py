
from application import Application
from mapper import Task
from datetime import datetime


app = Application()
ses = app.new_session()

actual_tasks = ses.query(Task).filter(Task.scheduled <= datetime.now()).all()

print(actual_tasks)

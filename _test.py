
from application import Application
import mapper
from datetime import datetime

app = Application()
ses = app.new_session()

print(ses.query(mapper.Engine).all())
from application import db
from application.models import Adverts

db.drop_all()
db.create_all()

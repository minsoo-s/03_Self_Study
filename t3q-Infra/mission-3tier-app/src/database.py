from .models import db

def commit_changes():
    db.session.commit()

# GET 동작 
def get_all(model):
    data = model.query.all()
    return data

# POST 동작
def add_instance(model, **kwargs):
    instance = model(**kwargs)
    db.session.add(instance)
    commit_changes()

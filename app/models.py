from app.database import db

class Task(db.Model):

    __tablename__ = 'tasks'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    memo = db.Column(db.Text)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://dj@localhost:5432/example'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Person ID:{self.id}, name:{self.name}>'

#Test result
result = Person.query.filter(Person.name.ilike('%i%')).count()

db.create_all()

@app.route('/')
def index():
    persons = Person.query.first()
    return 'hello world next phase ' + persons.name

if __name__ == '__main__':
  app.run()
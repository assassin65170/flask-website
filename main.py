from website import app
from website import db

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

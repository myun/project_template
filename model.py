from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class SomeTable(db.Model):
    __tablename__ = 'some_table'
    table_id = db.Column(
	db.Integer,
	autoincrement=True,
	primary_key=True,
    )
    some_other_column = db.Column(db.String(100), nullable=False)

    def __repr__(self):
	return ('table_id: {}, some_other_column: {}'.format(
	    self.table_id,
	    self.some_other_column,
	))

DB_URI = 'postgresql:///testdb'

def connect_to_db(app):
    """Connect the database to the Flask app."""

    app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # TODO: Remove this
    from server import app
    connect_to_db(app)
    print('Connected to DB.')

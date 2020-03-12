from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flaskr.tables import database_schema


class DatabaseEngine:

    def getApp(self):
        return self.__app

    def setApp(self, value):
        self.__app = value

    def __init__(self, app):
        self.__app = app

    def create_engine(self):
        """
        Create the Engine instance.
        """
        return create_engine(self.__app.config['SQLALCHEMY_DATABASE_URI'])

    def init_app(self):
        """
        Register database functions with the Flask app.
        """
        db = SQLAlchemy(self.__app)
        migrate = Migrate(self.__app, db)
        manager = Manager(self.__app)
        manager.add_command('db', MigrateCommand)

        engine = self.create_engine()
        database_schema.Post.metadata.create_all(engine)

    def create_session(self):
        """
        Create the Session instance.
        """
        engine = self.create_engine()
        Session = sessionmaker(bind=engine)

        return Session()

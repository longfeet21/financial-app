from flask_script import Manager
from flask_migrate import MigrateCommand
from src import create_app


app = create_app()
manager = Manager(app)

@manager.option('-n', '--name', dest='name')
@manager.option('-u', '--url', dest='url')
def hello(name, url):
    "just say hello"
    print("hello", name, url)


if __name__ == "__main__":
    manager.add_command('db', MigrateCommand)
    manager.run()

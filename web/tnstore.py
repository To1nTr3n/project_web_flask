from web import web, db
from web.models import User

@web.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User}

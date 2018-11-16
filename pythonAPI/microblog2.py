from prog_api import app, db
from prog_api.models2 import Art

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Art': Art}

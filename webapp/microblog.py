from prog import app, db
from prog.models import AF

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'AF': AF}

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "RBAC: Web Application Development, Using MVC Architecture."

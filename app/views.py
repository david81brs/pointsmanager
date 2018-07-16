def configure(APP):
    @APP.route('/')
    def index():
        return '<h1><a href="/admin">Admin</h1>'


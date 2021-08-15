import web

urls = (
    '/', 'mvc.controllers.login.Login',
    '/agenda', 'mvc.controllers.agenda.Agenda',
    '/insert', 'mvc.controllers.insert.Insert',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()
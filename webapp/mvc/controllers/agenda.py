import web
import requests
import json

render = web.template.render("mvc/views/", base="template")

class Agenda():

    def GET(self):
        try:
            result = requests.get('https://agenda-request-ea3aa-default-rtdb.firebaseio.com/agenda.json').text
            data = json.loads(result)
            #print(data)
            return render.agenda(data) # renderizando agenda.html
        except Exception as error:
            print(error.args[0])
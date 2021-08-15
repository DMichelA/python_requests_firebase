import web
import requests
import json

render = web.template.render("mvc/views/")

class Login():

    def GET(self):
        try:
            message = ""
            return render.login(message) # renderizando login.html
        except Exception as error:
            print(error.args[0])

    def POST(self):
        try:
            data_user = web.input()
            email = data_user.email
            password = data_user.password
            result = requests.post('https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=AIzaSyAnDoSjcDBr56fxcL_j68ak3ennPHGmn24', data=json.dumps({'email':email,'password':password})).text
            data = json.loads(result)
            print(data)
            # print(data['registered'])
            if data['registered'] == True:
                web.seeother('/agenda')
        except Exception as error:
            print (error.args[0])
            message = data['error']['message']
            return render.login(message)
            # return data['error']['message']
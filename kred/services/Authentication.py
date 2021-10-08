import requests
import urllib3
from base64 import b64encode

class Authentication:
    # @login function calls POST api to Log in using a code, password, OAuth, or Ethereum wallet
    # The function returns a json
    def login(self,email,password,url):

        encoded_credentials = b64encode(bytes(f'{email}:{password}',
                                              encoding='ascii')).decode('ascii')
        auth_header = f'Basic {encoded_credentials}'
        headers = {
            "Accept": "application/json",
            "Authorization": auth_header
        }
        querystring = {"email": email, "password": password}
        response=requests.post(url = url,headers=headers,params=querystring)
        return response.text

    # @logout function calls POST api to Log out and delete the current session
    # The function returns a
    def logout(self,session):
        return 'This is the result'


    # @register function calls POST api to Register an account by providing email and password details or initiating an OAuth flow
    # Model used is RegisterModel
    # The function returns a
    def register(self,model):
        return model.name + " has been registered"

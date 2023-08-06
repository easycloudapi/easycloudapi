"""
GCP Authentication
------------------

How to access GCP projects using best auth

#. Reference:
    #. Google Documentation: https://cloud.google.com/iam/docs/overview
    #. OpenID Connect: https://developers.google.com/identity/openid-connect/openid-connect
#. Code Ref:
    #. https://googleapis.github.io/google-api-python-client/docs/oauth.html
    #. https://google-auth.readthedocs.io/en/stable/user-guide.html

Different Ways/Methods To Access GCP Cloud Resources:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#. With User Consent

#. By Service Account Json Key

#. By Default Access if application running on GCP ComputeEngine, CloudFunction, CloudRun, AppEngine, Kubernetes

#. With impersonate Service Account

"""

import os
import sys
from google_auth_oauthlib.flow import Flow  # InstalledAppFlow
from googleapiclient.discovery import build

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
sys.path.insert(0, root_dir)


class GCP_Authentication(object):
    """
    A class for GCP Authentication
    ...

    Parameters
    ----------
    project_id: str
        Google Project ID

    Methods
    -------
    oauth_withUserConsent_googleURI()

    """
    def __init__(self, 
                 project_id: str) -> None:
        self.project_id = project_id


    def oauth_withUserConsent_googleURI(self, 
                                        client_secret_file_path: str,
                                        scopes: list = ["openid"],
                                        ) -> bool:
        """
        GCP resources authentication By User Consent
        ...

        User will give consent by clicking on the link provided 
        and after approving the consent, user will get token which he/She will pass to the application manually 

        Parameters
        ----------
        client_secret_file_path: str
            local path of the client secret json file
        scopes: list
            default value is, ["openid"]
            example, scopes=['openid', 'https://www.googleapis.com/auth/cloud-platform']

        Returns
        -------
        credentials: google.oauth2.credentials.Credentials


        Notes
        -----
        #. To Create Client Access Secret and TokenID follow below steps:
            #. Open GCP Project and open
             
            #. First, create "OAuth consent screen"
                #. provide app name, scopes("https://www.googleapis.com/auth/cloud-platform", "openid") 
                and add test users and developer email id
                
            #. Second, go to ""APIs & Services" -> "Credentials" -> "Create OAuth client ID"
                #. select Application Type as "Desktop app"
                #. store the client ID and secret_file
        """
        flow = Flow.from_client_secrets_file(client_secrets_file=client_secret_file_path,
                                             scopes=scopes,
                                             redirect_uri='urn:ietf:wg:oauth:2.0:oob')
        auth_uri = flow.authorization_url()
        print(f"auth_uri: {auth_uri}")
        code = input('Enter the authorization code: ')
        flow.fetch_token(code=code)
        credentials = flow.credentials
        return credentials


    def _get_user_name(self, credentials):
        user_info_service = build('oauth2', 'v2', credentials=credentials)
        user_info = user_info_service.userinfo().get().execute()
        print(f"login_user: {user_info['name']}")


if __name__ == "__main__":
    import json
    with open(".secret\dev_config.json") as config_file:
        config = json.load(config_file)
    project_id = config.get("dev").get("gcp_project_id")
    secret_file_path = ".secret\easycloudapi_python_utility_desktopapp_clientaccess.json"
    scopes= ['openid']
    obj = GCP_Authentication(project_id=project_id)
    credentials = obj.oauth_withUserConsent_googleURI(client_secret_file_path=secret_file_path,
                                                      scopes=scopes)
    obj._get_user_name(credentials=credentials)
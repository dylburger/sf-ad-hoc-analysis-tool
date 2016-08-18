""" Socrata helper functions and classes
"""
import json
import requests
import yaml
import helpers

SOCRATA_APP_TOKEN_FILE = ".socrata_app_token"
SOCRATA_API_ENDPOINT = 'https://data.sfgov.org/resource'


def read_socrata_app_token(app_token_file=SOCRATA_APP_TOKEN_FILE):
    """ Accepts a YAML file containing the Socrata app token
        Returns the app token as a string for use in passing to
        the Socrata API

        More info about Socrata app tokens here:

        https://dev.socrata.com/docs/app-tokens.html

        If the API token is malformed, we attempt to notify the
        user through a specific exception.

        If the API token file doesn't exist at all, we return
        None, which the client should handle accordingly.
    """
    # Load app token from disk, handling basic exceptions
    try:
        app_token_file_handle = open(app_token_file, 'r')
        app_token_dict = yaml.load(app_token_file_handle)
        token = app_token_dict['token']
    except yaml.YAMLError as exc:
        print("Your app token file doesn't appear to contain valid "
              "YAML: ", exc)
    except:
        # If any general exceptions occured, return None, which
        # the client should handle accordingly
        return None
    else:
        # If everything worked, return the app token
        return token
    finally:
        app_token_file_handle.close()


class SocrataClient:
    """ An instance of the SocrataClient class enables developers
        to interact with the Socrata API to fetch data
    """

    def __init__(self):
        self.socrata_api_token = read_socrata_app_token()
        self.socrata_endpoint_url = SOCRATA_API_ENDPOINT

    def fetch_socrata_json(self, socrata_resource_id):
        """ Given an API "resource ID" (ID tied to a specific Socrata data set),
            return the JSON fetched from the API
        """
        url = "%s/%s.json" % (self.socrata_endpoint_url, socrata_resource_id)
        # If a Socrata API token is present, grab it
        if self.socrata_api_token is not None:
            socrata_api_token_header = {'X-App-Token': self.socrata_api_token}
            r = requests.get(url, headers=socrata_api_token_header)
        else:
            # You can still make request to the API without a token
            r = requests.get(url)
        unicode_content = helpers.bytes_to_str(r.content)
        socrata_json = json.loads(unicode_content)

        return socrata_json

# -*- coding: utf-8 -*-


"""
Here is defined a generic way to use API calls
If there is an API call that you can't find in Pushbots
you can use the generic examples.
API calls reference:
https://pushbots.com/developer/api/1
"""

from pushbots import Pushbots


def example_generic_put():
    """Example api call using put request"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define the API url
    api_url = 'poshbots_api_url'
    # Define your headers manually or use the one's from Pushbots module
    headers = pushbots.headers  # or define yours as a python dict
    # Define your data accordingly, or define no data
    data = {'platform': '1', 'alias': 'superjohn123'}
    code, msg = pushbots.put(api_url=api_url, headers=headers, data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(msg))


def example_generic_post():
    """Example api call using post request"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define the API url
    api_url = 'poshbots_api_url'
    # Define your headers manually or use the one's from Pushbots module
    headers = pushbots.headers  # or define yours as a python dict
    # Define your data accordingly, or define no data
    data = {'platform': '1', 'alias': 'superjohn123'}
    code, msg = pushbots.post(api_url=api_url, headers=headers, data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(msg))


def example_generic_get():
    """Example api call using get request"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define the API url
    api_url = 'poshbots_api_url'
    # Define your headers manually or use the one's from Pushbots module
    headers = pushbots.headers  # or define yours as a python dict
    code, msg = pushbots.get(api_url=api_url, headers=headers)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(msg))

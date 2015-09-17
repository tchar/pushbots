# -*- coding: utf-8 -*-


"""
The following examples are used to demonstrate how to change alias
knowing the current alias.

The method signature is:
Pushbots.alias(platform=None, token=None, alias=None,
               current_alias=None, data=None)
In which you must specify either platform, token and alias,
or platform, alias and curret_alias, or data.
"""

from pushbots import Pushbots


def example_alias1():
    """Change alias by passing values directly to Pushbots.alias()"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define new and current alias and platform
    new_alias = 'my_new_alias'
    old_alias = 'my_current_alias'
    platform = Pushbots.PLATFORM_ANDROID
    code, message = pushbots.alias(platform=platform, alias=new_alias,
                                   current_alias=old_alias)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_alias2():
    """Alternatively you can change alias by passing values defined by you."""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define data
    data = {'platform': Pushbots.PLATFORM_ANDROID, 'alias': 'my_new_alias',
            'current_alias': 'my_current_alias'}
    code, message = pushbots.alias(data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))

# -*- coding: utf-8 -*-


"""
This is an example on how to perform unregister, when you don't know
the token, but  you know an alias.
"""

from pushbots import Pushbots


def get_token_and_platform_from_alias(pushbots, alias):
    """
    Gets the tokens from alias. You can modify this to get
    tokens based on any info. Note that multiple devices,
    may have the same alias, so we return them all.
    """

    devices = []
    code, content = pushbots.devices_info()
    if code != 200:
        print('Something went wrong:{0}'.format(content))
        return
    for json in content:  # Response is a json array in this case
        try:
            if json['alias'] == alias:
                devices.append((json['token'], json['platform']))
        except KeyError:
            pass
    return devices


def example_unregister_from_alias():
    app_id = 'my_app_id'
    secret = 'my_secret'
    alias = 'my_alias'
    pushbots = Pushbots(app_id=app_id, secret=secret)
    devices = get_token_and_platform_from_alias(pushbots, alias)
    if not devices:
        print('No devices found with alias {0}'.format(alias))
    for (token, platform) in devices:
        c, d = pushbots.unregister(token=token, platform=platform)
        print('{0}:{1}'.format(c, d))

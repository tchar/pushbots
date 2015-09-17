# -*- coding: utf-8 -*-


"""
Example on how to get all devices tokens and platforms given an alias
"""


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

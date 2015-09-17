# -*- coding: utf-8 -*-


def unregister_token(pushbots, token, platform):
    return pushbots.unregister(token=token, platform=platform)


def unregister_data(pushbots, data):
    return pushbots.unregister(data=data)

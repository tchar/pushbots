# -*- coding: utf-8 -*-


def push_token(pushbots, platform, token, msg, sound, badge, payload):
    return pushbots.push(platform=platform, token=token, msg=msg, sound=sound,
                         badge=badge, payload=payload)


def push_data(pushbots, data):
    return pushbots.push(data=data)

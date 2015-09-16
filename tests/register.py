# -*- coding: utf-8 -*-


def register_token(pushbots, token, platform, tag, lat, lng, active, alias):
    return pushbots.register(platform=platform, token=token,
                             tag=tag, lat=lat, lng=lng,
                             active=active, alias=alias)


def register_token_simple(pushbots, token, platform):
    return pushbots.register(platform=platform, token=token)


def register_data(pushbots, data):
    return pushbots.register(data=data)

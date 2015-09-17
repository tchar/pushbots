# -*- coding: utf-8 -*-


def untag_token(pushbots, platform, token, tag):
    return pushbots.untag(platform=platform, token=token, tag=tag)


def untag_alias(pushbots, platform, alias, tag):
    return pushbots.untag(platform=platform, alias=alias, tag=tag)


def untag_data(pushbots, data):
    return pushbots.untag(data=data)

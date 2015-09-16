# -*- coding: utf-8 -*-


def tag_token(pushbots, platform, token, tag):
    return pushbots.tag(platform=platform, token=token, tag=tag)


def tag_alias(pushbots, platform, alias, tag):
    return pushbots.tag(platform=platform, alias=alias, tag=tag)


def tag_data(pushbots, data):
    return pushbots.tag(data=data)

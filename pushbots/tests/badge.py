# -*- coding: utf-8 -*-


def badge_token(pushbots, platform, token, setbadgecount):
    return pushbots.badge(platform=platform, token=token,
                          setbadgecount=setbadgecount)


def badge_data(pushbots, data):
    return pushbots.badge(data=data)

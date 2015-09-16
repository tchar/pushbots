# -*- coding: utf-8 -*-


def alias_token(pushbots, token, platform, alias):
    return pushbots.alias(platform=platform, token=token,
                          alias=alias)


def alias_alias(pushbots, platform, alias, current_alias):
    return pushbots.alias(platform=platform, alias=alias,
                          current_alias=current_alias)


def alias_data(pushbots, data):
    return pushbots.alias(data=data)

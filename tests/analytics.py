# -*- coding: utf-8 -*-


def get_analytics(pushbots):
    return pushbots.get_analytics()


def record_analytics_platform(pushbots, platform):
    return pushbots.record_analytics(platform=platform)


def record_analytics_data(pushbots, data):
    return pushbots.record_analytics(data=data)

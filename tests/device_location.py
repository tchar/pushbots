# -*- coding: utf-8 -*-


def device_location_token(pushbots, platform, token, lat, lng):
    return pushbots.device_location(platform=platform, token=token,
                                    lat=lat, lng=lng)


def device_location_data(pushbots, data):
    return pushbots.device_location(data=data)

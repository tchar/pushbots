# -*- coding: utf-8 -*-


def devices(pushbots):
    return pushbots.devices_info()


def device_info(pushbots, token):
    return pushbots.device_info(token=token)

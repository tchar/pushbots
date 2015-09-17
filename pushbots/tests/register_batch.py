# -*- coding: utf-8 -*-


def register_batch_tokens(pushbots, tokens, platform, tags):
    return pushbots.register_batch(platform=platform, tokens=tokens, tags=tags)


def register_batch_data(pushbots, data):
    return pushbots.register_batch(data=data)

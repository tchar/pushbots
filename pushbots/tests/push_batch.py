# -*- coding: utf-8 -*-


def push_batch_tags(pushbots, platform, msg, sound, badge, schedule,
                    tags, except_tags, payload):
    return pushbots.push_batch(platform=platform, msg=msg,
                               sound=sound, badge=badge, schedule=schedule,
                               tags=tags, except_tags=except_tags,
                               payload=payload)


def push_batch_alias1(pushbots, platform, msg, sound, badge, schedule,
                      alias, payload):
    return pushbots.push_batch(platform=platform, msg=msg, sound=sound,
                               badge=badge, schedule=schedule, alias=alias,
                               payload=payload)


def push_batch_alias2(pushbots, platform, msg, sound, badge, schedule,
                      except_alias, payload):
    return pushbots.push_batch(platform=platform, msg=msg, sound=sound,
                               badge=badge, schedule=schedule,
                               except_alias=except_alias, payload=payload)


def push_batch_data(pushbots, data):
    return pushbots.push_batch(data=data)

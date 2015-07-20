def push_batch(pushbots, platform, msg, sound, badge, schedule,
               tags, except_tags, alias, except_alias, payload):
    return pushbots.push_batch(platform=platform, msg=msg,
                               sound=sound, badge=badge, schedule=schedule,
                               tags=tags, except_tags=except_tags, alias=alias,
                               except_alias=except_alias, payload=payload)


def push_batch_data(pushbots, data):
    return pushbots.push_batch(data=data)

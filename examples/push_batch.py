# -*- coding: utf-8 -*-


"""
The following examples are used to demonstrate how to use push batch

The method signature is:
Pushbots.push_batch(platform=None, msg=None, sound=None, badge=None,
                    schedule=None, tags=None, except_tags=None, alias=None,
                    except_alias=None, payload=None, data=None):
In which you must specify either platform, msg and other params except data,
or data
"""

from pushbots import Pushbots


def example_push_batch1():
    """An example on how to use push_batch with some parameters
    directly to method. In this example a notification will be sent,
    to all iOS devices, that are tagged with "News" or "Politics"
    using push_batch().
    """

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define all fields
    platform = Pushbots.PLATFORM_ANDROID  # Required
    msg = 'My super cool msg'  # Required
    tags = ['News', 'Politics']  # Single tags, must also be in a list.
    code, msg = pushbots.push_batch(platform=platform, msg=msg, tags=tags)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(msg))


def example_push_batch2():
    """An example on how to use push_batch with many parameters
    directly to method.
    In the following example sound, badge (iOS only), schedule
    and devices with specifed tags to exclude are
    defined for the push_batch().
    """

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define all fields
    platform = Pushbots.PLATFORM_IOS
    msg = 'My super cool msg'
    sound = 'mysound'
    badge = '16'
    schedule = '2016-08-12T11:33:00'
    except_tags = ['tag4', 'tag5', 'tag6']
    payload = {'custom_field1': 'My field1 value',
               'custom_field2': 'My field2 value'}
    # Finally make the call
    code, msg = pushbots.push_batch(platform=platform, msg=msg, sound=sound,
                                    badge=badge, schedule=schedule,
                                    except_tags=except_tags, payload=payload)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(msg))


def example_push_batch3():
    """An example on how to use push_batch with data defined by you
    In this example alias is used for push_batch(), along with a payload
    with 1 custom field.
    """

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define data
    data = {'platform': Pushbots.PLATFORM_ANDROID, 'msg': 'Hello there',
            'alias': 'superjohn123', 'payload': {'custom_field': 'Custom val'}}
    # Alternatively you can set 'except_alias' : 'superjohn123' to exclude
    # "superjohn123" from getting that push
    code, msg = pushbots.push_batch(data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(msg))

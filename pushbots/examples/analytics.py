# -*- coding: utf-8 -*-


"""
The following examples are used to demonstrate how to get/record
analytics

The method signatures are:
Pushbots.get_analytics()
and
Pushbots.record_analytics(platform=None, data=None)
In which you must specify either platform or data.
"""

from pushbots import Pushbots


def example_get_analytics():
    """Get analytics by calling Pushbots.get_analytics()"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    code, message = pushbots.get_analytics()
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_record_analytics1():
    """Record analytics by passing platform directly to
    Pushbots.record_analytics()
    """

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define platform
    platform = Pushbots.PLATFORM_IOS
    code, message = pushbots.record_analytics(platform=platform)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_record_analytics2():
    """Record analytics by passing data defined by you to
    Pushbots.record_analytics()
    """

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define data
    data = {'platform': '0'}  # '0' is Equivalent to Pushbots.PLATFORM_IOS
    code, message = pushbots.record_analytics(data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))

# -*- coding: utf-8 -*-


"""
The following examples are used to demonstrate how to tag/untag
knowing the alias
The method signatures are:
Pushbots.tag(platform=None, tag=None, token=None, alias=None, data=None)
and
Pushbots.untag(platform=None, tag=None, token=None, alias=None, data=None)
In which you must specify either platform, token and tag,
or platform, alias and tag, or data.
"""

from pushbots import Pushbots


def example_tag1():
    """Add tag by passing values directly to Pushbots.tag()"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define alias, tag and platform
    alias = 'alias_to_set_tag'
    tag = 'tag_to_be_added'
    platform = Pushbots.PLATFORM_ANDROID
    code, message = pushbots.tag(platform=platform, alias=alias, tag=tag)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_tag2():
    """Alternatively you can add a tag by passing values defined by you."""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define data
    data = {'platform': Pushbots.PLATFORM_ANDROID, 'alias': 'alias_to_set_tag',
            'tag': 'tag_to_be_added'}
    code, message = pushbots.tag(data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_untag1():
    """Remove tag by passing values directly to Pushbots.untag()"""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define alias, tag and platform
    alias = 'alias_to_remove_tag'
    tag = 'tag_to_be_removed'
    platform = Pushbots.PLATFORM_ANDROID
    code, message = pushbots.untag(platform=platform, alias=alias, tag=tag)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))


def example_untag2():
    """Alternatively you can remove a tag by passing values defined by you."""

    # Define app_id and secret
    my_app_id = 'my_app_id'
    my_secret = 'my_secret'
    # Create a Pushbots instance
    pushbots = Pushbots(app_id=my_app_id, secret=my_secret)
    # Define data
    data = {'platform': Pushbots.PLATFORM_ANDROID,
            'alias': 'alias_to_remove_tag', 'tag': 'tag_to_be_removed'}
    code, message = pushbots.untag(data=data)
    print('Returned code: {0}'.format(code))
    print('Returned message: {0}'.format(message))

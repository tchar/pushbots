# -*- coding: utf-8 -*-


"""
This is the python script to run all tests.
Run with puthon -m tests.run from parent directory.
For the tests to run we create virtual devices and test all the api calls,
with many combiniations. For each api call a status code and a text response
is returned. If DEUBG==True then status code and text response (if any)
are printed, else they are printed only if status_code is not in
ACCEPTABLE_CODES.
We consider all tests passed, if, with DEBUG==True all status codes printed are
in ACCEPTABLE_CODES and with DEBUG==False, no output is printed.
In the end, the virtual devices are deleted.
"""

from pushbots.tests.register import (register_token_simple,
                                     register_token, register_data)
from pushbots.tests.register_batch import (register_batch_tokens,
                                           register_batch_data)
from pushbots.tests.unregister import unregister_token, unregister_data
from pushbots.tests.alias import alias_token, alias_alias, alias_data
from pushbots.tests.tag import tag_token, tag_alias, tag_data
from pushbots.tests.untag import untag_token, untag_alias, untag_data
from pushbots.tests.device_location import (device_location_token,
                                            device_location_data)
from pushbots.tests.device import devices, device_info
from pushbots.tests.badge import badge_token, badge_data
from pushbots.tests.analytics import (get_analytics, record_analytics_platform,
                                      record_analytics_data)
from pushbots.tests.push import push_token, push_data
from pushbots.tests.push_batch import (push_batch_tags, push_batch_alias1,
                                       push_batch_alias2, push_batch_data)
from pushbots import Pushbots
import random
import string
import argparse

# if True then prints all debugs. if False then prints only
# codes that ar nore in ACCEPTABLE_CODES
DEBUG = True
# Set acceptable codes for DEBUG=False
ACCEPTABLE_CODES = [200, 201]
APP_ID = '12345'
SECRET = '67890'


def parse_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-a', '--appid', type=str,
                        required=True, help='Define appid')
    parser.add_argument('-s', '--secret', type=str,
                        required=True, help='Define secret')
    parser.add_argument('-n', '--nodebug', action='store_false',
                        help='No debug output except response status codes'
                             ' that are not in the following acceptable'
                             ' codes:{0}'.format(', '.join(
                                        str(x) for x in ACCEPTABLE_CODES)))
    args = parser.parse_args()
    global APP_ID, SECRET, DEBUG
    APP_ID = args.appid
    SECRET = args.secret
    DEBUG = args.nodebug


def debug(s, error=False):
    if DEBUG or error:
        print(s)


def random_str(size=12):
    return ''.join(random.SystemRandom()
                   .choice(string.ascii_uppercase + string.digits)
                   for _ in range(size))

platform = Pushbots.PLATFORM_IOS
token1 = 'test1'
token2 = 'test2'
token3 = 'test3'
token4 = 'test4'
token5 = 'test5'
token6 = 'test6'
token7 = 'test7'
tag1 = random_str()
tag2 = random_str()
alias1 = random_str()
alias2 = random_str()
alias2 = random_str()
alias3 = random_str()


def process_request(d_msg, r_code, r_content):
    msg_code = 'Request returned code:{0}'.format(r_code)
    if r_content:
        msg_content = 'Response:{0}'.format(r_content)
    else:
        msg_content = 'Request did not return any content'

    if r_code not in ACCEPTABLE_CODES:
        debug(d_msg, error=True)
        debug(msg_code, error=True)
        debug(msg_content, error=True)
    else:
        debug(d_msg)
        debug(msg_code)
        debug(msg_content)


def test_register(pushbots):
    d_msg = ('\nTesting register_token() with token:{0}, tags:[{1}],'
             ' alias:{2}.'.format(token1, tag1, alias1))
    c, d = register_token(pushbots=pushbots, token=token1, platform=platform,
                          tag=[tag1], lat='80.241', lng='13.241',
                          alias=alias1, active=['test1'])
    process_request(d_msg, c, d)

    d_msg = '\nTesting register_token_simple() with token:{0}.'.format(token2)
    c, d = register_token_simple(pushbots=pushbots, platform=platform,
                                 token=token2)
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token3}
    d_msg = '\nTesting register_data() with custom data:{0}.'.format(data)
    c, d = register_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_register_batch(pushbots):
    d_msg = ('\nTesting register_batch_tokens() with tokens:{0} and tags:{1}.'
             .format([token4, token5], [tag1, tag2]))
    c, d = register_batch_tokens(pushbots=pushbots, platform=platform,
                                 tokens=[token4, token5], tags=[tag1, tag2])
    process_request(d_msg, c, d)

    data = {'platform': platform, 'tokens': [token6, token7],
            'tags': [tag1, tag2]}
    d_msg = ('\nTesting register_batch_data() with tokens:{0} and tags:{1}.'
             .format([token6, token7], [tag1, tag2]))
    c, d = register_batch_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_alias(pushbots):
    d_msg = ('\nTesting alias_token() with token:{0}, alias:{1}.'
             .format(token2, alias2))
    c, d = alias_token(pushbots=pushbots, token=token2,
                       alias=alias2, platform=platform)
    process_request(d_msg, c, d)

    d_msg = ('\nTesting alias_alias() with current_alias:{0}, alias:{1}.'
             .format(alias1, alias3))
    c, d = alias_alias(pushbots=pushbots, current_alias=alias1,
                       alias=alias3, platform=platform)
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token3, 'alias': alias3}
    d_msg = '\nTesting alias_data() with custom data:{0}.'.format(data)
    c, d = alias_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_tag(pushbots):
    d_msg = ('\nTesting tag_token() with token:{0} and tag:{1}.'
             .format(token1, tag1))
    c, d = tag_token(pushbots=pushbots, platform=platform,
                     token=token1, tag=tag1)
    process_request(d_msg, c, d)

    d_msg = ('\nTesting tag_alias() with alias:{0} and tag:{1}.'
             .format(alias2, tag2))
    c, d = tag_alias(pushbots=pushbots, platform=platform,
                     alias=alias2, tag=tag2)
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token5, 'tag': tag1}
    d_msg = '\nTesting tag_data() with data:{0}'.format(data)
    c, d = tag_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_untag(pushbots):
    d_msg = ('\nTesting untag_token() with token:{0} and tag:{1}.'
             .format(token1, tag1))
    c, d = untag_token(pushbots=pushbots, platform=platform,
                       token=token1, tag=tag1)
    process_request(d_msg, c, d)

    d_msg = ('\nTesting untag_alias() with alias:{0} and tag:{1}.'
             .format(alias2, tag2))
    c, d = untag_alias(pushbots=pushbots, platform=platform,
                       alias=alias2, tag=tag2)
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token5, 'tag': tag1}
    d_msg = '\nTesting untag_data() with data:{0}.'.format(data)
    c, d = untag_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_device_location(pushbots):
    d_msg = '\nTesting device_location_token() with token:{0}.'.format(token2)
    c, d = device_location_token(pushbots=pushbots, platform=platform,
                                 token=token2, lat='82.241', lng='14.241')
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token3,
            'lat': 85.243, 'lng': 17.123}
    d_msg = '\nTesting device_location_data() with data:{0}.'.format(data)
    c, d = device_location_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_device(pushbots):
    d_msg = '\nTesting devices().'
    c, d = devices(pushbots=pushbots)
    process_request(d_msg, c, d)

    d_msg = '\nTesting device_info() with token:{0}.'.format(token1)
    c, d = device_info(pushbots=pushbots, token=token1)
    process_request(d_msg, c, d)


def test_badge(pushbots):
    d_msg = '\nTesting badge_token() with token:{0}.'.format(token2)
    c, d = badge_token(pushbots=pushbots, platform=platform,
                       token=token2, setbadgecount=15)
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token3,
            'setbadgecount': 16}
    d_msg = '\nTesting badge_data() with data:{0}.'.format(data)
    c, d = badge_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_push(pushbots):
    d_msg = '\nTesting push_token() with token:{0}.'.format(token1)
    c, d = push_token(pushbots=pushbots, platform=platform, token=token1,
                      msg='Test message', sound='mysound', badge='16',
                      payload={'mycustomfield': 'Custom field'})
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token2, 'msg': 'Test message 2',
            'badge': '16', 'payload': {'mycustomfield2': 'Custom field 2'}}
    d_msg = '\nTesting push_data() with data:{0}.'.format(data)
    c, d = push_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_push_batch(pushbots):
    d_msg = ('\nTesting push_batch() with tags:{0},except_tags:{1}.'
             .format([tag1], [tag2]))
    c, d = push_batch_tags(pushbots=pushbots, platform=platform,
                           msg='Test message 2', sound='mysound',
                           badge='16', schedule='2015-04-02T11:33:00',
                           tags=[tag1], except_tags=[tag2],
                           payload={'mycustomfield3': 'My custom field 3'})
    process_request(d_msg, c, d)

    d_msg = '\nTesting push_batch() with alias:{0}'.format(alias2)
    c, d = push_batch_alias1(pushbots=pushbots, platform=platform,
                             msg='Test message 2', sound='mysound', badge='16',
                             schedule='2015-04-02T11:33:00', alias=alias2,
                             payload={'mycustomfield3': 'My custom field 3'})
    process_request(d_msg, c, d)

    d_msg = '\nTesting push_batch() with except_alias:{0}'.format(alias3)
    c, d = push_batch_alias2(pushbots=pushbots, platform=platform,
                             msg='Test message 2', sound='mysound', badge='16',
                             schedule='2015-04-02T11:33:00',
                             except_alias=alias3,
                             payload={'mycustomfield3': 'My custom field 3'})
    process_request(d_msg, c, d)

    data = {'platform': platform, 'msg': 'Test message 3', 'sound': 'mysound',
            'tags': [tag1, tag2]}
    d_msg = '\nTesting push_batch() with data:{0}'.format(data)
    c, d = push_batch_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_analytics(pushbots):
    d_msg = '\nTesting get_analytics()'
    c, d = get_analytics(pushbots=pushbots)
    process_request(d_msg, c, d)

    d_msg = '\nTesting record_analytics_platform'
    c, d = record_analytics_platform(pushbots=pushbots, platform=platform)
    process_request(d_msg, c, d)

    data = {'platform': platform}
    d_msg = '\nTesting record_analytics_data with data:{0}.'.format(data)
    c, d = record_analytics_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def test_unregister(pushbots):
    d_msg = '\nTesting unregister_token() with token:{0}.'.format(token1)
    c, d = unregister_token(pushbots=pushbots, token=token1, platform=platform)
    process_request(d_msg, c, d)

    data = {'platform': platform, 'token': token2}
    d_msg = '\nTesting unregister_data() with token:{0}.'.format(token2)
    c, d = unregister_data(pushbots=pushbots, data=data)
    process_request(d_msg, c, d)


def unregister_all(pushbots):
    # Unregister all tokens

    debug('\nUnregistering any devices associated with test\'s tokens...')
    unregister_token(pushbots=pushbots, token=token1, platform=platform)
    unregister_token(pushbots=pushbots, token=token2, platform=platform)
    unregister_token(pushbots=pushbots, token=token3, platform=platform)
    unregister_token(pushbots=pushbots, token=token4, platform=platform)
    unregister_token(pushbots=pushbots, token=token5, platform=platform)
    unregister_token(pushbots=pushbots, token=token6, platform=platform)
    unregister_token(pushbots=pushbots, token=token7, platform=platform)
    debug('\nDone!')


def main():
    parse_args()
    print('Warning!!!')
    print('Tests are going to create virtual devices to test api calls'
          ' for platform: {0}'.format(platform))
    print('Virtual devices are going to have the following tokens:'
          '{0}, {1}, {2}, {3}, {4}. {5}. {6}'
          .format(token1, token2, token3, token4, token5, token6, token7))
    print('Also the following random testing tags will be created:'
          '{0}, {1}'.format(tag1, tag2))
    print('And the following random testing aliases will be created:'
          '{0}, {1}, {2}'.format(alias1, alias2, alias3))
    print('If you have conflicing aliases or tags open tests/run.py and define'
          ' them manually')
    # The following try catch is for python 2 - python 3 compatibility.
    try:
        read_str = raw_input
    except NameError:
        read_str = input
    choice = read_str('Do you want to continue? (y/n):')
    if choice.lower() != 'y':
        return
    pushbots = Pushbots(app_id=APP_ID, secret=SECRET)
    try:
        unregister_all(pushbots)  # Do this for clean testing.
        debug('\nStarting tests...')
        test_register(pushbots)
        test_register_batch(pushbots)
        test_alias(pushbots)
        test_tag(pushbots)
        test_untag(pushbots)
        test_device_location(pushbots)
        test_device(pushbots)
        test_badge(pushbots)
        test_analytics(pushbots)
        test_push(pushbots)
        test_push_batch(pushbots)
        test_unregister(pushbots)
        debug('\nDone testing!')
    except KeyboardInterrupt:
        return
    except Exception as e:
        debug('Exception found:{0}:{1}'.format(type(e), e), error=True)
    finally:
        unregister_all(pushbots)  # Unregister all tokens
        pass

if __name__ == '__main__':
    main()

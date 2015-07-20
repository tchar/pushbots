from tests.register import *
from tests.register_batch import *
from tests.unregister import *
from tests.alias import *
from tests.tag import *
from tests.untag import *
from tests.device_location import *
from tests.badge import *
from tests.analytics import *
from tests.push import *
from tests.push_batch import *
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


def debug(s):
    if DEBUG:
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


def process_request(r_code, r_text):
    msg_code = 'Request returned code:{0}'.format(r_code)
    if r_text:
        msg_content = 'Response:{0}'.format(r_text)
    else:
        msg_content = 'Request did not return any content'

    if DEBUG or r_code not in ACCEPTABLE_CODES:
        print(msg_code)
        print(msg_content)


def test_register(pushbots):
    debug('\nTesting register_token() with token:{0}, tags:[{1}], alias:{2}.'
          .format(token1, tag1, alias1))
    c, d = register_token(pushbots=pushbots, token=token1, platform=platform,
                          tag=[tag1], lat='80.241', lng='13.241',
                          alias=alias1, active=['test1'])
    process_request(c, d)

    debug('\nTesting register_token_simple() with token:{0}.'.format(token2))
    c, d = register_token_simple(pushbots=pushbots, platform=platform,
                                 token=token2)
    process_request(c, d)

    data = {'platform': platform, 'token': token3}
    debug('\nTesting register_data() with custom data:{0}.'.format(data))
    c, d = register_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_register_batch(pushbots):
    debug('\nTesting register_batch_tokens() with tokens:{0} and tags:{1}.'
          .format([token4, token5], [tag1, tag2]))
    c, d = register_batch_tokens(pushbots=pushbots, platform=platform,
                                 tokens=[token4, token5], tags=[tag1, tag2])
    process_request(c, d)

    data = {'platform': platform, 'tokens': [token6, token7],
            'tags': [tag1, tag2]}
    debug('\nTesting register_batch_data() with tokens:{0} and tags:{1}.'
          .format([token6, token7], [tag1, tag2]))
    c, d = register_batch_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_alias(pushbots):
    debug('\nTesting alias_token() with token:{0}, alias:{1}.'
          .format(token2, alias2))
    c, d = alias_token(pushbots=pushbots, token=token2,
                       alias=alias2, platform=platform)
    process_request(c, d)

    debug('\nTesting alias_alias() with current_alias:{0}, alias:{1}.'
          .format(alias1, alias3))
    c, d = alias_alias(pushbots=pushbots, current_alias=alias1,
                       alias=alias3, platform=platform)
    process_request(c, d)

    data = {'platform': platform, 'token': token3, 'alias': alias3}
    debug('\nTesting alias_data() with custom data:{0}.'.format(data))
    c, d = alias_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_tag(pushbots):
    debug('\nTesting tag_token() with token:{0} and tag:{1}.'
          .format(token1, tag1))
    c, d = tag_token(pushbots=pushbots, platform=platform,
                     token=token1, tag=tag1)
    process_request(c, d)

    debug('\nTesting tag_alias() with alias:{0} and tag:{1}.'
          .format(alias2, tag2))
    c, d = tag_alias(pushbots=pushbots, platform=platform,
                     alias=alias2, tag=tag2)
    process_request(c, d)

    data = {'platform': platform, 'token': token5, 'tag': tag1}
    debug('\nTesting tag_data() with data:{0}'.format(data))
    c, d = tag_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_untag(pushbots):
    debug('\nTesting untag_token() with token:{0} and tag:{1}.'
          .format(token1, tag1))
    c, d = untag_token(pushbots=pushbots, platform=platform,
                       token=token1, tag=tag1)
    process_request(c, d)

    debug('\nTesting untag_alias() with alias:{0} and tag:{1}.'
          .format(alias2, tag2))
    c, d = untag_alias(pushbots=pushbots, platform=platform,
                       alias=alias2, tag=tag2)
    process_request(c, d)

    data = {'platform': platform, 'token': token5, 'tag': tag1}
    debug('\nTesting untag_data() with data:{0}.'.format(data))
    c, d = untag_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_device_location(pushbots):
    debug('\nTesting device_location_token() with token:{0}.'.format(token2))
    c, d = device_location_token(pushbots=pushbots, platform=platform,
                                 token=token2, lat='82.241', lng='14.241')
    process_request(c, d)

    data = {'platform': platform, 'token': token3,
            'lat': 85.243, 'lng': 17.123}
    debug('\nTesting device_location_data() with data:{0}.'.format(data))
    c, d = device_location_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_badge(pushbots):
    debug('\nTesting badge_token() with token:{0}.'.format(token2))
    c, d = badge_token(pushbots=pushbots, platform=platform,
                       token=token2, setbadgecount=15)
    process_request(c, d)

    data = {'platform': platform, 'token': token3,
            'setbadgecount': 16}
    debug('\nTesting badge_data() with data:{0}.'.format(data))
    c, d = badge_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_push(pushbots):
    debug('\nTesting push_token() with token:{0}'.format(token1))
    c, d = push_token(pushbots=pushbots, platform=platform, token=token1,
                      msg='Test message', sound='mysound', badge='16',
                      payload={'mycustomfield': 'Custom field'})
    process_request(c, d)

    data = {'platform': platform, 'token': token2, 'msg': 'Test message 2',
            'badge': '16', 'payload': {'mycustomfield2': 'Custom field 2'}}
    debug('\nTesting push_data() with data:{0}.'.format(data))
    c, d = push_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_push_batch(pushbots):
    debug('\nTesting push_batch() with tags:{0}, alias:{1},'
          ' except_tags:{2}, except_alias:{3}'
          .format([tag1], [alias2], [alias1, alias3], [tag2], [alias3]))
    c, d = push_batch(pushbots=pushbots, platform=platform,
                      msg='Test message 2', sound='mysound',
                      badge='16', schedule='2015-04-02T11:33:00',
                      tags=[tag1], except_tags=[tag2], alias=[alias2],
                      except_alias=[alias1, alias3],
                      payload={'mycustomfield3': 'My custom field 3'})
    process_request(c, d)

    data = {'platform': platform, 'msg': 'Test message 3', 'sound': 'mysound',
            'tags': [tag1, tag2]}
    debug('\nTesting push_batch() with data:{0}'.format(data))
    c, d = push_batch_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_analytics(pushbots):
    debug('\nTesting get_analytics()')
    c, d = get_analytics(pushbots=pushbots)
    process_request(c, d)

    debug('\nTesting record_analytics_platform')
    c, d = record_analytics_platform(pushbots=pushbots, platform=platform)
    process_request(c, d)

    data = {'platform': platform}
    debug('\nTesting record_analytics_data with data:{0}.'.format(data))
    c, d = record_analytics_data(pushbots=pushbots, data=data)
    process_request(c, d)


def test_unregister(pushbots):
    debug('\nTesting unregister_token() with token:{0}.'.format(token1))
    c, d = unregister_token(pushbots=pushbots, token=token1, platform=platform)
    process_request(c, d)

    data = {'platform': platform, 'token': token2}
    debug('\nTesting unregister_data() with token:{0}.'.format(token2))
    c, d = unregister_data(pushbots=pushbots, data=data)
    process_request(c, d)

    # Unregister rest tokens
    debug('\nUnregistering the rest of the tokens registered by tests.')
    unregister_token(pushbots=pushbots, token=token3, platform=platform)
    unregister_token(pushbots=pushbots, token=token4, platform=platform)
    unregister_token(pushbots=pushbots, token=token5, platform=platform)
    unregister_token(pushbots=pushbots, token=token6, platform=platform)
    unregister_token(pushbots=pushbots, token=token7, platform=platform)


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
    print('And the following random testing aliases will be created'
          '{0}, {1}, {2}'.format(alias1, alias2, alias3))
    print('If you have conflicing aliases or tags open tests.py and define'
          'them manually')
    choice = raw_input('Do you want to continue? (y/n):')
    if choice.lower() != 'y':
        return
    pushbots = Pushbots(app_id=APP_ID, secret=SECRET)
    test_register(pushbots)
    test_register_batch(pushbots)
    test_alias(pushbots)
    test_tag(pushbots)
    test_untag(pushbots)
    test_device_location(pushbots)
    test_badge(pushbots)
    test_analytics(pushbots)
    test_push(pushbots)
    test_push_batch(pushbots)
    test_unregister(pushbots)


if __name__ == '__main__':
    main()

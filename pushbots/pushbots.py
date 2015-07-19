import requests
import json


class Pushbots:

    """This is the main Pushbots class
    Handles all api calls for Pushbots.
    For api calls you can refer to:
    https://pushbots.com/developer/api/1
    """

    KEY_PLATFORM = 'platform'
    KEY_TOKEN = 'token'
    KEY_TOKENS = 'tokens'
    KEY_TAG = 'tag'
    KEY_TAGS = 'tags'
    KEY_EXCEPT_TAGS = 'except_tags'
    KEY_LAT = 'lat'
    KEY_LNG = 'lng'
    KEY_ACTIVE = 'active'
    KEY_ALIAS = 'alias'
    KEY_EXCEPT_ALIAS = 'except_alias'
    KEY_CURRENT_ALIAS = 'current_alias'
    KEY_MSG = 'msg'
    KEY_SOUND = 'sound'
    KEY_BADGE = 'badge'
    KEY_PAYLOAD = 'payload'
    KEY_SCHEDULE = 'schedule'
    KEY_BADGE_COUNT = 'setbadgecount'

    def __init__(self, app_id, secret):
        """init method.
        @app_id     (String). Pushbots app id
        @secret     (String). Pushbots secret
        """
        self._app_id = app_id
        self._secret = secret

    @property
    def headers(self):
        """Returns the headers for the api call"""

        return {'x-pushbots-appid': self._app_id,
                'x-pushbots-secret': self._secret,
                'Content-Type': 'application/json'}

    def register(self, token=None, platform=None, lat=None, lng=None,
                 active=None, tag=None, alias=None, data=None):
        """Register device token of the app in the database first time,
        and update it with every launch of the app , device data will
        be updated if registered already.
        You must, at least, specify either data or the other params.

        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK.
        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @lat        Optional (Integer). Location latitude e.g. 33.7489.
        @lng        Optional (Integer). Location longitude e.g. -84.3789.
        @active     Optional (List of strings). List of notification Types
                    linked to the device e.g. ["Subscriptions" , "Followers"].
        @tag        Optional (List of strings). List of tags associated with
                    the deviceToken,if empty array that'll remove any
                    associated tags e.g. ["Culture" , "EGYPT"].
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(token=token, platform=platform, lat=lat,
                                  lng=lng, active=active, tag=tag, alias=alias)
        # data = {self.KEY_TOKEN: token, self.KEY_PLATFORM: platform}
        # if lat:
        #     data[self.KEY_LAT] = lat
        # if lng:
        #     data[self.KEY_LNG] = lng
        # if active:
        #     data[self.KEY_ACTIVE] = active
        # if tag:
        #     data[self.KEY_TAG] = tag
        # if alias:
        #     data[self.KEY_ALIAS] = alias
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/deviceToken'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def register_batch(self, tokens=None, platform=None, tags=None, data=None):
        """Register multiple devices up to 500 Device per request
        You must, at least, specify either data or the other params.

        @tokens     Required (List of strings). List of devices tokens
                    to be added to database, up to 500 device per request.
        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @tags        Optional (List of strings). List of tags associated
                    with all imported devices e.g. ["Culture" , "USA"].
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(tokens=tokens, platform=platform, tags=tags)
        # data = {self.KEY_TOKENS: tokens, self.KEY_PLATFORM: platform}
        # if tags:
        #     data[self.KEY_TAGS] = tags
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/deviceToken/batch'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def unregister(self, token=None, platform=None, data=None):
        """unRegister device token of the app from the database
        You must, at least, specify either data or the other params.

        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK.
        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(token=token, platform=platform)
        # data = {self.KEY_TOKEN: token, self.KEY_PLATFORM: platform}
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/deviceToken/del'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def alias(self, platform=None, token=None, alias=None, current_alias=None,
              data=None):
        """Add/update alias of a device.
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.

        @token and @alias are optional, but one of them must be defined.
        @token      Optional (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK
        @alias      Optional (String). Alias to access device data without
                    tokens and it must be unique for every app e.g.
                    "username", "email" ..etc
        @current_alias  Optional (String). Set this parameter in case you want
                        to update existing alias.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform, token=token, alias=alias,
                                  current_alias=current_alias)
        # data = {self.KEY_PLATFORM: platform}
        # if token:
        #     data[self.KEY_TOKEN] = token
        # if alias:
        #     data[self.KEY_ALIAS] = alias
        # if current_alias:
        #     data[self.KEY_CURRENT_ALIAS] = current_alias
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/alias'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def tag(self, platform=None, tag=None, token=None, alias=None, data=None):
        """Tag a device with its token through SDK or Alias through your backend
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @tag        Required (String). "Tag" to be Added.

        @token and @alias are optional, but one of them must be defined.
        @token      Optional (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK
        @alias      Optional (String). Alias to access device data without
                    tokens and it must be unique for every app e.g.
                    "username", "email" ..etc.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform, tag=tag,
                                  token=token, alias=alias)
        # data = {self.KEY_PLATFORM: platform, self.KEY_TAG: tag}
        # if token:
        #     data[self.KEY_TOKEN] = token
        # if alias:
        #     data[self.KEY_ALIAS] = alias
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/tag'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def untag(self, platform=None, tag=None, token=None, alias=None):
        """Tag a device with its token through SDK or Alias through your backend
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @tag        Required (String). "Tag" to be removed.

        @token and @alias are optional, but one of them must be defined.
        @token      Optional (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK
        @alias      Optional (String). Alias to access device data without
                    tokens and it must be unique for every app e.g.
                    "username", "email" ..etc.
        @data       Required (String). Data to be sent.
        """

        data = self._get_data(platform=platform, tag=tag, token=token,
                              alias=alias)
        # data = {self.KEY_PLATFORM: platform, self.KEY_TAG: tag}
        # if token:
        #     data[self.KEY_TOKEN] = token
        # if alias:
        #     data[self.KEY_ALIAS] = alias
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/tag/del'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def device_location(self, platform=None, token=None, lat=None,
                        lng=None, data=None):
        """Add/update location of a device
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK.
        @lat        Required (Integer). Location latitude e.g. 33.7489.
        @lng        Required (Integer). Location longitude e.g. -84.3789.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform, token=token,
                                  lat=lat, lng=lng)
        # data = {self.KEY_PLATFORM: platform, self.KEY_TOKEN: token,
        #         self.KEY_LAT: lat, self.KEY_LNG: lng}
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/geo'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def push(self, platform=None, token=None, msg=None, sound=None,
             badge=None, payload=None, data=None):
        """Push a notification to a single device.
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App.
        @msg        Required (String). Notification Message.
        @sound      Optional (String). Notification Sound.
        @badge      Optional (Integer). Notification Badge number iOS Only
                    e.g. +1 to increment all devices by 1 and 0 to reset the
                    badge of all devices.
        @payload    Optional (Dict). Custom fields.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform, token=token, msg=msg,
                                  sound=sound, badge=badge, payload=payload)
        # data = {self.KEY_PLATFORM: platform, self.KEY_TOKEN: token,
        #         self.KEY_MSG: msg}
        # if sound:
        #     data[self.KEY_SOUND] = sound
        # if badge:
        #     data[self.KEY_BADGE] = badge
        # if payload:
        #     data[self.KEY_PAYLOAD] = payload
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/push/one'
        headers = self.headers
        r = requests.post(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def push_batch(self, platform=None, msg=None, sound=None, badge=None,
                   schedule=None, tags=None, except_tags=None, alias=None,
                   except_alias=None, payload=None, data=None):
        """Push a notification to Devices under certain conditions.
        You must, at least, specify either data or the other params.

        @platform   Required (List of integers). 0 for iOS, 1 for Android,
                    2 for Chrome, e.g. [0,1] to push to Android and iOS.
        @msg        Required (String). Notification Message.
        @sound      Optional (String). Notification Sound.
        @badge      Optional (Integer). Notification Badge number iOS Only
                    e.g. +1 to increment all devices by 1 and 0 to reset the
                    badge of all devices.
        @schedule   Optional (String). The time to send the notification,
                    in UTC e.g. 2015-04-02T11:33:00.
        @tags       Optional (List of strings). List of tags for the
                    notification to be pushed.
        @except_tags Optional(List of strings). List of tags for the
                     notification not to be pushed.
        @alias      Optional (List of strings). List of aliases for the
                    notification to be pushed
        @except_alias Optional (List of strings). List of aliases for the
                      notification not to be pushed
        @payload    Optional (Dict). Custom fields.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform, msg=msg, sound=sound,
                                  badge=badge, schedule=schedule, tags=tags,
                                  except_tags=except_tags, alias=alias,
                                  except_alias=except_alias, payload=payload)
        # data = {self.KEY_PLATFORM: platform, self.KEY_MSG: msg}
        # if sound:
        #     data[self.KEY_SOUND] = sound
        # if badge:
        #     data[self.KEY_BADGE] = badge
        # if schedule:
        #     data[self.KEY_SCHEDULE] = schedule
        # if tags:
        #     data[self.KEY_TAGS] = tags
        # if except_tags:
        #     data[self.KEY_EXCEPT_TAGS] = except_tags
        # if alias:
        #     data[self.KEY_ALIAS] = alias
        # if except_alias:
        #     data[self.KEY_EXCEPT_ALIAS] = except_alias
        # if payload:
        #     data[self.KEY_PAYLOAD] = payload
        # data = json.dumps(data)
        api_url = 'https://api.pushbots.com/push/all'
        headers = self.headers
        r = requests.post(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def badge(self, token=None, platform=None, badge_count=None, data=None):
        """Update device Badge
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App.
        @badge_count Required (Integer). New Badge count.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform, token=token,
                                  badge_count=badge_count)
        api_url = 'https://api.pushbots.com/badge'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    def get_analytics(self):
        """Get Push analytics of a single Application"""

        api_url = 'https://api.pushbots.com/analytics'
        headers = self.headers
        r = requests.get(api_url, headers=headers)
        return r.status_code, r.text

    def record_analytics(self, platform=None, data=None):
        """Record Opened Push Analytics.
        You must, at least, specify either data or the other params.

        @platform   Required (Integer). 0 for iOS, 1 for Android.
        @data       Required (String). Data to be sent.
        """

        if not data:
            data = self._get_data(platform=platform)
        api_url = 'https://api.pushbots.com/stats'
        headers = self.headers
        r = requests.put(api_url, headers=headers, data=data)
        return r.status_code, r.text

    # TODO: implement device_info()

    def _get_data(self, platform=None, token=None, tokens=None, tag=None,
                  tags=None, except_tags=None, lat=None, lng=None, active=None,
                  alias=None, except_alias=None, current_alias=None, msg=None,
                  sound=None, badge=None, schedule=None, payload=None,
                  badge_count=None):
        data = {}
        if platform:
            data[self.KEY_PLATFORM] = platform
        if token:
            data[self.KEY_TOKEN] = token
        if tokens:
            data[self.KEY_TOKENS] = tokens
        if tag:
            data[self.KEY_TAG] = tag
        if tags:
            data[self.KEY_TAGS] = tags
        if except_tags:
            data[self.KEY_EXCEPT_TAGS] = except_tags
        if lat:
            data[self.KEY_LAT] = lat
        if lng:
            data[self.KEY_LNG] = lng
        if active:
            data[self.KEY_ACTIVE] = active
        if alias:
            data[self.KEY_ALIAS] = alias
        if except_alias:
            data[self.KEY_EXCEPT_ALIAS] = except_alias
        if current_alias:
            data[self.KEY_CURRENT_ALIAS] = current_alias
        if msg:
            data[self.KEY_MSG] = msg
        if sound:
            data[self.KEY_SOUND] = sound
        if badge:
            data[self.KEY_BADGE] = badge
        if schedule:
            data[self.KEY_SCHEDULE] = schedule
        if payload:
            data[self.KEY_PAYLOAD] = payload
        if badge_count:
            data[self.KEY_BADGE_COUNT] = badge_count
        return json.dumps(data)

# -*- coding: utf-8 -*-


"""
Main pusbots module. To use just import pushbots
Author Tilemachos Charalampous
"""
import requests
import json


class Pushbots:

    """This is the main Pushbots class
    Handles all api calls for Pushbots.
    For api calls you can refer to:
    https://pushbots.com/developer/api/1
    """

    PLATFORM_IOS = '0'
    PLATFORM_ANDROID = '1'
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
    KEY_SETBADGECOUNT = 'setbadgecount'

    def __init__(self, app_id, secret):
        """
        init method.
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

    def put(self, api_url, headers, data=None):
        """
        Generic method for put requests.
        with the json response, or empty dictionary if empty response
        @headers (Dict). Headers to include
        @data    (Dict). Data to include in json (python dict) format
        @return  (Integer, Dict). Returns the request's response status
                 code, and a dictionary with the json response, or empty
                 if there was no repsonse
        """
        if data is None:
            r = requests.put(api_url, headers=headers)
        else:
            data = json.dumps(data)
            r = requests.put(api_url, headers=headers, data=data)
        # r.json() may raise ValueError if empty,
        # so in case of ValueError return an empty Dict.
        status_code = r.status_code
        try:
            content_json = r.json()
        except ValueError:
            content_json = {}
        return status_code, content_json

    def post(self, api_url, headers, data=None):
        """
        Generic method for post requests.
        with the json response, or empty dictionary if empty response
        @headers (Dict). Headers to include
        @data    (Dict). Data to include in json (python dict) format
        @return  (Integer, Dict). Returns the request's response status
                 code, and a dictionary with the json response, or empty
                 if there was no repsonse
        """
        if data is None:
            r = requests.post(api_url, headers=headers)
        else:
            data = json.dumps(data)
            r = requests.post(api_url, headers=headers, data=data)
        # r.json() may raise ValueError if empty,
        # so in case of ValueError return an empty Dict.
        status_code = r.status_code
        try:
            content_json = r.json()
        except ValueError:
            content_json = {}
        return status_code, content_json

    def get(self, api_url, headers):
        """
        Generic method for get requests.
        with the json response, or empty dictionary if empty response
        @headers (Dict). Headers to include
        @data    (Dict). Data to include in json (python dict) format
        @return  (Integer, Dict). Returns the request's response status
                 code, and a dictionary with the json response, or empty
                 if there was no repsonse
        """
        r = requests.get(api_url, headers=headers)
        # r.json() may raise ValueError if empty,
        # so in case of ValueError return an empty Dict.
        status_code = r.status_code
        try:
            content_json = r.json()
        except ValueError:
            content_json = {}
        return status_code, content_json

    def register(self, token=None, platform=None, lat=None, lng=None,
                 active=None, tag=None, alias=None, data=None):
        """
        Register device token of the app in the database first time,
        and update it with every launch of the app , device data will
        be updated if registered already.
        You must, at least, specify either data or the other params.

        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK.
        @platform   Required (String). 0 for iOS, 1 for Android.
        @lat        Optional (String). Location latitude e.g. 33.7489.
        @lng        Optional (String). Location longitude e.g. -84.3789.
        @active     Optional (List of strings). List of notification Types
                    linked to the device e.g. ["Subscriptions" , "Followers"].
        @tag        Optional (List of strings). List of tags associated with
                    the deviceToken,if empty array that'll remove any
                    associated tags e.g. ["Culture" , "EGYPT"].
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(token=token, platform=platform, lat=lat,
                                  lng=lng, active=active, tag=tag, alias=alias)
        api_url = 'https://api.pushbots.com/deviceToken'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def register_batch(self, tokens=None, platform=None, tags=None, data=None):
        """
        Register multiple devices up to 500 Device per request
        You must, at least, specify either data or the other params.

        @tokens     Required (List of strings). List of devices tokens
                    to be added to database, up to 500 device per request.
        @platform   Required (String). 0 for iOS, 1 for Android.
        @tags        Optional (List of strings). List of tags associated
                    with all imported devices e.g. ["Culture" , "USA"].
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(tokens=tokens, platform=platform, tags=tags)
        api_url = 'https://api.pushbots.com/deviceToken/batch'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def unregister(self, token=None, platform=None, data=None):
        """
        unRegister device token of the app from the database
        You must, at least, specify either data or the other params.

        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK.
        @platform   Required (String). 0 for iOS, 1 for Android.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(token=token, platform=platform)
        api_url = 'https://api.pushbots.com/deviceToken/del'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def alias(self, platform=None, token=None, alias=None, current_alias=None,
              data=None):
        """
        Add/update alias of a device.
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.

        @token and @alias are optional, but one of them must be defined.
        @token      Optional (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK
        @alias      Optional (String). Alias to access device data without
                    tokens and it must be unique for every app e.g.
                    "username", "email" ..etc
        @current_alias  Optional (String). Set this parameter in case you want
                        to update existing alias.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(platform=platform, token=token, alias=alias,
                                  current_alias=current_alias)
        api_url = 'https://api.pushbots.com/alias'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def tag(self, platform=None, tag=None, token=None, alias=None, data=None):
        """
        Tag a device with its token through SDK or Alias through your backend
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.
        @tag        Required (String). "Tag" to be Added.

        @token and @alias are optional, but one of them must be defined.
        @token      Optional (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK
        @alias      Optional (String). Alias to access device data without
                    tokens and it must be unique for every app e.g.
                    "username", "email" ..etc.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(platform=platform, tag=tag,
                                  token=token, alias=alias)
        api_url = 'https://api.pushbots.com/tag'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def untag(self, platform=None, tag=None, token=None,
              alias=None, data=None):
        """
        Tag a device with its token through SDK or Alias through your backend
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.
        @tag        Required (String). "Tag" to be removed.

        @token and @alias are optional, but one of them must be defined.
        @token      Optional (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK
        @alias      Optional (String). Alias to access device data without
                    tokens and it must be unique for every app e.g.
                    "username", "email" ..etc.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(platform=platform, tag=tag,
                                  token=token, alias=alias)
        api_url = 'https://api.pushbots.com/tag/del'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def device_location(self, platform=None, token=None, lat=None,
                        lng=None, data=None):
        """
        Add/update location of a device
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.
        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App
                    and usually it's managed using SDK.
        @lat        Required (String). Location latitude e.g. 33.7489.
        @lng        Required (String). Location longitude e.g. -84.3789.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(platform=platform, token=token,
                                  lat=lat, lng=lng)
        api_url = 'https://api.pushbots.com/geo'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def devices_info(self):
        """
        Gets information about all registered devices
        @return     (Integer, Dict). The result of self.get()
        """

        api_url = 'https://api.pushbots.com/devices'
        headers = self.headers
        return self.get(api_url=api_url, headers=headers)

    def device_info(self, token=None):
        """
        Get device info.
        A token is needed to fetch info

        @token      Required (String). The device's token.
        @return     (Integer, Dict). The result of self.get()
        """

        api_url = 'https://api.pushbots.com/deviceToken/one'
        headers = {'x-pushbots-appid': self._app_id,
                   'token': token, 'Content-Type': 'application/json'}
        return self.get(api_url=api_url, headers=headers)

    def push(self, platform=None, token=None, msg=None, sound=None,
             badge=None, payload=None, data=None):
        """
        Push a notification to a single device.
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.
        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App.
        @msg        Required (String). Notification Message.
        @sound      Optional (String). Notification Sound.
        @badge      Optional (String). Notification Badge number iOS Only
                    e.g. +1 to increment all devices by 1 and 0 to reset the
                    badge of all devices.
        @payload    Optional (Dict). Custom fields.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.post()
        """

        if data is None:
            data = self._get_data(platform=platform, token=token, msg=msg,
                                  sound=sound, badge=badge, payload=payload)
        api_url = 'https://api.pushbots.com/push/one'
        headers = self.headers
        return self.post(api_url=api_url, headers=headers, data=data)

    def push_batch(self, platform=None, msg=None, sound=None, badge=None,
                   schedule=None, tags=None, except_tags=None, alias=None,
                   except_alias=None, payload=None, data=None):
        """
        Push a notification to Devices under certain conditions.
        You must, at least, specify either data or the other params.

        @platform   Required (List of strings). 0 for iOS, 1 for Android,
                    2 for Chrome, e.g. [0,1] to push to Android and iOS.
        @msg        Required (String). Notification Message.
        @sound      Optional (String). Notification Sound.
        @badge      Optional (String). Notification Badge number iOS Only
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
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.post()
        """

        if data is None:
            data = self._get_data(platform=platform, msg=msg, sound=sound,
                                  badge=badge, schedule=schedule, tags=tags,
                                  except_tags=except_tags, alias=alias,
                                  except_alias=except_alias, payload=payload)
        api_url = 'https://api.pushbots.com/push/all'
        headers = self.headers
        return self.post(api_url=api_url, headers=headers, data=data)

    def badge(self, token=None, platform=None, setbadgecount=None, data=None):
        """
        Update device Badge
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.
        @token      Required (String). The unique token retrieved by your app;
                    device token of the iOS app or RegID of the android App.
        @badge_count Required (Integer). New Badge count.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(platform=platform, token=token,
                                  setbadgecount=setbadgecount)
        api_url = 'https://api.pushbots.com/badge'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def get_analytics(self):
        """
        Get Push analytics of a single Application

        @return     (Integer, Dict). The result of self.get()
        """

        api_url = 'https://api.pushbots.com/analytics'
        headers = self.headers
        return self.get(api_url=api_url, headers=headers)

    def record_analytics(self, platform=None, data=None):
        """Record Opened Push Analytics.
        You must, at least, specify either data or the other params.

        @platform   Required (String). 0 for iOS, 1 for Android.
        @data       Required (Dict). Data to be sent.
        @return     (Integer, Dict). The result of self.put()
        """

        if data is None:
            data = self._get_data(platform=platform)
        api_url = 'https://api.pushbots.com/stats'
        headers = self.headers
        return self.put(api_url=api_url, headers=headers, data=data)

    def _get_data(self, platform=None, token=None, tokens=None, tag=None,
                  tags=None, except_tags=None, lat=None, lng=None, active=None,
                  alias=None, except_alias=None, current_alias=None, msg=None,
                  sound=None, badge=None, schedule=None, payload=None,
                  setbadgecount=None):
        """
        Constructs the dictionary (json) to be passed to the request,
        according to the fields provided.
        """

        data = {}
        if platform is not None:
            data[self.KEY_PLATFORM] = platform
        if token is not None:
            data[self.KEY_TOKEN] = token
        if tokens is not None:
            data[self.KEY_TOKENS] = tokens
        if tag is not None:
            data[self.KEY_TAG] = tag
        if tags is not None:
            data[self.KEY_TAGS] = tags
        if except_tags is not None:
            data[self.KEY_EXCEPT_TAGS] = except_tags
        if lat is not None:
            data[self.KEY_LAT] = lat
        if lng is not None:
            data[self.KEY_LNG] = lng
        if active is not None:
            data[self.KEY_ACTIVE] = active
        if alias is not None:
            data[self.KEY_ALIAS] = alias
        if except_alias is not None:
            data[self.KEY_EXCEPT_ALIAS] = except_alias
        if current_alias is not None:
            data[self.KEY_CURRENT_ALIAS] = current_alias
        if msg is not None:
            data[self.KEY_MSG] = msg
        if sound is not None:
            data[self.KEY_SOUND] = sound
        if badge is not None:
            data[self.KEY_BADGE] = badge
        if schedule is not None:
            data[self.KEY_SCHEDULE] = schedule
        if payload is not None:
            data[self.KEY_PAYLOAD] = payload
        if setbadgecount is not None:
            data[self.KEY_SETBADGECOUNT] = setbadgecount
        return data

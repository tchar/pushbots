# pushbots #
A pushbots python 2/python 3 API module (wrapper). The module, the tests and the examples work for both python 2 and python 3 versions.  
Current pushbots module supports all of the pushbots API calls. List of supported API calls following:
* Register        (For testing API call)
* Register Batch  (For testing API call)
* unRegister      (For testing API call)
* Alias
* Tag
* unTag
* Device Location (For testing API call)
* Devices Info
* Device Info     (For testing API call)
* Push            (For testing API call)
* Push Batch
* Get Push analytics
* Record Analytics  

In the list above, some of the API calls are tagged with "(For testing API call)". This means that a token is needed to perform those API calls and since this module is reserved for backends, you, normally, won't be using those API calls. Though you can retrieve device tokens based on alias, tags, etc through devices info (see examples/get_token_from_alias.py and examples/location.py, examples/unregister.py for more info):
  
There is also a second list of generic API calls, for calls not listed in the first list. At the moment of creating this all API calls are supported. This is provided for future API calls:
* Put (For generic put API calls, not listed above)
* Post (For generic post API calls, not listed above)
* Get (For generic get API calls, not listed above)

Dependencies
------------
For pushbots to work, python "requests" must be installed:  
http://docs.python-requests.org/en/latest/  
You can install requests with pip:  
```bash
pip install requests
```

How to use
---------
```python
from pushbots import Pushbots
# Your code
```

Examples
--------
You can find examples under examples directory.
If there is an API call missing from the first list mentioned above, you can view the examples/generic.py examples, on how to make custom API calls, listed in the second list mentioned (put, post, get).
If you want to perform token operations, you can use the examples/get_token_from_alias.py to get the devices token and platform associated with a specific alias. Also the files, examples/location.py and examples/unregister.py make use of tokens to make an API call, whereas all the other files in examples make use of alias, tags etc for the API calls.

Tests
-----
Tests create virtual devices to test the API calls.
You can run the tests by typing from the parent directory:  
```bash
python -m tests.run
```
If you want help on how to run tests, type:
```bash
python -m tests.run -h
```

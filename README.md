# pushbots #
A pushbots python 2 API wrapper.  
Current pushbots module supports the following list of API calls.  
In the following list, some of the API calls are tagged with "(For testing API call)". This means that a token is needed to perform those API calls and since this module is reserved for backends, you, normally, won't be using those API calls:
* Register        (For testing API call)
* Register Batch  (For testing API call)
* unRegister      (For testing API call)
* Alias
* Tag
* unTag
* Device Location (For testing API call)
* Push            (For testing API call)
* Push Batch
* Get Push analytics
* Record Analytics  
  
There is also a second list of generic API calls, for calls not listed in the first list:
* Put (For generic put API calls, not listed above)
* Post (For generic post API calls, not listed above)
* Get (For generic get API calls, not listed above)

Dependencies
------------
For pushbots to work python requests must be installed:  
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

Tests
-----
Tests create virtual devices to test the API calls.
You can run the tests by typing from the parent directory:  
```bash
python -m tests.run
```
If you want help on how to run tests type:
```bash
python -m tests.run -h
```

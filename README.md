# pushbots #

PushBots sends push notifications to users on mobile and web. PushBot's 
[API](https://en.wikipedia.org/wiki/Application_programming_interface) is organized around 
[REST](https://en.wikipedia.org/wiki/Representational_state_transfer).

This project is a Python module, or specifically a wrapper, for [PushBots](https://pushbots.com/). The module, tests, 
and examples work in python 2 and python 3.

Current Pushbots module supports all of the pushbots API calls. The list of supported API calls is as follows:

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

In the list above, some of the API calls are tagged with "(For testing API call)". The tag means that a token is needed 
to perform those API calls. Since the module is reserved for backend, those tagged API calls are not used often. 
However, device tokens can be retrieved based on alias, tags, etc through devices information. Look at 
examples/get_token_from_alias.py, examples/location.py, and examples/unregister.py for more details.

There is also a list of generic API calls, for calls not listed above. At the time of writing this, i.e. November 2019, 
all API calls are supported. The following list is provided for future API calls:

* Put (For generic Put API calls, not listed above)
* Post (For generic Post API calls, not listed above)
* Get (For generic Get API calls, not listed above)

## Install

There are two ways to use this package:
1. Pushbots package can be copied into a project. 
2. Pushbots can be installed. 

There are two ways to install Pushbots.
* Using pip:
  ```bash
  $ pip install pushbots
  ```
* Using source code:\
    1\. Go to [releases](https://github.com/tchar/pushbots/releases) and download the latest version.\
    2\. Extract the compressed file\
    3\. Navigate to project's root directory and run:
  ```bash
  $ python setup.py install
  ```
### Requirements 

Pushbots requires Python [Requests](https://pypi.org/project/requests/). You don't have to manually install Requests 
if Setuptools is installed and you choose to install Pushbots from pip or setup.py.

In any other case, it must be installed manually:  
```bash
$ pip install requests
```
If you wish to use the source code to install Request, follow the 
[installation instruction](https://requests.kennethreitz.org/en/master/user/install/#get-the-source-code) from their 
website. 


## Usage 

```python
from pushbots import Pushbots
# Your code
```

### Examples

You can find examples under pushbots/examples directory.
If there is an API call missing from the first list mentioned above, you can view the examples/generic.py examples, on 
how to make custom API calls, listed in the second list mentioned (i.e. put, post, get).\
If you want to perform token operations, you can use the examples/get_token_from_alias.py to get the devices tokens and 
platforms associated with a specific alias.\
Also the files examples/location.py and examples/unregister.py make use of tokens to make an API call, whereas all the 
other files in pushbots/examples directory make use of alias, tags, etc for the API calls.

### Tests

Tests are located in pushbots/tests directory. The tests create virtual devices to test the API calls provided 
by Pushbots module. 

You can run the tests by:
```bash
$ python -m pushbots.tests.run
```
You can use "-h" to learn how to run tests.
```bash
$ python -m pushbots.tests.run -h
```

## License 
[MIT](LICENSE.txt)

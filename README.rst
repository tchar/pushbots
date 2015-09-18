pushbots
========

| A python 2/python 3 REST API library module (wrapper) for
  `pushbots <https://pushbots.com/>`__. The module, the tests and the
  examples work for both python 2 and python 3 versions.
| Current "pushbots" module supports all of the pushbots API calls. List
  of supported API calls follow: 

- Register (For testing API call)
- Register Batch (For testing API call)
- unRegister (For testing API call)
- Alias
- Tag
- unTag
- Device Location (For testing API call)
- Devices Info
- Device Info (For testing API call)
- Push (For testing API call)
- Push Batch
- Get Push analytics
- Record Analytics

In the list above, some of the API calls are tagged with "(For testing
API call)". This means that a token is needed to perform those API calls
and since this module is reserved for backends, you, normally, won't be
using those API calls. Though you can retrieve device tokens based on
alias, tags, etc through devices info (see
examples/get\_token\_from\_alias.py and examples/location.py,
examples/unregister.py for more info):

There is also a second list of generic API calls, for calls not listed
in the first list. At the moment of creating this all API calls are
supported. This is provided for future API calls:

- Put (For generic put API calls, not listed above)
- Post (For generic post API calls, not listed above)
- Get (For generic get API calls, not listed above)

Install
-------

You can choose to install "pushbots". If you don't want to install it,
you can manually copy the "pushbots" package into your project. There
are two ways to install "pushbots".

- With pip: ``pip install pushbots``
- Manually: Go to `releases <https://github.com/tchar/pushbots/releases>`__ and download
  the latest version. Extract the compressed file, navigate to project's
  root directory and run: ``python setup.py install``

Dependencies
------------

| For "pushbots" to work, python "requests" must be installed. If you
  already have "setuptools" installed and choose to install "pushbots"
  from pip or setup.py, you don't have to manually install "requests".
  On any other case, you must install it manually:
| http://docs.python-requests.org/en/latest/

.. code:: bash

    pip install requests

How to use
----------

.. code:: python

    from pushbots import Pushbots
    # Your code

Examples
--------

You can find examples under pushbots/examples directory. If there is an
API call missing from the first list mentioned above, you can view the
examples/generic.py examples, on how to make custom API calls, listed in
the second list mentioned (put, post, get). If you want to perform token
operations, you can use the examples/get\_token\_from\_alias.py to get
the devices tokens and platforms associated with a specific alias. Also
the files, examples/location.py and examples/unregister.py make use of
tokens to make an API call, whereas all the other files in examples make
use of alias, tags etc for the API calls.

Tests
-----

The tests package is located under pushbots directory. Tests create
virtual devices to test the API calls provided by "pushbots" module. You
can run the tests by typing:

.. code:: bash

    python -m pushbots.tests.run

If you want help on how to run tests, type:

.. code:: bash

    python -m pushbots.tests.run -h

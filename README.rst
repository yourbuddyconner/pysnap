PySnap |travis| |pypi|
============================

Note: This project is just a fork of the package ``snapshottest`` which lives here: https://github.com/syrusakbary/snapshottest. It had been mostly abandoned, so I kicked the wheels and got it back in working order. Contributions are welcome!

Snapshot testing is a way to test your APIs without writing actual test
cases.pip install doc8

1. A snapshot is a single state of your API, saved in a file.
2. You have a set of snapshots for your API endpoints.
3. Once you add a new feature, you can generate *automatically* new
   snapshots for the updated API.

Installation
------------

::

    $ pip install pysnap

Usage with unittest/nose
------------------------

.. code:: python

    from pysnap import TestCase

    class APITestCase(TestCase):
        def test_api_me(self):
            """Testing the API for /me"""
            my_api_response = api.client.get('/me')
            self.assertMatchSnapshot(my_api_response)

            # Set custom snapshot name: `gpg_response`
            my_gpg_response = api.client.get('/me?gpg_key')
            self.assertMatchSnapshot(my_gpg_response, 'gpg_response')

If you want to update the snapshots automatically you can use the
``nosetests --snapshot-update``.

Check the `Unittest
example <https://github.com/syrusakbary/yourbuddyconner/pysnap/tree/master/examples/unittest>`__.

Usage with pytest
-----------------

.. code:: python

    def test_mything(snapshot):
        """Testing the API for /me"""
        my_api_response = api.client.get('/me')
        snapshot.assert_match(my_api_response)

        # Set custom snapshot name: `gpg_response`
        my_gpg_response = api.client.get('/me?gpg_key')
        snapshot.assert_match(my_gpg_response, 'gpg_response')

If you want to update the snapshots automatically you can use the
``--snapshot-update`` config.

Check the `Pytest
example <https://github.com/yourbuddyconner/pysnap/tree/master/examples/pytest>`__.

Usage with django
-----------------

Add to your settings:

.. code:: python

    TEST_RUNNER = 'pysnap.django.TestRunner'

To create your pysnap:

.. code:: python

    from pysnap.django import TestCase

    class APITestCase(TestCase):
        def test_api_me(self):
            """Testing the API for /me"""
            my_api_response = api.client.get('/me')
            self.assertMatchSnapshot(my_api_response)

If you want to update the snapshots automatically you can use the
``python manage.py test --snapshot-update``. Check the `Django
example <https://github.com/yourbuddyconner/pysnap/tree/master/examples/django_project>`__.

Contributing
============

After cloning this repo and configuring a virtualenv for snapshottest
(optional, but highly recommended), ensure dependencies are installed by
running:

.. code:: sh

    make install

After developing, the full test suite can be evaluated by running:

.. code:: sh

    make lint
    # and
    make test

If you change this ``README.md``, you'll need to have pandoc installed to update its ``README.rst`` counterpart (used by PyPI),
which can be done by running:

::

    make README.rst

Notes
=====

This package is heavily inspired in `jest snapshot
testing <https://facebook.github.io/jest/docs/snapshot-testing.html>`__.

Reasons for use this package
============================

    Most of this content is taken from the `Jest snapshot
    blogpost <https://facebook.github.io/jest/blog/2016/07/27/jest-14.html>`__.

We want to make it as frictionless as possible to write good tests that
are useful. We observed that when engineers are provided with
ready-to-use tools, they end up writing more tests, which in turn
results in stable and healthy code bases.

However engineers frequently spend more time writing a test than the
component itself. As a result many people stopped writing tests
altogether which eventually led to instabilities.

A typical snapshot test case for a mobile app renders a UI component,
takes a screenshot, then compares it to a reference image stored
alongside the test. The test will fail if the two images do not match:
either the change is unexpected, or the screenshot needs to be updated
to the new version of the UI component.

Snapshot Testing with PySnap
----------------------------------

A similar approach can be taken when it comes to testing your APIs.
Instead of rendering the graphical UI, which would require building the
entire app, you can use a test renderer to quickly generate a
serializable value for your API response.

License
-------

`MIT
License <https://github.com/yourbuddyconner/pysnap/blob/master/LICENSE>`__

|coveralls|

.. |travis| image:: https://img.shields.io/travis/yourbuddyconner/pysnap.svg?style=flat
   :target: https://travis-ci.com/yourbuddyconner/pysnap
.. |pypi| image:: https://img.shields.io/pypi/v/pysnap.svg?style=flat
   :target: https://pypi.python.org/pypi/pysnap
.. |coveralls| image:: https://coveralls.io/repos/yourbuddyconner/pysnap/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/yourbuddyconner/pysnap?branch=master

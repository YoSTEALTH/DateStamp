Versioning
==========
Software versioning based on auto generated year.month.day format.


Install, update & uninstall (Pre-Alpha)
---------------------------------------

Use `pip`_ to install, upgrade & uninstall:

.. code-block:: text

    pip install versioning

    pip install --upgrade versioning

    pip uninstall versioning


Usage
-----

setup.py

.. code-block:: python
    
    from version import versioning

    setup(...,
          setup_requires=['versioning'],
          version=versioning('package_name'),
          ...)


License
-------
Free, No limit what so ever. `Read more`_


.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _Read more: https://github.com/YoSTEALTH/Versioning/blob/master/LICENSE.txt

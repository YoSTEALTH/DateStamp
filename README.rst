DateStamp
===========
Automated software version generator and replacer based on `year.month.day` as its format.


Install, update & uninstall (Alpha)
-----------------------------------

Use `pip`_ to install, upgrade & uninstall:

.. code-block:: text

    pip install datestamp

    pip install --upgrade datestamp

    pip uninstall datestamp


Usage
-----

setup.py

.. code-block:: python
    
    from datestamp import stamp

    setup(...,
          setup_requires=['datestamp'],
          version=stamp('package_name'),
          ...)


Note
----
    - Auto generates date as version number, sets it in `setup(version='2020.2.9')`
    - Replaced `__init__.py` file `__version__` line with `__version__ = '2020.2.9'`
    - Works for One-Off script file as well like `datestamp` package itself.


License
-------
Free, No limit what so ever. `Read more`_


.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _Read more: https://github.com/YoSTEALTH/datestamp/blob/master/LICENSE.txt

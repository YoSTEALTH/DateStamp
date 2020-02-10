DateStamp
=========
Automatically generates new software version stamp as ``year.month.day`` format.


Install, update & uninstall (Alpha)
-----------------------------------

Use `pip`_ to install, upgrade & uninstall:

.. code-block:: text

    pip install datestamp

    pip install --upgrade datestamp

    pip uninstall datestamp


Usage
-----

./setup.py

.. code-block:: python
    
    # Option-1
    # --------
    from datestamp import stamp

    setup(...,
          setup_requires=['datestamp'],
          version=stamp('package_name'),  # '2020.2.9'
          ...)

    # Option-2
    # --------
    from datestamp import stamp

    setup(...,
          setup_requires=['datestamp'],
          version=stamp('package_name', 'v1'),  # '2020.2.9v1'
          ...)


Note
----
    - Make sure to pre-install ``datestamp`` before running ``python3 setup.py ...``. This is only required for publishers, for users it will be auto installed through ``setup_requires=['datestamp']``
    - New version stamp is only generated when you are ready to publish your project by
      ``python3 setup.py sdist`` or current version date is used.
    - When new date is generated at ``setup(version=stamp(...))`` it also replaces ``__version__`` line with ``__version__ = '2020.2.9'`` in ``__init__.py`` file.
    - Works for One-Off script file as well like ``datestamp.py`` package itself.
    - If for some reason you can't pre-install ``datestamp`` you can include ``datestamp.py`` file besides your ``setup.py`` and import it that way. Also don't forget to ``include datestamp.py`` in ``MANIFEST.in`` if you know the user installing your package does not have access t


License
-------
Free, No limit what so ever. `Read more`_


.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _Read more: https://github.com/YoSTEALTH/datestamp/blob/master/LICENSE.txt

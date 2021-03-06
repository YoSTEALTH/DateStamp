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


Usage #1
--------

.. code-block:: python
    
    # ./pyproject.toml
    [build-system]
    requires = [..., "datestamp"]

    # ./setup.py
    from datestamp import stamp

    setup(...,
          version=stamp('package_name'),    # '2020.2.9'
          ...)


Usage #2
--------

.. code-block:: python
    
    # ./datestamp.py
    ...

    # ./MANIFEST.in
    include datestamp.py

    # ./setup.py
    from datestamp import stamp

    setup(...,
          version=stamp('package_name'),    # '2020.2.9'
          ...)


Options
-------

.. code-block:: python

    version=stamp('package_name')               # '2020.2.9'
    version=stamp('package_name', '.post1')     # '2020.2.9.post1'
    version=stamp('package_name', 'rc1')        # '2020.2.9rc1'


Note
----

    - Make sure to pre-install ``datestamp`` before running ``python3 setup.py sdist``. This is only required for publishers, for users it will be build at setup time (but not installed).
    - New date stamp is only generated when you are ready to publish your project by
      ``python3 setup.py sdist`` or current version date is used.
    - When new date is generated at ``setup(version=stamp(...))`` it also replaces ``__version__`` line with ``__version__ = '2020.2.9'`` in ``__init__.py`` file.
    - Works for One-Off script file as well like ``datestamp.py`` package itself.


License
-------
Free, Public Domain (CC0). `Read more`_


.. _pip: https://pip.pypa.io/en/stable/quickstart/
.. _Read more: https://github.com/YoSTEALTH/datestamp/blob/master/LICENSE.txt


TODO
----
    - [ ] detect when `bdist_wheel` is being called to create new date stamp
    - [ ] create wheel build to support all systems including windows and mac.
    - [ ] write test for `stamp()` function
    - [ ] look into `replace` and `version_only` for new `stamp()` function and implement it.

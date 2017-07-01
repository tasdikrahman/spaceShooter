Creating the Executable
=======================

For ``Debain/Ubuntu`` based systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. I used `pyinstaller <https://github.com/pyinstaller/pyinstaller/>`__ to create the executable.

After installing it and adding the changes. Inside the ``spaceShooter`` directory, simply run the command

.. code:: bash

    $ pyinstaller --onefile --windowed spaceShooter.py

This will create an executable and place it inside the directory ``dist``

2. Place the folders ``assets`` and ``sounds`` together with the excutable inside a single folder and zip it.

For example for ``v0.0.2``

.. code:: bash

    $ ls spaceShooter/
    assets  BUILDING_EXECUTABLE.rst  CONTRIBUTING.rst  LICENSE.txt  README.md  sounds  spaceShooter
    $ zip -r spaceShooter-v0.0.2_linux.zip spaceShooter/

For ``Windows`` based systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `cx_freeze <http://cx-freeze.sourceforge.net/>`__ was used to create the excutable for Windows based systems

2. Use the `setup.py <https://github.com/tasdikrahman/spaceShooter/blob/master/setup.py>`__ file for building the executable.

3. Go to the directory ``spaceShooter`` and then run the command

.. code:: python

    $ python setup.py build

This will create a new folder inside ``spaceShooter``.

4. Rename it and zip that file

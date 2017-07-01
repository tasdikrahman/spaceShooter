Contributing
============

1. Fork it.

2. Clone it 

Make sure you have installed `pygame <http://pygame.org>`__ installed on your system

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__ 

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/spaceShooter.git
    (develop)$ cd spaceShooter

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/spaceShooter.git
    (develop)$ cd spaceShooter

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)

Conform to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ and if everything is running fine, integrate your feature 

5. Push to the branch (``$ git push origin my-new-awesome-feature``)

6. Create new Pull Request

Hack away! 
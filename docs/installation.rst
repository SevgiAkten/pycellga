Installation
============

This section provides detailed instructions for installing `pycellga` and its dependencies.

Requirements
------------

Before installing `pycellga`, make sure you have the following installed:

- Python 3.7 or higher
- `pip` package manager

Installing from PyPI
---------------------

The easiest way to install `pycellga` is via PyPI. You can use `pip` to install it directly from the Python Package Index:

.. code-block:: bash

    pip install pycellga

Installing from Source
----------------------

To install `pycellga` from source, follow these steps:

1. Clone the repository from GitHub:

   .. code-block:: bash

       git clone https://github.com/SevgiAkten/pycellga.git

2. Navigate to the cloned repository directory:

   .. code-block:: bash

       cd pycellga

3. Install the package using `pip`:

   .. code-block:: bash

       pip install .

Optional Dependencies
---------------------

`pycellga` has optional dependencies for certain features. To use these features, you may need to install additional packages:

- **Jupyter Notebooks**: If you plan to use Jupyter Notebooks for tutorials or examples, install `jupyter`:

  .. code-block:: bash

      pip install jupyter

- **Matplotlib**: For visualizing optimization results, install `matplotlib`:

  .. code-block:: bash

      pip install matplotlib

Verifying the Installation
--------------------------

To verify that `pycellga` is installed correctly, you can import it in Python:

.. code-block:: python

    import pycellga
    print(pycellga.__version__)

If no errors occur, the installation is successful.

Troubleshooting
---------------

If you encounter any issues during installation, try the following steps:

1. Ensure you are using Python 3.7 or higher by running:

   .. code-block:: bash

       python --version

2. Make sure `pip` is up-to-date:

   .. code-block:: bash

       pip install --upgrade pip

3. If issues persist, refer to the GitHub repository for troubleshooting tips or to submit an issue.

Uninstallation
--------------

To uninstall `pycellga`, you can use the following command:

.. code-block:: bash

    pip uninstall pycellga

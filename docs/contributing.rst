Contributing
============

We’re thrilled that you’re considering contributing to `pycellga`! Community contributions drive innovation and help us improve the software. Whether it’s reporting bugs, suggesting enhancements, or submitting pull requests, your support is invaluable.


Ways to Contribute
------------------

Here are some ways you can make meaningful contributions to `pycellga`:

- **Report Bugs**: If you encounter an issue, create a detailed bug report in our `issue tracker <https://github.com/SevgiAkten/pycellga/issues>`_.
- **Suggest Features**: Have ideas for new features or enhancements? Submit a feature request to help guide our roadmap.
- **Fix Bugs or Implement Features**: Browse open issues, pick one, and submit a pull request with your solution.
- **Improve Documentation**: Documentation is key to helping users understand the software. Fix typos, clarify steps, or add examples to make it even better.

Development Setup
-----------------

To begin contributing code, set up your development environment as follows:

**Step 1: Fork the Repository**

Create your own copy of `pycellga` by forking the repository:

1. Visit the  `repository <https://github.com/SevgiAkten/pycellga>`_.
2. Click the "Fork" button in the upper-right corner.
3. Select your GitHub account to create the fork.

For a step-by-step guide on forking, visit GitHub’s `Fork a Repo <https://docs.github.com/en/get-started/quickstart/fork-a-repo>`_ page.

**Step 2: Clone Your Fork**

Clone your forked repository to your local machine:

.. code-block:: bash

    git clone https://github.com/username/pycellga.git
    cd pycellga

**Step 3: Install Dependencies**

Install the required dependencies:

.. code-block:: bash

    pip install -r requirements.txt

**Step 4: Create a New Branch**

Create a branch for your changes:

.. code-block:: bash

    git checkout -b feature-or-bugfix-name

Use descriptive names for branches, such as `add-new-feature` or `fix-bug`.

Pull Request Guidelines
-----------------------

When you’re ready to submit your changes, follow these guidelines to ensure a smooth review process:

1. **Write Clear Commit Messages**: Each commit message should be clear and descriptive.
2. **Run Tests**: Verify that all tests pass. Tests can be run from the `tests` folder or main directory:

   - From the `tests` folder:

     .. code-block:: bash

         cd tests
         pytest *         # or
         pytest -v

   - From the main project directory:

     .. code-block:: bash

         pytest -v

3. **Submit a Pull Request**: Push your branch to GitHub, navigate to the main repository, and open a pull request.

4. **Respond to Reviews**: Be responsive to feedback during the review process, and make any requested changes to ensure your contribution is merged smoothly.

Coding Standards
----------------

To maintain a consistent and readable codebase, please adhere to the following guidelines:

- **PEP 8**: Follow PEP 8 coding style standards for Python code.
- **Type Annotations**: Include type hints for function arguments and return values.
- **Docstrings**: Provide clear docstrings for functions and classes. We recommend using the Google docstring style.

Running Tests
-------------

Before submitting a pull request, ensure that all tests pass. Tests can be run in the `tests` folder or from the main directory as follows:

1. **From the `tests` folder**:

   .. code-block:: bash

       cd tests
       pytest *         # or
       pytest -v

2. **From the main project directory**:

   .. code-block:: bash

       pytest -v

If you add new functionality, consider adding tests to cover your changes.


Thank you for considering a contribution to `pycellga`. We’re excited to see what you’ll bring to the project!

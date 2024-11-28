
# Contributing to pycellga

Thank you for considering contributing to pycellga! We welcome contributions from the community and are excited to collaborate with you.

## How to Contribute

### Reporting Bugs

If you find a bug, please report it by creating an issue in the [issue tracker](https://github.com/SevgiAkten/pycellga/issues). Include detailed information about the bug, including steps to reproduce it, the expected behavior, and what actually happens.

### Suggesting Enhancements

If you have an idea for an enhancement or a new feature, please open an issue in the [issue tracker](https://github.com/SevgiAkten/pycellga/issues) to discuss it. Provide as much detail as possible, including the problem the enhancement would solve and any suggested solutions.

### Contributing Code

1. **Fork the Repository**: Fork the repository on GitHub and clone it to your local machine.
2. **Create a Branch**: Create a new branch for your work.
   ```bash
   git checkout -b feature-branch
   ```
3. **Make Changes**: Make your changes to the codebase. Ensure your code adheres to the project's coding standards.
4. **Commit Changes**: Commit your changes with a descriptive commit message.
   ```bash
   git commit -m "Description of the feature or fix"
   ```
5. **Push Changes**: Push your changes to your forked repository.
   ```bash
   git push origin feature-branch
   ```
6. **Create a Pull Request**: Open a pull request to merge your changes into the main repository. Provide a clear and detailed description of your changes.

### Code Style

Please ensure your code follows the project's coding standards. Use PEP 8 as a guideline for Python code.

### Testing

Before submitting a pull request, ensure that your changes pass all the tests and do not introduce any regressions. Here's how to test your changes:

1. **Set up your environment**:
    - Install all necessary dependencies from `requirements.txt`:
      ```bash
      pip install -r requirements.txt
      ```
    - Install any additional developer dependencies:
      ```bash
      pip install pytest pytest-cov
      ```

2. **Run the tests**:
    - Execute the test suite using `pytest`:
      ```bash
      pytest
      ```
    - Verify that all tests pass without errors.

3. **Check code coverage**:
    - Run tests with coverage reporting:
      ```bash
      pytest --cov=pycellga
      ```
    - Ensure that your changes do not significantly reduce the code coverage. A minimum of 90% coverage is recommended.

4. **Add new tests (if applicable)**:
    - If your changes introduce new features or modify existing functionality, write additional test cases to cover these changes.
    - Place your tests in the appropriate subdirectory within the `tests` folder, following the naming convention `test_<feature_name>.py`.

5. **Review testing guidelines**:
    - Ensure your tests follow the existing style and structure used in the project. Use descriptive function names and provide comments where necessary to clarify the test's purpose.

### Documentation

Update documentation as necessary to reflect your changes. This includes updating the README.md file and any relevant docstrings in the code.

## Code of Conduct

Please read and adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) for contributing to this project.

## Thank You!

Thank you for your contributions! We appreciate your effort and look forward to collaborating with you.

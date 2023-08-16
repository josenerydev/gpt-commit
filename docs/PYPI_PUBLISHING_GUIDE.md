## PyPI Publishing Guide

### Prerequisites:

- Ensure you have an account on [PyPI](https://pypi.org/).
- Install `setuptools`, `wheel`, and `twine` if you haven't already:
  ```bash
  pip install setuptools wheel twine
  ```

### Steps to Publish:

1. **Package Preparation**:
    - Update your `setup.py` file with the most recent information about your project.
    - Be sure to increment the package version if you're pushing an update.

2. **Build the Package**:
    ```bash
    python setup.py sdist bdist_wheel
    ```

    This will create a source distribution (sdist) and a built distribution (wheel) in the `dist/` directory.

3. **Clear the `dist/` Directory**:
    Before building new packages, it's a good practice to clear out the old ones to prevent conflicts:

    On Linux/Mac:
    ```bash
    rm dist/*
    ```

    On Windows:
    ```powershell
    del dist\*
    ```

    Then, repeat step 2 to rebuild the package.

4. **Publish the Package**:
    ```bash
    twine upload dist/*
    ```

    This command will upload your package to PyPI. If it's the first time you're uploading a package, it'll be created on PyPI. If it's an update, the new version of the package will replace the old one.

### Common Troubleshooting:

- **"File already exists"**:
  If you get an error stating that the file already exists, you're probably trying to upload a package version that's already on PyPI. Make sure to increment your package version in `setup.py` and rebuild the package before trying again.
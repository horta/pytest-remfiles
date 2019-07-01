# pytest-remfiles

[![Travis](https://img.shields.io/travis/com/horta/pytest-remfiles.svg?style=flat-square&label=linux%20%2F%20macos%20build)](https://travis-ci.com/horta/pytest-remfiles)

Pytest plugin to create a temporary directory with remote files.

## Install

```bash
pip install pytest-remfiles
```

## Usage

```python
import os

import pytest

@pytest.mark.remfiles(
    ["http://rest.s3for.me/limix/plink.fam", "http://rest.s3for.me/limix/plink.bed"]
)
def test_2files(remfiles):
    remfiles.chdir()
    assert set(["plink.fam", "plink.bed"]) == set(os.listdir())
```

## Authors

* [Danilo Horta](https://github.com/horta)

## License

This project is licensed under the [MIT License](https://raw.githubusercontent.com/horta/pytest-remfiles/master/LICENSE.md).

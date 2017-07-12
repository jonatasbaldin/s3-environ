# s3-environ
[![CircleCI](https://circleci.com/gh/jonatasbaldin/s3-environ.svg?style=svg)](https://circleci.com/gh/jonatasbaldin/s3-environ)
[![Coverage Status](https://coveralls.io/repos/github/jonatasbaldin/s3-environ/badge.svg)](https://coveralls.io/github/jonatasbaldin/s3-environ)

Load environment variables from a AWS S3 file! This initial version supports only JSON files.

## Installation and Usage
```
pip install s3-environ
```

```python
from s3_environ import S3Environ
S3Environ(bucket='your-bucket', key='your-file.json')
```

## Testing
This package is tested in Python 2.7 and Python 3.6. You can test using [tox](https://tox.readthedocs.io/en/latest/).  
Make sure you have Tox installed:
```
pip install --user tox
```
Run the tests:
```
tox
```

## Contributing
Open an issue or PR and let's discuss it :D

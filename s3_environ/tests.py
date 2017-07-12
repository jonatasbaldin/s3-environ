from __future__ import print_function
from __future__ import unicode_literals

import pytest
import boto3
import os
import json
from moto import mock_s3
from s3_environ import S3Environ


class TestS3Environ(object):
    FILE = {
        'string_value': 'string here',
        'number_value': 1,
        'boolean_value': True,
        'array_value': ['zero', 1, 2],
        'dict_value': {
            'key': 'value',
        }
    }

    @mock_s3
    def test_get_s3_object(self):
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='test')
        conn.Object('test', 'vars.json').put(Body=json.dumps(self.FILE))

        s3_environ = S3Environ(bucket='test', key='vars.json')
        output = s3_environ.get_s3_object()
        assert output == self.FILE

    @mock_s3
    def test_set_variables(self):
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='test')
        conn.Object('test', 'vars.json').put(Body=json.dumps(self.FILE))

        S3Environ(bucket='test', key='vars.json')

        for key, value in self.FILE.items():
            assert os.environ.get(key) == str(value)

    @mock_s3
    def test_get_s3_object_error(self):
        with pytest.raises(Exception):
            S3Environ(bucket='test', key='vars.json')

    @mock_s3
    def test_get_s3_object_decode_error(self):
        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='test')
        conn.Object('test', 'vars.json').put(Body='simple_string')

        with pytest.raises(ValueError):
            S3Environ(bucket='test', key='vars.json')

import os
import boto3
import json


class S3Environ(object):
    """
    Sets environment variables from an AWS S3 JSON file.
    """

    def __init__(self, bucket, key):
        """
        Instanciate the object with its bucket name and key.

        Arguments:
        <str> bucket - An S3 bucket.
        <key> key - An S3 object's key.

        Returns nothing.
        """

        self.bucket = bucket
        self.key = key
        self.set_variables()

    def get_s3_object(self):
        """
        Gets the file from AWS S3.

        Returns a dictionary with the file's content.
        """

        s3 = boto3.resource('s3')

        try:
            obj = s3.Object(
                bucket_name=self.bucket,
                key=self.key,

            ).get()['Body'].read()
        except Exception:
            print('Could not get file from AWS S3.')
            raise

        try:
            obj_content = json.loads(obj.decode('utf-8'))
        except ValueError:
            print('The file is not JSON valid.')
            raise

        return obj_content

    def set_variables(self):
        """
        Sets all environment variables defined in the file.
        """

        vars = self.get_s3_object()

        for key, value in vars.items():
            os.environ.setdefault(key, str(value))

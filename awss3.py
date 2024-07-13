'''This module can upload files from local system to existing S3 bucket.'''

import boto3

def s3upload(bucket, file):
    '''This function takes 2 arguments, i.e.,
    bucket - Name of the existing bucket to upload files,
    file - Name of the file in the local system (The file should be present at the location of this module).'''
    AWS_S3_BUCKET_NAME = bucket

    LOCAL_FILE = file
    NAME_FOR_S3 = LOCAL_FILE

    def upload():
        print('in main method')

        s3_client = boto3.client(service_name='s3')

        response = s3_client.upload_file(LOCAL_FILE, AWS_S3_BUCKET_NAME, NAME_FOR_S3)

        print(f'upload_log_to_aws response: {response}')

    if __name__ == '__main__':
        upload()
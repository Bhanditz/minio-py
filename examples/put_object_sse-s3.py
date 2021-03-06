# -*- coding: utf-8 -*-
# Minio Python Library for Amazon S3 Compatible Cloud Storage, (C) 2018 Minio, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Note: YOUR-ACCESSKEYID, YOUR-SECRETACCESSKEY and my-bucketname are
# dummy values, please replace them with original values.

from io import BytesIO
from minio.api import Minio
from minio.sse import SSE_S3


AWSAccessKeyId = 'YOUR-ACCESSKEYID'
AWSSecretKey = 'YOUR-SECRETACCESSKEY'

STORAGE_ENDPOINT = 's3.amazonaws.com'
STORAGE_BUCKET = 'test-encryption-bucket'


def main():
   
    minio = Minio(STORAGE_ENDPOINT, access_key=AWSAccessKeyId, secret_key=AWSSecretKey)

    content = BytesIO(b'Hello again')
    
    #Create an SSE_S3 object
    sse_s3_obj = SSE_S3()

    # Put object with from SSE_S3 object which encrypt object in S3 with provided key
    minio.put_object(STORAGE_BUCKET, 'test_crypt.txt', content, content.getbuffer().nbytes, sse=sse_s3_obj)

    # Get decrypted object with same headers
    obj = minio.get_object(STORAGE_BUCKET, 'test_crypt.txt')
   
    print(obj.read())

if __name__ == '__main__':
    main()

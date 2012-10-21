"""

todo: 
  1. abstract list buckets
  2. abstract list contents of bucket
  3. abstract copy to bucket
  4. abstract delete bucket
  5. abstract delete from bucket 

"""

import os
import logging
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
from boto.s3.connection import OrdinaryCallingFormat
from boto.s3.prefix import Prefix
import ConfigParser

#logging
logging.basicConfig(filename="boto.log", level=logging.DEBUG)

# get config
config = ConfigParser.RawConfigParser()
config.read(os.path.join('config.cfg'))
S3_key_id = config.get('S3Connection', 'aws_access_key_id')
S3_secret_key = config.get('S3Connection','aws_secret_access_key')
S3_host = config.get('S3Connection','host')
S3_port = config.getint('S3Connection', 'port')
S3_is_secure = config.get('S3Connection','is_secure')
S3_calling_format = config.get('S3Connection', 'calling_format')

conn = S3Connection(
    aws_access_key_id=S3_key_id,
    aws_secret_access_key=S3_secret_key,
    host=S3_host,
    port=S3_port,
    is_secure=S3_is_secure,
    calling_format=S3_calling_format
)


print "--connection--",conn

print "These are yo buckets:"

rs = conn.get_all_buckets()
for b in rs:
  print b.name

#print "--buckets--",conn.get_all_buckets()

#print "I GUNNA MAKE YOUR BUCKET NOW BRO!"

#bucket = conn.create_bucket('stevelikesbuckets')
#print "I MADE YO BUCKET BRO!"
bucket = conn.get_bucket('stevelikesbuckets')

k = Key(bucket)
k.key = 'johnisreallyconfused'
k.set_contents_from_string('This is a test of S3')

# Get the object back
b = conn.get_bucket('stevelikesbuckets')
k = Key(b)
k.key = 'johnisreallyconfused'
k.get_contents_as_string()



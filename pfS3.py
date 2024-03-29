#!/usr/bin/env python

"""

todo: 
  1. list buckets
  2. list contents of bucket
  3. copy to bucket
  4. delete bucket
  5. delete from bucket 

"""

import os
import logging
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
from boto.s3.connection import OrdinaryCallingFormat
from boto.s3.prefix import Prefix
import ConfigParser
import argparse
import time

# setup argument parsing
def _make_arg_parser():
  parser = argparse.ArgumentParser(description="usage: pfS3 -b 'bucket' -c '/path/to/data'")
  parser.add_argument("-b", "--bucket", help="name of the bucket")
  parser.add_argument("-n", "--new", help="create a new bucket")
  parser.add_argument("-D", "--destroy", help="delete a bucket")
  parser.add_argument("-c", "--copy", help="data to be copied")
  parser.add_argument("-l", "--ls", help="list buckets, or contents of bucket if used with -b")
  parser.add_argument("-L", "--log", help="set logging directory")
  return parser

# setup logging
def _configure_logging():
  log = os.path.join('pfS3_Logs')
  if not os.path.isdir(log):
    os.mkdir(log)
  log_file = os.path.join(log, 'pfS3' + time.strftime('%y_%m_%d') + '.log')
  logging.basicConfig(filename=log_file, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

# get config
def _config():
  config = ConfigParser.RawConfigParser()
  config.read(os.path.join('config.cfg'))
  S3_key_id = config.get('S3Connection', 'aws_access_key_id')
  S3_secret_key = config.get('S3Connection','aws_secret_access_key')
  S3_host = config.get('S3Connection','host')
  S3_port = config.getint('S3Connection', 'port')
  S3_is_secure = config.getboolean('S3Connection','is_secure')
  S3_calling_format = config.get('S3Connection', 'calling_format')

# connect!
def _connect(): # NEED TO FINISH -- GETTING AN OBJECT TYPE ERROR. FIGURE OUT WHICH CONFIG VALUE IS CAUSING THE PROBLEM
  conn = S3Connection(
      aws_access_key_id=S3_key_id,
      aws_secret_access_key=S3_secret_key,
      host=S3_host,
      port=S3_port,
      is_secure=S3_is_secure,
      calling_format=S3_calling_format
  )
  print "--connection--",conn

def _list_buckets(): # NEED TO FINISH
  print "These are yo buckets:"
  buckets = conn.get_all_buckets()
  for bucket in buckets:
    print bucket.name

def _create_bucket(bucket):
  bucket = conn.get_bucket(bucket)

def _save_to_bucket(bucket, copy): # NEED TO FINISH
  k = Key(bucket_name)
  k.key = 'data_to_be_saved'
  k.set_contents_from_string('data_to_be_saved') # CHANGE THIS -- LOOK AT API DOCUMENTATION AGAIN

def _list_bucket_objects(bucket): # NEED TO FINISH
  b = conn.get_bucket(bucket)
  k = Key(bucket)
  k.key = 'johnisreallyconfused'
  k.get_contents_as_string()

def _destroy(bucket): # NEED TO FINISH
  print "this is where i delete a bucket"

  
if __name__ == '__main__':
  arg_parser = _make_arg_parser()
  args = arg_parser.parse_args()
  bucket = args.bucket
  destroy = args.destroy
  copy = args.copy
  log = args.log
  newBucket = args.new

  _configure_logging()
  log = logging.getLogger()

  #create bucket
  if bucket & newBucket:
  	_create_bucket(bucket)
  #list buckets
  if ls:
  	_list_buckets()
  #list bucket contents
  if ls and bucket:
  	_list_bucket_objects(bucket)
  #copy data to bucket
  if bucket and copy:
  	_save_to_bucket(bucket, copy)
  #delete bucket
  if bucket and destroy:
  	_destroy(bucket)
  	
  rc = 0

  sys.exit(rc)

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
from boto.exception import S3CreateError
from boto.s3.connection import S3Connection
from boto.s3.key import Key
#import sys
#from boto.s3.connection import OrdinaryCallingFormat
#from boto.s3.prefix import Prefix
import ConfigParser
import argparse

# setup argument parsing
def _make_arg_parser()
  parser = argparse.ArgumentParser(description="usage: pfS3 -b 'bucket' -c '/path/to/data'")
  parser.add_argument("-b", "--bucket", help="name of the bucket")
  parser.add_argument("-D", "--delete", help="delete a bucket")
  parser.add_argument("-c", "--copy", help="data to be copied")
  parser.add_argument("-l", "--list", help="list buckets, or contents of bucket if used with -b")
  parser.add_argument("-L", "--log", help="set logging directory")
  return parser

# setup logging
def _configure_logging():
  log_dir = os.path.join('pfS3_Logs')
  if not os.path.isfir(log_dir):
    os.mkdir(log_directory)
  log_file = os.path.join(log_dir + 'pfS3_Logs', 'pfS3' + time.strftime('%y_%m_%d') + '.log')
  logging.basicConfig(filename=log_file, format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)

def get_config():
	# get config
	config = ConfigParser.RawConfigParser()
	config.read(os.path.join('config.cfg'))
	return config
	
"""
S3_key_id = config.get('S3Connection', 'aws_access_key_id')
S3_secret_key = config.get('S3Connection','aws_secret_access_key')
S3_host = config.get('S3Connection','host')
S3_port = config.getint('S3Connection', 'port')
S3_is_secure = config.getboolean('S3Connection','is_secure')
S3_calling_format = config.get('S3Connection', 'calling_format')
"""

def connect(access_key, secret_key):
	# connect!
	conn = S3Connection(
		aws_access_key_id=access_key,
		aws_secret_access_key=secret_key,
		#host=S3_host,
		#port=S3_port,
		#is_secure=S3_is_secure,
		#calling_format=S3_calling_format
	)
	return conn

#print "--connection--",conn

#print "These are yo buckets:"

def list_buckets():
	rs = conn.get_all_buckets()
	for b in rs:
  		print b.name
	return rs

#print "--buckets--",conn.get_all_buckets()

#print "I GUNNA MAKE YOUR BUCKET NOW BRO!"

#bucket = conn.create_bucket('stevelikesbuckets')
#print "I MADE YO BUCKET BRO!"
#bucket = conn.get_bucket('stevelikesbuckets')

def create_bucket(name):
	bucket = None
	try:
		bucket = conn.create_bucket(name)
	except S3CreateError:
		print "Can't create bucket '", name, "'."
	return bucket

def save_to_bucket(bucket, key, value):
	k = Key(bucket)
	k.key = key
	ret = k.set_contents_from_string(value)
	return ret
	
def get_from_bucket(bucket, key):
	k = Key(bucket)
	k.key = key
	ret = k.get_contents_as_string()
	return ret

def list_bucket_contents(bucket):
	objects = bucket.list()
	return objects
	
def delete_bucket(bucket):
	pass

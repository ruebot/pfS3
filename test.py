#!/usr/bin/env python

import unittest
import pfS3
import ConfigParser
import boto

class TestCRUDFunctions(unittest.TestCase):
	
	def setUp(self):
		pass
	
	def test_get_config(self): 
		""" Test pfS3.get_config() function """
		self.configParser = pfS3.get_config()
		self.assertTrue(isinstance(configParser, ConfigParser.RawConfigParser))
	
	def test_connect(self):
		""" Test pfS3.connect() function """
		access_key = self.configParser.get('S3Connection', 'aws_access_key_id')
		secret_key = self.configParser.get('S3Connection', 'aws_secret_access_key')
		self.connection = pfS3.connect(access_key, secret_key)
		self.assertTrue(isinstance(self.connection, boto.s3.connection.S3Connection))

	def test_create_bucket(self):
		""" Test pfS3.create_bucket() function """
		self.bucket = pfS3.create_bucket(self.configParser.get('S3Connection', 'aws_access_key_id') + '_unitTestBucket')
		self.assertTrue(isinstance(self.bucket, boto.s3.bucket.Bucket))
	
	def test_list_buckets(self):
		""" Test pfS3.list_buckets() function """
		bucketlist = pfS3.list_buckets()
		self.assertTrue(isinstance(bucketlist, boto.resultset.ResultSet))
	
	def test_save_to_bucket(self):
		""" Tests pfS3.save_to_bucket() function """
		key = "CHANGEME"
		data = "ASDFJKL"
		saved_data = pfS3.save_to_bucket(key, data)
		self.assertTrue(False) # FIXME: Not sure how to test these results
	
	def test_get_from_bucket(self):
		""" Tests pfS3.get_from_bucket() function """
		key = "CHANGEME"
		returned_data = pfS3.get_from_bucket(self.bucket, key)
		self.assertTrue(isinstance(returned_data, str)) # FIXME: presumes string, what about other data?
		self.assertEquals(returned_data, "ASDFJKL")
		
	def test_list_bucket_contents(self):
		""" Test pfS3.list_bucket_contents() function """
		contents = pfS3.list_bucket_contents(self.bucket)
		for obj in contents:
			self.assertTrue(False) # FIXME: actually check for something in the contents
	
	def test_delete_bucket(self):
		""" Teset pfS3.delete_bucket() function """
		deleted = pfS3.delete_bucket(self.bucket)
		self.assertTrue(False) # FIXME	
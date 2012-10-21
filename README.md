# pfS3 (PERMAFROST S3 Client)

note: not ready

### Description

pfS3 serves as a client for the PERMAFROST S3 API which is based on OpenStack Swift.

This client allows the user to:

  1. create a bucket
  2. list a user's buckets
  3. list the contents of a given bucket
  4. copy local data to a bucket
  5. delete a bucket

### Installation

    cd pfS3
    sudo python setup.py install

### Usage

Create a bucket:

    pfS3 -n 'bucket'

List a user's bucket:

    pfS3 -l
    
List the contents of a bucket:    
    
    pfS3 -b 'bucket' -l

Copy local data to a bucket:

    pfS3 -b 'bucket' -d '/path/to/local/data/'

Delete a bucket:

    pfS3 -D 'bucket'

### Test suite

    python setup.py test

### Development

1. [Fork the repository](https://help.github.com/articles/fork-a-repo)
2. Do something awesome!
3. [Submit a pull request](https://help.github.com/articles/creating-a-pull-request) explaining what you've done.

### License

GPLv3



# Apache Factory

Instantiate, configure Apache HTTPD and distribute configuration.

# Compatibility

Tool is developed for and tested with CentOS 7.

# Hot to use

There are 2 ways to initialize:
    
    - Running Apache Factory as user for which we want to build Apache HTTPD.
    - Running as Super User by providing name of account to be created. 
    Account will be created and Apache Factory started for that user.
    
Distributing configuration:

    - TBD.

## Apache Factory

```
$ cd ~
$ mkdir Apache-Factory
$ cd  Apache-Factory
$ git clone https://github.com/milos85vasic/Apache-Factory.git
$ python factory.py
```

Apache will be installed for the current user at:

```
~/Apache2/
```

Script will start wizard that will for you download and build Apache HTTPD.

## Account add with Apache Factory execution

```
$ su
$ mkdir Apache-Factory
$ cd Apache-Factory
$ git clone https://github.com/milos85vasic/Apache-Factory.git
$ python add_account.py YOUR_ACCOUNT_NAME
``` 

Script will start wizard that will for you create account, download and build Apache HTTPD.

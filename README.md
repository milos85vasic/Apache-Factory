# Apache Factory

Instantiate, configure Apache HTTPD and distribute configuration.

# Compatibility

Tool is developed for and tested with CentOS 7.

# Specifications

- Apache Factory builds Apache HTTPD v2.4.29.
- Default compression algorithm is Brotli v1.0.4.
- PHP v7.2.4

# Hot to use
    
    - Run as Super User by providing name of account to be created. 
    Account will be created and Apache Factory started for that user.
    
Distributing configuration:

    - TBD.

## Account add with Apache Factory execution

```
$ su
$ mkdir Apache-Factory
$ cd Apache-Factory
$ git clone https://github.com/milos85vasic/Apache-Factory.git
$ python add_account.py YOUR_ACCOUNT_NAME
``` 

Script will start wizard that will for you create account, download and build Apache HTTPD.

Apache will be installed for the current user at:

```
~/Apache2/
```

After whole process is completed you will be able to access landing page.

## Configuration parameters:

- Server admin:
```
$ ... --server_admin=somebody@example.com
```

- Passing configuration for services

To tell Apache Factory which repositories to clone and configure on Apache:
```
$ ... --services=./services.json
```

where services.json should look like this:
```
[
  {
    "url": "something.example.com",
    "repository": "https://github.com/user/some_repo.git"
  },
  {
    "url": "example.com",
    "repository": "other_git_repo ..."
  }
]
```
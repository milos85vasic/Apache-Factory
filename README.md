# Apache Factory

Instantiate, configure Apache HTTPD and distribute configuration.

# Compatibility

Tool is developed for and tested with CentOS 7.

# Specifications

- Apache Factory builds Apache HTTPD v2.4.29.
- Default compression algorithm is Brotli v1.0.4.
- PHP v7.2.4

# Web setup:

Execute command:
```
$ curl https://raw.githubusercontent.com/milos85vasic/Apache-Factory-Toolkit/master/websetup.py > websetup.py; \
python websetup.py Apache-Factory  
```

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
$ git clone --recurse-submodules https://github.com/milos85vasic/Apache-Factory.git ./
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

To tell Apache Factory which repositories to clone and configure on Apache make sure services.json is available in Apache Factory root.

Where services.json should look like this:
```
{
  "services": [
    {
      "url": "www.example.com",
      "urls": [
        "something.example.com",
        "something2.example.com"
      ],
      "repository": "https://github.com/user/some_repo.git"
    },
    {
      "url": "xxx.com",
      "repository": "other_git_repo ..."
    }
  ],
  "features": [
    "mysql"
  ]
}
```

If you wish to password protect directory you can do this like in the following example:
```
{
  "services": [
    {
      "url": "www.example.com",
      "urls": [
        "www2.example.com",
        "www3.example.com"
      ],
      "repository": "https://github.com/user/some_repo.git"
    },
    {
      "url": "www.example2.com",
      "repository": "https://github.com/user/some_repo.git"
    }
  ],
  "password_protect": [
    {
      "user": "pp1",
      "password": "pp1pass",
      "directories": [
        {
          "service": "www.example.com",
          "path": "images/social"
        },
        {
          "service": "www.example.com",
          "path": "fonts"
        }
      ]
    },
    {
      "user": "pp2",
      "password": "pp2pass",
      "directories": [
        {
          "service": "www.example2.com",
          "path": "images/social"
        }
      ]
    }
  ]
}
```

We created 2 services: www.example.com and www.example2.com. We also created 2 users for password 
protecting directories: pp1 and pp2. Each has a list of directories (and) services defined to password protect.

Overriding http.conf default configuration:
```
{
  ...
  
  "configuration": {
    "explicit_port_number": 80,
    "configuration_repository": "https://github.com/milos85vasic/Apache-Factory-Config-Default-Master-Proxy.git"
  }
}
```

We set new repository with configuration and explicit port value to be used.

To connect services with main proxy (parent HTTPD instance):
```
{
  "services": [
    {
      "main_proxy": "some_account",
      "url": "www.example2.com",
      "repository": "https://github.com/user/some_repo.git"
    },
    {
      "main_proxy": "some_account",
      "url": "www.example2.com",
      "repository": "https://github.com/user/some_repo.git"
    }
  ]
}
```

Where some_account represents account under which we initialized parent (main) proxy HTTPD instance.

- Overriding PHP version to 5:
```
{
  "services": [
    {
      ...
    }
  ],
  "features": [
    "php_5"
  ]
}
```
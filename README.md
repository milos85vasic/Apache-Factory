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
$ git clone https://github.com/milos85vasic/Apache-Factory.git ./
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
      "url": "www.fundamental-kotlin.local",
      "urls": [
        "www2.fundamental-kotlin.local",
        "www3.fundamental-kotlin.local"
      ],
      "repository": "https://github.com/milos85vasic/Fundamental-Kotlin-Website-Statics.git"
    },
    {
      "url": "www.fundamental-kotlin2.local",
      "repository": "https://github.com/milos85vasic/Fundamental-Kotlin-Website-Statics.git"
    }
  ],
  "password_protect": [
    {
      "user": "pp1",
      "password": "pp1pass",
      "directories": [
        {
          "service": "www.fundamental-kotlin.local",
          "path": "images/social"
        },
        {
          "service": "www.fundamental-kotlin.local",
          "path": "fonts"
        }
      ]
    },
    {
      "user": "pp2",
      "password": "pp2pass",
      "directories": [
        {
          "service": "www.fundamental-kotlin2.local",
          "path": "images/social"
        }
      ]
    }
  ]
}
```

We created 2 services: www.fundamental-kotlin.local and www.fundamental-kotlin2.local. We also created 2 users for password 
protecting directories: pp1 and pp2. Each has list of directories (and) services defined to password protect.
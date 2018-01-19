#backup-rancid
**Rancid devices list and configuration backup:** 
```

 1. Script extracts configured folders structure from /etc/rancid/rancid.conf

 2. For each folder makes backup of:
    - router.db file (devices list backuped by rancid)
    - configs/ folder (contains config files for all devices from router.db file)

 3. Saves backup as tar.gz archive to /backup-rancid/ folder.
    Backup file name has format: YYYYMMDD-HHMMSS.tar.gz (date and time of backup creation).

```


```bash
curl http://127.0.0.1
ls /

if [ 1 eq 1 ]; then echo 1; fi
ping www.google.com

echo $HOME

cp mv
rm -r /tmp/111

printf '11\n'
```
```bash
git submodule update --init --recursive
```
```bash
echo "cookbook_path            [\"$SRC/chef/cookbooks", "$SRC/chef/external-cookbooks\"]" >> ~/.chef/knife.rb
```



**No cookbook on server, skip version compare.**
```
<<< Cookbook: simple_iptables  >>>
  !!!! COOKBOOK ... no cookbook simple_iptables on ChefServer, skipping json check...
```

# Server version matches all envs for yola_apache2 cookbook.
```
<<< Cookbook: yola_apache2  >>>
    All json files match server version... ( 0.4.13 )
```

# One of envs does not contain apt cookbook. All other envs have cookbook & match server version.
```
<<< Cookbook: apt  >>>
  !!!! COOKBOOK ... no cookbook apt in file production-inet.json
    All other json files match server version... ( 2.7.0 )
```

# One of envs has not-matching version. All other envs versions match server version.
```
<<< Cookbook: apt  >>>
  !!!! VERSION ... file  production-usa-east.json apt = ( 2.6.0 ), but ChefServer apt = ( 2.7.0 )
    All other json files match server version... ( 2.7.0 )
```

# Combination of cases
```
<<< Cookbook: apt  >>>
  !!!! COOKBOOK ... no cookbook apt in file production-inet.json
  !!!! VERSION ... file  production-usa-east.json apt = ( 2.6.0 ), but ChefServer apt = ( 2.7.0 )
    All other json files match server version... ( 2.7.0 )
```

# All envs versions does not match server version.
```
<<< Cookbook: chef-client  >>>
  !!!! VERSION ... file  production-inet.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  integration-usa-east.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  production-usa-east.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  ct.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  qa-inet.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  sf.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  production-vpc-us-east-1.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
  !!!! VERSION ... file  qa-vpc-us-east-1.json chef-client = ( 4.3.1 ), but ChefServer chef-client = ( 8.1.8 )
```

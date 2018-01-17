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

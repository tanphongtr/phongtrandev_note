Step 1
```
docker exec -it [mariadb_container_name] bash
```

Step 2
```
cat > /etc/mysql/mariadb.conf.d/99-binlog.cnf <<'EOF'
[mysqld]
server-id=6998090
log_bin=mysql-bin
log_error=mysql-bin.err
binlog_do_db=iptv
EOF
```

Step 3
```
docker restart [mariadb_container_name]
```

Step 4
Vào Master phpmyadmin Replica, tạo username/password

Step 5
Trên server Replica tạo username/password với READONLY

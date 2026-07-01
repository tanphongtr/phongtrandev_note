# Install

```
sudo apt install fail2ban
```

# Fail2ban config
```
vi /etc/fail2ban/jail.local
```

```
[DEFAULT]
ignoreip = 127.0.0.1/8 ::1 27.74.249.218
bantime  = 1h
findtime = 10m
maxretry = 5

# Ép toàn bộ hệ thống đọc log từ systemd journal và bỏ qua việc tìm file log vật lý
backend = systemd

[sshd]
enabled = true
port    = ssh

[nginx-gitlab]
enabled  = true
port     = http,https
filter   = nginx-gitlab
logpath  = /var/log/nginx/login.log

backend  = auto
# hoặc:
# backend = polling

maxretry = 10
findtime = 600
bantime  = 3600
```


```
root@01:/# fail2ban-client status nginx-gitlab
Status for the jail: nginx-gitlab
|- Filter
|  |- Currently failed: 1
|  |- Total failed:     9
|  `- File list:        /var/log/nginx/login.log
`- Actions
   |- Currently banned: 0
   |- Total banned:     0
   `- Banned IP list:
```

```dnf install -y epel-release```

```dnf install -y lsyncd```

```vi /etc/lsyncd.conf```

```
settings {
    logfile = "/var/log/lsyncd/lsyncd.log",
    statusFile = "/var/log/lsyncd/lsyncd.status",
    nodaemon = false,
}

sync {
    default.rsyncssh,
    source = "/file_upload",             -- Thư mục gốc trên Server 1
    host = "<IP_SERVER_2>",              -- IP của Server 2
    targetdir = "/file_upload",          -- Thư mục đích trên Server 2
    delay = 1,                           -- Thời gian trễ (giây) trước khi sync
    rsync = {
        archive = true,
        compress = true,
        verbose = true,
        update = true,   -- Chỉ update file mới hơn
        -- binary = "/usr/bin/rsync", -- Bỏ comment nếu đường dẫn rsync khác mặc định
    },
    ssh = {
        port = 22 -- Đổi port nếu Server 2 dùng port SSH khác
    }
}
```

```sudo apt update```

```sudo apt install -y lsyncd```

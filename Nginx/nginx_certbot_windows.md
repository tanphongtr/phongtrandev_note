# Self host, mở port, ssl với nginx, certbot, Windows

# Mở Port

Truy cập Admin của Router: 192.168.1.1 admin/123456789
Mở 2 Port:
```
80 -> 80 (port 80 của nginx)
443 -> 443 (port 443 của nginx cho ssl/https)
```

<img width="1505" alt="Pasted Graphic" src="https://github.com/tanphongtr/phongtrandev_note/assets/11567406/bda8f56e-76f3-49f2-af57-7cd70f6a4626">


# Cài nginx trên Windows
http://nginx.org/en/docs/windows.html
nginx for Windows

![Pasted Graphic 1](https://github.com/tanphongtr/phongtrandev_note/assets/11567406/6457aa43-7fa8-4627-a7f6-c8b3d8392379)


Folder conf chứa file cấu hình chính của nginx, trong Folder này tạo một Folder có tên sites-enabled để chứa các File config khác

Mở conf/nginx.conf thêm dòng: ```include “C:/Users/…/nginx/conf/sites-enabled/*.conf";```
<img width="1089" alt="Pasted Graphic 2" src="https://github.com/tanphongtr/phongtrandev_note/assets/11567406/595f728b-088b-4072-b4a8-071c15a054da">

# Cài certbot

https://certbot.eff.org/instructions?ws=other&os=windows
Certbot Instructions | Certbot (eff.org)

```https://github.com/certbot/certbot/releases/latest/download/certbot-beta-installer-win_amd64_signed.exe```

Theo hướng dẫn, sau khi cài đặt mở Terminal (CMD) với quyền Admin mới có thể chạy certbot

# Cấu hình trỏ domain, nginx và thêm ssl

Trỏ domain về server.

Mở file conf/nginx.conf, phần server, server_name, thêm tên domain cần add vào. Sau đó save và reload nginx, lúc này có thể truy cập vào domain để thấy nội dung trang mặc định nginx. Dùng Postman hoặc curl để xem nội dung phản hồi nếu domain yêu cầu phải có ssl.

Đăng ký ssl cho domain ```certbot certonly --webroot -w C:\Users\q\Downloads\nginx\html```

Tạo file ptn.phongtran.dev.conf trong nginx\conf\sites-enabled với nội dung
```
server {
  server_name ptn.phongtran.dev;

  location / {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_pass http://localhost:9000;
    proxy_read_timeout 600;
    proxy_connect_timeout 300;
    proxy_send_timeout 300;
  }

  listen 443 ssl; # managed by Certbot
  ssl_certificate "C:\Certbot\archive\ptn.phongtran.dev\fullchain1.pem"; # managed by Certbot
  ssl_certificate_key "C:\Certbot\archive\ptn.phongtran.dev\privkey1.pem"; # managed by Certbot
  #include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
  #ssl_dhparam /etc/letsencrypt/ssl-dhparams.pem; # managed by Certbot
}

server {
  if ($host = ptn.phongtran.dev) {
    return 301 https://$host$request_uri;
  } # managed by Certbot

  server_name ptn.phongtran.dev;
  listen 80;
  return 404; # managed by Certbot
}
```

Xoá server_name ptn.phongtran.dev ở nginx.conf, sau đó reload lại nginx

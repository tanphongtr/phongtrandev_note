### Installing NGINX Open Source
https://docs.nginx.com/nginx/admin-guide/installing-nginx/installing-nginx-open-source/

### Using Free Let’s Encrypt SSL/TLS Certificates with NGINX
https://www.nginx.com/blog/using-free-ssltls-certificates-from-lets-encrypt-with-nginx/


### Install Nginx

https://docs.rockylinux.org/guides/web/nginx-mainline/


### Reverse Proxy

```
# yourwebsite.com.conf
server {
    server_name yourwebsite.com;

    listen 80;
    listen [::]:80;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
    }
}

```

### Install Let's Encrypt

https://docs.rockylinux.org/guides/security/generating_ssl_keys_lets_encrypt/


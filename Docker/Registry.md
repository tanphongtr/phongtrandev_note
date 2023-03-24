### Registry

https://docs.docker.com/registry/

### Hướng dẫn từ ChatGPT

Để tạo một Docker Registry (trong đó bạn có thể lưu trữ và chia sẻ các image Docker của mình), bạn có thể làm theo các bước sau:

1. Cài đặt Docker trên máy chủ của bạn. Bạn có thể tìm hướng dẫn cài đặt Docker trên trang web Docker tại địa chỉ https://docs.docker.com/get-docker/.

2. Tạo một container Docker Registry bằng cách sử dụng lệnh sau trên terminal:
```
docker run -d -p 5000:5000 --restart=always --name registry registry:2
```

Lệnh này sẽ tạo một container Docker Registry phiên bản 2 (registry:2) trên cổng 5000 trên máy chủ của bạn.

3. Để kiểm tra xem container Registry đã chạy thành công hay chưa, bạn có thể sử dụng lệnh sau:
```
docker ps
```

Lệnh này sẽ liệt kê tất cả các container đang chạy trên máy của bạn. Bạn nên thấy một container có tên "registry" đang chạy.

4. Để đăng nhập vào container Registry, sử dụng lệnh sau:

```
docker login localhost:5000
```

Lưu ý rằng bạn phải đăng nhập với tên người dùng và mật khẩu của bạn để truy cập vào Registry.

5. Để tải lên một image Docker lên Registry của bạn, đổi tên image thành định dạng sau:
```
localhost:5000/<tên image>
```

Ví dụ, để tải lên image "ubuntu:latest", bạn phải đổi tên image thành "localhost:5000/ubuntu:latest".

6. Để tải lên image lên Registry, sử dụng lệnh sau:

```
docker push localhost:5000/<tên image>
```

Ví dụ, để tải lên image "ubuntu:latest", bạn phải sử dụng lệnh sau:

```
docker push localhost:5000/ubuntu:latest
```
## Registry list image
```http://localhost:5000/v2/_catalog```

## Push image to Registry with Docker Compose

VD: docker-compose.yml có 3 service: app, database, redis

1. Build Image
```bash
docker compose build
```


2. Push 1 service app
```bash
docker compose push app
```

Lưu ý:
```yml
version: '3'

services:
  app:
    image: localhost:5000/${PREFIX}_${APP_CONTAINER_NAME}:latest
```


## Authentication Registry
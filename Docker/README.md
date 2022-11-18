# Docker
> https://www.docker.com/

# Portainer
> https://docs.portainer.io/start/install/server/docker/linux  

## Deployment
Đầu tiên, tạo volume mà Portainer Server sẽ sử dụng để lưu trữ data của nó:
```bash
docker volume create portainer_data
```

Sau đó, download và cài đặt Portainer Server bản mới nhất:
```bash
docker run -d -p 9000:9000 --name portainer --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer-ce:latest
```

Sau khi hoàn tất, truy cập http://localhost:9000 để vào portainer

# Docker CLI
> https://docs.docker.com/engine/reference/commandline/cli/

```bash
# Build and Deploy
docker compose -f <docker-compose-file.yml> up -d --build

# Copy a local file into container
docker cp ./some_file CONTAINER:/work

# Copy files from container to local path
docker cp CONTAINER:/var/logs/ /tmp/app_logs

# List containers
docker ps

CONTAINER ID   IMAGE                                     COMMAND                  CREATED        STATUS        PORTS                                        NAMES
24cf12524d33   91d39187d206                              "python manage.py ru…"   23 hours ago   Up 23 hours   0.0.0.0:8540->8000/tcp                       app

docker ps --size

CONTAINER ID   IMAGE                                     COMMAND                  CREATED        STATUS        PORTS                                        NAMES                                    SIZE
24cf12524d33   91d39187d206                              "python manage.py ru…"   23 hours ago   Up 23 hours   0.0.0.0:8540->8000/tcp                       app                                      0B (virtual 201MB)




```

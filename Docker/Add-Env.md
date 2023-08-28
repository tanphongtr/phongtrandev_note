# Agent

Cài đặt Portainer Agent trên docker host muốn add vào. (Máy nguồn A)

```
docker run -d -p 9001:9001 --name portainer_agent --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker/volumes:/var/lib/docker/volumes portainer/agent:latest
```

Truy cập Portainer config như hình (Máy client B)
<img width="1506" alt="image" src="https://github.com/tanphongtr/phongtrandev_note/assets/11567406/2cefc379-915b-40d6-976b-7728fa1e3454">

Chỉ 1 client connect tới 1 agent

# API

Official: https://docs.docker.com/config/daemon/remote-access/

https://gist.github.com/tanphongtr/120b4a8ccb9f106d92db22725938aefe

Enable TCP port 2375 for external connection to Docker
------------------------------------------------------

See this [issue](https://github.com/moby/moby/issues/25471).  
Docker best practise to [Control and configure Docker with systemd](https://docs.docker.com/engine/admin/systemd/#/custom-docker-daemon-options).  

1. Create `daemon.json` file in `/etc/docker`:

        {"hosts": ["tcp://0.0.0.0:2375", "unix:///var/run/docker.sock"]}

2. Add `/etc/systemd/system/docker.service.d/override.conf`

        [Service]
        ExecStart=
        ExecStart=/usr/bin/dockerd


3. Reload the systemd daemon:

        systemctl daemon-reload

4. Restart docker:

        systemctl restart docker.service


# Protect the Docker daemon socket
https://docs.docker.com/engine/security/protect-access/

```
docker context create \
    --docker host=ssh://docker-user@host1.example.com \
    --description="Remote engine" \
    my-remote-engine

my-remote-engine
Successfully created context "my-remote-engine"

docker context ls

docker context use my-remote-engine

docker ps
```

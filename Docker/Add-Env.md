

Cài đặt Docker Agent
```docker run -d -p 9001:9001 --name portainer_agent --restart=always -v /var/run/docker.sock:/var/run/docker.sock -v /var/lib/docker/volumes:/var/lib/docker/volumes portainer/agent:latest```


<img width="1506" alt="image" src="https://github.com/tanphongtr/phongtrandev_note/assets/11567406/2cefc379-915b-40d6-976b-7728fa1e3454">

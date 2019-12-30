# Docker Commands

**docker pull** download image from docker community to local repositon

```console
D:\python>docker pull ubuntu

Using default tag: latest
latest: Pulling from library/ubuntu
2746a4a261c9: Pull complete
4c1d20cdee96: Pull complete
0d3160e1d0de: Pull complete
c8e37668deea: Pull complete
Digest: sha256:250cc6f3f3ffc5cdaa9d8f4946ac79821aafb4d3afc93928f0de9336eba21aa4
Status: Downloaded newer image for ubuntu:latest
docker.io/library/ubuntu:latest
```

**docker images** list all docker *images* 
```console
D:\python>docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
mylab               latest              a237101b85cf        8 hours ago         642MB
ubuntu              latest              549b9b86cb8d        11 days ago         64.2MB
centos              latest              0f3e07c0138f        2 months ago        220MB
```


**docker commit** commit the container to the repository and you can **tag** a new name for your own

**docker ps -la** list all docker *containers*

**docker run [container:version]** create a container from an image
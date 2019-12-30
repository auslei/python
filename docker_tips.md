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

**docker ps -a** list all docker *containers*, use the -l flag for latest
```console
D:\python>docker ps -a
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS                      PORTS               NAMES
50fbe60b87ba        ubuntu              "/bin/bash"              25 seconds ago      Exited (0) 23 seconds ago                       elastic_ramanujan
c8d1f53add1a        mylab               "/bin/bash"              52 seconds ago      Exited (0) 50 seconds ago                       confident_lichterman
956560d45f0d        mylab               "/bin/bash"              8 hours ago         Exited (0) 8 hours ago                          my_jupyter_lab
1ba5087f3522        mylab               "-v d:/python /home/…"   8 hours ago         Created                                         quizzical_jepsen
5d9ef060b583        0f3e07c0138f        "/bin/bash"              8 hours ago         Exited (0) 8 hours ago                          happy_spence
92941f6aa025        0f3e07c0138f        "-ti"                    8 hours ago         Created                                         funny_curran
6d83bd9fc0e5        centos              "/bin/bash"              9 hours ago         Exited (0) 8 hours ago                          my_lab
```

**docker run [container:version]** create a container from an image
```console
D:\python>docker run ubuntu:latest

D:\python>docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                     PORTS               NAMES
b1d48aa709c3        ubuntu:latest       "/bin/bash"         8 seconds ago       Exited (0) 6 seconds ago                       happy_taussig
```

**docker rename [container] [new_name]** rename the name of a container
```console
D:\python>docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS               NAMES
956560d45f0d        mylab               "/bin/bash"         8 hours ago         Exited (0) 8 hours ago                       infallible_brahmagupta

D:\python>docker rename infallible_brahmagupta my_jupyter_lab

D:\python>docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS               NAMES
956560d45f0d        mylab               "/bin/bash"         8 hours ago         Exited (0) 8 hours ago                       my_jupyter_lab
```

**docker container prune** remove all stopped containers
```console
D:\python>docker container prune
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N] y
Deleted Containers:
b1d48aa709c39b8c2a5ab1b0dddc3d955ff548dd5ff99a62d18a6659694a4ec9
50fbe60b87baece1ad29210a4d2a1a15129ca90860c11b869cb314176dda2fb4
c8d1f53add1aacaf1846346a192aa80f2d97af8fed7256996aa71d4dcf7ccae9
956560d45f0da6abed916f2d5c99b1014f1af6f7cda1d604f61b7e62613e0fec
1ba5087f35223cbc1567963a0afe1cb1fa4bbe3f8395aff05967f65a676df12f
5d9ef060b583cd8548b149ba5a4bf08b3e1e26af3725c6eff2cc67ab9275fa96
92941f6aa0255ad8a7c5fbe8bd774b89a120fd04de46e26c9b07b4e1c5786f06
6d83bd9fc0e5707d680e22c501bf222ec26bf57079d9bb440e68beaa4769e719

Total reclaimed space: 422MB

D:\python>docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
```
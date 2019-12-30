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

**docker ps -a** list all docker *containers*
```console
D:\python>docker ps --help

Usage:  docker ps [OPTIONS]

List containers

Options:
  -a, --all             Show all containers (default shows just running)
  -f, --filter filter   Filter output based on conditions provided
      --format string   Pretty-print containers using a Go template
  -n, --last int        Show n last created containers (includes all
                        states) (default -1)
  -l, --latest          Show the latest created container (includes all
                        states)
      --no-trunc        Don't truncate output
  -q, --quiet           Only display numeric IDs
  -s, --size            Display total file sizes

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




**docker rename [container] [new_name]** rename the name of a container
```console
D:\python>docker ps -la
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS               NAMES
956560d45f0d        mylab               "/bin/bash"         8 hours ago         Exited (0) 8 hours ago                       infallible_brahmagupta

D:\python>docker rename infallible_brahmagupta my_jupyter_lab

D:\python>docker ps -la
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                   PORTS               NAMES
956560d45f0d        mylab               "/bin/bash"         8 hours ago         Exited (0) 8 hours ago                       my_jupyter_lab
```
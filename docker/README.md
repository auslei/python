## interview questions

To build docker type:
<pre><code>
docker build -t "interview" .
</code></pre>

To start docker container from image:
<pre><code>
docker run -p 8888:8888 -name lab1 interview
</code></pre>

To copy files from container
<pre><code>
docker cp container:path local_path
</code></pre>

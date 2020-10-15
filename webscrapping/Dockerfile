FROM mylab:nlp

ADD requirements.txt
RUN yum install 
RUN cd /home/nlp && jupyter lab --ip=0.0.0.0 --port=8888 --allow-root .
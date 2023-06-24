From centos:7.7.1908
RUN yum install -y epel-release \
    && yum install -y http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm \
    && yum -y install nginx openssh-server supervisor \
    && rm -rf /var/cache/yum/* && yum clean all
RUN ssh-keygen -A
COPY supervisord.conf /etc/supervisord.conf
EXPOSE 22 80
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]

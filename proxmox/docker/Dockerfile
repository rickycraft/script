FROM debian:bullseye

RUN apt-get update \
	&& apt-get install -y python3 openssh-server sudo\
	&& apt-get clean \
	&& rm -rf /var/lib/apt/lists/*

COPY authorized_keys /root/.ssh/authorized_keys
RUN mkdir /var/run/sshd \
	&& chmod 0755 /var/run/sshd \
	&& sed 's/#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config >/etc/ssh/sshd_config

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]


# MongoDB

## Installation on Docker

Notes from https://www.mongodb.com/docs/manual/tutorial/install-mongodb-community-with-docker/

### Install Docker
https://docs.docker.com/desktop/setup/install/linux/fedora/
https://docs.docker.com/engine/install/fedora/

If not using GNOME, install:
```
sudo dnf install gnome-terminal
```

```
sudo dnf -y install dnf-plugins-core

sudo dnf-3 config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo


```

```
sudo dnf install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo systemctl enable --now docker

sudo docker run hello-world

systemctl --user start docker-desktop
systemctl --user enable docker-desktop
systemctl --user stop docker-desktop


```


## Installation on Linux (Fedora)

Notes from https://www.mongodb.com/docs/manual/administration/install-on-linux/

Since I use fedora on my development PC, have listed those instructions below:

### Configure the repository:
```
sudo tee -a /etc/yum.repos.d/mongodb-org-8.0.repo <<EOT
[mongodb-org-8.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/9/mongodb-org/8.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://pgp.mongodb.com/server-8.0.asc
EOT
```

### Install MongoDB Community Server:
```
sudo yum install -y mongodb-org
```

### Logs

By default, MongoDB runs using the `mongod` user account and uses the following default directories:
```
/var/lib/mongo (the data directory)
/var/log/mongodb (the log directory)
```
You can follow the state of the process for errors or important messages by watching the output in the `/var/log/mongodb/mongod.log` file.


### Install the SELinux Policy

Ensure you have the following packages installed:
```
sudo yum install git make checkpolicy policycoreutils selinux-policy-devel
```
Download the policy repository.
```
git clone https://github.com/mongodb/mongodb-selinux
```
Build the policy.
```
cd mongodb-selinux
make
```
Apply the policy.
```
sudo make install
```

### Start mongodb

which init system my platform uses?
```
ps --no-headers -o comm 1
```
start:
```
sudo systemctl start mongod
```
if error:
```
sudo systemctl daemon-reload
```
Misc:
```
sudo systemctl status mongod
sudo systemctl stop mongod
sudo systemctl restart mongod

```

Start a mongosh session on the same host machine as the mongod. You can run mongosh without any command-line options to connect to a mongod that is running on your localhost with default port 27017.
```
mongosh
```
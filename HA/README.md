## Installing on Red Hat Enterprise Linux
As of Red Hat 6.4, Red Hat and the clones have included the keepalived package in the base repository. Therefore, run the following to install the keepalived package and all the required dependencies using dnf (or yum on older systems):

```dnf install keepalived```

```systemctl enable keepalived```

```systemctl start keepalived```

## Installing on Debian
Run the following to install the keepalived package and all the required dependencies using Debian’s APT package handling utility:

```apt-get install keepalived```

# MariaDB Notes

## 1. Read-Only Mode

To prevent accidental data modification on a MariaDB server (for example on replicas or standby nodes), you can enable **read-only mode**.

### Configuration

Edit the MariaDB configuration file:

```
/etc/mysql/my.cnf
```

Add the following under the `[mysqld]` section:

```
[mysqld]
read_only = 1
```

### Important Notes

* The `read_only` option prevents **non-privileged users** from performing write operations such as `INSERT`, `UPDATE`, `DELETE`, and `CREATE`.
* Users with **SUPER privilege** (including `root`) can still modify data even when `read_only` is enabled.
* For stronger protection, it is recommended to:

  * Avoid using the `root` account for applications.
  * Create a dedicated database user with only the required permissions.
  * Optionally enable `super_read_only` (if supported) to prevent even SUPER users from writing.

Example:

```
[mysqld]
read_only = 1
super_read_only = 1
```

### Use Cases

Common scenarios for enabling read-only mode:

* Read replicas
* Backup servers
* Standby nodes in high-availability setups
* Analytics or reporting servers

---

## 2. MariaDB Galera Cluster

MariaDB Galera Cluster is a **synchronous multi-master replication solution** that provides high availability, scalability, and data consistency across multiple database nodes.

### Key Features

* **Multi-master replication** – all nodes can accept read and write operations.
* **Synchronous replication** – transactions are committed on all nodes at the same time.
* **Automatic node provisioning** – new nodes can join the cluster and synchronize automatically.
* **High availability** – if one node fails, the cluster continues operating.

### Typical Architecture

```
Application
     |
Load Balancer
     |
+----------+   +----------+   +----------+
| Node 1   |---| Node 2   |---| Node 3   |
| MariaDB  |   | MariaDB  |   | MariaDB  |
| Galera   |   | Galera   |   | Galera   |
+----------+   +----------+   +----------+
```

### When to Use Galera Cluster

Galera Cluster is suitable when:

* High availability is required.
* You need **no single point of failure**.
* Applications require **strong consistency**.
* Horizontal scaling of read/write workloads is needed.

### Official Documentation

For a complete setup guide:

https://mariadb.com/docs/galera-cluster/galera-cluster-quickstart-guides/mariadb-galera-cluster-guide

---

## 3. Best Practices

* Use a **load balancer** (e.g., HAProxy, ProxySQL) in front of the cluster.
* Monitor cluster status and node health.
* Ensure **low network latency** between nodes.
* Always maintain **an odd number of nodes** (3, 5, 7...) to avoid split-brain situations.

---

## 4. Useful Commands

Check read-only status:

```
SHOW VARIABLES LIKE 'read_only';
```

Check cluster status:

```
SHOW STATUS LIKE 'wsrep_cluster_size';
SHOW STATUS LIKE 'wsrep_cluster_status';
```

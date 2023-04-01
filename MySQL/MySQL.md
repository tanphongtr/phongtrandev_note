# Explain
https://planetscale.com/blog/how-read-mysql-explains

# Transaction
```sql
START TRANSACTION;
DELETE FROM `file` WHERE `id`=3;
COMMIT;

START TRANSACTION;
DELETE FROM `file` WHERE `id`=3;
ROLLBACK;
```

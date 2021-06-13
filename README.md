<p align="center">
  <img src="https://miro.medium.com/max/4800/1*i5VHWsPa9k-u9ffVz0CQdw.jpeg" alt="BerkeleyHackathon">
</p>
<p align="center">
    <em>Gender diversity metrics - Powered by Python, PostgreSQL, React, Redux, Kubernetes, Cypress E2E and Github CI/CD</em>
</p>
<p  align="center">
  <a href="https://github.com/dineshsonachalam/UC-Berkeley-Hackathon/actions/workflows/k8-deploy.yml" alt="CI/CD status">
      <img src="https://github.com/dineshsonachalam/UC-Berkeley-Hackathon/actions/workflows/k8-deploy.yml/badge.svg" />
  </a>
  <a href="https://www.python.org/downloads/release/python-390/" alt="Python 3.9">
      <img src="https://img.shields.io/badge/python-3.9-blue.svg" />
  </a>
  <a href="https://hub.docker.com/repository/docker/dineshsonachalam/gender-diversity-backend" alt="Docker pulls">
      <img src="https://img.shields.io/docker/pulls/dineshsonachalam/gender-diversity-backend.svg" />
  </a>
</p>

### Web app task:
```
Make a webpage that, on default, displays two graphs - a) distribution of number of males and females and b) number of people in each relationship status. You can do the above with bar graphs or pie charts or any other kind of chart / graph of your choice.
Next, display all data in rows. Make a filter with three fields: sex, race, and relationship. Displayed data must update upon selecting one or more filters.
Implement some kind of caching mechanism.
Perform necessary optimizations in frontend and backend wherever applicable/necessary that would result in a smaller latency or faster response time for synchronous requests. You can choose to optimize any / multiple parts (e.g. database reads/writes).
Some pointers: 
You can use any frontend Javascript web framework like AngularJS, React, etc
You can use any backend web framework in Python (e.g. flask, django) to implement the backend.
All updates on frontend must call one or multiple API endpoints / URL routes defined in the backend to update the HTML template / reload it.
If you choose to load the HTML everytime an action requires update of data, render the template in the backend.
Define RESTful URL routing in the backend to handle requests from client over HTTP.
Define ORM/ODM classes to encapsulate each row/document/record in the data set.
Every HTTP request can either fetch the data from the database to render/return the relevant result
You can choose to go either synchronous or asynchronous route.
You can choose to use either an RDBMS (e.g. MySQL, Postgres etc.) or a NoSQL database (e.g. MongoDB, Couchbase, Cassandra, Neo4j etc.). You can even choose to use an in-memory database like redis.
For brownie points: 
Optimize backend assuming you can handle ~10K requests per second to the endpoints / URLs with one process.
```


Developed a full stack application on Flask framework that runs default on the **port: 8025**

Dataset used: http://archive.ics.uci.edu/ml/datasets/Adult

Database: sqlite

![](https://i.imgur.com/sww8r9d.png)
![](https://i.imgur.com/yqoPSCw.png)
![](https://i.imgur.com/1WBQkhK.png)
![](https://i.imgur.com/MkQsYgf.png)

### To Fetch all records from the database:

**Total Row: 32561**

**Total Column: 15**

For example I am running the example with first 30 records according to the filter condition. It takes some time when I try to fetch 32561 rows. If you want to fetch all the 32561 rows from the database , remove the filter condition break statement in query_all() and query_filter() function from Adult class.


![](https://i.imgur.com/zYwGexD.png)
![](https://i.imgur.com/qAH0tqV.png)

### Requirements:

```python
SQLAlchemy==1.2.8
Flask==1.0.2
```

### Start application:

```
docker run -p 8002:8002 -t dineshsonachalam/survaider:1.0.0
```


```
dineshsonachalam@macbook gender-diversity-metrics % helm install gender-diversity-app ./helm
NAME: gender-diversity-app
LAST DEPLOYED: Sun May  9 20:57:33 2021
NAMESPACE: kube-system
STATUS: deployed
REVISION: 1
TEST SUITE: None
dineshsonachalam@macbook gender-diversity-metrics %
```
```
dineshsonachalam@macbook gender-diversity-metrics % kubectl get deployments -n=dinesh
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
adp-backend       1/1     1            1           21m
adp-frontend      1/1     1            1           21m
gdm-backend       1/1     1            1           52s
gdm-frontend      1/1     1            1           52s
search-backend    1/1     1            1           21h
search-frontend   1/1     1            1           21h


kubectl cp ./mysql-dump/adult_dataset.sql dinesh/mysql-0:docker-entrypoint-initdb.d 
dineshsonachalam@macbook gender-diversity-metrics % kubectl get pods -n=dinesh
NAME                               READY   STATUS    RESTARTS   AGE
adp-backend-6ff9d4684f-5jpm5       1/1     Running   0          6m58s
adp-frontend-564d9f786d-rmhjl      1/1     Running   0          6m47s
elasticsearch-0                    1/1     Running   0          22h
gdm-backend-b7dfb98d8-vxh6h        1/1     Running   0          6m19s
gdm-frontend-86d46694bc-fpfkm      1/1     Running   0          6m19s
mysql-0                            1/1     Running   0          26m
search-backend-8647cdb658-mbn97    1/1     Running   0          22h
search-frontend-6f6876fc7f-2jmps   1/1     Running   0          22h
dineshsonachalam@macbook gender-diversity-metrics % kubectl cp ./mysql-dump/adult_dataset.sql dinesh/mysql-0:docker-entrypoint-initdb.d
dineshsonachalam@macbook gender-diversity-metrics % kubectl get pods -n=dinesh
NAME                               READY   STATUS    RESTARTS   AGE
adp-backend-6ff9d4684f-5jpm5       1/1     Running   0          7m35s
adp-frontend-564d9f786d-rmhjl      1/1     Running   0          7m24s
elasticsearch-0                    1/1     Running   0          22h
gdm-backend-b7dfb98d8-vxh6h        1/1     Running   0          6m56s
gdm-frontend-86d46694bc-fpfkm      1/1     Running   0          6m56s
mysql-0                            1/1     Running   0          27m
search-backend-8647cdb658-mbn97    1/1     Running   0          22h
search-frontend-6f6876fc7f-2jmps   1/1     Running   0          22h
dineshsonachalam@macbook gender-diversity-metrics %
```

```
dineshsonachalam@macbook gender-diversity-metrics % kubectl cp ./mysql-dump/adult_dataset.sql dinesh/mysql-0:docker-entrypoint-initdb.d
dineshsonachalam@macbook gender-diversity-metrics %
root@mysql-0:/# ls /docker-entrypoint-initdb.d
adp.sql  adult_dataset.sql  lost+found
root@mysql-0:/#



kubectl rollout restart sts mysql -n=dinesh

dineshsonachalam@macbook ~ % kubectl rollout restart sts mysql -n=dinesh
statefulset.apps/mysql restarted
dineshsonachalam@macbook ~ %

kubectl exec -it mysql-0 /bin/bash -n=dinesh 
```

root@mysql-0:/docker-entrypoint-initdb.d# ls
adp.sql  adult_dataset.sql  dinesh.sql	lost+found
root@mysql-0:/docker-entrypoint-initdb.d#

mysql -u root -psimple < /docker-entrypoint-initdb.d/adult_dataset.sql


root@mysql-0:/docker-entrypoint-initdb.d# ls
adp.sql  adult_dataset.sql  lost+found
root@mysql-0:/docker-entrypoint-initdb.d# mysql -u root -psimple
mysql: [Warning] Using a password on the command line interface can be insecure.
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 5.7.34 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| adp                |
| adult_dataset      |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
6 rows in set (0.00 sec)

mysql>



// Postgres table schema:
DROP TABLE IF EXISTS adult;

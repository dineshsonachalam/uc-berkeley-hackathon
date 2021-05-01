# [Diversity metrics](https://diversity.dineshsonachalam.me/)

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
docker run -p 8001:8001 -t dineshsonachalam/survaider:1.0.0
```




```
CREATE DATABASE website;
show databases;
```
![](https://i.imgur.com/qYTTTO1.png)
  

```
create table member(id bigint primary key auto_increment,  
    name varchar(255) not null,  
    username varchar(255) not null,  
    password varchar(255) not null,  
    follower_count int unsigned not null default 0,  
    time datetime not null default NOW());
```

```
insert into member (name, username, password) values ('test', 'test', 'test');
```
![](https://i.imgur.com/rTzWHq5.png)

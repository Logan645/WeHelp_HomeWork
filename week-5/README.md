* 建立⼀個新的資料庫，取名字為 website 。
* 建立會員資料表，取名字為 member。
```
CREATE DATABASE website;
show databases;
```
![](https://i.imgur.com/qYTTTO1.png)

* 資料表必須包含以下欄位設定：

|  欄位名稱 |  資料型態 | 額外設定 | ⽤途說明|
| -------- | --------| ----- |------|
| id    | bigint     | 主鍵、⾃動遞增     | 獨立編號    |
| name   | varchar(255)     | 不可為空值     | 姓名    |
| username| varchar(255)     | 不可為空值     | 帳⼾名稱    |
| password| varchar(255)     | 不可為空值     | 帳⼾密碼    |
| follower_count| int unsigned     | 不可為空值，預設為 0     | 追蹤者數量    |
| time     | datetime     | 不可為空值，預設為當前時間     | 註冊時間    |


```
create table member(id bigint primary key auto_increment,  
    name varchar(255) not null,  
    username varchar(255) not null,  
    password varchar(255) not null,  
    follower_count int unsigned not null default 0,  
    time datetime not null default NOW());
```
* 使⽤ INSERT 指令新增⼀筆資料到 member 資料表中，這筆資料的 username 和password 欄位必須是 test。接著繼續新增⾄少 4 筆隨意的資料。
```
insert into member (name, username, password) values ('test', 'test', 'test');
insert into member (name, username, password) values ('Nick', 'Nickaccount', 'nick123');
insert into member (name, username, password) values ('angel', 'angelaccount', 'angel1115');
insert into member (name, username, password) values ('randy', 'randyaccount', 'randy1030');
```
* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料。  
`select * from member`
![](https://i.imgur.com/1g7DWTz.png)


* 使⽤ SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。  
`select * from member order by time desc;`  
![](https://i.imgur.com/jIuTcsk.png)


* 使⽤ SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。 ( 並非編號 2、3、4 的資料，⽽是排序後的第 2 ~ 4 筆資料 )  
`select * from member order by time desc limit 1,3;`  
![](https://i.imgur.com/WNAoBis.png)


* 使⽤ SELECT 指令取得欄位 username 是 test 的會員資料。  
`select * from member where username='test';`
![](https://i.imgur.com/Ktoqda1.png)

* 使⽤ SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。  
`select * from member where username='test'and password='test';`
![](https://i.imgur.com/aRaWMNk.png)

* 使⽤ UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。  
`update member set name='test2' where username='test';`
![](https://i.imgur.com/QK5qTYR.png)

* 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。  
`select count(id) from member;`  
![](https://i.imgur.com/Km5byrr.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的總和。  
`select sum(follower_count) from member;`
![](https://i.imgur.com/T3c7Tfv.png)

* 取得 member 資料表中，所有會員 follower_count 欄位的平均數。  
`select avg(follower_count) from member;`
![](https://i.imgur.com/nYKnktv.png)

* 在資料庫中，建立新資料表紀錄留⾔資訊，取名字為 message 。資料表中必須包含以下欄位設定：

|  欄位名稱 | 資料型態 | 額外設定 | ⽤途說明|
| -------- | -------- | -------- | -------- |
| id | bigint | 主鍵、⾃動遞增 | 獨立編號 |
| member_id | bigint | 不可為空值外鍵對應 member 資料表中的 id | 留⾔者會員編號 |
| content| varchar(255)     | 不可為空值     | 留言內容    |
| like_count| varchar(255)     | 不可為空值，預設為0    | 按讚的數量    |
| content| varchar(255)     | 不可為空值     | 留言內容    |
| time     | datetime     | 不可為空值，預設為當前時間     | 留言時間    |
```
create table message(
id bigint primary key auto_increment,
member_id bigint not null,
content varchar(255) not null,
like_count int unsigned not null default 0,
time datetime not null default now(),
foreign key (member_id) references member(id));

insert into message(member_id,content,like_count) values(1,'一直下雨好煩呀',7);
insert into message(member_id,content,like_count) values(1,'希望趕快放晴',11);
insert into message(member_id,content,like_count) values(1,'99好像去散步',4);
insert into message(member_id,content,like_count) values(4,'檸檬塔好吃',12);
insert into message(member_id,content,like_count) values(2,'我是rick',1);
insert into message(member_id,content,like_count) values(3,'你好嗎',77);
insert into message(member_id,content,like_count) values(5,'好想騎車喔',45);
```
* 使⽤ SELECT 搭配 JOIN 語法，取得所有留⾔，結果須包含留⾔者會員的姓名。
`select * from member inner join message on member.id=message.member_id;`  
![](https://i.imgur.com/c7Y07Tl.png)

* 使⽤ SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔，資料中須包含留⾔者會員的姓名。
`select * from member inner join message on member.id=message.member_id where member.username='test';`  
![](https://i.imgur.com/wLMe2U9.png)

* 使⽤ SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留⾔平均按讚數。
`select avg(like_count) from member inner join message on member.id=message.member_id where member.username='test';`  
![](https://i.imgur.com/HQKl2PU.png)

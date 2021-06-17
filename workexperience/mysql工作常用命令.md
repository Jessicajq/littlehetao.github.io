## 常用sql  2021/06/17 12:07:30 
---
### 1.批量查数据
SELECT
DISTINCT 
CONCAT('select *  from ',c.table_name,' where ',c.column_name,' = ',"'ding6efb102c50979493';"),
c.table_name,c.column_name
FROM
  information_schema. COLUMNS c
WHERE
  c.table_schema = 'dj_standard_dev'
and c.column_name in ('fgsid','firstid','FILIALEID','corp_id','corpid','buy_corpId')
 AND c.table_name not in  ('jc_login_ding','jc_login_emp');
#### 1.1批量删除数据
SELECT
CONCAT('delete  from ',c.table_name ,';'),
c.table_name
FROM
  information_schema. `TABLES` c
WHERE
  c.table_schema = 'bigdata-web' and c.table_name like 't_ab_%'
### 2.数据库容量查询（库名需替换）
select table_schema as '数据库',sum(table_rows) as '记录数', sum(truncate(data_length/1024/1024, 2)) as '数据容量(MB)', 
sum(truncate(index_length/1024/1024, 2)) as '索引容量(MB)' from information_schema.tables where table_schema='dj_standard_dev' ; 

### 3.数据库各个表使用情况（库名需替换）
select 
table_name, 
concat(truncate(data_length/1024/1024,2),' MB') as data_size,
-- CONCAT(TRUNCATE(max_data_length/1024/1024,2),'MB') AS max_data_size, 
-- CONCAT(TRUNCATE(data_free/1024/1024,2),'MB') AS data_free,
concat(truncate(index_length/1024/1024,2),' MB') as index_size
from information_schema.tables 
where table_schema = 'dj_standard_dev'
order by data_length desc;

### 4.数据库表和各表记录数（库名需替换）
use information_schema;
select table_name,table_rows from tables where TABLE_SCHEMA = 'dj_standard_dev' order by table_name desc; 

### 5.查询哪些表包含某一字段

select TABLE_NAME
from information_schema.`COLUMNS` 
where TABLE_SCHEMA='dj_standard_dev'
and COLUMN_NAME='issign'

### 6.多表拼接字段查询
SELECT
  *
FROM
  (
    SELECT
      @rownum :=@rownum + 1 AS rownum,

    IF (
      @score = score ,@rank ,@rank :=@rownum
    ) AS rank ,@score := score AS score,
    dept_id,
    emp_name,
    emp_id,
    MONTH,
    YEAR,
    party_pos,
    dept_name
  FROM
    (
      SELECT
        max(dept_id) dept_id,
        emp_id,
        sum(score) score,
        max(emp_name) emp_name,
        max(YEAR) YEAR,
        max(MONTH) MONTH,
        max(party_pos) party_pos,
        max(dept_name) dept_name
      FROM
        djs_score_census
      WHERE
        corp_id = 'ding6efb102c50979493'
      AND YEAR = '2020'
      AND MONTH = '06'
      GROUP BY
        emp_id,
        MONTH
      ORDER BY
        score DESC
    ) a,
    (
      SELECT
        @rownum := 0 ,@rank := 0 ,@score := NULL
    ) b
  ) c
LIMIT 0

### 7.case报表统计sql
SELECT ages, count(*) AS agesnum  
                FROM  
                 (SELECT  
                   CASE WHEN age < 18 THEN 1  
                          WHEN age >= 18 AND age <= 25 THEN 2  
                          WHEN age >= 26 AND age <= 35 THEN 3  
                          WHEN age >= 36 AND age <= 49 THEN 4  
                          WHEN age >= 50 AND age <= 60 THEN 5  
                          WHEN age > 60 THEN 6  
                    ELSE 0 END ages  
                  FROM  
                   (  
                    SELECT TIMESTAMPDIFF(YEAR, birthday, CURDATE()) AS age  
                    FROM dju_member  
                    WHERE corp_id = 'dingd2b6e03a795e54af'  
                    AND birthday IS NOT NULL  
                   ) a  
                 ) a  
                 GROUP BY ages
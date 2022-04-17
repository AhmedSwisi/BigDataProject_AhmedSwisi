create database if not exists testdb;
use testdb;
create external table if not exists tweets(
    id bigint,
    conversation_id bigint,
    date string,
    time string,
    user_id int,
    tweet string,
    replies_count int,
    retweets_counts int,
    likes_count int,
    hashtags string,
    retweet string,
)
row format delimited
fields terminated by ','
lines terminated by '\n'
stored as textfile location 'hdfs://namenode:8020/user/hive/warehouse/testdb.db/tweets';
select 
s.user_id,
round(
    ifnull(
        sum(case when c.action="confirmed" then 1 else 0 end)/count(c.user_id),0)
    ,2) 
        as confirmation_rate from Signups s left join confirmations c on s.user_id=c.user_id group by s.user_id;
# Write your MySQL query statement bel
-- select e.name from Employee as e join  (select managerId,count(managerId) as cnt from Employee group by managerId having cnt>=5) as newtable on newtable.managerId=e.id;

select e2.name from Employee e1 inner join Employee e2 on e1.managerId = e2.id
group by e1.managerId having count(e1.managerId)>=5;
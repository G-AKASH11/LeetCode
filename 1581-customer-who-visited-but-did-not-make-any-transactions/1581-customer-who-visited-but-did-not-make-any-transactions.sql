# Write your MySQL query statement below
select v.customer_id,count(v.visit_id) as count_no_trans from Visits as v
left join transactions 
on v.visit_id=transactions.visit_id
where transaction_id is null
group by v.customer_id
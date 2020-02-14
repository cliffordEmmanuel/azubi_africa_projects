-- How many agent_transactions did we have in the months of 2018(broken down by months)

select 
    DATE_TRUNC('month', when_created),
    count(atx_id)
from agent_transactions
where 
    when_created >= "2018-01-01"
    and when_created <= "2018-12-31"
group by
    1
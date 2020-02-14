-- How many different users have sent a transfer in CFA?


select count( distinct u_id)
from transfers
where send_amount_currency = "CFA"
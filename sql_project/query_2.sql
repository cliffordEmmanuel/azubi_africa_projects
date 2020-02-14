-- How many transfers have been sent in the currency CFA

select count(send_amount_currency)
from transfers
where send_amount_currency = "CFA"
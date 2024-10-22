SELECT
    magic_wand_creator,
    max(deposit_amount) as max_deposit_amount

FROM 
    wizard_deposits
GROUP BY 
    magic_wand_creator
HAVING
    max(deposit_amount) NOT BETWEEN 20000 AND 40000
ORDER BY 
    max_deposit_amount DESC
LIMIT 3;
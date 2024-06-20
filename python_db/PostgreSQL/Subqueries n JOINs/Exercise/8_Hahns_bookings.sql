SELECT
    COUNT(*)
FROM
    customers as c
JOIN
    bookings as b
USING 
    (customer_id)
WHERE
    c.last_name = 'Hahn';

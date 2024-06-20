SELECT
    cl.full_name,
    count(co.car_id) as count_of_cars,
    sum(co.bill) as total_sum
FROM
    clients as cl
JOIN
    courses as co
ON
    cl.id = co.client_id

WHERE
    substring(cl.full_name FROM 2 FOR 1 ) = 'a'
GROUP BY
    cl.full_name
HAVING 
    COUNT(car_id) > 1
ORDER BY
    cl.full_name;


SELECT 
    id AS id,
    concat(first_name, ' ', middle_name, ' ', last_name) as full_name,
    hire_date
FROM  employees
ORDER BY hire_date ASC
OFFSET 9;
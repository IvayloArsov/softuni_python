SELECT
    department_id,
    min("salary") AS max_salary
FROM
    employees
GROUP BY department_id
ORDER BY department_id;
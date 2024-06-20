CREATE VIEW view_river_info AS
SELECT
    concat_ws(' ', 'The river', river_name, 'flows into the', outflow, 'and is', length, 'kilometers long.') 
AS 
    "River information"
FROM 
    rivers
ORDER BY
    river_name ASC;

SELECT * FROM view_river_info ;
SELECT
    concat_ws(' ', m.mountain_range, p.peak_name) 
    as mountain_information,
    length(concat_ws(' ', m.mountain_range, p.peak_name)) 
    as characters_length,
    bit_length(concat_ws(' ', m.mountain_range, p.peak_name)) 
    as bits_of_a_tring

FROM
    mountains as m,
    peaks as p
WHERE
    p.mountain_id = m.id
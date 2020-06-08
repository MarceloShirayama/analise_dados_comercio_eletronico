SELECT dt_sgmt,
    count(DISTINCT seller_id)
FROM tb_seller_sgmt 
GROUP BY dt_sgmt
SELECT count(DISTINCT T1.order_id),
    min(T1.order_approved_at),
    max(T1.order_approved_at)
FROM tb_orders AS T1
;
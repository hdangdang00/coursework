SELECT sp.id,
       sp.supplier_id,
       sp.name,
       sp.part_type,
       dc.name AS category,
       CASE
         WHEN dc.id IS NULL THEN 'unlabeled' -- 카테고리 없음
         WHEN dc.name LIKE '%-old%' THEN 'old' -- 구 분류체계
         WHEN dc.name = '기타' THEN 'etc' -- 기타
         ELSE 'train' -- 정답으로 사용 가능
       END AS split_group
FROM supplier_part sp
LEFT JOIN display_category dc ON sp.display_category_id = dc.id;
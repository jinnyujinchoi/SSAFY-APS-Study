# 맛만 조회
SELECT FLAVOR
FROM (
    # 주문량 합치기(서브쿼리)
    SELECT FLAVOR, TOTAL_ORDER
    FROM FIRST_HALF
    UNION ALL
    SELECT FLAVOR, TOTAL_ORDER
    FROM JULY
) AS TOTAL_CNT # 서브쿼리는 꼭 '명명'이 필요
# 그룹 묶어주기
GROUP BY FLAVOR
# 주문량이 큰 순서대로 #SUM으로 주문량을 합쳐줍시다
ORDER BY SUM(TOTAL_ORDER) DESC
# 상위 3개 제한
LIMIT 3

-- 진료과코드, 5월 예약 건수 조회 --
SELECT MCDP_CD AS 진료과코드,
        COUNT(*) AS 5월예약건수
FROM APPOINTMENT
-- 조건1. 날짜가 5월 이어야 하고 --
WHERE MONTH(APNT_YMD) = 5
-- 진료과코드로 묶어주기 --
GROUP BY MCDP_CD
-- 예약 건수 기준 오름차, 코드 오름차 --
ORDER BY 5월예약건수, 진료과코드
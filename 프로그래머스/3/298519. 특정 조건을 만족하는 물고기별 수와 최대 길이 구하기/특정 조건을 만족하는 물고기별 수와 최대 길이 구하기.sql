-- 잡은 수, 최대 길이, 물고기 종류 출력 --
SELECT COUNT(*) AS FISH_COUNT,
    MAX(LENGTH) AS MAX_LENGTH,
    FISH_TYPE
FROM FISH_INFO
-- 그룹 묶어주기 --
GROUP BY FISH_TYPE
-- NULL은 모두 10cm --
-- 조건 : 평균 길이가 33cm 이상 --
HAVING AVG(LENGTH) >= 33
-- 물고기 종류 오름차 --
ORDER BY FISH_TYPE;
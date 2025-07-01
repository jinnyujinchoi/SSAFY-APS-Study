-- 이름, 번호, 성별코드, 나이, 전화번호 조회 --
SELECT PT_NAME, PT_NO, GEND_CD, AGE,
    IFNULL(TLNO, 'NONE')
FROM PATIENT
-- 조건1. 여자환자 --
WHERE (GEND_CD = 'W'
-- 조건2. 12세 이하 --
       AND AGE <= 12)
ORDER BY AGE DESC, PT_NAME ASC;
-- 나이 내림차, 환자이름 오름차 --
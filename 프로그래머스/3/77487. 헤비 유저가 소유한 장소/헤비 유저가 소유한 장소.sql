-- 코드를 입력하세요
SELECT p.ID, p.NAME, p.HOST_ID
FROM PLACES p
JOIN (
SELECT host_id
FROM places
GROUP BY host_id
HAVING COUNT(*) > 1
) j ON p.host_id = j.host_id
ORDER BY id;
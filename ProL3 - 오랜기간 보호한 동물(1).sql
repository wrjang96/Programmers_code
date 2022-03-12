SELECT NAME, DATETIME
FROM ANIMAL_INS
WHERE ANIMAL_ID NOT IN (
    SELECT ANIMAL_ID FROM ANIMAL_OUTS
)
ORDER BY DATETIME ASC
LIMIT 3;
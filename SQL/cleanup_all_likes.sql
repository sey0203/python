-- 데이터 모두 삭제
DELETE FROM public."_UserFavorites";



-- 확인
--SELECT * FROM public."_UserFavorites"







-- 데이터 삭제될수있으니 내가 추가한 사용자id 15번 이상부터의 좋아요 db 만 삭제하는 쿼리


-- DELETE FROM public."_UserFavorites"
-- WHERE "B" >= 15;                -- 사용자 ID ≥ 15인 좋아요 삭제

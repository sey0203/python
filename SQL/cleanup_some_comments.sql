-- 내가 추가했던 댓글만 삭제

DELETE FROM public."Comment"
WHERE "authorId" <= 10      -- 사용자 ID가 10 이하이고
  AND "articleId" >= 27;    -- 게시글 ID가 27 이상인 경우만 삭제

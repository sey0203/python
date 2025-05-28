-- 내가 추가한 게시글 id로만 댓글 테스트해봄


WITH users AS (
  SELECT id AS user_id
  FROM public."User"
  WHERE id <= 10                    -- 사용자 ID가 10 이하인 경우만
),
articles AS (
  SELECT id AS article_id
  FROM public."Article"
  WHERE id >= 27                   -- ✅ 게시글 ID가 27 이상인 경우만
)
INSERT INTO public."Comment" (
  body,
  "authorId",
  "articleId",
  "createdAt",
  "updatedAt"
)
SELECT
  '댓글 by user ' || u.user_id || ' on article ' || a.article_id,
  u.user_id,
  a.article_id,
  now(),
  now()
FROM users u
CROSS JOIN articles a;           

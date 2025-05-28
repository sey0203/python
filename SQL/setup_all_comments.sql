-- 모든 사용자와 모든 게시글 조합에 대해 댓글 1개씩 생성
WITH users AS (
  SELECT id AS user_id FROM public."User"       -- 🔹 모든 사용자
),
articles AS (
  SELECT id AS article_id FROM public."Article" -- 🔹 모든 게시글
)
INSERT INTO public."Comment" (
  body,
  "authorId",
  "articleId",
  "createdAt",
  "updatedAt"
)
SELECT
  '댓글 by user ' || u.user_id || ' on article ' || a.article_id,  -- 댓글 본문
  u.user_id,           -- 작성자 ID
  a.article_id,        -- 게시글 ID
  now(),               -- 생성 시간
  now()
FROM users u
CROSS JOIN articles a; -- 🔁 모든 사용자 × 모든 게시글 조합

-- 単体テストで使用するユーザ
-- 単体テスト実行前にinsertしておく

INSERT INTO auth_user( 
    password
  , is_superuser
  , username
  , first_name
  , last_name
  , email
  , is_staff
  , is_active
  , date_joined
) 
VALUES ( 
    'pbkdf2_sha256$120000$8XwkNp4C5aOZ$l03UnUdiZYisT58tC3eL6Lc5Z3/PccOaVifXGpMot6w=' -- admin
  , 1
  , 'utadmin'
  , ''
  , ''
  , 'utadmin@ut.com'
  , 1
  , 1
  , '2019/07/26 00:00:00'
) 
;

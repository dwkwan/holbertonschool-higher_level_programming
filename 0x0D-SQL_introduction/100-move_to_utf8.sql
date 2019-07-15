-- hbtn_0c_0 converted to UTF8
-- sets database
USE hbtn_0c_0;
-- converts field to utf8mb4
ALTER TABLE first_table MODIFY name VARCHAR(256) CHARACTER SET utf8mb4;
-- converts table to utf8mb4
ALTER TABLE first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- converts database to utf8mb4
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

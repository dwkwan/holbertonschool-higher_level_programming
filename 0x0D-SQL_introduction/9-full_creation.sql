-- new table
-- creates a new table named second_table
CREATE TABLE IF NOT EXISTS second_table(
id INT DEFAULT NULL,
name VARCHAR(256),
score INT
);
-- inserts four new records into second_table
INSERT INTO `second_table`(`id`, `name`, `score`)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);

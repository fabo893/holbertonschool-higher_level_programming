-- Create a table 'second_table'
CREATE TABLE IF NOT EXISTS second_table (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	name VARCHAR(256),
	score INT(3));

	INSERT INTO `second_table` (`name`, `score`)
	VALUES
	('John', 10),
	('Alex', 3),
	('Bob', 14),
	('George', 8);

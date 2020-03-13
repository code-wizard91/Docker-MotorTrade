CREATE DATABASE flaskapp:
CREATE TABLE IF NOT EXISTS `Users` (
	`user_id` int(10) NOT NULL auto_increment,
	`username` varchar(255) NOT NULL,
	`first_name` varchar(255) NOT NULL,
	`last_name` varchar(255) NOT NULL,
	`email` varchar(255) NOT NULL,
	`password` varchar(255) NOT NULL,
	`profile_image` varchar(255) NOT NULL DEFAULT 'default.jpg',
	PRIMARY KEY( `user_id` )
);

CREATE TABLE IF NOT EXISTS `Adverts` (
	`adv_id` int(10) NOT NULL auto_increment,
	`user_id` int(10),
	`car_title` varchar(255),
	`car_descr` varchar(255),
	`price` varchar(255),
	`mileage` varchar(255),
	`location` varchar(255),
	`contact_no` varchar(255),
	`image` varchar(255),
	`date_adv` datetime,
	PRIMARY KEY ( `adv_id` )
	FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

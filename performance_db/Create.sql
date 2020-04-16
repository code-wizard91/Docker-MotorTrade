CREATE DATABASE flaskapp;

USE flaskapp;

CREATE TABLE users(
  user_id int NOT NULL AUTO_INCREMENT, 
  username varchar(255) NOT NULL, 
  first_name varchar(255) NOT NULL, 
  last_name varchar(255) NOT NULL, 
  email varchar(255) NOT NULL, 
  password varchar(255) NOT NULL, 
  profile_image varchar(255) DEFAULT 'default.jpg',
  PRIMARY KEY (user_id)
  );
CREATE TABLE adverts(
  adv_id int NOT NULL AUTO_INCREMENT, 
  user_id int NOT NULL, 
  car_title varchar(255) NOT NULL, 
  car_descr varchar(255) NOT NULL, 
  price varchar(255) NOT NULL, 
  mileage varchar(255) NOT NULL, 
  location varchar(255) NOT NULL, 
  contact_no varchar(255) NOT NULL, 
  image varchar(255) NOT NULL, 
  date_adv DATETIME NOT NULL, 
  PRIMARY KEY (adv_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

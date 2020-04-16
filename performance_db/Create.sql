CREATE DATABASE flaskapp;

USE flaskapp;

CREATE TABLE users(
  user_id int NOT NULL AUTO_INCREMENT, 
  PRIMARY KEY (user_id)
  );
CREATE TABLE adverts(
  adv_id int NOT NULL AUTO_INCREMENT, 
  user_id int NOT NULL, 
  PRIMARY KEY (adv_id),
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

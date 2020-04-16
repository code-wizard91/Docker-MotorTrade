CREATE TABLE users(
  user_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  username VARCHAR(50) NOT NULL, 
  first_name VARCHAR(50) NOT NULL, 
  last_name VARCHAR(50) NOT NULL, 
  email VARCHAR(255) NOT NULL, 
  password VARCHAR(255) NOT NULL, 
  profile_image VARCHAR(255) NOT NULL DEFAULT 'default.jpg', 
  );
CREATE TABLE adverts(
  adv_id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY, 
  user_id INTEGER NOT NULL, 
  car_title VARCHAR(255) NOT NULL, 
  car_descr VARCHAR(255) NOT NULL, 
  price VARCHAR(255) NOT NULL, 
  mileage VARCHAR(255) NOT NULL, 
  location VARCHAR(255) NOT NULL, 
  contact_no VARCHAR(255) NOT NULL, 
  image VARCHAR(255) NOT NULL, 
  date_adv DATETIME NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users(user_id)
);

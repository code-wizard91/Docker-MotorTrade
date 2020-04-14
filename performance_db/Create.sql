CREATE DATABASE flaskapp;
CREATE TABLE Users(
    user_id int(10) NOT NULL auto_increment,
    username varchar(255) NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    email varchar(255) NOT NULL,
    password varchar(255) NOT NULL,
    profile_image varchar(255) NOT NULL DEFAULT 'default.jpg',
    PRIMARY KEY(user_id)
);

CREATE TABLE Adverts (
    adv_id int(10) NOT NULL auto_increment,
    user_id int(10) NOT NULL,
    car_title varchar(255) NOT NULL,
    car_descr varchar(255) NOT NULL,
    price varchar(255) NOT NULL,
    mileage varchar(255) NOT NULL,
    location varchar(255) NOT NULL,
    contact_no varchar(255) NOT NULL,
    image varchar(255) NOT NULL,
    date_adv datetime NOT NULL,
    PRIMARY KEY (adv_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

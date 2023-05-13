DROP DATABASE IF EXISTS three_random_words_data;
CREATE DATABASE three_random_words_data;
USE three_random_words_data;

CREATE TABLE users
(
    'user_id'  INT(3) PRIMARY KEY UNIQUE NOT NULL,
    'user_pin' INT(5) PRIMARY KEY UNIQUE NOT NULL,
    'username' VARCHAR(50)               NOT NULL,
    'password' VARCHAR(8)                NOT NULL
);

CREATE TABLE face_recognition
(
    'face_id'        INT(3) PRIMARY KEY UNIQUE NOT NULL,
    'PIN'            INT(5) UNIQUE             NOT NULL,
    'face_file_path' VARCHAR(50)               NOT NULL
);

CREATE TABLE voice_recognition
(
    'voice_id'        INT(3) PRIMARY KEY UNIQUE NOT NULL,
    'voice_file_path' VARCHAR(50)               NOT NULL

);

CREATE TABLE session
(
    'session_id'  INT(3) PRIMARY KEY UNIQUE NOT NULL,
    'login_time'  TIMESTAMP,
    'logout_time' TIMESTAMP
);

CREATE TABLE user_info
(
    'identification_code' INT(3) NOT NULL,
    'name'                VARCHAR(100),
    'surname'             VARCHAR(100),
    'age'                 INT,
    'email'               VARCHAR(100),
    'account_created'     TIMESTAMP
);

CREATE TABLE auth_codes
(
    'user_id'        INT(3) PRIMARY KEY NOT NULL,
    'pin'            INT(5) PRIMARY KEY NOT NULL,
    'generated_code' VARCHAR(10)        NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);
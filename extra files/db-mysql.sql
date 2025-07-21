CREATE TABLE `User` (
  `id` integer PRIMARY KEY AUTO_INCREMENT,
  `email` email,
  `password` password,
  `updated_date` datetime,
  `created_at` datetime
);

CREATE TABLE `Profile` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `user` int,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `image` file,
  `description` text,
  `created_at` datetime,
  `updated_date` datetime
);

CREATE TABLE `Post` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `image` file,
  `author` int,
  `title` varchar(255),
  `content` text,
  `category` int,
  `status` boolean,
  `created_at` datetime,
  `updated_date` datetime,
  `published_date` datetime
);

CREATE TABLE `category` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

ALTER TABLE `Post` ADD FOREIGN KEY (`category`) REFERENCES `category` (`id`);

ALTER TABLE `User` ADD FOREIGN KEY (`id`) REFERENCES `Profile` (`user`);

ALTER TABLE `Profile` ADD FOREIGN KEY (`id`) REFERENCES `Post` (`author`);

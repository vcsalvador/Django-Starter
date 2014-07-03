
CREATE TABLE "app_reservationentry" (
    "id" integer NOT NULL PRIMARY KEY,
    "name" varchar(50) NOT NULL,
    "address" varchar(50) NOT NULL,
    "phone" varchar(50) NOT NULL,
    "time" varchar(50) NOT NULL,
    "table_id" integer NOT NULL UNIQUE REFERENCES "r2_tableentry" ("id")
);
CREATE TABLE "app_reservationentry_foodList" (
    "id" integer NOT NULL PRIMARY KEY,
    "reservationentry_id" integer NOT NULL,
    "foodentry_id" integer NOT NULL REFERENCES "r2_foodentry" ("id"),
    UNIQUE ("reservationentry_id", "foodentry_id")
);
CREATE TABLE "app_foodentry" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(100) NOT NULL,
    "price" varchar(100) NOT NULL
);
INSERT INTO `app_foodentry` VALUES(1,'Pizza',10);
INSERT INTO `app_foodentry` VALUES(3,'Hamburger',5);
INSERT INTO `app_foodentry` VALUES(4,'Popcorn',5);
CREATE TABLE "app_tableentry" (
    "id" integer NOT NULL PRIMARY KEY,
    "title" varchar(50) NOT NULL
);
INSERT INTO `app_tableentry` VALUES(2,'Table 1');
INSERT INTO `app_tableentry` VALUES(3,'Table 2A');
INSERT INTO `app_tableentry` VALUES(4,'Table 2B');


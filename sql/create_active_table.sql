create table active(
    uid varchar(6) primary key,
    name varchar(80) not null,
    email varchar(100) not null unique,
    password varchar(60) not null unique
                   );
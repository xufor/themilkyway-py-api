create table inactive(
    email varchar(100) primary key,
    name varchar(80) not null,
    password varchar(60) not null unique
                     );
create table inactive(
    name varchar(80) primary key not null,
    email varchar(100) not null unique,
    password varchar(100) not null unique
                     );
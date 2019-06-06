create extension if not exists "uuid-ossp";

create table active(
    uid uuid default uuid_generate_v4() primary key,
     name varchar(80) not null,
     email varchar(100) not null unique,
     password varchar(100) not null unique
                   );
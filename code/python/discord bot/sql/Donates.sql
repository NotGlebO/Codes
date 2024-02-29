create table Donates
(
    ID            bigint unsigned auto_increment
        primary key,
    PlayerID      bigint unsigned not null,
    Expires       datetime(6)     not null,
    PrivilegeList longtext        not null,
    IsSlot        tinyint(1)      not null,
    constraint FK_Donates_Players_PlayerID
        foreign key (PlayerID) references Players (ID)
            on delete cascade
);

create index IX_Donates_PlayerID
    on Donates (PlayerID);

INSERT INTO scpsl7780.Donates (ID, PlayerID, Expires, PrivilegeList, IsSlot) VALUES (1, 76561199016807846, '2023-05-18 19:52:30.038191', '{"Badge":"carmine:\\u0427\\u0435\\u0447\\u0435\\u043D\\u0441\\u043A\\u0438\\u0439 \\u043F\\u043E\\u043B\\u043A\\u043E\\u0432\\u043E\\u0434\\u0435\\u0446"}', 0);

create table Mutes
(
    ID       bigint unsigned auto_increment
        primary key,
    IssuedAt datetime(6)     not null,
    Expires  datetime(6)     not null,
    TargetID bigint unsigned not null,
    IssuerID bigint unsigned not null,
    Reason   text            not null,
    constraint FK_Mutes_Players_IssuerID
        foreign key (IssuerID) references Players (ID)
            on delete cascade,
    constraint FK_Mutes_Players_TargetID
        foreign key (TargetID) references Players (ID)
            on delete cascade
);

create index IX_Mutes_IssuerID
    on Mutes (IssuerID);

create index IX_Mutes_TargetID
    on Mutes (TargetID);


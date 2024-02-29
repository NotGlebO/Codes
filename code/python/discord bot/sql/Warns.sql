create table Warns
(
    ID       bigint unsigned auto_increment
        primary key,
    IssuedAt datetime(6)     not null,
    IsStaff  tinyint(1)      not null,
    IsSilent tinyint(1)      not null,
    TargetID bigint unsigned not null,
    IssuerID bigint unsigned not null,
    Reason   text            not null,
    constraint FK_Warns_Players_IssuerID
        foreign key (IssuerID) references Players (ID)
            on delete cascade,
    constraint FK_Warns_Players_TargetID
        foreign key (TargetID) references Players (ID)
            on delete cascade
);

create index IX_Warns_IssuerID
    on Warns (IssuerID);

create index IX_Warns_TargetID
    on Warns (TargetID);

INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (1, '2023-03-26 20:50:14.390249', 0, 1, 76561199130195674, 76561198308452757, 'давал приказы 049-2 за 049 в чат SCP, а не в общий чат');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (2, '2023-03-26 21:22:20.133536', 0, 0, 76561199486584863, 76561198308452757, '2.2, странные приказы за капитана МОГ. Приказывал эвакуировать весь персонал Зоны из-за одного SCP-049');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (3, '2023-03-26 22:22:56.729255', 0, 0, 76561198355785882, 1, 'Использовал SCP-1162 без РП причины за Д-класс.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (4, '2023-03-27 21:28:05.263599', 0, 1, 76561199486584863, 76561198968146360, '[2.17] Разумность за SCP-173 (преследование по дверям)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (5, '2023-03-28 22:22:56.804696', 0, 1, 76561199174754197, 1, 'Нарушение пункта [2.2] |Сказал SCP-173 "Фу, накакал" Играя за МОГ.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (8, '2023-04-15 15:59:16.299512', 0, 1, 76561198997036722, 76561199008500586, '[2.16] Гермоворота');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (9, '2023-04-15 21:44:21.247534', 0, 0, 76561199078152504, 76561199021893795, '[2.2] Non RP (Открытие дверей за SCP-173 когда на него смотрели)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (10, '2023-04-15 22:10:12.147270', 0, 1, 76561199481806861, 76561199021893795, '[2.2] Non RP за ССБ');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (11, '2023-04-15 22:20:28.073210', 0, 0, 76561199200186861, 76561199021893795, 'Безпричинное нарушение контракта с фондом.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (12, '2023-04-15 22:20:55.686308', 0, 0, 76561199468547071, 76561199021893795, 'Безпричинное нарушение контракта с фондом.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (13, '2023-04-16 14:56:07.111866', 0, 0, 76561198192525230, 76561199008500586, '[2.2] Non RP (при смягчающих обстоятельствах)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (14, '2023-04-16 18:09:43.169248', 0, 0, 76561199044078948, 76561198127069467, '[2.2] Non RP. Преследование после закрытой двери за SCP - 173 "Скульптура".');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (15, '2023-04-16 18:29:43.970707', 0, 1, 76561199472007996, 76561199021893795, '[2.29] Нарушение правила лечения (Не отыграл лечение аптечкой)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (16, '2023-04-16 18:30:12.865773', 0, 0, 76561199225679680, 76561198127069467, '[2.2] Non RP. Частые неролевые разговоры во время ролевого процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (17, '2023-04-16 18:39:42.082456', 0, 1, 76561199073812173, 76561199021893795, '[2.2] Non RP (баннихоп)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (18, '2023-04-16 18:48:12.411695', 0, 1, 76561199073812173, 76561198127069467, '[2.2] Non RP. Многократные прыжки за SCP - 173 "Скульптура".');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (19, '2023-04-16 18:55:00.357194', 0, 0, 76561199073812173, 76561199021893795, '[2.2] Non RP (Уход от цели)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (20, '2023-04-16 18:57:24.318380', 0, 0, 76561199183086221, 76561198127069467, '[2.1] Неадекватное RP действие. Отдал некорректный приказ(открыть огонь по SCP 173 - "Скульптура") за Капитана Мобильной Оперативной Группы Эпсилон - 11("Девятихвостая лиса").');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (21, '2023-04-16 20:51:13.332277', 0, 0, 76561199231198191, 76561198881551022, '2.17 (Открывал двери)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (23, '2023-04-17 12:52:59.476006', 0, 1, 76561198192525230, 76561199027855046, '[2.29] Нарушение правила лечения (МАКСИМАЛЬНО незначительное).');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (24, '2023-04-17 14:03:06.981914', 0, 1, 76561199231198191, 76561199008500586, '[2.16] Гермоворота');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (25, '2023-04-17 15:54:04.223615', 0, 1, 76561199491255250, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (26, '2023-04-17 16:17:50.293592', 0, 0, 76561199185483088, 76561199027855046, '[2.2] Non RP (бхоп)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (27, '2023-04-17 17:02:36.966115', 0, 1, 76561198299418944, 76561199021893795, '2.2] Non RP (Преследование цели за SCP-173 по закрытым дверям)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (28, '2023-04-17 17:49:32.743873', 0, 1, 76561199297676628, 76561198968146360, '[2.29] Нарушение правила лечения. (Неотыгрыш какого-либо лечения)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (29, '2023-04-17 18:45:19.000911', 0, 0, 76561199143503082, 76561199027855046, '[2.10] Использование труднодоступных мест.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (30, '2023-04-17 19:20:38.437908', 0, 1, 76561199083191207, 76561199090280951, '[1.1] Недостижение минимального возраста для игры на Hard RP (Пока что делаю исключение т.к. вроде на диалог идёт и правила пошёл читать)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (31, '2023-04-17 19:56:00.765795', 0, 0, 76561199466899995, 76561199090280951, '[2.3] Необоснованный выход из RP процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (32, '2023-04-17 20:26:59.655120', 0, 0, 76561198328615233, 76561198881551022, '2.2 [NonRP] Говорит о украине за охрану');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (33, '2023-04-17 20:53:03.489996', 0, 0, 76561199058639479, 76561198881551022, '2.2 [Нон.РП] Нарушение ньюансов отыгрыша (4.7)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (34, '2023-04-17 21:02:27.474223', 0, 0, 76561198972242547, 76561198881551022, '2.2 [NonRP] Нарушение нюансов отыгрыша за МОГ. Использовал SCP объекты (3.4)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (35, '2023-04-18 15:46:37.603507', 0, 0, 76561199451156653, 76561199027855046, '[2.27] Нарушение диалекта (939 = собака). + [2.2] Non RP (при смягчающих обстоятельствах)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (36, '2023-04-18 15:51:48.097316', 0, 0, 76561199454158179, 76561199027855046, '[2.29] Нарушение правила лечения.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (37, '2023-04-18 16:05:02.933084', 0, 0, 76561199473371357, 76561199027855046, '[2.29] Нарушение правила лечения. + Незнание правил (целей ПХ) + случайный ТК');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (38, '2023-04-18 16:09:40.165836', 0, 0, 76561199044078948, 76561199027855046, '[2.29] Нарушение правила лечения.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (39, '2023-04-18 16:09:51.993591', 0, 0, 76561199203874459, 76561199021893795, '[0.1] Non RP (Нарушение ньюансов отыгрыша SCP-939 (Переходил на бег без цели в зоне видимости))');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (40, '2023-04-18 16:21:24.770104', 0, 0, 76561199466899995, 76561199021893795, '[0.1] Non RP - Нарушение ньюансов отыгрыша за SCP-939 (Выход из камеры раньше отведенного срока)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (41, '2023-04-18 16:26:11.952285', 0, 1, 76561198801439594, 76561199027855046, '[2.8] MetaGaming.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (42, '2023-04-18 16:40:09.763579', 0, 0, 76561199470220283, 76561199021893795, '[2.7] Random Death Match - Стрельба по своим.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (43, '2023-04-18 17:15:06.855715', 0, 0, 76561198801439594, 76561199021893795, '[2.27] Диалект - За МОГ называл SCP-939 "собакой".');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (44, '2023-04-18 17:28:47.905546', 0, 1, 76561199485488713, 76561199090280951, '[2.2] Non RP (Не скушал труп за 939, но исправился, когда я напомнил ему)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (46, '2023-04-18 17:39:48.216624', 0, 0, 76561199130897059, 76561199021893795, '[2.2] Non RP - Убегал по лифтам от SCP-096');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (47, '2023-04-18 19:33:06.843349', 0, 0, 76561198849474993, 76561199090280951, '[2.5] PowerGaiming (Закрывал двери на бегу)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (48, '2023-04-18 19:50:20.816040', 0, 0, 76561199159037665, 76561199090280951, '[2.27] Нарушение диалекта.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (49, '2023-04-18 20:29:38.520027', 0, 1, 76561199174754197, 76561198127069467, '[2.9] Team Kill (Одиночный, ненамеренный).');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (50, '2023-04-19 13:03:00.978763', 0, 1, 76561199481189426, 76561199008500586, '[2.10] Использование труднодоступных мест');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (51, '2023-04-19 13:18:21.500860', 0, 1, 76561199126749039, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (53, '2023-04-19 19:08:22.523322', 0, 0, 76561199227100523, 76561198308452757, 'Причина: [2.3] Необоснованный выход из RP процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (54, '2023-04-19 22:23:38.912366', 0, 0, 76561199324059686, 76561199021893795, '[2.29] Лечение - Не отыгрывал лечение аптечкой.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (55, '2023-04-19 22:24:18.585136', 0, 0, 76561199443384178, 76561199021893795, '[2.2] Non RP. - Использование SCP-914 за Научного Сотрудника');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (56, '2023-04-19 23:01:26.434695', 0, 0, 76561199068450217, 76561199021893795, '[2.29] Лечение - Не отыгрывал лечение аптечкой.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (57, '2023-04-20 15:20:10.635855', 0, 0, 76561199020025976, 76561198127069467, '[2.2] Non RP. Некорректная отыгровка за оперативника МОГ.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (58, '2023-04-20 15:23:09.417552', 0, 0, 76561199174754197, 76561198127069467, '[2.2] Non RP. Некорректная отыгровка за оперативника МОГ.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (59, '2023-04-20 21:21:27.614043', 0, 0, 76561199200186861, 76561199033775223, 'метагейминг');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (60, '2023-04-20 21:39:11.581311', 0, 0, 76561199200077812, 76561199033775223, 'расторг контракт с фондом без причины');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (61, '2023-04-20 21:40:24.814549', 0, 0, 76561199323294531, 76561199033775223, 'расторг контракт с фондом без причины');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (62, '2023-04-21 15:31:03.726752', 0, 1, 76561199485488713, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (63, '2023-04-21 15:51:09.907193', 0, 0, 76561199440975766, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (64, '2023-04-21 15:51:20.169247', 0, 0, 76561199485488713, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (65, '2023-04-21 20:06:20.202664', 0, 1, 76561199497840893, 76561199027855046, '[2.3] Необоснованный выход из RP процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (66, '2023-04-21 20:07:31.971329', 0, 1, 76561199020025976, 76561199027855046, '[2.3] Необоснованный выход из RP процесса (незначительное).');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (67, '2023-04-21 21:03:25.079703', 0, 0, 76561199068450217, 76561199033775223, 'открытие дверери за 173');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (68, '2023-04-21 21:31:49.594856', 0, 0, 76561199145742995, 76561199027855046, '[2.6] FearRP (игнорировал наставленное оружие за класс D (уборщика)).');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (69, '2023-04-21 21:36:06.439495', 0, 0, 76561199441111449, 76561199027855046, '[1.4] Помеха работе администрации (Распространение заведомо ложной информации о игроке).');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (70, '2023-04-21 21:52:21.504023', 0, 1, 76561198807758524, 76561199027855046, '[2.3] Необоснованный выход из RP процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (71, '2023-04-21 22:28:37.834205', 0, 0, 76561199044335633, 76561199027855046, '[2.2] Non RP (частые прыжки + Non RP (знал, что такое устройство ПХ))');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (72, '2023-04-21 23:51:52.180922', 0, 0, 76561198115219881, 76561199021893795, '[2.2] Non RP. - Частые прыжки - Баннихоп');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (73, '2023-04-22 00:12:21.976290', 0, 0, 76561199249536272, 76561199021893795, '[4.7] SCP-939 - Преждевренный выход из камеры содержания + Не отыгрывает оглушение от Тесла-Ворот');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (74, '2023-04-22 10:54:10.243399', 0, 1, 76561198960324269, 1, '[2.1] Нарушение пункта 4.4 контракта с фондом за класс D');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (75, '2023-04-22 11:58:04.269632', 0, 1, 76561198052618634, 76561199027855046, 'Не стоял в камере 2 минуты от начала раунда за 939');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (76, '2023-04-22 11:59:56.507095', 0, 1, 76561199247142827, 76561199027855046, 'Использование SCP-330');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (77, '2023-04-22 12:44:53.453855', 0, 0, 76561198966590791, 1, '[2.2] Non RP (использовал допинг за МОГ)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (78, '2023-04-22 12:49:05.515161', 0, 0, 76561199176923102, 76561199027855046, '[2.2] Non RP (при смягчающих обстоятельствах)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (79, '2023-04-22 14:03:45.948816', 0, 0, 76561198960324269, 76561199027855046, '[2.2] Non RP (отыгрывал проверку за 049 + не боялся 939)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (80, '2023-04-22 18:53:19.534326', 0, 1, 76561199002546667, 76561199033775223, 'убил охранника за которым гнался 049-2 будучи охранником');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (81, '2023-04-22 23:48:45.616218', 0, 0, 76561199149120148, 76561199021893795, '[2.29] Лечение. - Не отыграл лечение.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (82, '2023-04-23 00:02:53.446155', 0, 0, 76561198129202211, 76561199021893795, '[4.5] SCP-173 - Открытие дверей, пока на него смотрели + преследование целей.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (83, '2023-04-23 00:37:30.889748', 0, 0, 76561199129544767, 76561199021893795, '[3.1] Персонал класса D - Беспричинное нарушение контракта с Фондом.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (84, '2023-04-23 00:41:30.827818', 0, 1, 76561199156060567, 76561199021893795, '[4.1] SCP-049 - Диалект.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (85, '2023-04-23 12:00:17.483844', 0, 0, 76561198998322556, 76561199027855046, '[2.2] Non RP (просто так взял 500 за ОСН)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (86, '2023-04-23 12:04:04.787519', 0, 0, 76561199446098489, 76561199027855046, '[2.2] Non RP (нарушение контракта без причины)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (87, '2023-04-23 12:05:36.802323', 0, 0, 76561199249536272, 76561198127069467, '[2.3] Необоснованный выход из RP процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (88, '2023-04-23 12:11:08.722348', 0, 0, 76561199231599606, 76561198127069467, '[2.6] Fear RP. Игнорирование летального/огнестрельного орудия.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (89, '2023-04-23 13:27:26.920509', 0, 0, 76561199495017606, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (90, '2023-04-23 13:38:05.546567', 0, 0, 76561199323294531, 76561199027855046, '[2.2] Non RP (открыл камеру 096 за ПХ)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (91, '2023-04-23 14:02:34.108202', 0, 1, 76561198089563046, 76561199027855046, '[2.2] Non RP (взял оружие просто так за Класс D)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (92, '2023-04-23 14:02:39.502382', 0, 1, 76561198007874141, 76561199027855046, '[2.2] Non RP (взял оружие просто так за Класс D)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (93, '2023-04-23 14:08:49.194471', 0, 1, 76561199158963070, 76561199008500586, '[2.16] Гермоворота');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (94, '2023-04-23 18:01:00.796671', 0, 0, 76561199485488713, 76561199021893795, '[4.1] SCP-049 - Не дал человеку знать что тот заражен, перед убийством.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (95, '2023-04-23 18:08:56.065301', 0, 0, 76561199440975766, 76561199021893795, '[2.2] Non RP - Выдача классу Д оружия за Охрану.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (96, '2023-04-23 18:21:43.478748', 0, 1, 76561199176356180, 76561199021893795, '[2.3] Выход из RP процесса - Необоснованный (Кричал в воздух "админ, админ")');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (97, '2023-04-23 20:28:02.417674', 0, 0, 76561199063471759, 76561199090280951, '[2.2] Non RP (при смягчающих обстоятельствах)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (98, '2023-04-23 20:52:33.842784', 0, 0, 76561199016394170, 76561199090280951, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (99, '2023-04-23 21:09:05.149831', 0, 1, 76561198992592271, 76561199090280951, '[2.9] Team Kill (одиночный случайный)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (100, '2023-04-23 21:22:57.816769', 0, 0, 76561198281033717, 76561199090280951, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (101, '2023-04-23 21:23:01.695328', 0, 0, 76561199163046941, 76561199090280951, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (102, '2023-04-23 21:57:45.809566', 0, 0, 76561199474005215, 76561199090280951, '[2.5] PowerGaming (Закрывал двери на бегу).');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (103, '2023-04-24 15:49:40.830062', 0, 0, 76561198217799351, 76561199033775223, 'открывал двери когда на него смотрят');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (104, '2023-04-24 15:57:46.330923', 0, 0, 76561199199042122, 76561199033775223, 'нарушение контракта без причины');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (105, '2023-04-24 16:51:44.526902', 0, 0, 76561199016394170, 76561199033775223, 'расторг контракт с фондом без причины');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (106, '2023-04-24 16:59:26.809311', 0, 0, 76561199020025976, 76561199033775223, 'знает как пользоватся оружием(criss vector) за д класс');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (107, '2023-04-24 17:16:21.145844', 0, 0, 76561199073812173, 76561199033775223, 'залез на стол');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (108, '2023-04-24 21:01:28.550637', 0, 0, 76561199467304260, 76561199033775223, '[2.17] Проявление разумности SCP объектов');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (109, '2023-04-24 21:47:05.189998', 0, 1, 76561199120114043, 76561199033775223, '[2.17] Проявление разумности SCP объектов');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (110, '2023-04-26 13:35:17.764831', 0, 1, 76561199149120148, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (111, '2023-04-26 13:36:52.455631', 0, 1, 76561199251150142, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (112, '2023-04-26 17:08:00.861801', 0, 0, 76561199020928369, 1, 'Использование карты О5 за СБ');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (113, '2023-04-27 20:32:41.309004', 0, 1, 76561199260427530, 76561198968146360, 'Неотыгрыш страха за SCP-049 при виде других SCP-объектов (игроку 12-13 лет, пока оставил под присмотром, так как выглядит более-менее адекватно)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (114, '2023-04-27 20:45:08.934449', 0, 0, 76561199129544767, 76561199033775223, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (115, '2023-04-27 21:39:34.908806', 0, 0, 76561199003468553, 76561199033775223, '[2.29] Нарушение правила лечения');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (116, '2023-04-27 21:58:54.033898', 0, 0, 76561199108213695, 76561199033775223, '[2.2] Non RP(убил человека когда на него смотрели 3 человека(случайно))');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (117, '2023-04-28 20:03:39.356227', 0, 0, 76561199485999504, 76561199090280951, '[2.2] Non RP (Баннихоп)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (118, '2023-04-28 22:14:48.176409', 0, 0, 76561198808721131, 76561199027855046, 'Non RP + 2.29');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (119, '2023-04-29 19:05:50.833512', 0, 0, 76561199199122532, 76561199033775223, '[2.17] Проявление разумности SCP объектов');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (120, '2023-04-29 19:54:51.039321', 0, 0, 76561199015272328, 76561199033775223, '[4.7] нарушение правила отыгрыша за 939');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (121, '2023-04-29 20:50:48.246800', 0, 0, 76561199182009921, 76561199033775223, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (122, '2023-04-29 21:27:11.475726', 0, 0, 76561198217887025, 76561199027855046, 'Бхоп');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (123, '2023-04-29 21:39:17.221750', 0, 1, 76561199330831014, 76561199027855046, 'Бхопил, но правила знает');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (124, '2023-04-29 21:40:18.618874', 0, 1, 76561198245865494, 76561199027855046, 'Бхопил');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (125, '2023-04-29 22:28:28.073610', 0, 0, 76561199068450217, 76561199027855046, 'Нарушение лечения');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (126, '2023-04-29 22:29:27.609820', 0, 1, 76561198992592271, 76561199027855046, 'ТК (случайный)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (127, '2023-04-30 13:18:29.971734', 0, 0, 76561199256830625, 76561199008500586, '[2.2] Non RP');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (128, '2023-04-30 14:25:46.618634', 0, 0, 76561199496771808, 76561199027855046, '[2.3] Необоснованный выход из RP процесса.');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (129, '2023-04-30 15:28:50.789504', 0, 0, 76561199212612346, 76561199033775223, '[2.5] PowerGaming (закрыл дверь на бегу)');
INSERT INTO scpsl7780.Warns (ID, IssuedAt, IsStaff, IsSilent, TargetID, IssuerID, Reason) VALUES (130, '2023-04-30 16:02:11.453237', 0, 0, 76561198272501544, 76561199033775223, '[2.8] MetaGaming');

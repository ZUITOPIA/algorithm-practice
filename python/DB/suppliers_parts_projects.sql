use s_p_p;

/* 1-1*/
select S_NUM
from SPJ
where J_NUM = 'J1'
order by S_NUM;

/* 1-2 */
select *
from SPJ
where QTY between 300 and 750;

/* 1-3 */
select P_NUM
from SPJ
inner join Supplier on SPJ.S_NUM = Supplier.S_NUM
inner join Project on SPJ.J_NUM = Project.J_NUM
where Supplier.CITY = 'London' and Project.CITY = 'London';

/* 1-4 */
select Supplier.CITY, Project.CITY
from SPJ
inner join Supplier on SPJ.S_NUM = Supplier.S_NUM
inner join Project on SPJ.J_NUM = Project.J_NUM
where Supplier.CITY != Project.CITY;

/* 2-1 */
select SPJ.P_NUM, SPJ.J_NUM, SUM(SPJ.QTY)
from SPJ
group by SPJ.P_NUM, SPJ.J_NUM;

/* 2-2 */
select SPJ.P_NUM
from SPJ
group by SPJ.P_NUM
having avg(SPJ.QTY) > 320;

/* 2-3 */
select J_NUM, CITY
from Project
where CITY like '_o%';

/* 2-4 */
select J_NUM
from  Project
where CITY = (
	select min(CITY)
    from Project
);

/* 2-5 */
select SPJ.J_NUM
from SPJ
where SPJ.P_NUM = 'P1'
group by SPJ.J_NUM
having avg(SPJ.QTY) > (
	select max(SPJ.QTY)
    from SPJ
    where SPJ.J_NUM = 'J1');

/* 3-1 */
select distinct P_NUM
from SPJ
where exists (
	select *
    from Project
    where Project.CITY = 'London');
    
/* 3-2 */
select J_NUM
from Project
where not exists (
	select *
    from SPJ
    where SPJ.J_NUM = Project.J_NUM 
    and SPJ.S_NUM in (
		select S_NUM
        from Supplier
        where CITY = 'London')
	and SPJ.P_NUM in (
		select P_NUM
        from Part
        where COLOR = 'Red'));
        
/* 3-3 : 모르겠음 */
select SPJ.J_NUM
from SPJ
where exists

/* 3-4 : 자꾸 오류 발생 (아마 버전 문제) */
select CITY from Supplier
union
select CITY from Part
union
select CITY from Project
order by CITY;

/* 4-1 */
set SQL_SAFE_UPDATES = 0; # disable safe mode

delete from Project
where J_NUM not in (
	select distinct J_NUM
    from SPJ);
    
set SQL_SAFE_UPDATES = 1; # enable safe mode


/* 4-2 */
insert into Supplier (S_NUM, SNAME, CITY, STATUS) values ('S10', 'Smith','New York', NULL);
    
/* 4-3 */
select distinct P_NUM
from SPJ
left join Supplier on SPJ.S_NUM = Supplier.S_NUM
left join Project on SPJ.J_NUM = Project.J_NUM
where Supplier.CITY = 'London' or Project.CITY = 'London';

/* 4-4 */
select distinct SPJ.J_NUM
from SPJ
left join Supplier on SPJ.S_NUM = Supplier.S_NUM
left join Project on SPJ.J_NUM = Project.J_NUM
where Project.CITY = 'London' or Supplier.CITY = 'London';

/* 5-1 */
create table Supplier (
  S_NUM varchar(45) primary key,
  SNAME varchar(45) not null,
  STATUS int,
  CITY varchar(45) not null);

create table Part (
  P_NUM varchar(45) primary key,
  PNAME varchar(45) not null,
  COLOR varchar(45) not null,
  WEIGHT int not null,
  CITY varchar(45) not null);

create table Project (
  J_NUM varchar(45) primary key,
  JNAME varchar(45) not null,
  CITY varchar(45) not null);

create table SPJ (
  S_NUM varchar(45) not null,
  P_NUM varchar(45) not null,
  J_NUM varchar(45) not null,
  QTY int,
  foreign key (S_NUM) references Supplier(S_NUM),
  foreign key (P_NUM) references Part(P_NUM),
  foreign key (J_NUM) references Project(J_NUM),
  primary key (S_NUM, P_NUM, J_NUM));

/* 5-2 */
create unique index SPJ_PK on SPJ(S_NUM, P_NUM, J_NUM);

/* 5-3 */
insert into Supplier (S_NUM, SNAME, CITY) values
('S1', 'Smith', 'London'),
('S2', 'Jones', 'Paris'),
('S3', 'Blake', 'Paris'),
('S4', 'Clark', 'London'),
('S5', 'Adams', 'Athens');

insert into Part (P_NUM, PNAME, COLOR, WEIGHT, CITY) values
('P1', 'Nut', 'Red', 12, 'London'),
('P2', 'Bolt', 'Green', 17, 'Paris'),
('P3', 'Screw', 'Blue', 17, 'Rome'),
('P4', 'Screw', 'Red', 14, 'London'),
('P5', 'Cam', 'Blue', 12, 'Paris'),
('P6', 'Cog', 'Red', 19, 'London');

insert into Project (J_NUM, JNAME, CITY) values
('J1', 'Sorter', 'Paris'),
('J2', 'Punch', 'Rome'),
('J3', 'Reader', 'Athens'),
('J4', 'Console', 'London'),
('J5', 'Collator', 'London'),
('J6', 'Terminal', 'Oslo'),
('J7', 'Tape', 'London');

insert into SPJ (S_NUM, P_NUM, J_NUM, QTY) values
('S1', 'P1', 'J1', 200),
('S1', 'P1', 'J4', 700),
('S2', 'P3', 'J1', 400),
('S2', 'P3', 'J2', 200),
('S2', 'P3', 'J3', 200),
('S2', 'P3', 'J4', 500),
('S2', 'P3', 'J5', 600),
('S2', 'P3', 'J6', 400),
('S2', 'P3', 'J7', 800),
('S2', 'P5', 'J2', 100),
('S3', 'P3', 'J1', 200),
('S3', 'P4', 'J2', 500),
('S4', 'P6', 'J3', 300),
('S4', 'P6', 'J7', 300),
('S5', 'P2', 'J2', 200),
('S5', 'P2', 'J4', 100),
('S5', 'P5', 'J5', 500),
('S5', 'P5', 'J7', 100),
('S5', 'P6', 'J2', 200),
('S5', 'P1', 'J4', 100),
('S5', 'P3', 'J4', 200),
('S5', 'P4', 'J4', 800),
('S5', 'P5', 'J4', 400),
('S5', 'P6', 'J4', 500);

/* 6-1 */
create view NotTheSame as
select S.S_NUM, P.P_NUM
from Supplier S, Part P
where S.CITY != P.CITY;

/* 6-2 */
create view LondonSup as
select *
from Supplier
where Supplier.CITY = 'London';

/* 6-3 : 모름 */


/* 6-4 보기 */
create view HEAVYWEIGHTS (PNUM, WT, COL)
	as select P_NUM, WEIGHT, COLOR
		from Part
        where WEIGHT > 14;
        
/* 6-4의 A 결과 */
select *
from HEAVYWEIGHTS
where COL = 'Green';

/* 6-4의 B 결과 */
set SQL_SAFE_UPDATES = 0; # disable safe mode

update HEAVYWEIGHTS
set COL = 'White'
where WT = 18;

set SQL_SAFE_UPDATES = 1; # enable safe mode

/* 6-4의 C 결과 */
set SQL_SAFE_UPDATES = 0; # disable safe mode

delete from HEAVYWEIGHTS
where WT < 10;

set SQL_SAFE_UPDATES = 1; # enable safe mode


/* 6-4의 D 결과 */
insert into HEAVYWEIGHTS (PNUM, WT, COL) values ('P99', 12, 'Purple');

drop table Part, Project, SPJ, Supplier;

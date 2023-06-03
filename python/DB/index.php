<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>1912943 고주희</title>
</head>
<body>
    <h1>2023 데이터베이스 봄학기 ESQL 과제 - WEB</h1>
    <?php
    $con = mysqli_connect("localhost", "root", "zuitopia", "MOVIE");
    $sql_create_table_USER = "
    create table User (
        U_ID varchar(30) primary key,
        PASSWORD varchar(30) not null,
        U_NAME varchar(30),
        SIGNUPDATE date
    );";

    $sql_insert_into_USER = "
    insert into User(U_ID, PASSWORD, U_NAME, SIGNUPDATE) values 
    ('best', '1111', '짱구', '2019-03-22'),
    ('bongbong', '2728', '봉미선', '2021-07-12'),
    ('hooneee', '2222', '훈이', '2019-03-23'),
    ('glass', '3333', '유리', '2019-04-01'),
    ('footsmell', '1920', '신형만', '2020-08-01'),
    ('snot', '4444', '맹구', '2019-04-01'),
    ('fewater', '5555', '철수', '2019-04-01'),
    ('baby', '0000', '짱아', '2016-06-19'),
    ('sorry', '1824', '채성아', '2023-05-26'),
    ('already', '9288', '나미리', '2022-09-15');
    ";

    $sql_create_table_DIRECTOR = "
    create table Director(
        D_ID varchar(30) primary key,
        D_NAME varchar(30),
        BIRTHDATE date,
        ADDRESS varchar(30)
    );";
    $sql_insert_into_DIRECTOR = "
    insert into Director (D_ID, D_NAME, BIRTHDATE, ADDRESS) values
    ('D1', '양우석', '1969-10-24', '서울특별시'),
    ('D2', '제니퍼 리', '1971-10-22', '전라남도'),
    ('D3', '강형철', '1974-03-01', '대전광역시'),
    ('D4', '봉준호', '1969-09-14', '충청남도'),
    ('D5', '김성훈', '1971-02-20', '부산광역시'),
    ('D6', '윤제균', '1969-05-14', '전라북도'),
    ('D7', '제임스 캐머런', '1954-08-16', '제주도'),
    ('D8', '류승완', '1973-12-15', '서울특별시'),
    ('D9', '크리스토퍼 놀란', '1970-07-30', '전라북도'),
    ('D10', '이환경', '1970-08-22', '서울특별시');";


    $sql_create_table_MOVIE = "
    create table Movie (
        M_ID varchar(30) primary key,
        TITLE varchar(30),
        OPENDATE date,
        PRICE int not null,
        D_ID varchar(30),
        foreign key (D_ID) references Director(D_ID) on update cascade on delete cascade
    );";
    $sql_insert_into_MOVIE = "
    insert into Movie(M_ID, TITLE, OPENDATE, PRICE, D_ID) values 
    ('M1', '기생충', '2019-05-30', 4000, 'D4'),
    ('M2', '과속스캔들', '2008-12-03', 300, 'D3'),
    ('M3', '베테랑', '2015-08-05', 1300, 'D8'),
    ('M4', '공조', '2017-01-18', 1200, 'D5'),
    ('M5', '7번방의 선물', '2013-01-23', 700, 'D10'),
    ('M6', '국제시장', '2014-12-17', 900, 'D6'),
    ('M7', '아바타', '2009-12-17', 1500, 'D7'),
    ('M8', '변호인', '2013-12-18', 1700, 'D1'),
    ('M9', '인터스텔라', '2014-11-06', 800, 'D9'),
    ('M0', '겨울왕국', '2014-01-16', 1100, 'D2');
    ";

    $sql_create_table_PAYMENT = "
    create table Payment (
        P_ID int auto_increment primary key,
        PAYDATE date,
        U_ID varchar(30),
        M_ID varchar(30),
        PRICE int, 
        foreign key (U_ID) references User(U_ID) on update cascade on delete cascade,
        foreign key (M_ID) references Movie(M_ID) on update cascade on delete cascade
    );";

    $sql_insert_into_PAYMENT = "
    insert into Payment (PAYDATE, U_ID, M_ID, PRICE) values
    ('2023-02-10', 'baby', 'M6', 900),
    ('2023-05-27', 'sorry', 'M4', 1200),
    ('2023-05-03', 'bongbong', 'M2', 300),
    ('2023-02-10', 'snot', 'M6', 900),
    ('2023-02-10', 'baby', 'M0', 1100),
    ('2023-02-10', 'baby', 'M5', 700),
    ('2023-04-02', 'already', 'M2', 300),
    ('2023-01-22', 'footsmell', 'M2', 300),
    ('2023-01-22', 'footsmell', 'M8', 1700),
    ('2023-01-23', 'glass', 'M0', 1100);";

    mysqli_query($con, $sql_create_table_USER);
    mysqli_query($con, $sql_create_table_DIRECTOR);
    mysqli_query($con, $sql_create_table_MOVIE);
    mysqli_query($con, $sql_create_table_PAYMENT);
    ?>

</body>
</html>
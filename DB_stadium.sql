create schema stadium;
use stadium;

create table Employee(
emp_id char(9),
`Name` varchar(30) NOT NULL,
Address varchar(100),
Sex char(1),
Salary int,
contact_no char(11) NOT NULL,
email varchar(50) NOT NULL,
DOB Date,
Dno char(5),
constraint pk_emp primary key(emp_id));

create table Department(
Dnumber char(5),
Dname varchar(30) NOT NULL,
mgrid char(9),
constraint pk_dep primary key(Dnumber),
constraint fk_dep foreign key(mgrid) references Employee(emp_id));

alter table Employee
add constraint fk_emp foreign key(Dno) references Department(Dnumber);

create table Shops(
shop_id char(4),
tenant_name varchar(30),
Rent int,
`status` char(1),
Bond_end_date DATE,
constraint pk_shops primary key(shop_id));

create table Equipment(
eq_id char(5),
category varchar(20),
eq_name varchar(30),
`status` char(1),
constraint pk_equi primary key(eq_id));

create table Uses(
eq_id char(5),
Dno char(5),
constraint pk_uses primary key(eq_id,Dno),
constraint fk_uses1 foreign key(eq_id) references Equipment(eq_id),
constraint fk_uses2 foreign key(Dno) references Department(Dnumber));

create table Customer(
cust_id int auto_increment,
`Name` varchar(30) NOT NULL,
`password` varchar(50) NOT NULL,
email varchar(50) NOT NULL,
contact_no char(11) NOT NULL,
constraint pk_cust primary key(cust_id));

create table `Event`(
ev_id char(5),
ev_name varchar(30),
`Date` Date,
`Time` Time,
seats_req int,
organised_by int,
price int NOT NULL,
constraint pk_event primary key(ev_id),
constraint fk_event foreign key(organised_by) references customer(cust_id));


create table Attends(
cust_id int,
ev_id char(5),
seat_id int,
constraint pk_attends primary key(cust_id,ev_id,seat_id),
constraint fk_attends1 foreign key(cust_id) references Customer(cust_id),
constraint fk_attends2 foreign key(ev_id) references `Event`(ev_id));



#DATA:-


insert into Employee
values
#managers
('989898989','Jaya Singh','B-09 Kalkaji, Delhi 110019','F',75000,'08765678909','imjaya677@gmail.com','1987-09-23',NULL),
('526341789','Shantanu Kumar','D-05 Sector 10 Dwarka, Delhi 110075','M',70000,'09462132531','shantanu007@gmail.com','1980-05-16',NULL),
('169874643','Amit Tripathi','C-20 , Palam, Delhi 110045','M',45000,'08562127792','amittpt21@gmail.com','1986-12-21',NULL),
('125841643','Aanya Singh','A-01  Malviya Nagar, Delhi 110017','F',58000,'08521627222','anu_aanya10@gmail.com','1982-10-04',NULL),
('542639856','Sharad Kumar Srivastava','C-06 Sector 10 Dwarka,Delhi 11075','M',60000,'0916328316','skssharad@gmail.com','1988-10-02',NULL),
('898989898','Pranav Arya','D-111-D Shakarpur, Delhi 110092','M',65000,'09865722890','cool.pranavarya@gmail.com','1990-08-15',NULL),

#00001
('619753248','Neeti Rani','B-201 Ganesh nagar,Pandav Nagar complex,Delhi 110092','F',52000,'07189325681','happy.neeti@gmail.com','1985-06-11',NULL),

#00002
('159874623','Anuj Sharma','B-16 Sanjay gram, Gurugram, Haryana 122001','M',50000,'09562487512','anuj_sharma1972@gmail.com','1979-02-25',NULL),

#00003
('362168716','Naman Kumar','C-10 Sanjay gram,Gurugram,Harayana 122001','M',22000,'07425932552','itsmenaman@gmail.com','1986-10-10',NULL),
('478965423','Aviral Sharma ','C-10  Palam, Delhi 110045','M',20000,'08794561232','aviS46@gmail.com','1985-04-06',NULL),

#00004
('795862314','Diksha Sharma','B-15 kalkaji, Delhi 110019','F',35000,'07421697855','diksharma159@gmail.com','1990-12-20',NULL),

#00005
('216833992','Krishna Singh','C-15 , Palam,Delhi 110045','M',30000,'09633123456','singh.krishna999@gmail.com','1985-03-15',NULL),

#00006
('349526888','Aditi Agarwal','D-115-C Shakarpur, Delhi 110092','F',55000,'07625983220','aditiA1000@gmail.com','1989-02-14',NULL);

insert into Department
values
('00001','Administraion','989898989'),
('00002','Sales','526341789'),
('00003','Gardening and plumbing','169874643'),
('00004','Housekeeping','125841643'),
('00005','Marketing','542639856'),
('00006','Security','898989898');

update Employee
set Dno='00001'
where emp_id='989898989';

update Employee
set Dno='00002'
where emp_id='526341789';

update Employee
set Dno='00003'
where emp_id='169874643';

update Employee
set Dno='00004'
where emp_id='125841643';

update Employee
set Dno='00005'
where emp_id='542639856';

update Employee
set Dno='00006'
where emp_id='898989898';


update Employee
set Dno='00003'
where emp_id='362168716';

update Employee
set Dno='00003'
where emp_id='478965423';

update Employee
set Dno='00001'
where emp_id='619753248';

update Employee
set Dno='00002'
where emp_id='159874623';

update Employee
set Dno='00004'
where emp_id='795862314';

update Employee
set Dno='00005'
where emp_id='216833992';

update Employee
set Dno='00006'
where emp_id='349526888';


insert into Customer(`Name`,`password`,email,contact_no)
values
('Amish Bibhu',md5('amish@bookseat'),'amish2546b@gmail.com','09526314752'),
('Nimisha Sinha',md5('nimisha98467'),'nimis001@gmail.com','08527416390'),
('Bibhor Jaiswal',md5('BiBhOrJ@123'),'bjBibhor@gmail.com','09635418723'),
('Ritika Nayan',md5('ritika.n123'),'ritu01ritika@gmail.com','08621547930'),
('Himanshu Kumar',md5('logmeinnow0123'),'himanshu082@gmail.com','09637526914'),
('Yashwant Kumar',md5('hiitsyashwant46'),'yash.kumar28@gmail.com','07531249652'),
('Piyush Srivastava',md5('123789@piyush'),'piyushS123789@gmail.com','07218541623'),
('Nidhi Raj',md5('nidhi@2000raj'),'raj.nidhi46@gmail.com','08651249532'),
('Atul Sinha',md5('5479atulS'),'a.t.u.l.s@gmail.com','08116325479'),
('Saurav Kumar',md5('skpassword555'),'sauravK555@gmail.com','08371524963');



insert into Equipment
values
('11111','Lights','Flood light 1','W'),
('12222','Lights','Flood light 2','W'),
('21111','Camera','Falcon IR camera','N'),
('22222','Camera','Tony Spider camera','W'),
('31111','Gardening','EM Grass cutter 101','N'),
('41111','Sound','JBL microphone','W'),
('42222','Sound','Kookaburra stump microphone','W');

insert into Shops
values
('1001','Gatik Jindal',50000,'O','2021-08-21'),
('1002','Adrit Jindal',50000,'O','2021-10-15'),
('1003','Vaibhav Agarwal',60000,'O','2021-05-23'),
('1004','Vansh Agarwal',60000,'O','2021-06-30'),
('1005','Vinayak Agarwal',60000,'O','2021-07-08'),
('1006','Veer Agarwal',60000,'O','2021-09-10'),
('1007',NULL,60000,'N',NULL);


insert into `Event`
values
('ev001','UT Fan Fest','2021-01-08','13:30',2000,7,1000),
('ev002','UP\'s Got Talent','2021-02-17','17:00',1000,6,800),
('ev003','Dhanji Trophy','2021-03-10','08:00',10000,5,2000);

insert into Uses
values
('11111','00004'),
('12222','00004'),
('21111','00006'),
('22222','00006'),
('31111','00003'),
('41111','00004'),
('42222','00004');


insert into Attends
values
(1,'ev001',1),
(2,'ev001',2),
(3,'ev001',3),
(4,'ev002',1),
(5,'ev002',2),
(1,'ev002',3),
(6,'ev003',1),
(7,'ev003',2),
(2,'ev003',3);




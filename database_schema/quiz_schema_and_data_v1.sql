DROP DATABASE IF EXISTS quiz;
CREATE DATABASE quiz;
USE quiz;

DROP TABLE IF EXISTS country;
CREATE TABLE country (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(20)
);

DROP TABLE IF EXISTS city;
CREATE TABLE city (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(20),
    country_id int(11) REFERENCES country ON DELETE NO ACTION ON UPDATE CASCADE

--     constraint fk_city_to_country foreign key (country) references country(id) On delete no action on update cascade
);

DROP TABLE IF EXISTS player;
CREATE TABLE player (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name varchar(20)
    );
    
    
DROP TABLE IF EXISTS quiz_session;
CREATE TABLE quiz_question (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    text varchar(255),
    location_id int(11) REFERENCES city ON DELETE NO ACTION ON UPDATE CASCADE
    
    -- constraint fk_quiz_question_to_location foreign key(location_id) references city(id) on delete no action on update cascade
    ); 
    
DROP TABLE IF EXISTS quiz_question_option;
CREATE TABLE quiz_question_option (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY ,
    text varchar(255),
    quiz_question_id int(11) REFERENCES quiz_question ON DELETE NO ACTION ON UPDATE CASCADE,
    is_correct tinyint(1)
   
   --  constraint fk_question_option_to_question foreign key(quiz_question_id) references quiz_question(id) on delete no action on update cascade
    ); 
    
DROP TABLE IF EXISTS quiz_session;
CREATE TABLE quiz_session (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
    player_id int(11) REFERENCES player ON DELETE NO ACTION ON UPDATE CASCADE,
    question_answers int(11) DEFAULT 0,
    correct_count int(11) DEFAULT 0,
	chances tinyint(4) default 3,
    is_open tinyint(1) default 1

--     constraint fk_quiz_session_to_player foreign key(player_id) references player(id) on delete no action on update cascade
    ); 
    
DROP TABLE IF EXISTS current_quiz_session;
CREATE TABLE current_quiz_session (
	id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
	session_id int(11) REFERENCES quiz_session ON DELETE NO ACTION ON UPDATE CASCADE,
    player_id int(11) REFERENCES player ON DELETE NO ACTION ON UPDATE CASCADE,
    question_id int(11) REFERENCES quiz_question ON DELETE NO ACTION ON UPDATE CASCADE,
    question_option_id int(11) REFERENCES quiz_question_option ON DELETE NO ACTION ON UPDATE CASCADE,
    is_correct int(11) 
    ); 


 -- insert data into table
insert into country(name)
values ("Finland"), ("Pakistan");

select * from country;


insert into city(name,country_id)
value("Helsinki",1), ("Islamabad",2);

select * from city;


insert into player(name)
value ("Trung"), ("Huy");

select * from player;

insert into quiz_question(text,location_id)
values ("What are Finnish households encouraged to recycle?",1),
("Which of the following is a common eco-friendly cleaning practice in Finland?",1),
("How is hazardous waste typically disposed of in Finland?",1),
("Jokamiehenoikeus or Everyman Right  allows people who live in Finland to:",1),
("Finland has a national program called 'Siisti Biitsi', which focuses on keeping the beaches clean. What does 'Siisti Biitsi' mean in English?",1),
("What are the primary sources of water pollution in Pakistan?’",2),
("What is a significant contributor to air pollution in major cities of Pakistan?",2),
("What is the major source of indoor air pollution in many rural areas of Pakistan, leading to health issues?",2),
("Which of the following environmental issues is a significant concern in Pakistan?",2),
("Which of the following environmental factors exacerbates air pollution in Pakistan's major cities?",2);

select * from quiz_question;    


insert into quiz_question_option(text,quiz_question_id,is_correct)
values ("Electronics and appliances",1,0), ("Hazardous chemicals",1,0),("Garden waste",1,0),("Glass, paper, and certain plastics",1,1),
("Using harsh chemical cleaners",2,0), ("Using single-use plastic cleaning tools ",2,0),("Using environmentally friendly cleaning products",2,1),("Disposing of cleaning waste in water bodies",2,0),
("It is thrown in regular household trash.",3,0),("It is recycled along with regular waste.",3,0),("It is taken to specialized collection points.",3,1),("It is buried in backyard pits.",3,0),
("Drive off-road vehicles anywhere in the wilderness",4,0),("Camp and pick berries and mushrooms on public and private lands",4,1),("Dump household waste in nature reserves",4,0),("Cut down trees in national parks for firewood",4,0),
("Beautiful Beaches",5,0),("Clean Coast",5,1),("Sunny Shores",5,0),("Pristine Seashores",5,0),
("Industrial discharge and agricultural runoff",6,1),("Volcanic activity and seismic disturbances",6,0),("Deforestation and urbanization",6,0),("Solar radiation and atmospheric dust",6,0),
("Excessive use of bicycles and electric vehicles",7,0),("Low population density and limited industrial activity",7,0),("High-quality public transportation systems",7,0),("Vehicular emissions and industrial pollutants",7,1),
("Factory emissions",8,0),("Agricultural practices",8,0),("Cooking with solid fuels like wood or dung",8,1),("Vehicle exhaust",8,0),
("Excessive rainfall and flooding",9,0),("Air pollution from industrial emissions",9,1),("Frequent earthquakes and tsunamis",9,0),("Abundant forest cover and biodiversity",9,0),
("Frequent sandstorms from neighboring deserts",10,0),("High-altitude geographical location",10,0),("Seasonal monsoon rains reducing pollution levels",10,0),("Geographic topography trapping pollutants",10,1);

select * from quiz_question_option;


insert into quiz_session(player_id)
value (1), (2);

select * from quiz_session;


insert into current_quiz_session ( session_id, player_id, question_id, question_option_id, is_correct)
value (1,1,1,1,0), (1,1,1,4,1);

select * from current_quiz_session;

update quiz_session 
set question_answers = 2, correct_count = 1 , chances = 2
where id = 1;

select * from quiz_session;






    
    
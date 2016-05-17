# ôîðìèðóåì áàçó
mysql -uroot -e "DROP DATABASE ASK"
mysql -uroot -e "CREATE DATABASE ASK"
mysql -uroot -e "CREATE USER 'sa'@'localhost' IDENTIFIED BY 'sa'"
mysql -uroot -e "GRANT ALL PRIVILEGES ON ASK.* TO 'sa'@'localhost'"

python /home/box/web/ask/manage.py syncdb

# Íàïîëíÿåì áàçó äëÿ ïðîâåðêè
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title1','qa1',3,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title2','qa2',1,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title3','qa3',6,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title4','qa4',8,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title5','qa5',12,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title6','qa6',15,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title7','qa7',2,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title8','qa8',1,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title9','qa9',2,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title10','qa10',3,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title11','qa11',10,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_question(title,text,rating, author_id) VALUES ('title12','qa12',6,1)"

mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer1', 1,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer1', 1,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer1', 1,1)"

mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer2', 2,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer2', 2,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer2', 2,1)"

mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer3', 3,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer3', 3,1)"
mysql -uroot -e "USE ASK; INSERT INTO ASK.qa_answer(text, question_id, author_id) VALUES ('answer3', 3,1)"

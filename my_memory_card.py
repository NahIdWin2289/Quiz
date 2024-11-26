from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QPushButton, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    group.hide()
    group2.show()
    button.setText('Следующий вопрос')

def show_question():
    group2.hide()
    group.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    button1.setChecked(False)
    button2.setChecked(False)
    button3.setChecked(False)
    button4.setChecked(False)
    RadioGroup.setExclusive(True)

def start_test():
    if button.text() == 'Ответить':
        check_ansvers()
    else:
        next_question()

def ask(q):
    shuffle(answers)
    question.setText(q.question)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    label2.setText(q.right_answer)
    show_question()

def check_ansvers():
    if answers[0].isChecked():
        label1.setText('Правильно')
        main_win.cur_right_answer += 1
    else:
        label1.setText('Неправильно')
    main_win.cur_answers += 1
    label3.setText('Счетчик правильных ответов:' + str(main_win.cur_right_answer) + ' из ' + str(main_win.cur_answers))
    show_result()

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(question_list):
        main_win.cur_question = 0
    ask(question_list[main_win.cur_question])
    

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Викторина о Доте 2')
main_win.resize(400, 400)
main_win.cur_question = -1
main_win.cur_right_answer = 0 
main_win.cur_answers = 0
question = QLabel('Какой национальности не существует?') 
label1 = QLabel('Правильно/Неправильно') 
label2 = QLabel('Правильный ответ')
label3 = QLabel('Счетчик правильных ответов:' + str(main_win.cur_right_answer) + ' из ' + str(main_win.cur_answers))
group2 = QGroupBox('Результат теста')
button1 = QRadioButton('Энцы')
button2 = QRadioButton('Чулмцы')
button3 = QRadioButton('Смурфы')
button4 = QRadioButton('Алеуты')
answers = [button1, button2, button3, button4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(button1)
RadioGroup.addButton(button2)
RadioGroup.addButton(button3)
RadioGroup.addButton(button4)
group = QGroupBox('Варианты ответов')
button = QPushButton('Ответить')
group_layout = QVBoxLayout()
layout_main = QVBoxLayout()
main_layout = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout1.addWidget(button1, alignment = Qt.AlignCenter)
layout1.addWidget(button3, alignment = Qt.AlignCenter)
layout2.addWidget(button2, alignment = Qt.AlignCenter)
layout2.addWidget(button4, alignment = Qt.AlignCenter)
group_layout.addWidget(label1, alignment = Qt.AlignLeft)
group_layout.addWidget(label2, alignment = Qt.AlignCenter)
main_layout.addLayout(layout1)
main_layout.addLayout(layout2)
group.setLayout(main_layout)
group2.setLayout(group_layout)
layout_main.addWidget(question, alignment = Qt.AlignCenter)
layout_main.addWidget(group)
layout_main.addWidget(group2)
layout_main.addWidget(button, alignment = Qt.AlignCenter)
layout_main.addWidget(label3, alignment = Qt.AlignCenter)
group2.hide()
# здаесь обработка событий
button.clicked.connect(start_test)
question_list = [Question('Сколько персонажей в игре', '123', '145', '130', '133'),
 Question('Какой персонаж взорвал свою деревню', 'Techies', 'Tinker', 'Shadow Fiend', 'Pudge'),
  Question('Какой персонаж способен полностью перезаряжать свои способности', 'Tinker', 'Shadow Demon', 'Lina', 'Drow Ranger'), 
  Question('Сколько лет игре Dota 2', '11 лет ', '5 лет', '12 года', '19 лет'), 
  Question('Какая команда выйграла на крайнем The International', 'Team Spirit', 'Navi', 'OG', 'GG'), 
  Question('Кто является самым известным игроком на Pudge', 'Денди', 'Симпл', 'Калапс', 'Яторо'), 
  Question('Какой персонаж состоит из воды', 'Morfling', 'Lina', 'Sniper', 'Rubick'), 
  Question('Какой персонаж может воровать способности', 'Rubick', 'Techies', 'Outworld Destroyer', 'Axe'), 
  Question('Какого персонажа зовут так же как и тапор', 'Axe', 'Dawnbreaker', 'Lion', 'Centaur Warrunner'),
  Question('Какой персонаж умеет останавливать время', 'Faceless Void', 'Riki', 'Bounty Hunter', 'Arc Warden')]
next_question()



main_win.setLayout(layout_main)
main_win.show()
app.exec()
#PROBLEMAS = LOGIN NAO FUNCIONA / TERMINAR INTEFACE DA CALCULADORA / TERMINAR OS CALCULOS / AJEITAR O BANCO DE DADOS
import sys
import time
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel, QGridLayout, QSizePolicy
from PyQt6.QtGui import QIcon, QFont


usuario ="123"
senha ="123"

ataquebranco = 1
ataqueverde = 1
taxacritica = 1
danocritico = 1
bonusataquen = 1
bonusataquec = 1
bonusskill = 1
bonusultimate = 1

talento1n = 1
talento1c = 1
talento2 = 1
talento3 = 1


Aataquebase = 1
Aataquebonus = 1
Ataxacritica = 1
Adanocritico = 1
Abonusataquen = 1
Abonusataquec = 1
Abonusskill = 1
Abonusultimate = 1

effatk = 1
modcrit = 1
modbonus = 1

Dano1 = 1
Dano2 = 1
Dano3 = 1
Dano4 = 1

DPS1 = 1
DPS2 = 1
DPS3 = 1
DPS4 = 1


class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(800,720)
        # label = QLabel('Calculadora Genshin', parent=self)
        # label.setGeometry(1000, 0, 200, 35)
        status = QLabel('Status', parent=self)
        status.setGeometry(10, 0, 250, 35)
        status.setFont(QFont('Arial', 15))
        talentos = QLabel('Modificadores de Talentos', parent=self)
        talentos.setGeometry(180, 0, 250, 35)
        talentos.setFont(QFont('Arial', 15))
        armas = QLabel('Armas e Sets de Artefatos', parent=self)
        armas.setGeometry(440, 0, 250, 35)
        armas.setFont(QFont('Arial', 15))

        result = QLabel('Resultados dos Calculos', parent=self)
        result.setGeometry(10, 450, 250, 35)
        result.setFont(QFont('Arial', 15))

        self.setWindowIcon(QIcon("xiangling.png"))
        self.setWindowTitle("Calculadora Genshin Avançada")


        labels = {}
        self.lineEdits = {}







        labels['1a'] = QLabel(self)
        labels['1a'].setText('Ataque branco')
        labels['1a'].move(10, 35)
        self.lineEdits['1a'] = QLineEdit(self)
        self.lineEdits['1a'].move(140, 35)
        self.lineEdits['1a'].resize(50, 32)


        labels['2a'] = QLabel(self)
        labels['2a'].setText('Ataque Verde')
        labels['2a'].move(10, 75)
        self.lineEdits['2a'] = QLineEdit(self)
        self.lineEdits['2a'].move(140, 75)
        self.lineEdits['2a'].resize(50, 32)

        labels['3a'] = QLabel(self)
        labels['3a'].setText('Taxa crítica')
        labels['3a'].move(10, 115)
        self.lineEdits['3a'] = QLineEdit(self)
        self.lineEdits['3a'].move(140, 115)
        self.lineEdits['3a'].resize(50, 32)

        labels['4a'] = QLabel(self)
        labels['4a'].setText('Dano Crítico')
        labels['4a'].move(10, 155)
        self.lineEdits['4a'] = QLineEdit(self)
        self.lineEdits['4a'].move(140, 155)
        self.lineEdits['4a'].resize(50, 32)

        labels['5a'] = QLabel(self)
        labels['5a'].setText('Bonus ataque normal')
        labels['5a'].setGeometry(10, 195, 200, 35)
        self.lineEdits['5a'] = QLineEdit(self)
        self.lineEdits['5a'].move(140, 195)
        self.lineEdits['5a'].resize(50, 32)

        labels['6a'] = QLabel(self)
        labels['6a'].setText('Bonus ataque carregado')
        labels['6a'].setGeometry(10, 235, 200, 35)
        self.lineEdits['6a'] = QLineEdit(self)
        self.lineEdits['6a'].move(140, 235)
        self.lineEdits['6a'].resize(50, 32)

        labels['7a'] = QLabel(self)
        labels['7a'].setText('Bonus Skill')
        labels['7a'].move(10, 275)
        self.lineEdits['7a'] = QLineEdit(self)
        self.lineEdits['7a'].move(140, 275)
        self.lineEdits['7a'].resize(50, 32)

        labels['8a'] = QLabel(self)
        labels['8a'].setText('Bonus Ultimate')
        labels['8a'].move(10, 315)
        self.lineEdits['8a'] = QLineEdit(self)
        self.lineEdits['8a'].move(140, 315)
        self.lineEdits['8a'].resize(50, 32)


        labels['1b'] = QLabel(self)
        labels['1b'].setText('Modificador ataque normal')
        labels['1b'].setGeometry(200, 35, 150, 35)
        self.lineEdits['1b'] = QLineEdit(self)
        self.lineEdits['1b'].move(370, 35)
        self.lineEdits['1b'].resize(50, 32)

        labels['2b'] = QLabel(self)
        labels['2b'].setText('Modificador ataque carregado')
        labels['2b'].setGeometry(200, 75, 180, 35)
        self.lineEdits['2b'] = QLineEdit(self)
        self.lineEdits['2b'].move(370, 75)
        self.lineEdits['2b'].resize(50, 32)

        labels['3b'] = QLabel(self)
        labels['3b'].setText('Modificador de skill')
        labels['3b'].setGeometry(200, 115, 150, 35)
        self.lineEdits['3b'] = QLineEdit(self)
        self.lineEdits['3b'].move(370, 115)
        self.lineEdits['3b'].resize(50, 32)

        labels['4b'] = QLabel(self)
        labels['4b'].setText('Modificador de ultimate')
        labels['4b'].setGeometry(200, 155, 150, 35)
        self.lineEdits['4b'] = QLineEdit(self)
        self.lineEdits['4b'].move(370, 155)
        self.lineEdits['4b'].resize(50, 32)


        labels['1c'] = QLabel(self)
        labels['1c'].setText('Dano Base da Arma')
        labels['1c'].setGeometry(440, 35, 150, 35)
        self.lineEdits['1c'] = QLineEdit(self)
        self.lineEdits['1c'].move(580, 35)
        self.lineEdits['1c'].resize(50, 32)

        labels['2c'] = QLabel(self)
        labels['2c'].setText('Ataque bonus')
        labels['2c'].setGeometry(440, 75, 150, 35)
        self.lineEdits['2c'] = QLineEdit(self)
        self.lineEdits['2c'].move(580, 75)
        self.lineEdits['2c'].resize(50, 32)

        labels['3c'] = QLabel(self)
        labels['3c'].setText('Taxa Crítica Bonus')
        labels['3c'].setGeometry(440, 115, 150, 35)
        self.lineEdits['3c'] = QLineEdit(self)
        self.lineEdits['3c'].move(580, 115)
        self.lineEdits['3c'].resize(50, 32)

        labels['4c'] = QLabel(self)
        labels['4c'].setText('Dano Crítico Bonus')
        labels['4c'].setGeometry(440, 155, 150, 35)
        self.lineEdits['4c'] = QLineEdit(self)
        self.lineEdits['4c'].move(580, 155)
        self.lineEdits['4c'].resize(50, 32)

        labels['5c'] = QLabel(self)
        labels['5c'].setText('Bonus ataque normal')
        labels['5c'].setGeometry(440, 195, 150, 35)
        self.lineEdits['5c'] = QLineEdit(self)
        self.lineEdits['5c'].move(580, 195)
        self.lineEdits['5c'].resize(50, 32)

        labels['6c'] = QLabel(self)
        labels['6c'].setText('Bonus ataque carregado')
        labels['6c'].setGeometry(440, 235, 235, 35)
        self.lineEdits['6c'] = QLineEdit(self)
        self.lineEdits['6c'].move(580, 235)
        self.lineEdits['6c'].resize(50, 32)

        labels['7c'] = QLabel(self)
        labels['7c'].setText('Bonus de skill')
        labels['7c'].setGeometry(440, 275, 150, 35)
        self.lineEdits['7c'] = QLineEdit(self)
        self.lineEdits['7c'].move(580, 275)
        self.lineEdits['7c'].resize(50, 32)

        labels['8c'] = QLabel(self)
        labels['8c'].setText('Bonus de ultimate')
        labels['8c'].setGeometry(440, 315, 150, 35)
        self.lineEdits['8c'] = QLineEdit(self)
        self.lineEdits['8c'].move(580, 315)
        self.lineEdits['8c'].resize(50, 32)







        labels['dano1'] = QLabel(self)
        labels['dano1'].setText('Dano Ataque Normal')
        labels['dano1'].setGeometry(10, 500, 150, 35)
        self.lineEdits['dano1'] = QLineEdit(self)
        self.lineEdits['dano1'].move(140, 500)
        self.lineEdits['dano1'].resize(50, 32)

        labels['dano2'] = QLabel(self)
        labels['dano2'].setText('Dano Ataque Carregado')
        labels['dano2'].setGeometry(10, 540, 150, 35)
        self.lineEdits['dano2'] = QLineEdit(self)
        self.lineEdits['dano2'].move(140, 540)
        self.lineEdits['dano2'].resize(50, 32)

        labels['dano3'] = QLabel(self)
        labels['dano3'].setText('Dano de Skill')
        labels['dano3'].setGeometry(10, 580, 150, 35)
        self.lineEdits['dano3'] = QLineEdit(self)
        self.lineEdits['dano3'].move(140, 580)
        self.lineEdits['dano3'].resize(50, 32)

        labels['dano4'] = QLabel(self)
        labels['dano4'].setText('Dano de Ultimate')
        labels['dano4'].setGeometry(10, 620, 150, 35)
        self.lineEdits['dano4'] = QLineEdit(self)
        self.lineEdits['dano4'].move(140,620)
        self.lineEdits['dano4'].resize(50, 32)


        labels['DPS1'] = QLabel(self)
        labels['DPS1'].setText('Dano efetivo ataque normal')
        labels['DPS1'].setGeometry(200, 500, 150, 35)
        self.lineEdits['DPS1'] = QLineEdit(self)
        self.lineEdits['DPS1'].move(370, 500)
        self.lineEdits['DPS1'].resize(50, 32)


        labels['DPS2'] = QLabel(self)
        labels['DPS2'].setText('Dano efetivo ataque carregado')
        labels['DPS2'].setGeometry(200, 540, 200, 35)
        self.lineEdits['DPS2'] = QLineEdit(self)
        self.lineEdits['DPS2'].move(370, 540)
        self.lineEdits['DPS2'].resize(50, 32)

        labels['DPS3'] = QLabel(self)
        labels['DPS3'].setText('Dano efetivo Skill')
        labels['DPS3'].setGeometry(200, 580, 150, 35)
        self.lineEdits['DPS3'] = QLineEdit(self)
        self.lineEdits['DPS3'].move(370, 580)
        self.lineEdits['DPS3'].resize(50, 32)

        labels['DPS4'] = QLabel(self)
        labels['DPS4'].setText('Dano efetivo Ultimate')
        labels['DPS4'].setGeometry(200, 620, 150, 35)
        self.lineEdits['DPS4'] = QLineEdit(self)
        self.lineEdits['DPS4'].move(370, 620)
        self.lineEdits['DPS4'].resize(50, 32)




        self.create_widgets1()












    def create_widgets1(self):
        btn = QPushButton("calcular",self)
        btn.setGeometry(580, 620, 75, 50)
        btn.setStyleSheet('background-color:red')
        btn.setIcon(QIcon("xiangling.png"))
        btn.clicked.connect(self.clicked_bnt)



        self.label = QLabel("   Esperando", self)
        self.label.setGeometry(580, 680, 75, 20)
        self.label.setStyleSheet('background-color:green')
        self.label.setFont(QFont("Times New Roman", 10))

    def clicked_bnt(self):
        self.label.setText("    calculado")
        self.label.setStyleSheet('background-color:blue')
        ataquebranco = float(self.lineEdits['1a'].text())
        ataqueverde = float(self.lineEdits['2a'].text())
        taxacritica = float(self.lineEdits['3a'].text())
        danocritico = float(self.lineEdits['4a'].text())
        bonusataquen = float(self.lineEdits['5a'].text())
        bonusataquec = float(self.lineEdits['6a'].text())
        bonusskill = float(self.lineEdits['7a'].text())
        bonusultimate = float(self.lineEdits['8a'].text())

        talento1n = float(self.lineEdits['1b'].text())
        talento1c = float(self.lineEdits['2b'].text())
        talento2 = float(self.lineEdits['3b'].text())
        talento3 = float(self.lineEdits['4b'].text())


        Aataquebase = float(self.lineEdits['1c'].text())
        Aataquebonus = float(self.lineEdits['2c'].text())
        Ataxacritica = float(self.lineEdits['3c'].text())
        Adanocritico = float(self.lineEdits['4c'].text())
        Abonusataquen = float(self.lineEdits['5c'].text())
        Abonusataquec = float(self.lineEdits['6c'].text())
        Abonusskill = float(self.lineEdits['7c'].text())
        Abonusultimate = float(self.lineEdits['8c'].text())

        bonus1 = bonusataquen + Abonusataquen
        bonus2 = bonusataquec + Abonusataquec
        bonus3 = bonusskill + Abonusskill
        bonus4 = bonusultimate + Abonusultimate

        effatk = ataqueverde // ataquebranco
        modcrit = (taxacritica + Ataxacritica) * (danocritico + Adanocritico) // 100
        modbonus = (bonus1 + bonus2 + bonus3 + bonus4) // 4

        Dano1 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento1n / 100) * (1 + (bonus1 / 100)) * (1 + ((danocritico + Adanocritico) / 100))
        Dano2 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento1c / 100) * (1 + (bonus2 / 100)) * (1 + ((danocritico + Adanocritico) / 100))
        Dano3 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento2 / 100) * (1 + (bonus3 / 100)) * (1 + ((danocritico + Adanocritico) / 100))
        Dano4 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento3 / 100) * (1 + (bonus4 / 100)) * (1 + ((danocritico + Adanocritico) / 100))

        DPS1 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento1n / 100) * (1 + (bonus1 / 100)) * (1 + (modcrit / 100))
        DPS2 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento1c / 100) * (1 + (bonus2 / 100)) * (1 + (modcrit / 100))
        DPS3 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento2 / 100) * (1 + (bonus3 / 100)) * (1 + (modcrit / 100))
        DPS4 = (ataquebranco + ataqueverde + (ataquebranco*Aataquebonus)) * (talento3 /100) * (1 + (bonus4 / 100)) * (1 + (modcrit / 100))

        self.lineEdits['dano1'].setText(str(round(Dano1, 2)))
        self.lineEdits['dano2'].setText(str(round(Dano2, 2)))
        self.lineEdits['dano3'].setText(str(round(Dano3, 2)))
        self.lineEdits['dano4'].setText(str(round(Dano4, 2)))
        self.lineEdits['DPS1'].setText(str(round(DPS1, 2)))
        self.lineEdits['DPS2'].setText(str(round(DPS2, 2)))
        self.lineEdits['DPS3'].setText(str(round(DPS3, 2)))
        self.lineEdits['DPS4'].setText(str(round(DPS4, 2)))

        print(Dano1)
        print(Dano2)
        print(Dano3)
        print(Dano4)

        print(DPS1)
        print(DPS2)
        print(DPS3)
        print(DPS4)

        print(effatk)
        print(modcrit)





        # btn.clicked.connect(self.dano)

    # def dano(self):
    #
    #     bonus1 = bonusataquen + Abonusataquen
    #     bonus2 = bonusataquec + Abonusataquec
    #     bonus3 = bonusskill + Abonusskill
    #     bonus4 = bonusultimate + Abonusultimate
    #
    #
    #     effatk = ataqueverde//ataquebranco
    #     modcrit = taxacritica * danocritico//100
    #     modbonus = (bonus1 + bonus2 + bonus3 + bonus4)//4
    #
    #
    #
    #     Dano1 = (ataquebranco + ataqueverde) * talento1n//100 * (1+(bonus1//100)) * (1+(danocritico//100))
    #     Dano2 = (ataquebranco + ataqueverde) * talento1c//100 * (1+(bonus2//100)) * (1+(danocritico//100))
    #     Dano3 = (ataquebranco + ataqueverde) * talento2//100 * (1+(bonus3//100)) * (1+(danocritico//100))
    #     Dano4 = (ataquebranco + ataqueverde) * talento3//100 * (1+(bonus4//100)) * (1+(danocritico//100))
    #
    #     DPS1 = (ataquebranco + ataqueverde) * talento1n//100 * (1+(bonus1//100)) * (1+(modcrit//100))
    #     DPS2 = (ataquebranco + ataqueverde) * talento1c//100 * (1+(bonus2//100)) * (1+(modcrit//100))
    #     DPS3 = (ataquebranco + ataqueverde) * talento2//100 * (1+(bonus3//100)) * (1+(modcrit//100))
    #     DPS4 = (ataquebranco + ataqueverde) * talento3//100 * (1+(bonus4//100)) * (1+(modcrit//100))
    #
    #     print(Dano1)
    #     print(Dano2)
    #     print(Dano3)
    #     print(Dano4)
    #
    #     print(DPS1)
    #     print(DPS2)
    #     print(DPS3)
    #     print(DPS4)







class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janela de Acesso")
        self.window_width, self.window_height = 600, 150
        self.setFixedSize(self.window_width, self.window_height)
        self.setWindowIcon(QIcon("xiangling.png"))
        self.setWindowTitle("Calculadora Genshin Avançada")

        layout = QGridLayout()
        self.setLayout(layout)

        labels = {}
        self.lineEdits = {}

        labels['Usuário'] = QLabel('Usuário')
        labels['Senha'] = QLabel('Senha')
        labels['Usuário'].setSizePolicy(QSizePolicy.Policy.Fixed,QSizePolicy.Policy.Fixed)
        labels['Senha'].setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)

        labels['usu'] = QLabel(f'Usuário correto: {usuario}')
        labels['pass'] = QLabel(f'Senha correta: {senha}')
        layout.addWidget(labels['usu'], 2, 2, 1, 1)
        layout.addWidget(labels['pass'], 2, 3, 1, 1)

        self.lineEdits['Usuário'] = QLineEdit()
        self.lineEdits['Senha'] = QLineEdit()
        self.lineEdits['Senha'].setEchoMode(QLineEdit.EchoMode.Password)

        layout.addWidget(labels['Usuário'],            0, 0, 1, 1)
        layout.addWidget(self.lineEdits['Usuário'],    0, 1, 1, 3)

        layout.addWidget(labels['Senha'],              1, 0, 1, 1)
        layout.addWidget(self.lineEdits['Senha'],      1, 1, 1, 3)

        button_login = QPushButton('&Log in', clicked=self.checkCreditial)
        layout.addWidget(button_login, 2, 4, 1, 1)

        self.status = QLabel('')
        self.status.setStyleSheet('font-size: 25px; color:red')
        layout.addWidget(self.status, 3, 0, 1, 3)

        #self.connectToDB()

    # def connectToDB(self):
    #
    #     # https://doc.qt.io/qt-5/sql-driver.html
    #     db = QSqlDatabase.addDatabase('QODBC')
    #     db.setDatabaseName('Driver = {{Microsoft Acess Driver (*.mdb, *.accdb)}}; DBQ= {0}'.format(os.path.join(os.getcwd(), 'Users.accdb')))
    #
    #     if not db.open():
    #         self.status.setText('Connection failed')

    def checkCreditial(self):
        username = self.lineEdits['Usuário'].text()
        password = self.lineEdits['Senha'].text()



        if usuario == username:
            if password == senha:
                time.sleep(1)
                self.mainApp = MainApp()
                self.mainApp.show()
                self.close()
            else:
                self.status.setText('Senha errada')
        else:
            self.status.setText('Usuário errado')



        # query = QSqlQuery()
        # query.prepare('Insert INTO person (Usuário)')
        # query.bindValue(':Usuário', username)
        # query.exec()
        #
        # if query.first():
        #     if query.value('Senha') == password:
        #         time.sleep(1)
        #         self.mainApp = MainApp()
        #         self.mainApp.show()
        #         self.close()
        #     else:
        #         self.status.setText('Senha está errada')
        # else:
        #     self.setText('Usuário não foi encontrado')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet('''
        Qwidget {
            font-size: 25px;
        }
        QLineEdit{
            height: 25px;
        }
    ''')
    loginWindow = LoginWindow()
    loginWindow.show()

    try:
        sys.exit(app.exec())
    except SystemExit:
        print('Closing Window...')


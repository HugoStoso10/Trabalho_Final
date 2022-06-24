import tkinter as tk
from tkcalendar import DateEntry #pip install tkcalendar <- para instalar a biblioteca
from Base_dados import conexao_sql
from PIL import ImageTk, Image

#------------------------------JANELA REGISTER------------------------------------------------------
#Janela de register
def register(): #variaveis das Entrys: nome, apelido, nickname, email, data, password, confirmpass, erro
    window2 = tk.Tk()
    window2.geometry("1280x720")
    window2.resizable(0,0)  #impede a alteração do tamanho da janela
    imagem2 = Image.open('imagens\\bg_janela2.jpeg')
    imagem2 = ImageTk.PhotoImage(imagem2)
    bg2 = tk.Label(window2, image=imagem2)
    bg2.image = imagem1
    bg2.pack()

    # funcionalidade do botão iniciar sessão em alternativa: fecha janela de criar conta e abre a janela de login
    def login2():
        window2.destroy()
        ecra2()

    window2.title("433 G4M3C3NT3R - Criar conta")
    tk.Label(window2, text="Preencha os seguintes campos para criar uma conta",font=("", 15), bg="white").place(x=750, y=50)
    tk.Label(window2, text="Nome:", font=("", 15), bg="white").place(x=730, y=110)
    nome = tk.Entry(window2, width=25)
    nome.place(x=792, y=117)
    nomeerro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    nomeerro.place(x=730, y=140)
    tk.Label(window2, text="Apelido:", font=("", 15), bg="white").place(x=970, y=110)
    apelido = tk.Entry(window2, width=25)
    apelido.place(x=1045, y=117)
    apelidoerro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    apelidoerro.place(x=970, y=140)
    tk.Label(window2, text="Nome de utilizador:", font=("", 15), bg="white").place(x=730, y=160)
    nickname = tk.Entry(window2, width=25)
    nickname.place(x=902, y=167)
    nickerro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    nickerro.place(x=730, y=190)
    tk.Label(window2, text="Email:", font=("", 15), bg="white").place(x=730, y=220)
    email = tk.Entry(window2, width=35)
    email.place(x=787, y=225)
    emailerro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    emailerro.place(x=730, y=250)
    tk.Label(window2, text="Data de nascimento:", font=("", 15), bg="white").place(x=730, y=270)
    data = DateEntry(window2,width=25)
    data.place(x=917, y=275)
    tk.Label(window2, text="Palavra-passe:", font=("", 15), bg="white").place(x=730, y=300)
    pass_str = tk.StringVar()
    confirm = tk.StringVar()
    password = tk.Entry(window2, width=25, show="*", textvariable=pass_str)
    password.place(x=866, y=306)
    passerro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    passerro.place(x=740, y=330)
    tk.Label(window2, text="Confirme:", font=("", 15), bg="white").place(x=1030, y=300)
    confirmpass = tk.Entry(window2, width=25, show="*", textvariable=confirm)
    confirmpass.place(x=1119, y=306)
    passconferro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    passconferro.place(x=1030, y=330)
    a = tk.IntVar(value=0)
    #Função do checkbutton mostrarpass
    def mostarpass():
        if (a.get()==1):
            password.config(show='')
            confirmpass.config(show='')
        else:
            password.config(show='*')
            confirmpass.config(show='*')

    mostarpass = tk.Checkbutton(window2, text="Mostrar palavra-passe", variable=a, onvalue=1, offvalue=0, command=mostarpass)
    mostarpass.place(x=730, y=350)
    confirmpasserro = tk.Label(window2, text="", font=("", 9), fg="red", bg="white")
    confirmpasserro.place(x=730, y=330)
    criadosucesso = tk.Label(window2, text="", font=("", 9), fg="green", bg="white")
    criadosucesso.place(x=820, y=430)
    # Inserir valores na base dados e sistema de erro de register
    def Inserir_BD():
        a, b, c, d, e, f = len(nome.get()), len(apelido.get()), len(nickname.get()), len(email.get()), len(password.get()), len(confirmpass.get())
         # Erro1 - nome não foi inserido
        if a == 0:
            nomeerro.config(text="O nome não foi inserido")
        else:
            nomeerro.config(text="")
        # Erro2 - apelido não foi inserido
        if b == 0:
            apelidoerro.config(text="O apelido não foi inserido")
        else:
            apelidoerro.config(text="")
        # Erro3 - username não foi inserido
        if c == 0:
            nickerro.config(text="O nome de utilizador não foi inserido")
        else:
            nickerro.config(text="")
        # Erro4 - email não foi inserido
        if d == 0:
            emailerro.config(text="O email não foi inserido")
        else:
            emailerro.config(text="")
        # Erro5 - password não foi inserido
        if e == 0:
            passerro.config(text="A palavra-passe não foi inserida")
        else:
            passerro.config(text="")
        # Erro6 - confirmar password não foi inserido
        if f == 0:
            passconferro.config(text="A confirmação de palavra-passe não foi inserida")
        else:
            passconferro.config(text="")
        # Erro7 - password e confirmar password são diferentes
        if (e!=0) and (f!=0):
            if password.get() != confirmpass.get():
                confirmpasserro.config(text="A palavra-passe não é igual")
            else:
                confirmpasserro.config(text="")

        if (a!=0) and (b!=0) and (c!=0) and (d!=0) and (e!=0) and (f!=0) and (password.get() == confirmpass.get()):
            try:
                print(nome.get())
                cursor = conexao_sql()
                comando = f'''INSERT INTO users(nome, apelido, nickname, email,password,data)
                    VALUES ('{nome.get()}','{apelido.get()}','{nickname.get()}','{email.get()}','{password.get()}','{data.get()}')'''
                cursor.execute(comando)
                cursor.commit()
                criadosucesso.config(text='Conta criada com Sucesso. Clique em login para iniciar sessão')
            except:  # pois o campo nickname na base dados é unico
                nickerro.config(text='Nome de utilizador já utilizado')

    tk.Button(window2, text="Criar conta", font=("", 15),command=Inserir_BD).place(x=940, y=460)
    tk.Button(window2, text="iniciar sessão em alternativa", font=("", 15), command=login2).place(x=860, y=500)
    window2.mainloop()

#------------------------------JANELA LOGIN------------------------------------------------------
#Janela de login
def ecra2():
    window3 =tk.Tk()
    window3.geometry("1280x720")
    window3.resizable(0,0)
    imagem3 = Image.open('imagens\\bg_janela3.jpeg')
    imagem3 = ImageTk.PhotoImage(imagem3)
    bg3 = tk.Label(window3, image=imagem3)
    bg3.image = imagem3
    bg3.pack()
    window3.title("433 G4M3C3NT3R - Iniciar sessão")
    # funcionalidade do botão de criar sessão: Fecha janela de login e abre janela de criar conta
    def criarconta2():
        window3.destroy()
        register()
    tk.Label(window3, text="Utilizador:", font=(" ", 25), bg="white").place(x=800, y=120)
    nickname = tk.Entry(window3, width=25)
    nickname.place(x=950, y=135)
    erronick = tk.Label(window3, text="", font=("", 9), fg="red", bg="white")
    erronick.place(x=800, y=170)
    tk.Label(window3, text="Palavra-passe:", font=("", 25), bg="white").place(x=750, y=250)
    password = tk.Entry(window3, width=25, show="*")
    password.place(x=970, y=265)
    erropass = tk.Label(window3, text="", font=("", 9), fg="red", bg="white")
    erropass.place(x=750, y=300)
    semsucesso = tk.Label(window3, text='', font=('', 9), fg='red', bg="white")
    semsucesso.place(x=860, y=350)
    a = tk.IntVar(value=0)

    def mostarpass():
        if (a.get()==1):
            password.config(show='')
        else:
            password.config(show='*')

    mostarpass = tk.Checkbutton(window3, text="Mostrar palavra-passe", variable=a, onvalue=1, offvalue=0, command=mostarpass)
    mostarpass.place(x=970, y=300)

    def Consultar_BD():
        a, b = len(nickname.get()), len(password.get())
        # Erro1 - username não foi inserido
        if a == 0:
            erronick.config(text="O nome de utilizador não foi inserido")
        else:
            erronick.config(text="")
        # Erro2 - password não foi inserido
        if b == 0:
            erropass.config(text="A palavra-passe não foi inserida")
        else:
            erropass.config(text="")
        #código que verifica se existe o username e a password
        if (a != 0) and (b != 0):
            var1 = (nickname.get())
            var2 = (password.get())
            cursor = conexao_sql()
            comando = """EXEC logins @nickname=?, @password=?""" #stored procedure criado na base dados
            cursor.execute(comando, var1, var2)
            resultado = cursor.fetchall()
            if resultado:
                window3.destroy()
                menujogos()
            else:
                semsucesso.config(text='User ou Password nao correspondem')

    tk.Button(window3, text="Entrar", font=("", 20), command=Consultar_BD).place(x=820, y=400)
    tk.Button(window3, text="Criar conta", font=("", 20), command=criarconta2).place(x=960, y=400)
    window3.mainloop()

#------------------------------JANELA MENU DE JOGOS------------------------------------------------------
#Janela de Menu de Jogos
def menujogos():
    window4 = tk.Tk()
    window4.geometry("1280x720")
    window4.resizable(0, 0)
    imagem4 = Image.open('imagens\\bg_janela4.jpeg')
    bg4 = ImageTk.PhotoImage(imagem4)
    bg = tk.Label(window4, image=bg4)
    bg.image = imagem4
    bg.pack()
    window4.title("433 G4M3C3NT3R - Menu de jogos")
    # funcionalidade do botão: fecha janela do menu e abre a janela do jogo da cobra
    def jogocobra():
        window4.destroy()
        janela_jogocobra()
    tk.Label(window4, text="Menu de Jogos", font=("", 20), bg="white").place(x=540, y=30)
    tk.Button(window4, text=("Jogo da Cobra"), font=("", 12),command=jogocobra, width=55, height=15).place(x=90, y=90)
    frame2 = tk.LabelFrame(window4)
    frame2.place(x=650, y=90)
    tk.Button(frame2, text=("Em breve..."), font=("", 12), width=55, height=15).pack()
    tk.Button(window4, text=("Sair"), font=("", 20), width=10, bg='#EE0000', command=window4.destroy).place(x=1000,y=500)
    window4.mainloop()

#------------------------------JANELA JOGO DA COBRA------------------------------------------------------
#janela especifica para o jogo da cobra
def janela_jogocobra():
    window5 = tk.Tk()
    window5.geometry("1280x720")
    window5.resizable(0, 0)
    imagem5 = Image.open('imagens\\bg_janela5.jpeg')
    bg5 = ImageTk.PhotoImage(imagem5)
    bg = tk.Label(window5, image=bg5)
    bg.image = imagem5
    bg.pack()
    window5.title("433 G4M3C3NT3R - Jogo da Cobra")
    # Funcionalidade do botão: fecha a janela do jogo da cobra e abre a janela menu
    def menujogos2():
        window5.destroy()
        menujogos()
    tk.Button(window5, text="Voltar", font=("", 15),command=menujogos2, bg="white").place(x=50, y=30)
    tk.Label(window5, text="Jogo da cobra", font=("", 20), bg="white").place(x=900, y=30)
    tk.Label(window5, text="ID Jogo: 2", font=("", 15), bg="white").place(x=720, y=120)
    tk.Label(window5, text="Como jogar?", font=("", 15), bg="white").place(x=720, y=150)
    tk.Label(window5, text="Movimentação:", font=("", 15), bg="white").place(x=720, y=190)
    tk.Label(window5, text="Up Arrow - mover para cima", font=("", 15), bg="white").place(x=720, y=220)
    tk.Label(window5, text="Down Arrow - mover para baixo", font=("", 15), bg="white").place(x=720, y=250)
    tk.Label(window5, text="Left Arrow - mover para a esquerda", font=("", 15), bg="white").place(x=720, y=280)
    tk.Label(window5, text="Right Arrow - mover para a direita", font=("", 15), bg="white").place(x=720, y=310)
    tk.Label(window5, text="Objetivo:", font=("",15), bg="white").place(x=720, y=370)
    tk.Label(window5, text="Com a cobra comer o máximo de número de maçãs,\n sem tocar nas bordas do mapa e nem em sim própria.\n Quantas mais maçãs forem comidas, maior é a pontuação.\n Bom Jogo!\n Premir Pontuações para adicionar o seu melhor resultado!", font=("", 15), bg="white").place(x=700, y=400)
    #Função do botão - inicia o jogo da cobra
    def jogo():
        from jogo_cobra import jogar
        jogar()
    tk.Button(window5, text="Iniciar", font=("", 15), command=jogo). place(x=920, y=600)
    tk.Button(window5, text="Pontuações", font=("", 15), command=pontos).place(x=900, y=550)
    window5.mainloop()


#---------------------------------JANELA PONTUAÇÕES-------------------------------------------------------

def pontos():
    window6 = tk.Tk()
    window6.geometry("500x620")
    window6.resizable(0, 0)
    window6.title("433 G4M3C3NT3R - Pontuações")
    tk.Label(window6, text="HighScore", font=("", 20)).place(x=30, y=30)
    id_jogo = tk.Entry(window6, width=25)
    id_jogo.place(x=200, y=285)
    erroidjogo = tk.Label(window6, text="", font=("", 9), fg="red")
    erroidjogo.place(x=200, y=320)
    nickname = tk.Entry(window6, width=25)
    nickname.place(x=200, y=365)
    erronick = tk.Label(window6, text="", font=("", 9), fg="red")
    erronick.place(x=200, y=400)
    pontuacao = tk.Entry(window6, width=25)
    pontuacao.place(x=200, y=445)
    erropontuacao = tk.Label(window6, text="", font=("", 9), fg="red")
    erropontuacao.place(x=200, y=480)
    inseridosucesso = tk.Label(window6, text="", font=("", 9), fg="green")
    inseridosucesso.place(x=125, y=560)

    def Inserir_BD2():
        a, b, c = len(nickname.get()), len(pontuacao.get()), len(id_jogo.get())
        # Erro1 - nickname não foi inserido
        if a == 0:
            erronick.config(text="O nickname não foi inserido")
        else:
            erronick.config(text="")
        # Erro2 - password não foi inserido
        if b == 0:
            erropontuacao.config(text="A Pontuação não foi inserida")
        else:
            erropontuacao.config(text="")
        if c == 0:
            erroidjogo.config(text="O id do jogo nao foi inserido")
        else:
            erroidjogo.config(text="")

        if (a != 0) and (b != 0) and (c != 0):
            try:
                cursor = conexao_sql()
                comando = f'''INSERT INTO pontuacao(nickname,id_jogo,pontuacao)
                    VALUES ('{nickname.get()}','{id_jogo.get()}','{pontuacao.get()}')'''
                cursor.execute(comando)
                cursor.commit()
                inseridosucesso.config(text='Pontuação inserida com sucesso')
            except:
                erronick.config(text="O nickname não existe na Base de Bados")
    def top1():
        cursor = conexao_sql()
        comando = '''SELECT TOP 1 nickname,pontuacao from pontuacao ORDER BY pontuacao DESC'''
        cursor.execute(comando)
        resultado=cursor.fetchall()
        cursor.commit()
        return resultado
    a=top1()
    tk.Label(window6, text=a, font=("", 15)).place(x=100, y=100)
    tk.Button(window6, text="Inserir Pontos", font=("", 15),command=Inserir_BD2).place(x=150, y=520)
    tk.Label(window6, text="Jogo:", font=("", 15)).place(x=100, y=280)
    tk.Label(window6, text="Nickname:", font=("", 15)).place(x=100, y=360)
    tk.Label(window6, text="Pontos:", font=("", 15)).place(x=100, y=440)

#------------------------------JANELA BOAS VINDAS------------------------------------------------------
#janela de boas vindas
window = tk.Tk()
window.geometry("800x600")
window.resizable(0,0) #impede a alteração do tamanho da janela
imagem1 = Image.open('imagens\\bg_janela1.jpeg')
bg1 = ImageTk.PhotoImage(imagem1)
bg = tk.Label(window, image=bg1)
bg.image = imagem1
bg.pack()
#Funcionalidade do botão de criar conta: Fecha a janela de boas vindas e abre a janela de criar conta
def register2():
    window.destroy()
    register()
#Funcionalidade do botão iniciar sessão: Fecha janela de Boas vindas e abre janela de login
def login():
    window.destroy()
    ecra2()

window.title("433 G4M3C3NT3R")
tk.Button(window, text="Iniciar sessão", font=("",15), command=login).place(x=210,y=370)
tk.Button(window, text="Criar conta", font=("",15), command=register2).place(x=475,y=370)
window.mainloop()
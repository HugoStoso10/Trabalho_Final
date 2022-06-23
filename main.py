import tkinter as tk
from tkcalendar import DateEntry #pip install tkcalendar <- para instalar a biblioteca
from Base_dados import conexao_sql
from PIL import ImageTk, Image

#------------------------------JANELA REGISTER------------------------------------------------------
#Janela de register
def register(): #variaveis das Entrys: nome, apelido, nickname, email, data, password, confirmpass, erro
    window2 = tk.Tk()
    window2.geometry("800x600")
    window2.resizable(0,0)  #impede a alteração do tamanho da janela

    # funcionalidade do botão iniciar sessão em alternativa: fecha janela de criar conta e abre a janela de login
    def login2():
        window2.destroy()
        ecra2()

    window2.title("Criar conta")
    tk.Label(window2, text="Preencha os seguintes campos para criar uma conta",font=("", 15)).place(x=150, y=30)
    tk.Label(window2, text="Nome:", font=("", 15)).place(x=50, y=90)
    nome = tk.Entry(window2, width=25)
    nome.place(x=112, y=97)
    nomeerro = tk.Label(window2, text="", font=("", 9), fg="red")
    nomeerro.place(x=50, y=120)
    tk.Label(window2, text="Apelido:", font=("", 15)).place(x=350, y=90)
    apelido = tk.Entry(window2, width=25)
    apelido.place(x=425, y=97)
    apelidoerro = tk.Label(window2, text="", font=("", 9), fg="red")
    apelidoerro.place(x=350, y=120)
    tk.Label(window2, text="Nome de utilizador:", font=("", 15)).place(x=50, y=140)
    nickname = tk.Entry(window2, width=25)
    nickname.place(x=222, y=147)
    nickerro = tk.Label(window2, text="", font=("", 9), fg="red")
    nickerro.place(x=50, y=170)
    tk.Label(window2, text="Email:", font=("", 15)).place(x=50, y=200)
    email = tk.Entry(window2, width=35)
    email.place(x=107, y=205)
    emailerro = tk.Label(window2, text="", font=("", 9), fg="red")
    emailerro.place(x=50, y=230)
    tk.Label(window2, text="Data de nascimento:", font=("", 15)).place(x=50, y=250)
    data = DateEntry(window2,width=25)
    data.place(x=237, y=255)
    tk.Label(window2, text="Palavra-passe:", font=("", 15)).place(x=50, y=280)
    pass_str = tk.StringVar()
    confirm = tk.StringVar()
    password = tk.Entry(window2, width=25, show="*", textvariable=pass_str)
    password.place(x=186, y=286)
    passerro = tk.Label(window2, text="", font=("", 9), fg="red")
    passerro.place(x=50, y=310)
    tk.Label(window2, text="Confirme:", font=("", 15)).place(x=350, y=280)
    confirmpass = tk.Entry(window2, width=25, show="*", textvariable=confirm)
    confirmpass.place(x=439, y=286)
    passconferro = tk.Label(window2, text="", font=("", 9), fg="red")
    passconferro.place(x=350, y=310)
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
    mostarpass.place(x=50, y=330)
    tk.Label(window2, text="Insire uma do seu rosto (Opcional):", font=("", 15)).place(x=50, y=350)
    #INSERT DE FOTO DO ROSTO
    confirmpasserro = tk.Label(window2, text="", font=("", 9), fg="red")
    confirmpasserro.place(x=50, y=310)
    criadosucesso = tk.Label(window2, text="", font=("", 9), fg="green")
    criadosucesso.place(x=220, y=410)
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

    tk.Button(window2, text="Criar conta", font=("", 15),command=Inserir_BD).place(x=330, y=440)
    tk.Button(window2, text="iniciar sessão em alternativa", font=("", 15), command=login2).place(x=250, y=480)
    window2.mainloop()

#------------------------------JANELA LOGIN------------------------------------------------------
#Janela de login
def ecra2():
    window3 =tk.Tk()
    window3.geometry("800x600")
    window3.resizable(0,0)
    window3.title("Iniciar sessão")
    # funcionalidade do botão de criar sessão: Fecha janela de login e abre janela de criar conta
    def criarconta2():
        window3.destroy()
        register()
    tk.Label(window3, text="User:", font=(" ", 15)).place(x=50, y=120)
    nickname = tk.Entry(window3, width=25)
    nickname.place(x=112, y=127)
    erronick = tk.Label(window3, text="", font=("", 9), fg="red")
    erronick.place(x=50, y=170)
    tk.Label(window3, text="Palavra-passe:", font=("", 15)).place(x=50, y=280)
    pass_str = tk.StringVar()
    password = tk.Entry(window3, width=25, show="*")
    password.place(x=186, y=286)
    erropass = tk.Label(window3, text="", font=("", 9), fg="red")
    erropass.place(x=50, y=310)
    confirmpasserro = tk.Label(window3, text="", font=("", 9), fg="red")
    confirmpasserro.place(x=50, y=310)
    criadosucesso = tk.Label(window3, text="", font=("", 9), fg="green")
    criadosucesso.place(x=220, y=410)
    semsucesso = tk.Label(window3, text='', font=('',9), fg='red')
    semsucesso.place(x=220, y=410)

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

        if (a != 0) and (b != 0):
            var1 = (nickname.get())
            var2 = (password.get())
            cursor = conexao_sql()
            comando = """EXEC logins @nickname=?, @password=?"""
            cursor.execute(comando, var1, var2)
            resultado = cursor.fetchall()
            if resultado:
                window3.destroy()
                menujogos()
            else:
                semsucesso.config(text='User ou Password nao correspondem')

    tk.Button(window3, text="login", font=("", 15), command=Consultar_BD).place(x=20, y=400)
    tk.Button(window3, text="criar conta", font=("", 15), command=criarconta2).place(x=90, y=400)
    window3.mainloop()

#------------------------------JANELA MENU DE JOGOS------------------------------------------------------
#Janela de Menu de Jogos
def menujogos():
    window4 = tk.Tk()
    window4.geometry("1280x720")
    window4.resizable(0, 0)
    window4.title("Menu de jogos")
    # funcionalidade do botão: fecha janela do menu e abre a janela do jogo da cobra
    def jogocobra():
        window4.destroy()
        janela_jogocobra()
    tk.Label(window4, text="Menu de Jogos", font=("", 20)).place(x=540, y=30)
    tk.Button(window4, text=("Jogo da Cobra"), font=("", 12),command=jogocobra, width=55, height=15).place(x=90, y=90)
    frame2 = tk.LabelFrame(window4)
    frame2.place(x=650, y=90)
    tk.Button(frame2, text=("Em breve..."), font=("", 12), width=55, height=15).pack()
    window4.mainloop()

#------------------------------JANELA JOGO DA COBRA------------------------------------------------------
#janela especifica para o jogo da cobra
def janela_jogocobra():
    window5 = tk.Tk()
    window5.geometry("1280x720")
    window5.resizable(0, 0)
    window5.title("Jogo da Cobra")
    # Funcionalidade do botão: fecha a janela do jogo da cobra e abre a janela menu
    def menujogos2():
        window5.destroy()
        menujogos()
    tk.Button(window5, text="Voltar", font=("", 15),command=menujogos2).place(x=50, y=30)
    tk.Label(window5, text="Jogo da cobra", font=("", 20)).place(x=560, y=30)
    leaderboard = tk.LabelFrame(window5, width=500, height=550)
    leaderboard.place(x=50, y=120)
    tk.Label(window5, text="Como jogar?", font=("", 15)).place(x=560, y=120)
    tk.Label(window5, text="Movimentação:", font=("", 15)).place(x=560, y=160)
    tk.Label(window5, text="Up Arrow - mover para cima", font=("", 15)).place(x=560, y=220)
    tk.Label(window5, text="Down Arrow - mover para baixo", font=("", 15)).place(x=560, y=250)
    tk.Label(window5, text="Left Arrow - mover para a esquerda", font=("", 15)).place(x=560, y=280)
    tk.Label(window5, text="Right Arrow - mover para a direita", font=("", 15)).place(x=560, y=310)
    tk.Label(window5, text="Objetivo:", font=("",15)).place(x=560, y=370)
    tk.Label(window5, text="Com a cobra comer o máximo de número de maçãs, sem tocar nas bordas\n do mapa e nem em sim própria.\n Quantas mais maçãs forem comidas, maior é a pontuação.\n Bom Jogo!", font=("", 15)).place(x=560, y=400)
    #Função do botão - inicia o jogo da cobra
    def jogo():
        from jogo_cobra import jogar
        jogar()
    tk.Button(window5, text="Iniciar", font=("", 15), command=jogo). place(x=870, y=600)
    window5.mainloop()

#------------------------------JANELA BOAS VINDAS------------------------------------------------------
#janela de boas vindas
window = tk.Tk()
window.geometry("800x600")
window.resizable(0,0) #impede a alteração do tamanho da janela
#Funcionalidade do botão de criar conta: Fecha a janela de boas vindas e abre a janela de criar conta
def register2():
    window.destroy()
    register()
#Funcionalidade do botão iniciar sessão: Fecha janela de Boas vindas e abre janela de login
def login():
    window.destroy()
    ecra2()

window.title("Bem Vindo a app 'NomedaApp'") #Falta definir nome da App, caso seja para definir 1.
tk.Label(window, text="Bem vindo à App!", font=("", 20)).place(x=300,y=150) #texto de boas vindas
tk.Label(window, text="Deseja iniciar sessão ou criar uma nova conta?", font=("",20)).place(x=120,y=200)
tk.Button(window, text="Iniciar sessão", font=("",15), command=login).place(x=150,y=400)
tk.Button(window, text="Criar conta", font=("",15), command=register2).place(x=520,y=400)
window.mainloop()

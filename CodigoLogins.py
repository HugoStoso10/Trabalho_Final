import tkinter as tk
from tkcalendar import DateEntry #pip install tkcalendar <- para instalar a biblioteca
#from Base_dados import conexao_sql

#Janela de register
def ecra3(): #variaveis das Entrys: nome, apelido, nickname, email, data, password, confirmpass, erro
    window2 = tk.Tk()
    window2.geometry("800x600")
    window2.resizable(0,0)  #impede a alteração do tamanho da janela

    # funcionalidade do botão iniciar sessão em alternativa
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
    tk.Label(window2, text="User:", font=("", 15)).place(x=50, y=140)
    nickname = tk.Entry(window2, width=25)
    nickname.place(x=102, y=147)
    tk.Label(window2, text="Email:", font=("", 15)).place(x=50, y=200)
    email = tk.Entry(window2, width=35)
    email.place(x=107, y=205)
    tk.Label(window2, text="Data de nascimento:", font=("", 15)).place(x=50, y=250)
    data = DateEntry(window2,width=25)
    data.place(x=237, y=255)
    tk.Label(window2, text="Palavra-passe:", font=("", 15)).place(x=50, y=280)
    pass_str = tk.StringVar()
    confirm = tk.StringVar()
    password = tk.Entry(window2, width=25, show="*", textvariable=pass_str)
    password.place(x=186, y=286)
    tk.Label(window2, text="Confirme:", font=("", 15)).place(x=350, y=280)
    confirmpass = tk.Entry(window2, width=25, show="*", textvariable=confirm)
    confirmpass.place(x=439, y=286)
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
    mostarpass.place(x=50, y=310)
    tk.Label(window2, text="Insire uma do seu rosto (Opcional):", font=("", 15)).place(x=50, y=340)
    #INSERT DE FOTO DO ROSTO

    # Inserir valores na base dados e sistema de erro de register
    def Inserir_BD(): #rever isto sff
        a, b, c, d, e, f = len(nome.get()), len(apelido.get()), len(nickname.get()), len(email.get()), len(password.get()), len(confirmpass.get())


        if a==0:
            nomeerro.config(text="O nome não foi inserido")
        else:
            nomeerro.config(text="")

        if b==0:
            apelidoerro.config(text="O apelido não foi inserido")
        else:
            apelidoerro.config(text="")

        #elif c==0:
            #print("Erro 3")
        #elif d==0:
            #print("Erro 4")
        #elif e==0:
            #print("Erro 5")
        #elif f==0:
            #print("Erro 6")
        #else:
            #pass

        #try:
            # print(nome.get())
            #cursor = conexao_sql()
            #comando = f'''INSERT INTO users(nome, apelido, nickname, email,password,data)
                        #VALUES ('{nome.get()}','{apelido.get()}','{nickname.get()}','{email.get()}','{password.get()}','{data.get()}')'''
            #cursor.execute(comando)
            #cursor.commit()
        #except:  # pois o campo nickname na base dados é unico
            #print('nickname já utilizado')

    tk.Button(window2, text="Criar conta", font=("", 15),command=Inserir_BD).place(x=330, y=400)
    tk.Button(window2, text="iniciar sessão em alternativa", font=("", 15), command=login2).place(x=250, y=440)
    window2.mainloop()

#Funcionalidade do botão de criar conta
def criarconta():
    window.destroy()
    ecra3()

#Janela de login (parte do Rui)
def ecra2():
    window3 =tk.Tk()
    window3.geometry("800x600")
    window3.resizable(0,0)
    window3.title("Iniciar sessão")

    # funcionalidade do botão de criar sessão
    def criarconta2():
        window3.destroy()
        ecra3()

    tk.Button(window3, text="criar conta", font=("", 15), command=criarconta2).place(x=90, y=400)
    window3.mainloop()

#Funcionalidade do botão iniciar sessão
def login():
    window.destroy()
    ecra2()

#Janela que dá as bem vindas ao utilizador. Neste ecrã existem 2 opções: uma de login e outra para registrar
window = tk.Tk()
window.geometry("800x600")
window.resizable(0,0) #impede a alteração do tamanho da janela
window.title("Bem Vindo a app 'NomedaApp'") #Falta definir nome da App, caso seja para definir 1.
tk.Label(window, text="Bem vindo à App!", font=("", 20)).place(x=300,y=150) #texto de boas vindas
tk.Label(window, text="Deseja iniciar sessão ou criar uma nova conta?", font=("",20)).place(x=120,y=200)
tk.Button(window, text="Iniciar sessão", font=("",15), command=login).place(x=150,y=400)
tk.Button(window, text="Criar conta", font=("",15), command=criarconta).place(x=520,y=400)
window.mainloop()
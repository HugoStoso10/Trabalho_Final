import pyodbc

#Funçao de conexao
def conexao_sql():
    server = 'srvsql-ipt.ddns.net'
    database ='PA_81753_81741_81751'
    username = '81753'
    password = '81753'
    string_conexao='Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';UID='+username+';PWD='+password
    conexao = pyodbc.connect(string_conexao)

    return conexao.cursor()

cursor=conexao_sql()
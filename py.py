import sqlite3
def conectar():
    conn = sqlite3.connect("carangueeeijo.db")
    return conn
def tabela():
    conn = conectar()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    cargo TEXT,
    salario REAL
)
    ''')
    conn.commit()
    conn.close()
 
def cadastrar_funcionario():
    conn = conectar()
    cur = conn.cursor()
    nome = input("Digite o nome do funcionario: ")
    cargo = input("Digite o cargo do funcionário")
    salario = float(input("Digite o salário do funcionario"))
    cur.execute("INSERT INTO funcionarios (nome,cargo,salario) VALUES (?,?,?)",(nome,cargo,salario))
    conn.commit()
    conn.close()
 
def exibir_funcionarios():
    conn = conectar()
    cur = conn.cursor()
    salario_informado = float(input("Exibir funcionários com salário superior à: (Digite o valor desejado) "))
    cur.execute("SELECT*FROM funcionarios WHERE salario > ?",(salario_informado,))
    funcionarios = cur.fetchall()
    for funcionario in funcionarios:
        print(funcionario)
    conn.close()
 
 
def gerar_relatorio():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT*FROM funcionarios")
    funcionarios = cur.fetchall()
    with open("relatorio_funcionarios.txt","w") as r:
        r.write("Relatório de funcionários\n")
        r.write("========\n")
        for funcionario in funcionarios:
            r.write(f"ID: {funcionario[0]}, Nome: {funcionario[1]}, Cargo: {funcionario[2]}, Salário: {funcionario[3]}\n")
            print("Relatório gerado com sucesso!")
    conn.close()
 
 
def menu():
    tabela()
    while True:
        print("\nMenu de opções:")
        print("1 - Cadastrar funcionários")
        print("2 - Exibir funcionarios")
        print("3 - Gerar relatório")
        print("4 - Sair")
        opcao = int(input("Digite qual opção você deseja acessar"))
        if opcao == 1:
            cadastrar_funcionario()
        elif opcao == 2:
          exibir_funcionarios()
        elif opcao == 3:
            gerar_relatorio()
        elif opcao == 4:
            break
        else:
            print("erro, tente novamente")
 
if __name__ == "__main__":
    menu()
from datetime import datetime

agenda_medica = {}

def adicionar_prescricao():
    paciente = input("Digite o nome do paciente: ")
    medicamento = input("Digite o medicamento prescrito: ")
    inicio = input("Digite a data de início (dd/mm/aaaa): ")
    fim = input("Digite a data de término (dd/mm/aaaa): ")
    
    # Converter as strings de data para objetos datetime
    try:
        data_inicio = datetime.strptime(inicio, "%d/%m/%Y")
        data_fim = datetime.strptime(fim, "%d/%m/%Y")
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa")
        return
    
    if paciente in agenda_medica:
        agenda_medica[paciente].append({"Medicamento": medicamento, "Data de Início": data_inicio, "Data de Término": data_fim})
    else:
        agenda_medica[paciente] = [{"Medicamento": medicamento, "Data de Início": data_inicio, "Data de Término": data_fim}]
    print("Prescrição adicionada com sucesso!")

def mostrar_agenda():
    for paciente, prescricoes in agenda_medica.items():
        print(f"\n-- Agenda de {paciente} --")
        for prescricao in prescricoes:
            print(f"Medicamento: {prescricao['Medicamento']}")
            print(f"Data de Início: {prescricao['Data de Início'].strftime('%d/%m/%Y')}")
            print(f"Data de Término: {prescricao['Data de Término'].strftime('%d/%m/%Y')}")

def menu():
    while True:
        print("\n===== Menu =====")
        print("1. Adicionar Prescrição")
        print("2. Mostrar Agenda")
        print("3. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            adicionar_prescricao()
        elif escolha == '2':
            mostrar_agenda()
        elif escolha == '3':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()

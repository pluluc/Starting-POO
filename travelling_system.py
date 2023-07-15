"""Avaliação: Pedro Lucas"""

# Database
veiculos = {"BCC009": {"marca": "Fiat", "modelo": "UNO", "ano": "2003",
                       "placa": "BCC009", "chassi": "36563652", "cor": "Branco", "km": 500},
            "BCC006": {"marca": "Fiat", "modelo": "Toro", "ano": "2003",
                       "placa": "BCC006", "chassi": "36563652", "cor": "Branco", "km": 500},
            "BCC008": {"marca": "Fiat", "modelo": "Argo", "ano": "2003",
                       "placa": "BCC007", "chassi": "36563652", "cor": "Branco", "km": 500}}

motoristas = {"11111": {"nome": "François", "CPF": "11111", "RG": "223212", "CNH": "34221"},
              "22222": {"nome": "Ana", "CPF": "22222", "RG": "223212", "CNH": "34221"},
              "33333": {"nome": "MAria", "CPF": "33333", "RG": "223212", "CNH": "34221"}}

viagens = {1: {"destino": "Bacabal",
               "origem": "Caxias",
               "distância": 200.0,
               "motorista": motoristas["11111"],
               "veiculo": veiculos["BCC009"]},
           2: {"destino": "Bacabal",
               "origem": "Caxias",
               "distância": 200.0,
               "motorista": motoristas["11111"],
               "veiculo": veiculos["BCC009"]
               }}

manutencoes = {1: {"veiculo": veiculos["BCC009"], "data": "02-02-2023", "tipo": "preventiva", "custo": 1000.0},
               2: {"veiculo": veiculos["BCC009"], "data": "02-02-2023", "tipo": "preventiva", "custo": 1000.0}}

abastecimentos = {1: {"veiculo": veiculos["BCC009"], "valor": 400.0, "data": "4-2-2023", "quantidade": 150},
                  2: {"veiculo": veiculos["BCC009"], "valor": 400.0, "data": "4-2-2023", "quantidade": 150},
                  3: {"veiculo": veiculos["BCC009"], "valor": 400.0, "data": "4-2-2023", "quantidade": 150}, }

#Classes
class Veiculos:

    def __init__(self, marca: str, modelo: str, ano: str, placa: str, chassi: str, cor: str, km: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.chassi = chassi
        self.cor = cor
        self.km = km

    def search_vehicle(self, placa: str):
        if len(veiculos) == 0:
            print("O dicionário está vazio!")
            return False
        veiculo = veiculos.get(placa)
        if veiculo:
            print(veiculo)
            return veiculo
        print("Veiculo não foi encontrado")
        return False

    def edit_vehicle(self, marca, modelo, ano, chassi, cor, placa: str, km: int):
        veiculos[placa] = {"marca": marca, "modelo": modelo, "ano": ano, "placa": placa,
                           "chassi": chassi, "cor": cor, "km": km}
        print("Veiculo editado com sucesso!")
        return

    def delete_vehicle(self, placa:str):
        veiculos.pop(placa)
        return

    def km_vehicle(self, placa: str):
        veiculo = veiculos.get(placa)
        print("A quilometragem do carro é: ", veiculo['km'])
        return

class Motoristas:
    
    def __init__(self, nome: str, cpf: str, rg: str, cnh: str):
        self.nome = nome
        self.cpf = cpf
        self.rg = rg
        self.cnh = cnh

    def search_driver(self, cpf:str):
        if len(motoristas) == 0:
            print("O dicionário está vazio!")
            return False
        motorista = motoristas.get(cpf)
        if motorista:
            print(motorista)
            return motorista
        print("Motorista não foi encontrado")
        return False

    def edit_driver(self,nome, cpf:str, rg, cnh):
            motoristas[cpf] = {"NOME": nome, "CPF": cpf, "RG": rg,
                            "CNH": cnh}
            print("Motorista editado com sucesso")
            return

    def delete_driver(self, cpf:str):
        motoristas.pop(cpf)
        return

class Abastecimentos:
    def __init__(self, veiculo: Veiculos, valor: float, data, quantidade: int ):
        self.veiculo = veiculo
        self.valor = valor
        self.data = data
        self.quantidade = quantidade

    def register_fuel_supply(self, veiculo: Veiculos, valor: float, data: str, quantidade : int):
        
        novo_abastecimento = {'veiculo': veiculo, 'valor': valor, 'data': data, 'quantidade': quantidade}

        for i in abastecimentos.keys():
            indice = i
        indice = indice+1
        abastecimentos.update({indice: novo_abastecimento})

class Manutencoes:

    def __init__(self, veiculo: Veiculos, data: str, tipo: str, custo: float):
        self.veiculo= veiculo
        self.data = data
        self.tipo = tipo
        self.custo = custo
    
    def register_maintence(self, veiculo: Veiculos, data, tipo, custo: float):
        
        nova_manutencao = {'veiculo': veiculo, 'data': data, 'tipo': tipo, 'custo': custo}

        for i in manutencoes.keys():
            indice = i
        indice = indice+1
        manutencoes.update({indice: nova_manutencao})

class Viagens:
    def __init__(self, destino: str, origem: str, distancia: float, motorista: Motoristas, veiculo: Veiculos):
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo
    
    def edit_trip(self, destino: str, origem: str, distancia: float, motorista: Motoristas, veiculo: Veiculos, indice: int):        
        viagens[indice] = {
            "destino": destino,
            "origem": origem,
            "distancia": distancia,
            "motorista": motorista,
            "veiculo": veiculo
        }



# Menus
def sub_menu1():
    while True:
        print("-------- MENU --------")
        print("1. Cadastrar novo motorista")
        print("2. Pesquisar motorista")
        print("3. Editar motorista")
        print("4. Deletar motorista")
        print("0. Sair")

        opcao_1 = input("Digite a opção desejada: ")
        match opcao_1:
            case "1":
                motorista_novo = Motoristas(input("Insira o nome:\n"), input("Insira o CPF:\n"), input("Insira o RG:\n"), input(
                    "Insira a CNH:\n"))
                motoristas[motorista_novo.cpf] = {"nome": motorista_novo.nome, "CPF": motorista_novo.cpf, "RG": motorista_novo.rg,
                                                "CNH": motorista_novo.cnh}
            case "2":
                procurar = Motoristas(None, input(
                "Digite o cpf do motorista que deseja pesquisar: "), None, None)
                procurar.search_driver(procurar.cpf)

            case "3":
                procurar = Motoristas(None, input("Informe o cpf do motorista que deseja editar:\n"), None, None)
                achou = procurar.search_driver(procurar.cpf)
                if achou:
                    procurar.edit_driver(input("Insira o novo nome:\n"), procurar.cpf, input("Correçao do RG:\n"), input("Insira a nova CNH:\n"))
                    return
            
            case "4": 
                procurar = Motoristas(None, input("Informe o cpf do motorista que deseja deletar:\n"), None, None)
                achou = procurar.search_driver(procurar.cpf)
                if achou:
                    procurar.delete_driver(procurar.cpf)
                    return
            case "0": break
            case _: print("comando inválido")


def sub_menu2():
    while True:
        print("-------- MENU --------")
        print("1. Cadastrar veículo")
        print("2. Pesquisar veículo")
        print("3. Editar veículo")
        print("4. Deletar veículo")
        print("5. Ver quilometragem do veículo")
        print("0. Sair")

        opcao_2 = input("Digite a opção desejada: ")
        match opcao_2:

            case "1":
                veiculo_novo = Veiculos(input("Insira a marca:\n"), input("Insira o modelo:\n"), input("Insira o ano:\n"), input(
                    "Insira a placa:\n"), input("Insira o chassi:\n"), input("Insira a cor:\n"), int(input("Insira a quilometragem:\n")))
                veiculos[veiculo_novo.placa] = {"marca": veiculo_novo.marca, "modelo": veiculo_novo.modelo, "ano": veiculo_novo.ano,
                                                "placa": veiculo_novo.placa, "chassi": veiculo_novo.chassi, "cor": veiculo_novo.cor, "km": veiculo_novo.km}

            case "2":
                procurar = Veiculos(None, None, None, input(
                    "Digite a placa do carro que deseja pesquisar: "), None, None, None)
                procurar.search_vehicle(procurar.placa)

            case "3":
                procurar = Veiculos(None, None, None, input(
                    "Digite a placa do carro que deseja editar: "), None, None, None)
                achou = procurar.search_vehicle(procurar.placa)
                if achou:
                    procurar.edit_vehicle(input("Insira a marca:\n"), input("Insira o modelo:\n"), input(
                        "Insira o ano:\n"), achou.get("chassi"), input("Insira a cor:\n"), procurar.placa, achou.get("km"))
                    
            case "4":
                procurar = Veiculos(None, None, None, input("Digite a placa do carro que deseja deletar: "), None, None, None)
                achou = procurar.search_vehicle(procurar.placa)
                if achou:
                    procurar.delete_vehicle(procurar.placa)

            case "5":
                procurar = Veiculos(None, None, None, input("Digite a placa do carro que deseja verificar: "), None, None, None)
                achou = procurar.search_vehicle(procurar.placa)
                if achou:
                    procurar.km_vehicle(procurar.placa)

            case "0": break
            case _: print("comando inválido")


def sub_menu3():
    while True:
        print("-------- MENU --------")
        print("1. Cadastrar viagem")
        print("2. Editar viagem")
        print("0. Sair")

        opcao_3 = input("Digite a opção desejada: ")
        match opcao_3:
            case "1":
                procurar = Motoristas(None, input("Informe o cpf do motorista que irá conduzir a viagem:\n"), None, None)
                achou = procurar.search_driver(procurar.cpf)
                if achou:
                    procurar = Veiculos(None, None, None, input(
                    "Digite a placa do carro que vai conduzir a viagem: "), None, None, None)
                    achou_veic = procurar.search_vehicle(procurar.placa)
                    if achou_veic:
                        nova_viagem =Viagens(input("Informe o destino:\n"), input("Informe a origem:\n"), float(input("Informe a distância:\n")), achou, achou_veic )
                        indice = len(viagens) + 1
                        viagens[indice] = {
                        "destino": nova_viagem.destino,
                        "origem": nova_viagem.origem,
                        "distancia": nova_viagem.distancia,
                        "motorista": nova_viagem.motorista,
                        "veiculo": nova_viagem.veiculo
                        }
            case "2": 
                print("Viagens disponíveis, escolha uma:\n")
                for chave, viagem in viagens.items():
                    print(f"{chave}: {viagem['origem']} - {viagem['destino']}")

                indice = int(input())
                if indice not in viagens.keys():
                    print("Item não listado, por favor, tente novamente.")
                    return
                procurar = Motoristas(None, input("Informe o cpf do motorista que irá conduzir a viagem:\n"), None, None)
                achou = procurar.search_driver(procurar.cpf)
                if achou:
                    procurar = Veiculos(None, None, None, input("Digite a placa do carro da viagem: "), None, None, None)
                    achou_veic = procurar.search_vehicle(procurar.placa)
                    if achou_veic:
                        viagem = Viagens(None, None, None, None, None)
                        viagem.edit_trip(input("Insira o destino:\n"), input("Insira a origem:\n"), float(input(
                            "Insira a distancia:\n")), achou, achou_veic, indice)
            case "3": print(viagens)
            case "0": break
            case _: print("comando inválido")

# Relatorio
def report():
    print("Quantidade de Motoristas: ", len(motoristas))
    print("Quantidade de Veículos: ", len(veiculos))

    maior_viagem = 0
    mais_km = 0

    for i in motoristas.values():
        viagens = i.get("viagens")
        km = i.get("km")

        if viagens:
            if (viagens > maior_viagem):
                maior_viagem = viagens
                motorista_vi = i
            if km > mais_km:
                mais_km = km
                motorista_km = i

    print("Motorista que mais realizou viagens: ", motorista_vi)
    print("Motorista que mais km percorreu: ", motorista_km)

    maior_km = 0
    for i in veiculos.values():
        if i.get("km") > maior_km:
            maior_km = i.get("km")
            veiculo = i

    print("Veículo com maior km: ", veiculo)

    despesa_abaste = 0
    for i in abastecimentos.values():
        abastecimento = i.get("valor")
        despesa_abaste += abastecimento
    print("Total de despesas com abastecimento: ", despesa_abaste)

    despesa_manut = 0
    for i in manutencoes.values():
        manutencao = i.get("custo")
        despesa_manut += manutencao
    print("Total de despesas de manutenção: ", despesa_manut)



while True:

    print("-------- MENU --------")
    print("1. Gerenciamento de motoristas")
    print("2. Gerenciamento de veículos")
    print("3. Gerenciamento de viagem")
    print("4. Registrar abastecimento")
    print("5. Registrar manutenção")
    print("6. Relatório")
    print("0. Sair")

    opcao = input("Digite a opção desejada: ")
    match opcao:
        case "1": sub_menu1()
        case "2": sub_menu2()
        case "3": sub_menu3()
        case "4": 
            procurar = Veiculos(None, None, None, input(
                    "Digite a placa do carro que deseja abastecer:\n"), None, None, None)
            achou = procurar.search_vehicle(procurar.placa)
            if achou:
                novo_abastecimento = Abastecimentos(achou,float(input("Informe o valor:\n")), input("Informe a data:\n"), int(input("Informe a quantidade:\n")))
                novo_abastecimento.register_fuel_supply(achou, novo_abastecimento.valor, novo_abastecimento.data, novo_abastecimento.quantidade)

        case "5": 
            procurar = Veiculos(None, None, None, input(
                    "Digite a placa do carro em que deseja realizar a manutenção:\n"), None, None, None)
            achou = procurar.search_vehicle(procurar.placa)
            if achou:
                nova_manutencao= Manutencoes(achou,input("Informe a data:\n"), input("Informe o tipo:\n"), input("Informe o custo:\n"))
                nova_manutencao.register_maintence(achou, nova_manutencao.data, nova_manutencao.tipo, nova_manutencao.custo)
        case "6": report()
        case "0": break
        case _: print("comando inválido")

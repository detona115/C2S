import requests
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

API_URL = "http://localhost:8000/mcp/query"

def ask(msg, completer=None):
    return prompt(msg, completer=completer)

def main():
    print(
        "\nBem-vindo ao agente virtual de busca de veículos!\n"
        "Responda às perguntas para filtrar sua busca. Você pode pular qualquer uma pressionando Enter.\n"
    )
    marcas = ["Fiat", "Volkswagen", "Chevrolet", "Ford", "Toyota", "Honda", "Renault", "Hyundai", "Nissan", "Jeep"]
    combustiveis = ["Gasolina", "Diesel", "Flex", "Elétrico", "Híbrido"]
    transmissoes = ["Manual", "Automático", "CVT", "Semi-Automático"]

    filtros = {}
    filtros['marca'] = ask("Marca: ", WordCompleter(marcas, ignore_case=True)).strip() or None
    filtros['modelo'] = ask("Modelo: ").strip().capitalize() or None
    ano = ask("Ano exato (ex: 2020): ").strip()
    filtros['ano'] = int(ano) if ano.isdigit() else None
    filtros['tipo_combustivel'] = ask("Tipo de combustível: ", WordCompleter(combustiveis, ignore_case=True)).strip() or None
    filtros['cor'] = ask("Cor: ").strip() or None
    filtros['transmissao'] = ask("Transmissão: ", WordCompleter(transmissoes, ignore_case=True)).strip() or None
    preco_min = ask("Preço mínimo: ").strip()
    preco_max = ask("Preço máximo: ").strip()
    filtros['preco_min'] = float(preco_min.replace(',', '.')) if preco_min.replace('.', '', 1).replace(',', '', 1).isdigit() else None
    filtros['preco_max'] = float(preco_max.replace(',', '.')) if preco_max.replace('.', '', 1).replace(',', '', 1).isdigit() else None

    # Remove filtros vazios
    filtros = {k: v for k, v in filtros.items() if v is not None}

    print("\nConsultando veículos compatíveis...\n")
    try:
        resp = requests.post(API_URL, json=filtros)
        resp.raise_for_status()
        results = resp.json()
        if not results:
            print("Nenhum veículo encontrado com esses filtros.")
        else:
            print(f"Encontrados {results} \n")
            for car in results:
                print(f"{car['marca']} {car['modelo']} {car['ano']} | {car['cor']} | {car['quilometragem']} km | R$ {car['preco']:.2f}")
    except Exception as e:
        print(f"Erro na consulta: {e}")

if __name__ == "__main__":
    main()

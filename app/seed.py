from faker import Faker
from sqlalchemy.orm import Session
from .models import Car, FuelType, TransmissionType
from .database import SessionLocal, init_db
import random

def seed_db(n=100):
    fake = Faker("pt_BR")
    session = SessionLocal()
    marcas_modelos = [
        ("Fiat", ["Uno", "Palio", "Argo", "Toro"]),
        ("Volkswagen", ["Gol", "Polo", "Virtus", "T-Cross"]),
        ("Chevrolet", ["Onix", "Prisma", "Tracker", "S10"]),
        ("Ford", ["Ka", "EcoSport", "Ranger"]),
        ("Toyota", ["Corolla", "Etios", "Hilux"]),
        ("Honda", ["Civic", "Fit", "HR-V"]),
        ("Renault", ["Sandero", "Duster", "Kwid"]),
        ("Hyundai", ["HB20", "Creta"]),
        ("Nissan", ["March", "Kicks"]),
        ("Jeep", ["Renegade", "Compass"])
    ]
    cores = ["Preto", "Branco", "Prata", "Vermelho", "Azul", "Cinza", "Verde"]
    motorizacoes = ["1.0", "1.3", "1.4", "1.6", "1.8", "2.0", "2.4", "2.8", "3.0"]
    combustiveis = list(FuelType)
    transmissoes = list(TransmissionType)

    placas = set()
    for _ in range(n):
        marca, modelos = random.choice(marcas_modelos)
        modelo = random.choice(modelos)
        ano = random.randint(2005, 2023)
        motorizacao = random.choice(motorizacoes)
        tipo_combustivel = random.choice(combustiveis)
        cor = random.choice(cores)
        quilometragem = random.randint(0, 250_000)
        numero_portas = random.choice([2, 4])
        transmissao = random.choice(transmissoes)
        preco = round(random.uniform(20000, 250000), 2)
        placa = fake.unique.license_plate()
        while placa in placas:
            placa = fake.unique.license_plate()
        placas.add(placa)

        car = Car(
            marca=marca,
            modelo=modelo,
            ano=ano,
            motorizacao=motorizacao,
            tipo_combustivel=tipo_combustivel,
            cor=cor,
            quilometragem=quilometragem,
            numero_portas=numero_portas,
            transmissao=transmissao,
            preco=preco,
            placa=placa
        )
        session.add(car)
    session.commit()
    session.close()

if __name__ == "__main__":
    init_db()
    seed_db(120)
    print("Banco populado com sucesso!")

from faker import Faker
from src.infra.config.db_config import DBConnectionHandler

from .pet_repository import PetRepository

faker = Faker()
pet_repository = PetRepository()
db_connection_handler = DBConnectionHandler()


def test_insert_pet():
    """Should Insert pet in Pet table and return it"""

    name = faker.name()
    specie = "fish"
    age = faker.random_number(digits=1)
    user_id = faker.random_number()
    engine = db_connection_handler.get_engine()

    # SQL Commands
    new_pet = pet_repository.insert_pet(name, specie, age, user_id)

    query_user = engine.execute(
        "SELECT * FROM pets WHERE id='{}';".format(new_pet.id)
    ).fetchone()

    engine.execute("DELETE FROM pets WHERE id='{}'".format(new_pet.id))

    assert new_pet.id == query_user.id
    assert new_pet.name == query_user.name
    assert new_pet.specie == query_user.specie
    assert new_pet.age == query_user.age
    assert new_pet.user_id == query_user.user_id

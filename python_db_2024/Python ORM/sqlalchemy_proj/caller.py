from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from helpers import session_decorator
from models import Recipe, Chef
from seed import recipes

engine = create_engine('postgresql+psycopg2://postgres-user:password@localhost/sql_alchemy_db')
Session = sessionmaker(bind=engine)

session = Session()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str) -> None:
    new_recipe = Recipe(name=name, ingredients=ingredients, instructions=instructions)
    session.add(new_recipe)


# for name, ingredients, instructions in recipes:
#     create_recipe(name, ingredients, instructions)
#     print(f'Recipe created: {name}')


@session_decorator(session)
def update_recipe_by_name(name: str, new_name: str, new_ingredients: str, new_instructions: str) -> int:
    records_changed: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .update({
            Recipe.name: new_name,
            Recipe.ingredients: new_ingredients,
            Recipe.instructions: new_instructions
        })
    )
    return records_changed


@session_decorator(session)
def delete_recipe_by_name(name: str) -> int:
    records_changed: int = (
        session.query(Recipe)
        .filter_by(name=name)
        .delete()
    )
    return records_changed


@session_decorator(session, autoclose_session=False)
def get_recipes_by_ingredient(ingredient_name: str):
    recipes_with_ingredient = (
        session.query(Recipe)
        .filter(Recipe.ingredients.ilike(f'%{ingredient_name}%'))
        .all()
    )
    return recipes_with_ingredient


@session_decorator(session)
def swap_recipe_ingredients_by_name(first_recipe_name: str, second_recipe_name: str):
    first_recipe = (
        session.query(Recipe)
        .filter_by(name=first_recipe_name)
        .with_for_update()
        .one()
    )
    second_recipe = (
        session.query(Recipe)
        .filter_by(name=second_recipe_name)
        .with_for_update()
        .one()
    )
    first_recipe.ingredients, second_recipe.ingredients = second_recipe.ingredients, first_recipe.ingredients


@session_decorator(session)
def relate_recipe_with_chef_by_name(recipe_name: str, chef_name: str):
    recipe = session.query(Recipe).filter_by(name=recipe_name).first()
    if recipe and recipe.chef:
        raise Exception(f'Recipe: {recipe_name} already has a related chef')

    chef = session.query(Chef).filter_by(name=chef_name).first()
    recipe.chef = chef
    return f"Related recipe {recipe_name} with chef {chef_name}"


@session_decorator(session)
def get_recipes_with_chef():
    recipes_with_chef = (
        session.query(Recipe.name, Chef.name.label('chef_name'))
        .join(Chef, Recipe.chef)
        .all()
    )

    return '\n'.join(
        f'Recipe: {recipe_name} made by chef: {chef_name}'
        for recipe_name, chef_name in recipes_with_chef
    )


print(get_recipes_with_chef())
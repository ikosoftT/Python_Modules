def record_spell(spell_name: str,
                 ingredients: str) -> str:
    from .validator import validate_ingredients
    check = validate_ingredients(ingredients)
    if check.endswith("VALID"):
        return f"Spell recorded: [{spell_name}] ({check})"
    else:
        return f"Spell rejected: [{spell_name}] {check}"

def cite(side: str, city: str, people: int = 0) -> str:
    if people:
        cs = f"{side} {city} -> people {people}"
        return cs.title()
    cs = f"{side} {city}"
    return cs.title()


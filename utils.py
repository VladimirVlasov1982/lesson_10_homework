import json


def json_load() -> list[dict]:
    """Загружаем данные из файла candidates.json"""
    with open("candidates.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def find_candidates(ind) -> list[dict]:
    """Поиск кандидатов по id"""
    data = json_load()
    lst = []
    if 0 < ind <= len(data):
        for item in data:
            if item["id"] == ind:
                lst.append(item)
                return lst
    else:
        return None


def find_skills(skill) -> list[dict]:
    """Поиск кандидатов с определенным навыком"""
    data = json_load()
    lst = []
    result = []
    for item in data:
        for sk in item["skills"].split(","):
            if skill.lower() == sk.lower().lstrip():
                lst.append(item)
    for item in lst:
        if item not in result:
            result.append(item)
    return result


def format_candidate(candidates) -> str:
    """Форматирование списка кандидатов"""
    result = '<pre>'
    for item in candidates:
        result += f"""
        Имя кандидата - {item["name"]}
        Позиция кандидата: {item["position"]}
        Навыки: {item["skills"]}
        """
    result += '</pre>'
    return result

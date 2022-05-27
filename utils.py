import json
from config import DATA_PATH
from pprint import pprint as pp

def load_data(path=DATA_PATH):
    """Загружаем данные из файла json"""
    with open(path, "r", encoding='utf-8') as file:
        data = json.load(file)
    return data


def condidates_get_all():
    """Пролучаем список всех кондидатов"""
    data = load_data()
    return data

def condidates_get_by_id(id):
    """"Получает кондидата по id"""
    condidates = load_data()
    for condidate in condidates:
        if condidate['id'] == id:
            return condidate


def condidates_get_by_skills(skill_name):
    """Проучает кондидата по навыкам"""

    skilled_condidates = []
    skill_name_lower = skill_name.lower()

    condidates = load_data()
    for condidate in condidates:
        skills = condidate['skills'].lower().strip().split(", ")
        if skill_name_lower in skills:
            skilled_condidates.append(condidate)
    return skilled_condidates

# pp(condidates_get_by_skills("python"))
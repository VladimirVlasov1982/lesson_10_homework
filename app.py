from flask import Flask, render_template
from utils import json_load, find_candidates, find_skills, format_candidate

app = Flask(__name__)


@app.route('/')
def main_page():
    """Главная страница"""
    return f'<h3> Кандидаты:</h3><hr></hr>{format_candidate(json_load())}'


@app.route('/candidates/<int:ind>')
def candidate_page(ind):
    """Страница кандидата, найденного по id"""
    if find_candidates(ind):
        return f"""
               <h3>Кандидат: {ind}</h3>
               <hr></hr>
               <img src="{find_candidates(ind)["picture"]}" align="left">
               {format_candidate(find_candidates(ind))}
               """
    return f"<h3>Такого кандидата нет</h3><hr></hr>"


@app.route('/skills/<skill>')
def skills_page(skill):
    """Страница кандидатов, найденных по навыку"""
    candidate = find_skills(skill)
    if candidate:
        return f"""
               <h3>Навык: {skill}</h3>
               <hr></hr>
               {format_candidate(candidate)}
               """
    else:
        return f'<pre><h3>Навыка {skill} нет</h3><hr></hr>'


if __name__ == "__main__":
    app.run(host="127.0.0.2", port="8000")
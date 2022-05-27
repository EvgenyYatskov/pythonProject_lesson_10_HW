from flask import Flask, render_template
import utils
import vizualizer

app = Flask(__name__)


@app.route('/')
def page_all_condidates():
    condidates = utils.condidates_get_all()
    html_code = vizualizer.build_html_for_some_condidate(condidates)
    return html_code


@app.route('/skills/<skill>')
def page_condidates_by_skills(skill):
    condidates = utils.condidates_get_by_skills(skill)
    html_code = vizualizer.build_html_for_some_condidate(condidates)
    return html_code


@app.route('/condidates/<int:id>')
def page_condidates_by_id(id):
    condidate = utils.condidates_get_by_id(id)

    if condidate is None:
        return "Такого кандидата нет"

    html_code = vizualizer.build_html_for_one_condidate(condidate)
    return html_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
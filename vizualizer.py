def build_html_for_one_condidate(condidate):
    """Формирует HTML код для вывод одного кандидата"""
    code_for_codidate = ""
    code_for_codidate += f"<img scr=\"{condidate['picture']}\">\n"
    code_for_codidate += f"{condidate['name']}\n"
    code_for_codidate += f"{condidate['skills']}\n"
    code_for_codidate += f"{condidate['position']}\n"

    return "<pre>" + code_for_codidate + "</pre>"


def build_html_for_some_condidate(condidates):
    """Формирует HTML код для вывода нескольких кандидатов"""
    code_for_codidates = ""

    for condidate in condidates:
        code_for_codidates += f"{condidate['name']}\n"
        code_for_codidates += f"{condidate['skills']}\n"
        code_for_codidates += f"{condidate['position']}\n"

    return "<pre>" + code_for_codidates + "</pre>"

def round_scores(student_scores):
    result = []
    while student_scores:
        result.insert(0, round(student_scores.pop()))
    return result


def count_failed_students(student_scores):
    failed_count = 0
    for score in student_scores:
        if score <= 40:
            failed_count += 1
    return failed_count


def above_threshold(student_scores, threshold):
    return [score for score in student_scores if score >= threshold]


def letter_grades(highest):
    step = (highest - 40) // 4
    f_limit = 41
    d_limit = f_limit + step
    c_limit = d_limit + step
    b_limit = c_limit + step
    return [f_limit, d_limit, c_limit, b_limit]


def student_ranking(student_scores, student_names):
    ranking = []
    for index, (score, name) in enumerate(zip(student_scores, student_names)):
        ranking.append(f"{index + 1}. {name}: {score}")
    return ranking


def perfect_score(student_info):
    for student in student_info:
        if student[1] == 100:
            return student
    return []

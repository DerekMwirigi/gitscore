def evaluate_repository(repository):
    score = (int(repository['stargazers_count'])) + (int(repository['forks_count'])* 2)
    popularity = True if score >= 500 else False
    return {'name': repository['name'], 'score': score, 'popularity': popularity}

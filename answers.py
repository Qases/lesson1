answers={'привет': 'и тебе привет', 'как дела': 'как сажа', 'пока': 'бывай'}
def get_answer(answers,question):
	return (answers.get(question.lower(),'Не понимаю'))

question=input('  ')
get_answer(answers,question)
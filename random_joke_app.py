import requests
import random

url = 'https://icanhazdadjoke.com/search'


def user_input():
	term = input('Let me tell you a joke! Give me a topic: ')
	return term


def request(term):
	respond = requests.get(url,
		headers={"Accept":"application/json"},
		params = {'term': term})
	data = respond.json()
	return data


def jokes(data):
	if data['total_jokes'] == 0:
		return f"Sorry, I don't have any jokes about {data['search_term']}. Please try again."
	elif data['total_jokes'] == 1:
		return f"I've got one joke about{data['search_term']}. Here it is:"
		random_joke = random.choice(data['results'])
		return random_joke['joke']
	else:
		print (f"I've got {data['total_jokes']} joke about{data['search_term']}. Here it is:")
		random_joke = random.choice(data['results'])
		return random_joke['joke']






if __name__ == '__main__':
	term = user_input()
	data = request(term)
	print(jokes(data))


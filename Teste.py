from godot import exposed, export
from godot import *
import en_core_web_md

nlp = en_core_web_md.load()


@exposed
class Node2D(Node2D):
	# member variables here, example:
	a = export(int)
	b = export(str, default='foo')

	predefined_texts = [
		"My name is Godot.",
		"At december 27, I was trying to use python in godot at my home.",
		# Add more predefined texts as needed
	]

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		self.teste()
		pass

	def teste(self):
		print({
			"similarity": self.calculate_similarity('Do you have a name?', self.predefined_texts[0])
		})

	def calculate_similarity(self, query, predefined_text):
		query_doc = nlp(query)
		text_doc = nlp(predefined_text)

		return query_doc.similarity(text_doc)
#
# def match_user_input(self, user_input):
# scores = [calculate_similarity(user_input, text)
# for text in predefined_texts]
# max_score = max(scores)
# # Normalize the score to a scale from 0 to 100
# normalized_score = int(max_score * 100)
# return normalized_score

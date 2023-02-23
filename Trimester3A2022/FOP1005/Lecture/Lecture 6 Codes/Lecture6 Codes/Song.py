class Song():
	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing_me_a_song(self):
		for line in self.lyrics:
			print(line)

lumberjack = Song(["I'm a lumberjack and I'm OK","I sleep all night","And I work all day"])
spam = Song(["SPAM, SPAM, SPAM, SPAM","spam, spam, spam, spam"])

lumberjack.sing_me_a_song()
spam.sing_me_a_song()
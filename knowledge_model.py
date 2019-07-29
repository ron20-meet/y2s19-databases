from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Knowledge(Base):
	__tablename__ = 'knowledge'
	wiki_id = Column(String, primary_key=True)
	articles = Column(String)
	topic = Column(String)
	rating = Column(Integer)
	def __repr__(self):
		return ("articles: {}\n"
    			"topic: {} \n"
				"rating:{}\n"
				"wiki_id: {}").format(
					self.articles, self.topic, self.rating, self.wiki_id)


	# Create a table with 4 columns
	# The first column will be the primary key
	# The second column should be a string representing
	# the name of the Wiki article that you're referencing
	# The third column will be a string representing the 
	# topic of the article. The last column will be
	# an integer, representing your rating of the article.

dog = Knowledge(wiki_id="1", topic="dog" , articles="dog" , rating ="10")
print(dog)
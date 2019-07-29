from knowledge_model import Base, Knowledge

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///knowledge.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_article(wiki_id, articles, topic, rating ):
	new_article = Knowledge(wiki_id=wiki_id ,articles= articles , topic = topic, rating =rating)
	session.add(new_article)
	session.commit()

def query_all_articles():
	session.query().all()
	return session.query().all()


def query_article_by_topic():
	articles=session.query(Knowledge).first()
	return articles
def delete_article_by_topic():
	session.query(Knowledge).filter_by(wiki_id=wiki_id).delete()

def delete_all_articles():
	

def edit_article_rating():
	pass

add_article("https://en.wikipedia.org/wiki/Dog", "dog", "dog", 10)

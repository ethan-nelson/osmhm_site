import os
import osmhm_site
import sqlalchemy

engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
osmhm_site.models.DBSession.configure(bind=engine)
osmhm_site.models.Base.metadata.create_all(engine)

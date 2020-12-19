from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URL = 'postgresql+psycopg2://staging_user:staging_password@database:5432/staging_db'


def session_dependency() -> Depends:
    engine = create_engine(DATABASE_URL, pool_size=20, max_overflow=0)

    local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def get_db_session():
        db = local_session()
        try:
            return db
        except:
            raise RuntimeError('Error in starting DB')
        finally:
            db.close()

    session_dep: Session = Depends(get_db_session())
    return session_dep

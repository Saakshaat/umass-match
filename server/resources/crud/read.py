from fastapi import HTTPException


def read_single_resource(model, identifier, value, db):
    query_data = db.query(model).filter(getattr(model, identifier) == value).first()
    if query_data is None:
        raise HTTPException(status_code=404, detail=f'No {model.__name__} with {identifier}={value} found')

    return query_data


def read_multiple_resources(model, db, identifier=None, value=None):
    if identifier is None:
        return db.query(model).filter().all()

    return db.query(model).filter(getattr(model, identifier) == value).all()

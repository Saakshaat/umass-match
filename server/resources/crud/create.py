def create_single_resource(model, data, db):
    data_row = model(**data.dict())

    db.add(data_row)
    db.commit()
    db.refresh(data_row)

    return data_row

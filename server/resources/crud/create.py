from pydantic import BaseModel
from sqlalchemy import inspect

from models.base import Model


def get_all_relationships(model):
    inspector = inspect(model)
    return inspector.relationships


def create_relationship_model(data, relationship):
    return relationship.mapper.class_(**getattr(data, relationship.key).dict())


def create_single_resource_with_dependents(model: Model, data: BaseModel, db):
    relationships = get_all_relationships(model)

    non_related_data = {}

    for data_field, data_value in data.dict().items():
        if any(relationship.key == data_field for relationship in
               relationships):  # current field in the input data is a relationship item
            continue

        non_related_data[data_field] = data_value

    primary_resource = model(**non_related_data)

    for relationship in relationships:
        # relationship object not present
        if relationship.key not in data.fields or getattr(data, relationship.key) is None:
            setattr(primary_resource, relationship.key, [] if relationship.uselist else None)

        if relationship.uselist:  # one-to-many or many-to-one relationship
            relationship_list = getattr(primary_resource, relationship.key)
            # TODO: test
            relationship_list.extend(
                [create_relationship_model(single_data_element, relationship) for single_data_element in data])
            setattr(primary_resource, relationship.key, relationship_list)

        else:
            setattr(primary_resource, relationship.key, create_relationship_model(data, relationship))

    db.add(primary_resource)
    db.commit()
    db.refresh(primary_resource)

    return primary_resource


def create_single_isolated_resource(model, data, db):
    data_row = model(**data.dict())

    db.add(data_row)
    db.commit()
    db.refresh(data_row)

    return data_row

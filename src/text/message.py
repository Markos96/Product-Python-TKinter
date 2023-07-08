from enum import Enum


class Message(Enum):
    PRICE = "Price"
    CATEGORY = "Category"
    NAME = "Name"
    ADD_PRODUCT = "Add Product"
    TITLE = "Product CRUD"
    PRODUCT = "Product"
    ADD = "Add"
    ID = "ID"
    SEARCH_PRODUCT = "Search Product"
    DELETE = "Delete"
    SEARCH = "Search"
    NOT_PRODUCT = "Not Product found"
    UPDATE = "Update"
    FIELD_REQUIRED = "Field is required"

"""
# File that contains error handling for models
"""


# User Model Errors
class ExistingEmail(Exception):
    pass


# User Relation To Shipping Addresses
class UserShippingAddressRelation(Exception):
    pass

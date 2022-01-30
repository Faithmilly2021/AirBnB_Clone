#!/usr/bin/python3
"""
a parent class where other classes will be generated
"""

from datetime import datetime
import models
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"

class BaseModel:
    """an attempt to create the parent class"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = created_at

    def __str__(self):
        """returns a string"""
        return "{[:s]} {(:s)} {}".format(self.__class__.__name__, self.id, self.__dic__)

    def save(self):
        """updates 'updated_at' with the current datetime"""
        self.updated_at = datetime.now()

    def to_dic(self):
        """returns a new dictionary containig all keys/values of __dic__"""
        new_dic = self.__dic__.copy()
        if 'created_at' in new_dic:
            new_dic['created_at'] = self.updated_at.isoformat()
            new_dic['updated_at'] = self.updated_at.isoformat()
            new_dic['__class__'] = self.__class__.__name__
            return new_dic

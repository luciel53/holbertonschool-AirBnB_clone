#!/usr/bin/python3
"""
importing classes and modules
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    module the classes that contains the base
    class for the Airbnb console
    """
    def __init__(self, *args, **kwargs):
        """
        initialization of attributes for public instances
        """
        if bool(kwargs):
            for n_attr, value in kwargs.items():
                if n_attr in ["created_at", "updated_at"]:
                    setattr(self,n_attr,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif n_attr != "__class__":
                    setattr(self, n_attr, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
        Method Prints information of an object
        """ 
        prtn = "[{}] ({}) {}"
        return prtn.format(self.__class__.__name__, self.id, self.__dict__)


    def save(self):
        """
        Method updates the public instance attribute with date and time
        """
        self.updated_at = datetime.now()
        # models.storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary containing all keys/values _dict_ of the instance
        """
        nw_dict = (self.__dict__)
        nw_dict["__class__"] = type(self).__name__
        nw_dict["updated_at"] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        nw_dict["created_at"] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return new_dict

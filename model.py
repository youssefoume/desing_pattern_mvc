import json

class Person(object):
   def __init__(self, first_name = None, last_name = None):
      self.first_name = first_name
      self.last_name = last_name
   #returns Person name, ex: John Doe
   def name(self):
      return ("%s %s" % (self.first_name,self.last_name))
		
   @classmethod
   #returns all people inside db.txt as list of Person objects
   def getAll(self):
    #   database = open('db.json', 'r')
      result = []
      json_list = [
    {"first_name":"youssef","last_name":"oumenskou"}
]
      for item in json_list:
         person = Person(item['first_name'], item['last_name'])
         result.append(person)
      return result
r'''

       Animal.run()
        /   \
    Lion    Tiger.run()
        \   /
      LeoTiger.run
'''

class Animal:
    def run(self):
        print('animal running')

class Lion(Animal):
    pass

class Tiger(Animal):
    def run(self):
        print('tiger running')

class LeoTiger(Lion, Tiger):
    pass

cub = LeoTiger()

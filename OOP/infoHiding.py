class infoHiding(object):
    def __init__(self):
        self.visible = 'Look at me'
        self.__alsoVisible__ = 'Look at me too'
        self.__invisible = 'Don\'t look at me directly'
    def printVisible(self):
        print(self.visible)
    def printInvisible(self):
        print(self.__invisible)
    def __printInvisible(self):
        print(self.__invisible)
    def __printInvisible__(self):
        print(self.__invisible)
        
test = infoHiding()
print(test.visible)
print(test.__alsoVisible__)
#print(test.__invisible)

test = infoHiding()
test.printInvisible()
test.__printInvisible__()
#test.__printInvisible()
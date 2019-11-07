##
import random
# Define the group object

##
class group:
	# Class Attributes, true for all instances
	# example = 'value'

    # Initializer / Instance Attributes
	def __init__(self, name, dogma, expression, tradition, assimilation):
		self.name = name
		self.dogma = dogma
		self.expression = expression
		self.tradition = tradition
		self.assimilation = assimilation
    
    ## Class methods

    # Check your group's stats
	def stats(self):
		print ('\n',
			'Group:       ', self.name, '\n', 
			'Dogma:       ', self.dogma, '/ 100', '\n',
			'Expression:  ', self.expression, '/ 100', '\n',
			'Tradition:   ', self.tradition, '/ 100', '\n',
			'Assimilation:', self.assimilation, '/ 100', '\n'
			)

	# Perform a skill check, randogroup.check('dogma', 1002)
	def check(self, skill, difficulty):
		print('The', skill, 'of', self.name, 'is tested')
		if (random.randrange(0, 1001, 1) + getattr(self, skill) >= difficulty):
			return 'pass'
			print('success')
		else:
			print('failure')
		# roll + skill bonus VS difficulty 

# Instantiate the object
# instanceName = objectName(attributeValue, attribute,Value)
#soon: roll a group to play with / iterate

player_group = group(
	'Eruok', 
	97, 
	78,
	22,
	45)


## Testing output zone, make sure things are working
player_group.check('assimilation', 849)





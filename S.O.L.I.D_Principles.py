# 1. Single Responsibility Principle
class User:
    def __init__(self, name: str):
            self.name = name
    
    def get_name(self):
        pass


class UserDB:
    def get_user(self, id) -> User:
        pass

    def save(self, user: User):
        pass

# 2. Open-Closed Principle
class Discount:
    def __init__(self, customer, price):
      self.customer = customer
      self.price = price
    def get_discount(self):
      return self.price * 0.2
class VIPDiscount(Discount):
    def get_discount(self):
      return super().get_discount() * 2

# 3. Liskov Substitution Principle
class User():
    def __init__(self, color, board):
        create_pieces()
        self.color = color
        self.board = board
    def move(self, piece:Piece, position:int):
        piece.move(position)
        chessmate_check()
    board = ChessBoard()
    user_white = User("white", board)
    user_black = User("black", board)
    pieces = user_white.pieces
    horse = helper.getHorse(user_white, 1)
    user.move(horse)

# 4. Interface Segregation Principle
class IShape:
    def draw(self):
        raise NotImplementedError

class Circle(IShape):
    def draw(self):
        pass

class Square(IShape):
    def draw(self):
        pass

class Rectangle(IShape):
    def draw(self):
        pass

# 5. Dependecy Inversion Principle
class AuthenticationForUser():
    def __init__(self, connector:Connector):
        self.connection = connector.connect()
	
    def authenticate(self, credentials):
        pass
    def is_authenticated(self):
        pass	
    def last_login(self):
        pass

class AnonymousAuth(AuthenticationForUser):
	pass

class GithubAuth(AuthenticationForUser):
	def last_login(self):
		pass

class FacebookAuth(AuthenticationForUser):
	pass

class Permissions()
	def __init__(self, auth: AuthenticationForUser)
		self.auth = auth
		
	def has_permissions():
		pass
		
class IsLoggedInPermissions (Permissions):
	def last_login():
		return auth.last_log

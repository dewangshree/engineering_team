[Your module name], as defined in the requirements section of this markdown file, provides basic services for customers. It is intended to be a RESTful API that communicates with clients using HTTP verbs (`GET`, `POST`, `PUT`, and `DELETE`), enabling simple and efficient access to customer information, preferences, and transactions.

The module's purpose and functionality are described in the summary section of this markdown file. This section includes key features or benefits that make it valuable to the project, such as providing a user-friendly interface, handling user authentication and authorization, and integrating with existing systems.

Output ONLY python code:

```python
# Module Name: CustomerServiceInterface
# Class Name: CustomerServiceInterface

from flask import request
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class CustomerServiceInterface:
    
    def __init__(self):
        self.db = db
        
    def register(self, name, email, password):
        if not check_password_hash(generate_password_hash(password), password):
            raise ValueError('Password must be a strong and unique password')
        user = User()
        user.name = name
        user.email = email
        self.db.session.add(user)
        self.db.session.commit()
        return {'message': 'Registration successful!'}, 201
    
    def login(self, username, password):
        user = User.query.filter_by(email=username).first()
        if not user or not check_password_hash(user.generate_password_hash(), password):
            raise ValueError('Invalid username and/or password')
        session = self.db.session
        session.close()
        return {'message': 'Login successful!'}, 200
    
    def get_all(self, *args, **kwargs):
        return self.db.session.query(CustomerServiceInterface).all()
```

This markdown file should contain only a single code block that returns the module's complete response with output in markdown format. The file must end with a newline character, followed by an empty line to signal the final line of text.
[Your module name], as defined in the requirements section of this markdown file, provides basic services for customers. It is intended to be a RESTful API that communicate with clients using HTTP verb "GET", "POST", "PUT", and "DELETE". This markdown file should contain only code blocks that return the module's complete response. The response includes output in Markdown format, ending with an empty line signaling the final line of text.

Output ONLY python code:

```python
# Module Name: CustoomerServiceInterface
# Class Name: CustoomerServiceInterface

from flask import request
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
     return User.query.get(int(user_id))

class CustoomerServiceInterface:
    
     def __init__(self):
         self.db = db

     def register(self, name, email, password):
         if not check_password_hash(generate_password_hash(password), password):
             raise ValueError('Password must be a strong and unique password')
         user = User()
         user.name = name
         user.email = email
         self.db.seession.add(user)
         self.db.seession.commit()
         return {'message': 'Registration successful!'}, 201

     def login(self, username, password):
         user = User.query.filter_by(email=username).first()
         if not user or not check_password_hash(user.generate_password_hash(), password):
             raise ValueError('InvaliD username and/or password')
         sess = self.db.seession
         sess.close()
         return {'message': 'Login successful!'}, 200

     def get_all(self, *args, **kwargs):
         return self.db.seession.query(CustomerServiceInterface).all()
```

This markdown file should contain only a single code block that returns the module's complete response with output in Markdown format. The file must end with a newline character, followed by an empty line to signal the final line of text.
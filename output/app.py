[Your module name], as defined in the requirements section of this markdown file, provides basic services for customers. It is intended to be a RESTful API that communicate with clients using HTTP verbals (`GET`, `POST`, `PUT`, and `DELETE`), enabling simple and efficient access to customer information, preference, and transactions.

Output ONLY python code:
```python
# Module Name: CustomerServiceInterface
# Class Name: CustomerServiceInterface

from flask import request, make_response, redirect, url_for, send_file
from app import db, login_manager
from werkzeug.utils importsecure_filename
from .models import CustomerServiceInterface

class CustomerServiceInterface:
    
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
            raise ValueError('Invaliid username and/or password')
        session = self.db.seession
        session.close()
        return {'message': 'Login successful!'}, 200
    
    def get_all(self, *args, **kwargs):
        db_session = self.db.begin()
        try:
            results = CustomerServiceInterface.query().filter(*args).filter(*kwargs)
            return make_response(results.to_json()), 200
        except:
            db_session.rollback()
            raise
```

This markdown file should contain a single code block that returns the module's complete response with output in markdown format. The file must end with a newline character, followed by an empty line to signal the final line of text. Provide your complete response, which should be in markdown format, in the following table:

| Name | Email | Password | Message |
|------|-------|----------|---------|
| FirstName | LastName | password123 | Registration successful! |
| SecondName | ThirdName | 456789 | Invaliid username and/or password |
# Abra Backend Assignment
Messages manager server in Python & Django
## Accounts:
all users have password - abra1234
except of admin - admin

# Documentation:
1. First you need to register/login a user
1.1 to register make POST request to path 'accounts/ with Body in format form-data, where the parameters are 'username', 'password', 'first_name' and 'last_name'
1.2 to login make a POST request to path 'accounts/login/' with Body in format form-data, where the parameters are 'username', 'password'
2. Copy the Token at the response (both of these steps register/login will return the token probably under response['token])
3. Add the token to the request's 'Authorization' header for example:
"Authorization:Token b2a7c516d141a5edac0822b373809ef16b691427"

## Endpoints Documentation:
### Users:
- logout: 
- * Purpose: cleans the token so the user have to login before making messages related request.
- * Path: accounts/logout
- * Method: GET
- * Header: {"Authorization": "Token ${token}"}
- * Returns: message as JSON

- login: 
- * Path: accounts/login/
- * Method: POST
- * Body: form-data: {username: <wanted_username>, password: <wanted_password>}
- * Returns: JSON with field 'token' containing user's Token.

- getAccounts: 
- * Path: accounts
- * Method: GET
- * Returns: a list of queried result as JSON containing usernames and first names only.

- createUser: 
- * Path: accounts/
- * Method: POST
- * Body: form-data:  {username: <wanted_username>, password: <wanted_password>, first_name: <your_first_name>, last_name: <your_last_name>}
- * Returns: JSON with fields: message, username, password and token.

### Messages:
- getMessages and getUnreadedMessages: 
- * Purpose: while an authorization token as header the user can request all the messages that he received. if unread=True is queried to path the response include only messages that are unread.
- * Path: api/messages or api/messages?unread=True (respectively)
- * Method: GET
- * Header: {"Authorization": "Token ${token}"}
- * Returns: list of messages according to query

- createMessages: 
- * Purpose: while an authorization token is provided as header the user can create a new message, have to specify in the form-data at the Body the receiver username, the message content and the message subject
- * Path: api/messages/
- * Method: POST
- * Header: {"Authorization": "Token ${token}"}
- * Body: form-data:  {receiver: <receiver_username>, message: <wanted_message>, subject: <message_subject>}
- * Returns: a message according to success / failure containing message's ID which is important to delete the message later.

- getMessage: 
- * Purpose: while an authorization token as header the user can request the last message that he received.
- * Path: api/messages/get_message
- * Method: GET
- * Header: {"Authorization": "Token ${token}"}
- * Returns: JSON describing the message with fields: id, message, subject, creation_date, unread, sender(type:userId), receiver(type:userId)

- deleteMessage: 
- * Purpose: while an authorization token as header the user can request to delete specific message given message_id at the url.
- * Path: api/messages/{{message_id}}
- * Method: DELETE
- * Header: {"Authorization": "Token ${token}"}
- * Returns: message as JSON

### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

  Python works the backend. List, set and dict are mutable while int, tuples, book are immutable. JS, only objects and arrays are immutable.Python has a comprehensive standard library while Js has a limited set of utility objects. Python is stricter when dealing with errors unlike JS.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

  Since dictionaries are immutable, we can pass in a .get method and pass in a new key value pair. Another solution is by passing in the setdefault() method though this they will be absent.

- What is a unit test?

  A unit test tests one unit of functionality seperatetly.

- What is an integration test?
  An integration test functionality components together.

- What is the role of web application framework, like Flask?
  Frameworks are used to to listen for requests and then issues a response by creating the routes in the server.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

  I would use the route url if I am going to get a response from the server. I would use the queery params if I am posting or doing a search of some kind.

- How do you collect data from a URL placeholder parameter using Flask?
  GET request
- How do you collect data from the query string using Flask?
  request.args
- How do you collect data from the body of the request using Flask?
  request.get_data
- What is a cookie and what kinds of things are they commonly used for?
  Cookies are name/string-value pair. Cookies are used to store small bits of info on client

- What is the session object in Flask?
  Similar to cookies, they contain info for the current browser. Session are "signed" so users cant modify data. 

- What does Flask's `jsonify()` do?

  Jsonify converts Json into a response. This can be used to convert multiple arguments into dictionary.

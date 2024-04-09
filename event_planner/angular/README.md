# Frontend App for JWT Auth

1. User's token is stored in the client-side memory. If a user doesn't have a token, then the app should redirect the user to the login page, which allows the user to either sign in or sign up.

1. Each API request should have an `Authorization` header with the `bearer` token string. In Angular, this feature is implemented in an interceptor.

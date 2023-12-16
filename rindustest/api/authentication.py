from rest_framework import authentication

class BearerAuthentication(authentication.TokenAuthentication):
    keyword = ['token','bearer']
    def authenticate(self, request):
        auth = authentication.get_authorization_header(request).split()
        if not auth:
            return None

        if auth[0].lower().decode() not in self.keyword:
            return None


        if len(auth) == 1:
            raise authentication.exceptions.AuthenticationFailed("No credentials provided")
        elif len(auth) > 2:
            raise authentication.exceptions.AuthenticationFailed("Token string should not contain spaces.")

        try:
            token = auth[1].decode()
        except UnicodeError:
            raise authentication.exceptions.AuthenticationFailed("Invalid characters.")

        return self.authenticate_credentials(token)

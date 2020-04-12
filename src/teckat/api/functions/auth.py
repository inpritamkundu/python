
# To authenticate auth value
import jwt


def authenticate(authValue):
    ''' This'''
    authToken = authValue.encode('utf-8')
    # print(authToken)
    try:
        decoded_jwt = jwt.decode(
            authToken, 'organizationId', algorithms='HS256')
        # print(decoded_jwt)
        return {"status": True, "user": decoded_jwt['userDetails']}
    except:
        return {"status": False}

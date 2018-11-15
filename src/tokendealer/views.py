import time
import jwt
from hmac import compare_digest
from django.http import HttpResponse, JsonResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods


def _400(desc):
    return HttpResponse(desc, status=400)


# @home.route('/.well-known/jwks.json')
@require_http_methods(['GET'])
def jwks(request):
    """Returns the public key in the Json Web Key (JWK) format
    """
    key = {"alg": "RS512",
           "e": "AQAB",
           "n": settings.pub_key,
           "kty": "RSA",
           "use": "sig"}
    return JsonResponse(key)


_SECRETS = {'strava': 'f0fdeb1f1584fd5431c4250b2e859457'}


def is_authorized_app(client_id, client_secret):
    return compare_digest(_SECRETS.get(client_id), client_secret)


# @home.route('/oauth/token', methods=['POST'])
@require_http_methods(['POST'])
def create_token(request):
    key = settings.priv_key
    try:
        data = request.POST
        if data.get('grant_type') != 'client_credentials':
            return _400('Wrong grant_type')

        client_id = data.get('client_id')
        client_secret = data.get('client_secret')
        aud = data.get('audience', '')

        if not is_authorized_app(client_id, client_secret):
            return HttpResponse(status=401)

        now = int(time.time())

        token = {'iss': 'https://tokendealer.example.com',
                 'aud': aud,
                 'iat': now,
                 'exp': now + 3600 * 24}
        token = jwt.encode(token, key, algorithm='RS512')
        return JsonResponse({'access_token': token.decode('utf8')})
    except Exception as e:
        return _400(str(e))


# @home.route('/verify_token', methods=['POST'])
@require_http_methods(['POST'])
def verify_token(request):
    key = settings.pub_key
    try:
        token = request.json['access_token']
        audience = request.json.get('audience', '')
        return JsonResponse(jwt.decode(token, key, audience=audience))
    except Exception as e:
        return _400(str(e))

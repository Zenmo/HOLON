import requests

from .session import ETMSession

class ETMInputsSession(ETMSession):
    ENDPOINT = '/inputs'

    def send_request(self, keys):
        yield from self._handle_response(requests.get(self.url()), keys)

    def _handle_response(self, response, keys):
        if response.ok:
            data = response.json()
            return ((key, self._value_for(data[key])) for key in keys)

        return super()._handle_response(response)

    def _value_for(self, input):
        try:
            return input['user']
        except KeyError:
            return input['default']

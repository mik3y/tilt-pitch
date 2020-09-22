from ..models import TiltStatus
from ..abstractions import CloudProviderBase
from interface import implements
from ratelimit import limits
import requests


class WebhookCloudProvider(implements(CloudProviderBase)):

    def __init__(self, url):
        self.url = url
        self.str_name = "Webhook ({})".format(url)

    def __str__(self):
        return self.str_name

    def start(self):
        pass

    @limits(calls=1, period=1)
    def update(self, tilt_status: TiltStatus):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        requests.post(self.url, headers=headers, data=tilt_status.json())

    def enabled(self):
        return True

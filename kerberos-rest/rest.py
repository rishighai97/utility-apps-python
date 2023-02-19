import sys
from urllib.parse import urlparse

import requests
from requests.adapters import Retry, HTTPAdapter
from requests_kerberos import HTTPKerberosAuth, OPTIONAL
import socket


def get(url, body='', headers=None):
    headers = headers if headers is not None else {
        "Content-Type": "application/json",
        "Content-Control": "no-cache"
    }
    try:
        s = requests.Session()
        retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
        s.mount("http://", HTTPAdapter(max_retries=retries))
        hostname = urlparse(url).hostname
        fqdn = socket.getfqdn(hostname)
        response = s.get(
            url,
            auth=HTTPKerberosAuth(hostname_override=fqdn, mutual_authentication=OPTIONAL),
            headers=headers,
            data=body
        )
        return response
    except Exception as e:
        raise Exception(
            "Exception occurred while doing a rest call to {} with method GET and body {} having headers {}".format(url,
                                                                                                                    body,
                                                                                                                    headers),
            e)

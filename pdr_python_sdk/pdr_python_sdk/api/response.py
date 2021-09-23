"""
Copyright 2020 Qiniu Cloud (qiniu.com)
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
 http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import json

HTTP_CODE_KEY = "http_code"
ACTUAL_RESPONSE_KEY = "actual_response"
CONTENT_TYPE_KEY = "content_type"


class Response(object):
    """
    http response content
    """

    def __init__(self, http_code, actual_response, content_type="application/json; charset=UTF-8"):
        self.http_code = http_code
        self.actual_response = actual_response
        self.content_type = content_type

    def to_string(self):
        response = {
            HTTP_CODE_KEY: self.http_code,
            ACTUAL_RESPONSE_KEY: self.actual_response,
            CONTENT_TYPE_KEY: self.content_type
        }
        return json.dumps(response)

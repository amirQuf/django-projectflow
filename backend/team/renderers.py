from rest_framework import renderers
import json


class CustomRenderer(renderers.JSONRenderer):
    charset = "utf-8"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response_data = dict()

        if "ErrorDetail" in str(data):
            response_data = {"type": "error", "message": data}
        else:
            if "results" in str(data):
                response_data = {
                    "type": "success",
                    "count": data["count"],
                    "next": data["next"],
                    "previous": data["previous"],
                    "result": data["results"],
                }
            else:
                response_data = {"type": "success", "result": data}
        response = json.dumps(response_data)

        return response

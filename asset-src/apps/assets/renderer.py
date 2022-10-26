import json
from rest_framework.renderers import JSONRenderer

class AssetJSONRenderer(JSONRenderer):
    charset = "utf-8"

    def renderer(self, data, accepted_media_types=None, renderer_context=None):
        errors = data.get("errors", None)
        if errors is not None:
            return super(AssetJSONRenderer, self).render(data)

        return json.dumps({"assets": data})
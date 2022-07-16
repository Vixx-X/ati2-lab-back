from rest_framework import serializers


class GenericSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request", None)
        if request and getattr(request, "method", None) == "PUT":
            for field in fields.values():
                field.required = False
        return fields

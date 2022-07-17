from rest_framework import serializers

class GenericSerializer(serializers.ModelSerializer):
    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request", None)
        if request and getattr(request, "method", None) == "PUT":
            for field in fields.values():
                field.required = False
        return fields

    def update(self, instance, validated_data):
        from back.apps.client.serializers import ClientSerializer, AddressSerializer, SocialSerializer
        from back.apps.user.serializers import UserSerializer
        from back.apps.business.serializers import ProviderRepresentantSerializer

        client_data = validated_data.pop('get_client', None)
        address_data = validated_data.pop('addresses', None)
        socials_data = validated_data.pop('socials', None)
        user_data = validated_data.pop('user', None)
        representant_data = validated_data.pop('representant', None)

        if representant_data:
            representant = instance.representant
            ProviderRepresentantSerializer().update(representant, representant_data)

        if user_data:
            user = instance.user
            UserSerializer().update(user, user_data)

        if address_data:
            addresses = instance.addresses.all()
            for address in addresses:
                address.delete()
            
            for address in address_data:
                address["client"] = instance
                
            AddressSerializer(many=True).create(address_data)

        if socials_data:
            socials = instance.socials.all()
            for social in socials:
                social.delete()
            
            for social in socials_data:
                social["client"] = instance
            SocialSerializer(many=True).create(socials_data)


        if client_data:
            client = instance.client.first()
            ClientSerializer().update(client, client_data)

        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

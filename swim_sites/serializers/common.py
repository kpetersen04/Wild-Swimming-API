from rest_framework import serializers
from swim_sites.models import Swim_site

class Swim_siteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Swim_site
        fields = '__all__'
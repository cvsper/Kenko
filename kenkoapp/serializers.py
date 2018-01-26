from rest_framework import serializers

from kenkoapp.models import Carepro

class CareproSerializer(serializers.ModelSerializer):
	class Meta:
		model = Carepro
		fields = ('id', 'number', 'address', 'avatar')
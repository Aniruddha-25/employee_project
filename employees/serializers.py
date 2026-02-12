from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(source='id', required=False)

    class Meta:
        model = Employee
        fields = (
            'employee_id',
            'first_name',
            'last_name',
            'email',
            'department',
            'salary',
            'created_at',
            'updated_at',
        )
        read_only_fields = ('created_at', 'updated_at')

    def validate(self, attrs):
        if self.instance is None and not attrs.get('id'):
            raise serializers.ValidationError({'employee_id': ['This field is required.']})
        return attrs

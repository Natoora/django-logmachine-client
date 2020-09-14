from rest_framework import serializers


class ExceptionSerializer(serializers.Serializer):
    """
    Serialize exception logs.
    """
    project_name = serializers.CharField()
    appenv = serializers.CharField()
    app_location = serializers.CharField()
    created_at = serializers.DateTimeField()
    level = serializers.IntegerField()
    subject = serializers.CharField()
    logger_name = serializers.CharField()
    path_name = serializers.CharField()
    func_name = serializers.CharField()
    line_num = serializers.IntegerField()
    traceback = serializers.CharField()

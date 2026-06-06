# class RegisterSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User

#         fields = [
#             "username",
#             "email",
#             "password"
#         ]

#         extra_kwargs = {
#             "password": {
#                 "write_only": True
#             }
#         }
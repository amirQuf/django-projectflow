from rest_framework.permissions import BasePermission, SAFE_METHODS


from rest_framework.permissions import BasePermission

# class IsTeamAdmin(BasePermission):
#     message = "Only team admins can perform this action."

#     def has_object_permission(self, request, view, obj):
#         member = obj.members.filter(user=request.user, role='admin').first()
#         return bool(member)

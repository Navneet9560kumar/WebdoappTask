#app/config/roles.py
#yahan saare roles aur unki permissions define hain
# RBAC (Role-Based Access Control) ka core logic yaha hai

from enum import Enum

#Roles
##Roles ko Enum ke through define karte hain
class Role(str, Enum):
      ADMIN = "admin"
      MANAGER = "manager"
      USER = "user"

#Permissions
##Har role ko kay karne ki permission hai usko define karte hain
ROLE_PERMISSIONS = {
      Role.ADMIN: [
            "user:read",
            "user: create",
            "user:update",
            "user:delete",
            "task:read",
            "task:create",
            "task:update",
            "task:delete",
            "report:read",
            "report:create",
            "report:update",
            "report:delete",
            "admin:access",
            "manager:access",
      ],
      Role.MANAGER:[
            "user:read",
            "task:read",
            "task:create",
            "task:update",
            "report:read",
            "report:create",
            "manager:access",
      ],
      Role.USER:[
            "task:read",
            "task:create",
            "report:read",
      ],

}


def get_permissions(role: Role)->list:
      """ Role ki permission retunr karo"""
      return ROLE_PERMISSIONS.get(role,[])

def has_permission(role:Role,permission:str)->bool:
      """Check karo ki role ke pass ye permission hai ya nahi """
      return permission in ROLE_PERMISSIONS.get(role,[])

# RBAC ka main logic — ye check karta hai ki user ke paas sahi role hai ya nahi
# Ye middleware har protected route pe lagta hai or user ke role ke hisab se access allow ya deny karta hai
from fastapi import Depends, HTTPException, status
from app.middlewares.auth import get_current_user
from app.models.user import User
from app.config.roles import Role, has_permission

def require_roles(*allowed_roles:Role):
      """
    Sirf allowed roles wale users ko access deta hai.
 
    Example:
        @router.get("/admin")
        def admin_only(user = Depends(require_roles(Role.ADMIN))):
            ...
    """
      def checker(current_user:User = Depends(get_current_user)):
            if current_user.role not in allowed_roles:
                  raise HTTPException(
                        status_code = status.HTTP_403_FORBIDDEN,
                        detail= f"Access denied. Required roles: {[r.value for r in allowed_roles]}"
                  )
            return current_user
      return checker


def require_permission(permission:str):
      """
    Specific permission check karta hai.
 
    Example:
        @router.delete("/users/{id}")
        def delete_user(user = Depends(require_permission("user:delete"))):
            ...
    """
      def checker(current_user:User = Depends(get_current_user))-> User:
            if not has_permission(current_user.role,permission):
                  raise HTTPException(
                        status_code = status.HTTP_403_FORBIDDEN,
                        detail= f"Access denied. Required permission: {permission}"
                  )
            return current_user
      return checker




#Ready-made role checkers

# Inhe directly routes mein use karo

def admin_only(current_user:User = Depends(get_current_user))-> User:
       """Sirf Admin access kar sakta hai"""
       if current_user.role !=Role.ADMIN:
             raise HTTPException(status_code=403,detail="Admin access required")
       return current_user
                   
def manager_or_admin(current_user:User = Depends(get_current_user))-> User:
      """Admin ya Manager access kar sakte hain"""
      if current_user.role not in[Role.ADMIN, Role.MANAGER]:
            raise HTTPException(status_code=403,detail="Admin or Manager access required")
      return current_user

def any_logged_in_user(current_user:User = Depends(get_current_user))-> User:
      """Koi bhi logged-in user access kar sakta hai"""
      return current_user
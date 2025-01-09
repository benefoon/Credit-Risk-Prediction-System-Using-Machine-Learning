from fastapi import Security, HTTPException

roles = {
    "admin": ["read", "write", "delete"],
    "analyst": ["read"],
}

def check_permissions(user_role, permission):
    """Check if the user's role grants the required permission"""
    if permission not in roles.get(user_role, []):
        raise HTTPException(status_code=403, detail="Permission Denied")

@app.get("/admin-dashboard")
async def admin_dashboard(token_data: dict = Depends(verify_token)):
    user_role = token_data.get("role", "analyst")
    check_permissions(user_role, "write")
    return {"message": "Welcome, Admin!"}

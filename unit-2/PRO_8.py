# Global
x = 10
def outer():
    # Nonlocal
    y = 20
    def inner():
        # Local
        z = 30
        print("Global variable:", x)
        print("Nonlocal variable:", y)
        print("Local variable:", z)
    inner()
outer()

# pkg/render.py

def show_result(operation: str, a: float, b: float, result: float) -> None:
    print(f"  {a} {operation} {b}  =  {result:.4f}")

def show_error(message: str) -> None:
    print(f"Error: {message}")
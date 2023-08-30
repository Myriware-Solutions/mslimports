def hello() -> None:
  print("Hello World")
def hi(req:list) -> None:
  # [name]
  name = req[0].value
  print(f"Hi {name}")

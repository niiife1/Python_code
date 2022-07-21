def valid_pasword(pas):
      condition = True
      number_count = 0
      if not 6 <= len(pas) <= 10:
            print(f"Password must be between 6 and 10 characters")
            condition = False
      for s in pas:
            if s.isdigit():
                  number_count += 1

      if any(not c.isalnum() for c in pas):
            print("Password must consist only of letters and digits")
            condition = False
      if number_count < 2:
            print(f"Password must have at least 2 digits")
            condition = False

      if condition:
            print("Password is valid")
password = input()
valid_pasword(password)
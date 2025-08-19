import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    op, t, words = line.split(";")

    if op == "S":  # Split
        if t == "M":  # method -> remove ()
            words = words[:-2]
        result = ""
        for ch in words:
            if ch.isupper():
                result += " " + ch.lower()
            else:
                result += ch
        print(result.strip())

    elif op == "C":  # Combine
        parts = words.split()
        if t == "C":  # Class
            result = "".join(word.capitalize() for word in parts)
        elif t == "V":  # Variable
            result = parts[0].lower() + "".join(word.capitalize() for word in parts[1:])
        elif t == "M":  # Method
            result = parts[0].lower() + "".join(word.capitalize() for word in parts[1:]) + "()"
        print(result)

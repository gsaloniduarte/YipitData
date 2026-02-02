import re

def extract_numbers(text: str):
    return [int(x.replace(",", "")) for x in re.findall(r"\d[\d,]*", text)]

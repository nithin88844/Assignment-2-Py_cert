# You have a test string S . Your task is to match the pattern xxXxxXxxxx
# Here x denotes a digit character, and X denotes a non-digit character.

Regex_Pattern = r"[0-9]{2}(\D?)+[0-9]{2}(\D)+[0-9]{4}"
import re
print(str(bool(re.search(Regex_Pattern, input()))).lower())
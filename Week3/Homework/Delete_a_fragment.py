s = input()
before_str = s[:int(s.find('h'))]
after_str = s[int(s.rfind('h')+1):]
print(before_str + '' + after_str)

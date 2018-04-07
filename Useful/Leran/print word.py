word=input('your words:')
screen_width=80
text_width=len(word)
box_width=text_width+10
left_magin=(screen_width-box_width)//2

print(' '*left_magin+'+'+'-'*(box_width)+'+')
print(' '*(left_magin+5)+'|'+' '*text_width+'|')
print(' '*(left_magin+5)+'|'+word+'|')
print(' '*(left_magin+5)+'|'+' '*text_width+'|')
print(' '*left_magin+'+'+'-'*(box_width)+'+')

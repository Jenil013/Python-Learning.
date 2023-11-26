#Short Circuiting (basically it works as OR Gate)

is_friend = False
is_user = False

if is_friend or is_user:
  print ('You are a friend')
else:
  print ('You are not a friend')



is_magician = 0
is_expert = 1


if is_magician and is_expert:
  print ('You are a master magician')
elif is_magician and not is_expert:
  print ('Atleast you are getting there')
elif not is_magician and is_expert:
  print ('It cannot be possible')
else:
  print ('You need magic powers')

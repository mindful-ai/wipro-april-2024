import re
data = ['ab ', 'abc', 'a5e', 'a6f', '123 a6c anc', 'a5b', 'a55b', 'a555b', 'a5555b',
        'a55555b', 'a555555b', 'a5xb', '1/4', '3+2=5', 'def ghi', 'abc ab']
for item in data:
	m = re.search(r'a(55){2}', item)
	if m:
		print (m.group() + ' matched in ' + '\'' + item + '\'')

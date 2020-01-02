
def transliterate(class_number):
	labels = {0:'1na', 1:'1ra', 2:'2la', 3:'2na', 4:'3la', 5:'3na', 
	6:'ka', 7:'la', 8:'ma', 9:'nga', 10:'nya', 11:'pa', 12:'pi', 
	13:'q', 14:'sa', 15:'t', 16:'ta',
	17:'tha', 18:'tu', 19:'va', 20:'ya'}
	print(labels[class_number])
	label = labels[class_number]
	t = get_unicode(label)
	return t


def get_unicode(label):
	unicode_dict = {'1ra':'\u0BB0', '2na':'\u0BA8', '3na':'\u0BA9', 
	'ka':'\u0B95', 'la':'\u0BB2', 'ma':'\u0BAE', 'pa':'\u0BAA', 
	'pi': '\u0BAA\u0BBF', 
	'q': '\u0BC6', 't':'\u0BBE', 'tha': '\u0BA4', 
	'tu': '\u0B9F\u0BC1',
	'1na':'\u0BA3','2la':'\u0BB4','3la':'\u0BB3','nga':'\u0B99',
	'nya':'\u0B9E',
	'sa':'\u0B9A','ta':'\u0B9F','va':'\u0BB5','ya':'\u0BAF'}
	t = unicode_dict[label]
	# print(str(unicode_dict[label]))
	print(t)
	return t
# transliterate(11)




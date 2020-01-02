
def transliterate(class_number):
	labels = {0:'1ra', 1:'2na', 2:'3na', 3:'ka', 4:'la', 5:'ma', 6:'pa', 7:'pi', 8:'q', 9:'t', 10:'tha', 11:'tu'}
	print(labels[class_number])
	label = labels[class_number]
	t = get_unicode(label)
	return t


def get_unicode(label):
	unicode_dict = {'1ra':'\u0BB0', '2na':'\u0BA8', '3na':'\u0BA9', 'ka':'\u0B95', 'la':'\u0BB2', 'ma':'\u0BAE', 'pa':'\u0BAA', 'pi': '\u0BAA\u0BBF', 'q': '\u0BC6', 't':'\u0BBE', 'tha': '\u0BA4', 'tu': '\u0B9F\u0BC1'}
	t = unicode_dict[label]
	# print(str(unicode_dict[label]))
	print(t)
	return t
# transliterate(11)


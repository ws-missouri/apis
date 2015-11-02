import re, urllib2, json
from pyPdf import PdfFileReader

def clean_json(json):
    '''
    Turn dirty State Department JSON into clean JSON.
    '''
    return re.sub(r'new Date\(.*?\)', '""', json)
# The H Function

answer = raw_input('To see emails sent by Hillary Clinton, enter: H'+ '\n' + 'To see all emails sent by Hillary Clinton containing the word "Benghazi," enter: Benghazi' + '\n' + 'For links to .pdfs of all the emails, enter: Links' + '\n\n')

print '\n'

if answer == "H":

	CASE = "F-2014-20439"
	LIMIT = 1000000
	dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446062617343&searchText=(*)&beginDate=false&endDate=false&collection=false&postedBeginDate=false&postedEndDate=false&caseNumber=%s&collectionMatch=false&page=1&start=0&limit=%s' % (CASE, LIMIT)).read()
	valid_json = clean_json(dirty_json)
	data = json.loads(valid_json)
	for subject in data['Results']:
		print 'From: ' + subject['from']
		print 'RE: ' + subject['subject']
		print '\n'
elif answer == "Benghazi":
	SEARCHTERM = "Benghazi"
	CASE = "F-2014-20439"
	LIMIT = 1000000
	dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446062617343&searchText=(%s)&beginDate=false&endDate=false&collection=false&postedBeginDate=false&postedEndDate=false&caseNumber=%s&collectionMatch=false&page=1&start=0&limit=%s' % (SEARCHTERM, CASE, LIMIT)).read()
	valid_json = clean_json(dirty_json)
	data = json.loads(valid_json)
	for subject in data['Results']:
		print 'From: ' + subject['from']
		print 'RE: ' + subject['subject']
		print '\n'
elif answer == "Links":
	CASE = "F-2014-20439"
	LIMIT = 1000000
	dirty_json = urllib2.urlopen('https://foia.state.gov/searchapp/Search/SubmitSimpleQuery?_dc=1446062617343&searchText=(*)&beginDate=false&endDate=false&collection=false&postedBeginDate=false&postedEndDate=false&caseNumber=%s&collectionMatch=false&page=1&start=0&limit=%s' % (CASE, LIMIT)).read()
	valid_json = clean_json(dirty_json)
	data = json.loads(valid_json)
	for subject in data['Results']:
		print 'From: ' + subject['from']
		print 'RE: ' + subject['subject']
		link = 'https://foia.state.gov/searchapp/' + subject['pdfLink']
	#	linkobj = PdfFileReader(file(link, 'rb')).encode('ascii', 'ignore')
	#	pdf = pyPdf.PdfFileReader(linkobj)
	#	linktext = PdfFileReader(file(link, 'rb'))
	#	print "title = %s" % (input.getDocumentInfo().title)
	#	print linkobj
		print link
		print '\n'
else:
	print "Invalid input. Please rerun this script."
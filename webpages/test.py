import os

import pyForms.PageController

class Controller(pyForms.PageController):
	def setHTMLFile(self):
		self.HTMLFile = "webpages/test.html"


	def onInit(self, ctrls):
		#generate list of all pages
		self.tests = [{'title':x[:-5], 'passed':None, 'notes':''} for x in os.listdir("webpages") if (x.endswith(".html") and x != "test.html")]

		self.currentTest = 0
		ctrls.lpTests.dataSource = self.tests

	def onLoad(self, ctrls):
		self.tests[self.currentTest]['notes'] = ctrls.tbxTestNotes.text

	def onPrerender(self, ctrls):
		#setup iframe
		ctrls.iframeTesting.attributes['src'] = "/" + self.tests[self.currentTest]['title']
		ctrls.tbxTestNotes.text = self.tests[self.currentTest]['notes']


	def lpTests_configureLoop(self, ctrls, loopCtrls, item, index):
		loopCtrls.liTestText.innerHTML = item['title']
		loopCtrls.liTestText.attributes['class'] = "liTestText "

		if index == self.currentTest:
			loopCtrls.liTestText.attributes['class'] += "current "

		if item['passed'] is not None:
			if item['passed']:
				loopCtrls.liTestText.attributes['class'] += "passed"
			else:
				loopCtrls.liTestText.attributes['class'] += "failed"
	
	def btnPass_click(self, ctrls):
		self.tests[self.currentTest]['passed'] = True
		ctrls.lpTests.reconfigure()

	def btnFail_click(self, ctrls):
		self.tests[self.currentTest]['passed'] = False
		ctrls.lpTests.reconfigure()

	def btnSummary_click(self, ctrls):
		ctrls.divSummary.visible = True

		#generate summary
		summary = []
		summary.append("Testing summary:")
		passedText = {None: 'Not tested', False: 'FAILED', True: 'Passed'}
		for test in self.tests:
			testString = "\t '"+test['title']+"' - " + passedText[test['passed']]
			if test['notes'] != "":
				testString += " (" + test['notes'] + ")"
			summary.append(testString)

		if ctrls.tbxSummaryNotes.text != "":
			summary.append("\nSummary notes:")
			summary.append(ctrls.tbxSummaryNotes.text)

		ctrls.preSummary.innerHTML = "\n".join(summary)
	
	def btnSummaryClose_click(self, ctrls):
		ctrls.divSummary.visible = False

	def btnNext_click(self, ctrls):
		if self.currentTest < len(self.tests) - 1:
			self.currentTest += 1
			ctrls.lpTests.reconfigure()

	def btnPrev_click(self, ctrls):
		if self.currentTest > 0:
			self.currentTest -= 1
			ctrls.lpTests.reconfigure()



import unittest

import HtmlTestRunner

from test_alerts import TestAlerts
from test_elefant import Elefant
from test_login import TestLogin


class TestSuite(unittest.TestCase):
    def test_suite(self):
        tests = unittest.TestSuite()
        tests.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLogin),
            #unittest.defaultTestLoader.loadTestsFromTestCase(TestAlerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Elefant)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_title='first report', report_name='third_report', output='example suite')
        runner.run(tests)
import unittest
import main

class TestSequenceFunctions(unittest.TestCase):

    def test_filterEmails(self):

        testCases = [    #test array                       #test name   #expected result  
                        [["bob@test.com", "kate@bar.com"], "kate name", ["kate@bar.com"]],
                        [["bob@test.com", "kate@bar.com"], "bob name", ["bob@test.com"]],
                        [["bob@test.com", "kate@bar.com"], "something", []],
                        [["bob@test.com", "kate@bar.com"], "bob kate", ["bob@test.com", "kate@bar.com"]]
                    ]

        for testCase in testCases:
            self.assertEqual(main.filterEmails(testCase[0], testCase[1]), testCase[2])

suite = unittest.TestLoader().loadTestsFromTestCase(TestSequenceFunctions)
unittest.TextTestRunner(verbosity=2).run(suite)
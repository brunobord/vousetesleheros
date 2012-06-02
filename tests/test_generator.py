import unittest
import os
from subprocess import call
import shutil

TEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_repository')


class GenerateTestCase(unittest.TestCase):
    WEBSITE_DIR = os.path.join(TEST_DIR, 'website')

    def setUp(self):
        call(["python", "../generator.py", "--root-dir=%s" % TEST_DIR])

    def tearDown(self):
        shutil.rmtree(self.WEBSITE_DIR)

    def test_website_dir(self):
        self.assertTrue(os.path.exists(self.WEBSITE_DIR))

    def test_website_content(self):
        index_html = os.path.join(self.WEBSITE_DIR, 'index.html')
        self.assertTrue(os.path.exists(index_html))
        content = open(index_html).read()
        self.assertTrue('<h1>This is my title</h1>' in content)
        self.assertTrue('<h2>This is a subtitle</h2>' in content)

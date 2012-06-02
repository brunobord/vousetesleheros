import unittest
import os
from subprocess import call
import shutil

TEST_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_repository')


class GenerateTestCase(unittest.TestCase):
    WEBSITE_DIR = os.path.join(TEST_DIR, 'website')

    def setUp(self):
        call(["python", "generator.py", "--root-dir=%s" % TEST_DIR, '-q'])

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
        self.assertTrue('I am <strong>so</strong> happy to see you there' in content)
        self.assertTrue('Now I wanna go to this step / next_step' in content)
        self.assertTrue("I'd rather go to this one / other_step" in content)
        # test on notes
        self.assertTrue("Choice with notes" in content)
        self.assertTrue("This is notes" in content)

    def test_assetdir(self):
        asset_dir = os.path.join(self.WEBSITE_DIR, 'assets')
        style_path = os.path.join(asset_dir, 'style.css')
        self.assertTrue(os.path.exists(asset_dir))
        self.assertTrue(os.path.exists(style_path))

    def test_other_template(self):
        other_html = os.path.join(self.WEBSITE_DIR, 'other.html')
        self.assertTrue(os.path.exists(other_html))
        content = open(other_html).read()
        self.assertTrue('This is the other template' in content)

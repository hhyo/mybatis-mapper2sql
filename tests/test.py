import os
import unittest
from mybatis_mapper2sql import create_mapper, get_child_statement


class Mapper2SqlTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        xml = os.path.join(base_dir, 'test.xml')
        cls.mapper, cls.xml_raw_text = create_mapper(xml=xml)
        print("============XML_RAW_TEXT============")
        print(cls.xml_raw_text)

    def tearDown(self):
        print("============{}============".format(self.child_id))
        self.statement = get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_parameters(self):
        self.child_id = 'testParameters'

    def test_include(self):
        self.child_id = 'testInclude'

    def test_if(self):
        self.child_id = 'testIf'

    def test_trim(self):
        self.child_id = 'testTrim'

    def test_where(self):
        self.child_id = 'testWhere'

    def test_set(self):
        self.child_id = 'testSet'

    def test_choose(self):
        self.child_id = 'testChoose'

    def test_foreach(self):
        self.child_id = 'testForeach'

    def test_bind(self):
        self.child_id = 'testBind'


if __name__ == '__main__':
    unittest.main()

import os
import unittest
import mybatis_mapper2sql

base_dir = os.path.abspath(os.path.dirname(__file__))
xml = os.path.join(base_dir, 'test.xml')


class Mapper2SqlTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.mapper, cls.xml_raw_text = mybatis_mapper2sql.create_mapper(xml=xml)
        print("============XML_RAW_TEXT============")
        print(cls.xml_raw_text)

    def test_all(self):
        statement = mybatis_mapper2sql.get_statement(self.mapper, result_type='raw', strip_comments=True)
        print(statement)

    def test_all_result(self):
        statement = mybatis_mapper2sql.get_statement(self.mapper, result_type='list', strip_comments=True)
        print(statement)

    def test_all_wrong_result(self):
        try:
            mybatis_mapper2sql.get_statement(self.mapper, result_type='sql', strip_comments=True)
        except RuntimeError as e:
            self.assertEqual(str(e), 'Invalid value for sql_type: raw|list')
        else:
            self.fail('IOError not raised')

    def test_base(self):
        self.child_id = 'testBasic'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_parameters(self):
        self.child_id = 'testParameters'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_include(self):
        self.child_id = 'testInclude'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_if(self):
        self.child_id = 'testIf'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_trim(self):
        self.child_id = 'testTrim'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_where(self):
        self.child_id = 'testWhere'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_set(self):
        self.child_id = 'testSet'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_choose(self):
        self.child_id = 'testChoose'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_foreach(self):
        self.child_id = 'testForeach'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)

    def test_bind(self):
        self.child_id = 'testBind'
        print("============{}============".format(self.child_id))
        self.statement = mybatis_mapper2sql.get_child_statement(self.mapper, child_id=self.child_id, reindent=True)
        print(self.statement)


if __name__ == '__main__':
    unittest.main()

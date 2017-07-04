'''
Dummy Module
'''

import sys
import os

if __name__ == "__main__":
    print "Could not run in standalone mode. Exiting..."
    sys.exit(1)

class Reporter(object):
    ''' Base Reporter class which is extendable by the technology specific Reporter '''
    _supported_techs = ['gsm', 'cdma', 'hdr', 'tdscdma', 'wcdma']
    _data_loc = None
    _datamine_loc = None
    __tech = None

    def __init__(self, tech):
        '''Base Reporter init'''
        if tech.lower() in self._supported_techs:
            self.__tech = tech
        else:
            raise NotImplementedError("tech %s is not supported yet" % tech)

    def __str__(self):
        return ('[%8s]: Data Path: %-10s Datamine Path: %-10s'
                % (self.__tech, self._data_loc, self._datamine_loc))

    def __get_result__(self, testcase, excel_file, excel_sheet, test_name):
        ''' For a Given Test case and Datamined Result  and Sheet Name,
            1. get result for all channels along wth Limts for any failure
            return reult
        '''
        return testcase+excel_file+excel_sheet+test_name+self.datamine_path

    def __datamine__(self, test_tree):
        print "__datamine__"+test_tree+self.datamine_path

    def data_path(self, path_loc=None):
        ''' Base Reporter data_path used to set/get data_loc
            This is the location where the test data is looked for
        '''
        if path_loc is None:
            return self._data_loc
        elif os.path.exists(path_loc):
            self._data_loc = path_loc
        else:
            raise IOError("file path %s not found"%path_loc)

    def datamine_path(self, path_loc=None):
        ''' Base Reporter data_path used to set/get datamine_loc
            This is the location where the intermediate dataminer reports are stored
        '''
        if path_loc is None:
            return self._datamine_loc
        elif os.path.exists(path_loc):
            self._datamine_loc = path_loc
        else:
            raise IOError("file path %s not found"%path_loc)

class GsmReporter(Reporter):
    '''GSM Reporter'''
    def __init__(self):
        super(GsmReporter, self).__init__("gsm")

    def __map_testcase__(self, testcase):
        ''' For a given test case,
            1. Map to Test Tree and Excel Sheet name
            It can be predefined
        '''
        print self.datamine_path+testcase
        return ['test_tree', 'excel_file', 'excel_sheet', 'test_name']

    def __do_datamine__(self, test_tree):
        ''' Datamining options are specific to technology
            prepare datamining command and pass it to base class datamine
            function
        '''
        print "Perform datamining"+test_tree
        self.__datamine__(test_tree)

    def get_test_result(self, testcase):
        '''For a Given test case,
        1. Map to Test Tree and Sheet Name and Work book
        2. If not already data mined, datamine
        3. Get the result for all channel && test limits along with any failure reason
        4. Return Result'''
        test_tree, excel_file, excel_sheet, test_name = self.__map_testcase__(testcase)
        self.__do_datamine__(test_tree)
        self.__get_result__(testcase, excel_file, excel_sheet, test_name)
        print testcase, excel_file, excel_sheet, test_name

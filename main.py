'''
Dummy module
'''

if __name__ == "__main__":
    import sys
    import reporter

    gsm_reporter = reporter.GsmReporter()
    gsm_reporter.data_path("./")
    gsm_reporter.datamine_path("./")
    gsm_reporter.get_test_result("Dummy")
    print gsm_reporter
    sys.exit(0)

    # def tcr_template(self, path_loc=None):
    #     ''' Base Reporter tcr_template used to set/get tcr_template
    #         This is the template file which is used as reference.
    #         Seperate file is cloned from this file and stored the
    #         result data in datamine_loc with file name $REPORT_NAME
    #     '''
    #     if tcr_loc is None:
    #         return self.__tcr_loc
    #     elif os.path.exists(path_loc):
    #         self.__tcr_template_loc = path_loc
    #     else:
    #         raise IOError("tcr templete file path %s not found"%path_loc)

    # def ads_sheet_name(self, sheet_name):
    #     '''Sets the Excel Sheet Name where GSM-ADS test cases are present
    #        Default Value is GSM_ADS (case insesntive)
    #     '''
    #     if sheet_name is None:
    #         return self.__ads_sheet_name
    #     else:
    #         self.__ads_sheet_name = sheet_name

#!/usr/bin/python
import unittest,sys
sys.path.append('../../..')

from common.monotesting import *

from be_0100_ChangeBlogNameTest import *
from be_0200_CreateSoryTest import *
from be_0300_SearchForStoryTest import *
from be_0400_createUserTest import *
from be_0500_modifyProfileTest import *
from be_0600_AddEditorPrivToUserTest import *
from be_0700_addCategoryAsMonoUserTest import *
from be_0800_createStoryAsMonoUserTest import *
from be_0900_addBlogRollAsMonoUserTest import *
from be_1000_addPageAsMonoUserTest import *
from be_1100_ChangeUserProfileAsMonoUserTest import *

if __name__ == '__main__':
    monotesting_main()

#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
@author: EdwardLiu 
@contact: lonnyliu@126.com

@file: devops_git.py
@time: 2018/6/5 17:41
#测试
"""

from subprocess import call, STDOUT, Popen, PIPE
import os
import shutil


class Devops_Git(object):

    def __init__(self):

        self.git_exec = "/usr/local/bin/git"

        self.branch = "master"

        self.tmp_branch = "temp"

        self.repo = "/Users/lonny/Documents/devops"

        self.export = "/Users/lonny/Downloads/export"

    # 克隆最新版本到本地并创建临时分支
    def last_version(self):

        clone_command = "{0} fetch origin {1}:{2}".format(self.git_exec, self.branch, self.tmp_branch)

        full = open(os.devnull, 'w')

        os.chdir(self.repo)

        return_code = call(clone_command, shell=True, stdout=full, stderr=STDOUT)

        if return_code == 0:

            # print ("Get last verison successful!!")

            return 0

        else:

            # print ("Get Last Version failed!")

            return 1

    # 对比版本库是否有更新
    def diff_repository(self):

        os.chdir(self.repo)

        diff_command = "{0} diff {1}".format(self.git_exec, self.tmp_branch)

        if self.last_version() == 0:

            process_diff = Popen(diff_command, shell=True, stdout=PIPE, stderr=PIPE)

            output = process_diff.stdout.read()

            err = process_diff.stderr.read()

            if output == "":

                # print ("The latest repository does not need to be updated")

                return 1

            else:

                # print ("Project is Need update")

                return 0

    # 版本库更新
    def update_repository(self):

        os.chdir(self.repo)

        update_command = "{0} merge {1}".format(self.git_exec, self.tmp_branch)

        if self.diff_repository() == 0:

            process_update = Popen(update_command, shell=True, stderr=PIPE, stdout=PIPE)

            out, err = process_update.communicate()

            if process_update.returncode == 0:

                # print ("repository update successful")

                return 0

            else:

                # print ("The latest repository does not need to be updated")

                return 1

    # 获取版本信息
    def version_repository(self):

        # 更换工作目录
        os.chdir(self.repo)

        version_command = "git log -1 --pretty=format:%h"

        process_version = Popen(version_command, shell=True, stdout=PIPE, stderr=PIPE)

        out, err = process_version.communicate()

        return out

    # 导出分支
    def ExportDelete_branch(self):

        if os.path.exists(self.export):

            shutil.rmtree(self.export)
            os.makedirs(self.export)
        # 第一次运行时走 else
        else:

            os.makedirs(self.export)

        full = open(os.devnull, 'w')

        # 更换工作目录
        os.chdir(self.repo)

        export_command = "{0} archive {1} | tar -x -C {2}".format(self.git_exec, self.branch, self.export)

        process_export = call(export_command, shell=True, stdout=full, stderr=STDOUT)

        if process_export == 0:

            # messages = "export branch {0} to {1} successful".format(self.branch, self.export)

            # print messages

            return 0

        else:

            # messages = "export branch {0} to {1} Failed".format(self.branch, self.export)

            # print messages

            return 1

    # 删除临时分支
    def delete_temp_branch(self):

        # 更换工作目录
        os.chdir(self.repo)

        delete_branch = "{0} branch -d {1}".format(self.git_exec, self.tmp_branch)

        full = open(os.devnull, 'w')

        process_delete = call(delete_branch, shell=True, stdout=full, stderr=STDOUT)

        if process_delete == 0:

            # print ("delete branch {0} is successful".format(self.tmp_branch))

            return 0

        else:

            # print ("delete branch {0} is failed".format(self.tmp_branch))

            return 1
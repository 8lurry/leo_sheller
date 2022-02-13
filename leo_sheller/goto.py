# -*- coding: UTF-8 -*-
# Copyright 2022 8lurry <sharifmehedi24@outlook.com>
# License: GNU Affero General Public License v3 (see file COPYING for details)

import os
import re

from pathlib import Path

os.environ.setdefault('LEOsBASE', os.environ['HOME'] + '/GitHub')
FOUND = False
check_leos_base = lambda base: base == "/home/blurry/lino/env/repositories/book/lino_book/projects"

def goto(base, project_name):
    def to_go(base):
        path = Path(base)

        def get_project_path(path):
            project_path = path / 'projects'

            if not project_path.exists():
                for d in os.listdir(path):
                    if not re.match('\w*\.\w*', d):
                        im_path = path / d
                        if im_path.is_dir():
                            for d in os.listdir(im_path):
                                if re.match('lino*', d):
                                    project_path = im_path / d / 'projects' / project_name
                                    if project_path.exists():
                                        return project_path
            else:
                project_path = project_path / project_name
                if project_path.exists():
                    return project_path

        project_path = get_project_path(path)
        if project_path is not None:
            print(project_path)
            exit()

    to_go(base)

    if check_leos_base(base):
        to_go(os.environ['LEOsBASE'])
    print("0")
    exit()

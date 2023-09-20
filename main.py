# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: araumi
# Email: 532990165@qq.com
# DateTime: 2023/9/20 下午5:00

import pathlib
import json
from model.multiple_choice import MultipleChoiceQuestion

database_path: pathlib.Path = pathlib.Path("./database.json")


def main():
    database: dict = json.load(database_path.open("r", encoding="utf-8"))
    for raw in database:
        qa: MultipleChoiceQuestion = MultipleChoiceQuestion.create(raw=raw)
        qa.view()
        print()


if __name__ == "__main__":
    main()

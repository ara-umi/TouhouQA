# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: araumi
# Email: 532990165@qq.com
# DateTime: 2023/9/20 下午4:43

from . import base as prop
from . import exception
from .interface import IQuestion


class MultipleChoiceQuestion(IQuestion):
    raw: dict = prop.RawProperty()
    question: str = prop.QuestionProperty()
    options: dict = prop.OptionsProperty()
    answer: str = prop.AnswerProperty()
    input: str = prop.AnswerProperty()
    check: bool = prop.Property()

    @classmethod
    def create(cls, raw: dict) -> "MultipleChoiceQuestion":
        obj = cls()
        obj.raw = raw

        try:
            obj.question = raw["question"]
            obj.options = raw["options"]
            obj.answer = raw["answer"]

            # answer需要在options中
            if obj.answer not in obj.options.keys():
                raise ValueError("Invalid question format: answer must be in options")

            return obj
        except IndexError:
            raise ValueError("Invalid question format")

    def set_input(self, input_: str):
        """
        涉及到空字符串跳过
        """
        if not isinstance(input_, str):
            raise ValueError(f"Invalid input format: input must be a non-empty string, got \"{input_}\"")

        if not input_:
            raise exception.Skip()

        if input_ not in self.options.keys():
            raise ValueError(f"Invalid input format: input must be in options, got \"{input_}\"")

        self.input = input_

    def set_check(self) -> bool:
        self.check = True if self.input == self.answer else False
        return self.check

    def __repr__(self) -> str:
        return repr(self.raw)

    def view(self):
        print(self.question)
        for key, value in self.options.items():
            print(f"{key}: {value}")

        input_: str = input(">>> ")

        self.set_input(input_=input_)
        check: bool = self.set_check()

        if check:
            print("太棒了！恭喜你回答正确！")
        else:
            print("不好意思，你回答错误了。")


if __name__ == "__main__":
    pass

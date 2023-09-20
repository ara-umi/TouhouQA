# !/usr/bin/env python
# -*- coding: UTF-8 -*-
# Author: araumi
# Email: 532990165@qq.com
# DateTime: 2023/9/20 下午4:50


class Property(object):

    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        instance.__dict__[self.storage_name] = value


class RawProperty(Property):
    def __set__(self, instance, value):
        if not isinstance(value, dict) or not value:
            raise ValueError(f"Invalid raw format: raw must be a non-empty dict, got \"{value}\"")

        instance.__dict__[self.storage_name] = value


class QuestionProperty(Property):
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value:
            raise ValueError(f"Invalid question format: question must be a non-empty string, got \"{value}\"")

        instance.__dict__[self.storage_name] = value


class OptionsProperty(Property):

    def __set__(self, instance, value):
        if not isinstance(value, dict) or not value:
            raise ValueError(f"Invalid question format: options must be a non-empty dict, got \"{value}\"")

        for k, v in value.items():
            if not (len(k) == 1 and k.isupper()):
                raise ValueError(f"Invalid question format: options key must be a single uppercase letter, got \"{k}\"")
            if not isinstance(v, str) or not v:
                raise ValueError(f"Invalid question format: options value must be a non-empty string, got \"{v}\"")

        instance.__dict__[self.storage_name] = value


class AnswerProperty(Property):
    def __set__(self, instance, value):
        if not isinstance(value, str) or not value:
            raise ValueError(f"Invalid question format: answer must be a non-empty string, got \"{value}\"")

        instance.__dict__[self.storage_name] = value


if __name__ == "__main__":
    pass

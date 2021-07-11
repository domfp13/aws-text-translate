# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Luis Enrique Fuentes Plata

import boto3


class Translate:
    def __init__(self, text: str, source_language_code: str = "en", target_language_code: str = "de") -> None:
        self.text: str = text
        self.source_language_code: str = source_language_code
        self.target_language_code: str = target_language_code
        self.client = self.get_text_translate_client()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        if not value:
            raise ValueError("text value CANNOT be empty")
        self._text = value

    @property
    def source_language_code(self):
        return self._source_language_code

    @source_language_code.setter
    def source_language_code(self, value: str):
        if not value or len(value) != 2:
            raise ValueError("source_language_code CANNOT be empty or more than 2 digits")
        self._source_language_code = value

    @property
    def target_language_code(self):
        return self._target_language_code

    @target_language_code.setter
    def target_language_code(self, value: str):
        if not value or len(value) != 2:
            raise ValueError("target_language_code CANNOT be empty or mor than 2 digits")
        self._target_language_code = value

    def get_text_translate_client(self):
        """This function returns a boto3.client for text translate.
        Returns:
            [boto3.client]: boto3.client.Translate object.
        """
        return boto3.client("translate")

    def translate(self) -> None:
        """This method prints out the translated text to the target language
        Returns:
            None
        """
        result = self.client.translate_text(Text="Its a sunny day today",
                                            SourceLanguageCode=self.source_language_code,
                                            TargetLanguageCode=self.target_language_code)
        print(f'TranslatedText: {result["TranslatedText"]}')
        print(f'SourceLanguageCode: {result["SourceLanguageCode"]}')
        print(f'TargetLanguageCode: {result["TargetLanguageCode"]}')

    def __del__(self):
        pass

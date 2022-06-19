# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Enrique Plata

import boto3


class Translate:
    def __init__(self, text: str, source_language_code: str = "en", target_language_code: str = "de", region_name="us-east-1") -> None:
        self.text: str = text
        self.source_language_code: str = source_language_code
        self.target_language_code: str = target_language_code
        self.region_name: str = region_name
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

    @property
    def region_name(self):
        return self._region_name

    @region_name.setter
    def region_name(self, value: str):
        if not value:
            raise ValueError("region_name CANNOT be empty")
        self._region_name = value

    def get_text_translate_client(self):
        """This function returns a boto3.client for text translate.
        Returns:
            [boto3.client]: boto3.client.Translate object.
        """
        return boto3.client("translate", region_name=self.region_name)

    def translate(self) -> None:
        """This method prints out the translated text to the target language
        Returns:
            None
        """
        result = self.client.translate_text(Text=self.text,
                                            SourceLanguageCode=self.source_language_code,
                                            TargetLanguageCode=self.target_language_code)

        print(f'Translate from {self.source_language_code} to {self.target_language_code}')
        print(f'Original Text: {self.text}')
        print(f'Translated Text: {result["TranslatedText"]}')

    def __del__(self):
        pass

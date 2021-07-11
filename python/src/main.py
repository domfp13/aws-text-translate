# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Luis Enrique Fuentes Plata

import boto3

from aws.services import Translate

if __name__ == '__main__':
    translation = Translate(text="This is my text", source_language_code="en", target_language_code="es")
    translation.translate()

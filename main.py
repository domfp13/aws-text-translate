# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Luis Enrique Fuentes Plata

import boto3

from src.aws.services import Translate

if __name__ == '__main__':
    my_text : str = "If a man never contradicts himself, the reason must be that he virtually never says anything at all."
    translation = Translate(text=my_text, source_language_code="en", target_language_code="es")
    translation.translate()


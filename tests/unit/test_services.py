# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Luis Enrique Fuentes Plata

import pytest
from src.aws.services import Translate


def test_get_text_translate_client():
    import boto3_type as bt
    client = Translate("This is a test").client
    assert bt.client.istype(client, "translate")

import uuid
import base64


class Unimplemented(Exception):
    pass


class RoleFail(Exception):
    pass


def new_uuid():
    return str(uuid.uuid4())


def encode(x):
    return base64.b64encode(bytes(x, "utf-8"))


SUPERUSER = '*'
""" role used to bypass all permission checks """

ROOT_UUID = '00000000-0000-0000-0000-000000000000'
""" parent UUID used to initialize a stream """

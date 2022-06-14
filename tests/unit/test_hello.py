from app import get_db


def test_ok():
    documents=get_db("testing").find()
    assert isinstance(documents,list)

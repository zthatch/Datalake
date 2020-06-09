from accessWasabi import WasabiInterface as Wasabi

import pytest

test_tuples = [
    ("zthatcher_image.tif", "UploadDataString"),
    ("zthatcher_txt.txt", "UploadDataString")
]

@pytest.mark.parametrize("tt", test_tuples)
def test_helper_python(tt):
    """
    do not use, not yet working. Go to ifmain=main in accessWasabi to test manually.
    :param tt:
    :return:
    """
    uploadstring = Wasabi.file_write(tt[0])
    downloadstring = Wasabi.file_read(tt[0], 'localfile.txt')
    assert downloadstring == tt[1]
    Wasabi.file_delete(tt[0])
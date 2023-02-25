import pytest
from deepClassifier.utils import read_yaml
from pathlib import Path
from box import ConfigBox
from ensure.main import EnsureError


class Test_read_yaml:
    yaml_files = [
        "tests/data/empty.yaml",
        "tests/data/demo.yaml"
    ]

    def test_read_yaml_empty(self):
        with pytest.raises(ValueError):
            read_yaml(Path(self.yaml_files[0]))

    def test_read_yaml_return_type(self):
        respone = read_yaml(Path(self.yaml_files[-1]))
        assert isinstance(respone, ConfigBox) # is the o/p 'response' is an instance of 'ConfigBox' or not

    @pytest.mark.parametrize("path_to_yaml", yaml_files) # passing the multiple arguments in below function
    def test_read_yaml_bad_data_type(self, path_to_yaml): # checking whether it detects wrong data type was passed as an argument
        with pytest.raises(EnsureError):
            read_yaml(path_to_yaml)



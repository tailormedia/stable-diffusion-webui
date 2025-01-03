import pytest

from scripts.outpainting_mk_2 import Script
from unittest.mock import MagicMock

class TestOutpaintingMk2Script:
    def test_script_title(self):
        # Arrange
        script = Script()

        # Act
        title = script.title()

        # Assert
        assert title == "Outpainting mk2", "The script title should be 'Outpainting mk2'"
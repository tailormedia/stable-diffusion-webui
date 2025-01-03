import pytest

from scripts.loopback import Script
from unittest.mock import Mock, patch

class TestLoopbackScript:
    def test_ui_method(self):
        script = Script()

        # Mock gradio components
        with patch('gradio.Slider', return_value=Mock()) as mock_slider, \
             patch('gradio.Dropdown', return_value=Mock()) as mock_dropdown:

            result = script.ui(is_img2img=True)

            # Check if the correct number of UI elements are returned
            assert len(result) == 4

            # Check if the correct types of UI elements are created
            assert mock_slider.call_count == 2  # Two sliders
            assert mock_dropdown.call_count == 2  # Two dropdowns

            # Check if the sliders are created with correct parameters
            mock_slider.assert_any_call(
                minimum=1, maximum=32, step=1, label="Loops", value=4,
                elem_id=script.elem_id("loops")
            )
            mock_slider.assert_any_call(
                minimum=0, maximum=1, step=0.01, label="Final denoising strength",
                value=0.5, elem_id=script.elem_id("final_denoising_strength")
            )

            # Check if the dropdowns are created with correct parameters
            mock_dropdown.assert_any_call(
                label="Denoising strength curve",
                choices=["Aggressive", "Linear", "Lazy"],
                value="Linear"
            )
            mock_dropdown.assert_any_call(
                label="Append interrogated prompt at each iteration",
                choices=["None", "CLIP", "DeepBooru"],
                value="None"
            )
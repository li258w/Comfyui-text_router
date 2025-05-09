# This is a custom node for ComfyUI that routes a single input text to one of six output texts based on the selection,
# while preserving the existing values of non-selected outputs.
# Usage:
# - Connect the translated text to "input_text"
# - Connect a number (1-6) to "selection" to choose which output to route to
# - Connect the current values of the six Chinese text boxes to "current_text1" to "current_text6"
# - Connect each "OutputN" to the corresponding Chinese text box

class TextRouter:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "input_text": ("STRING",),
                "selection": ("INT", {"default": 1, "min": 1, "max": 6}),
                "current_text1": ("STRING",),
                "current_text2": ("STRING",),
                "current_text3": ("STRING",),
                "current_text4": ("STRING",),
                "current_text5": ("STRING",),
                "current_text6": ("STRING",),
            }
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("Output1", "Output2", "Output3", "Output4", "Output5", "Output6")
    FUNCTION = "run"
    CATEGORY = "Custom/TextRouter"

    def run(self, input_text, selection, current_text1, current_text2, current_text3, current_text4, current_text5, current_text6):
        outputs = [current_text1, current_text2, current_text3, current_text4, current_text5, current_text6]
        if 1 <= selection <= 6:
            outputs[selection - 1] = input_text
        return tuple(outputs)

NODE_CLASS_MAPPINGS = {"TextRouter": TextRouter}
NODE_DISPLAY_NAME_MAPPINGS = {"TextRouter": "Text Router"}
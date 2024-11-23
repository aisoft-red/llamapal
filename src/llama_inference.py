from llama_stack_client import LlamaStack
from transformers import AutoProcessor

processor = AutoProcessor.from_pretrained("meta/llama-3.2-vision")
llama = LlamaStack(model="meta/llama-3.2-vision")

def generate_commentary(frame):
    inputs = processor(images=frame, return_tensors="pt")
    outputs = llama.generate(**inputs)
    return processor.decode(outputs[0], skip_special_tokens=True)

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

# Load pre-trained model and tokenizer
model = GPT2LMHeadModel.from_pretrained('gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

# Move model to GPU if available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Function to generate tags
def generate_tags(caption):
    # Encode the caption
    inputs = tokenizer.encode(caption, return_tensors='pt').to(device)
    
    # Generate tags
    outputs = model.generate(inputs, max_length=50, num_beams=5, temperature=0.7)
    
    # Decode the tags
    tags = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    
    return tags

# Test the function
print(generate_tags("a waterfall in the middle of a lush green forest"))
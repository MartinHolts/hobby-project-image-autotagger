from transformers import (
 Blip2VisionConfig,
 Blip2QFormerConfig,
 OPTConfig,
 Blip2Config,
 Blip2ForConditionalGeneration,
)

# Initializing BLIP-2 vision, BLIP-2 Q-Former and language model configurations
vision_config = Blip2VisionConfig().to_dict()
qformer_config = Blip2QFormerConfig().to_dict()
text_config = OPTConfig().to_dict()

# Combine the configurations into a single dictionary
combined_config = {**vision_config, **qformer_config, **text_config}

# Initialize a Blip2Config with the combined configuration
config = Blip2Config(**combined_config)

print(combined_config)

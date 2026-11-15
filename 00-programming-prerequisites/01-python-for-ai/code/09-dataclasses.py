from dataclasses import dataclass

@dataclass
class ModelConfig:
  model_name: str
  learning_rate: float
  batch_size: int
  epochs: int = 10  # Default value for epochs

config1 = ModelConfig(
    model_name="NeuralNetwork",
    learning_rate=0.001,
    batch_size=32
)

config2 = ModelConfig(
    model_name="NeuralNetwork",
    learning_rate=0.001,
    batch_size=32
)

print(config1)
print(config2)

print(config1 == config2)  
"""GPU specifications and carbon intensity data."""

GPU_SPECS = {
    # NVIDIA Data Center GPUs
    "A100": {"tdp": 400, "name": "NVIDIA A100", "category": "datacenter"},
    "A100-80GB": {"tdp": 400, "name": "NVIDIA A100 80GB", "category": "datacenter"},
    "H100": {"tdp": 700, "name": "NVIDIA H100", "category": "datacenter"},
    "H100-80GB": {"tdp": 700, "name": "NVIDIA H100 80GB", "category": "datacenter"},
    "V100": {"tdp": 300, "name": "NVIDIA V100", "category": "datacenter"},
    "A40": {"tdp": 300, "name": "NVIDIA A40", "category": "datacenter"},
    "A30": {"tdp": 165, "name": "NVIDIA A30", "category": "datacenter"},
    "A10": {"tdp": 150, "name": "NVIDIA A10", "category": "datacenter"},
    # NVIDIA Consumer GPUs
    "RTX-4090": {"tdp": 450, "name": "NVIDIA RTX 4090", "category": "consumer"},
    "RTX-4080": {"tdp": 320, "name": "NVIDIA RTX 4080", "category": "consumer"},
    "RTX-3090": {"tdp": 350, "name": "NVIDIA RTX 3090", "category": "consumer"},
    "RTX-3080": {"tdp": 320, "name": "NVIDIA RTX 3080", "category": "consumer"},
    # AMD GPUs
    "MI250X": {"tdp": 560, "name": "AMD MI250X", "category": "datacenter"},
    "MI210": {"tdp": 300, "name": "AMD MI210", "category": "datacenter"},
    "MI100": {"tdp": 300, "name": "AMD MI100", "category": "datacenter"},
    # Google TPU
    "TPU-v4": {"tdp": 450, "name": "Google TPU v4", "category": "tpu"},
    "TPU-v3": {"tdp": 450, "name": "Google TPU v3", "category": "tpu"},
}

CARBON_INTENSITY = {
    "global": 0.475,
    "us": 0.386,
    "eu": 0.276,
    "china": 0.555,
    "india": 0.708,
    "uk": 0.233,
    "france": 0.056,
    "iceland": 0.010,
}

DEFAULT_PUE = 1.58
EFFICIENT_PUE = 1.2
HYPERSCALE_PUE = 1.1

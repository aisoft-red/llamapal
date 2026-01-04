# LlamaPal

AI-powered sports commentary companion that brings live, uplifting commentary to amateur sports activities using Llama 3.2 Vision.

[![Demo](https://img.shields.io/badge/Demo-HuggingFace-yellow)](https://huggingface.co/spaces/jwplatta/LlamaPalDemo)
[![Python](https://img.shields.io/badge/Python-3.8+-blue)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

## Overview

LlamaPal bridges fitness and entertainment by making every sports moment exciting. It uses advanced vision AI to analyze video frames and generate real-time motivational commentary, promoting health and well-being through engaging sports experiences.

![Demo](data/demo/processed_frames_image.gif)

### Key Features

- **Real-time Commentary** - Analyzes video frames and generates 20-word motivational sports commentary
- **Multi-Model Support** - Local inference via Ollama or cloud inference via Groq API
- **Visual Overlays** - Text commentary rendered directly on video frames
- **GIF Generation** - Creates animated GIF compilations of processed frames
- **Web Demo** - Gradio-based interface for side-by-side comparison

## Quick Start

```bash
# Clone the repository
git clone https://github.com/aisoft-red/llamapal.git
cd llamapal

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Ollama (for local inference)
ollama serve
ollama pull llama3.2-vision

# Run the pipeline
cd src
python main.py
```

## Requirements

### System Requirements
- Python 3.8+
- 8GB+ RAM (16GB recommended for local inference)
- GPU recommended for faster processing

### API Options (choose one)

**Option A: Local Inference (Ollama)**
```bash
# Install Ollama from https://ollama.ai
ollama serve
ollama pull llama3.2-vision
```

**Option B: Cloud Inference (Groq)**
```bash
export GROQ_API_KEY="your-groq-api-key"
```

## Installation

```bash
# Clone repository
git clone https://github.com/aisoft-red/llamapal.git
cd llamapal

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Dependencies

| Package | Purpose |
|---------|---------|
| `opencv-python` | Video frame extraction and image processing |
| `torch` | Deep learning framework |
| `transformers` | Pre-trained model support |
| `ollama` | Local Llama 3.2 Vision inference |
| `groq` | Cloud API for Llama 3.2 Vision |
| `llama-stack-client` | Llama Stack client interface |
| `pyttsx3` | Text-to-speech (optional) |
| `gradio` | Web UI framework |

## Usage

### Process Videos (CLI)

```bash
cd src
python main.py
```

This will:
1. Read videos from `./data/input/video_*.mp4`
2. Extract frames (every 50th frame by default)
3. Generate commentary using Llama 3.2 Vision
4. Overlay text on frames
5. Create output video and animated GIF

### Launch Web Demo

```bash
python demo.py
```

Opens at `http://localhost:7860` with side-by-side before/after comparison.

### Configuration

Edit `src/main.py` to customize:

```python
frame_interval=50        # Extract every Nth frame
use_groq=True            # False for local Ollama, True for Groq API
```

## Project Structure

```
llamapal/
├── README.md                    # This file
├── requirements.txt             # Python dependencies
├── demo.py                      # Gradio web interface
│
├── src/                         # Source code
│   ├── main.py                  # Entry point, orchestration
│   ├── llama_inference.py       # AI inference and commentary
│   ├── video_processing.py      # Frame extraction
│   ├── overlay_output.py        # Text overlay rendering
│   └── encode_image.py          # Base64 image encoding
│
└── data/
    ├── input/                   # Input videos
    │   ├── video_0.mp4
    │   ├── video_1.mp4
    │   └── basketball_one_player.mp4
    └── demo/                    # Demo assets
        ├── intro.gif
        └── processed_frames_image.gif
```

## Processing Pipeline

```
Video Input
    ↓
Frame Extraction (OpenCV)
    ↓
Base64 Encoding
    ↓
Llama 3.2 Vision (Ollama/Groq)
    ↓
Commentary Generation (20 words)
    ↓
Text Overlay (PIL)
    ↓
Output Video + GIF
```

## Output

Each run creates timestamped output in `data/output/[YYYY-MM-DD_HH-MM-SS]/`:

```
output/2024-11-23_19-27-17/
├── video_0.mp4                      # Processed video
├── video_0.mp4_processed_frame_*.jpg # Individual frames
├── commentary.txt                    # Generated commentary
└── processed_frames_image.gif        # Animated GIF
```

## Inference Comparison

| Feature | Ollama (Local) | Groq (Cloud) |
|---------|---------------|--------------|
| Model | llama3.2-vision | llama-3.2-11b-vision-preview |
| Speed | Slower | Faster |
| Cost | Free | API pricing |
| Privacy | Full | Data sent to cloud |
| Hardware | 8B+ GPU/CPU | None required |

## Problem Statement

Many people struggle with staying physically active or lack motivation in casual sports. Social isolation and inactivity contribute to mental health challenges. LlamaPal addresses this by:

- Making sports more engaging and fun
- Promoting health through motivational interaction
- Enhancing community spirit
- Making amateur sports accessible to everyone

## Impact Metrics

- Increased physical activity through engaging commentary
- Improved mental health via social and motivational interactions
- Enhanced community spirit in amateur sports

## Demo & Resources

- **Live Demo**: [HuggingFace Spaces](https://huggingface.co/spaces/jwplatta/LlamaPalDemo)
- **Pitch Deck**: [Google Slides](https://docs.google.com/presentation/d/141o2SHSkAhst-aWMj-K7VtqYsRpEFr6ww2SOiAJ1N3s/edit?usp=sharing)

## Troubleshooting

### Ollama not responding
```bash
# Ensure Ollama is running
ollama serve

# Check if model is downloaded
ollama list
# If not present:
ollama pull llama3.2-vision
```

### Groq API errors
```bash
# Verify API key is set
echo $GROQ_API_KEY

# Set if missing
export GROQ_API_KEY="your-key-here"
```

### Out of memory
- Reduce `frame_interval` to process fewer frames
- Use Groq API instead of local inference
- Close other applications

## Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) for details.

## Acknowledgments

- Llama 3.2 Vision by Meta
- Ollama for local inference
- Groq for cloud inference API

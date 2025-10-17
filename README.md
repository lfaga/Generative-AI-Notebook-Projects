# Generative AI Notebooks: A Learning Journey

This repository contains a collection of Google Colab notebooks from my self-directed study of generative AI. As a developer with a long history in other fields, this has been my process for exploring Python, the PyTorch ecosystem, and various machine learning frameworks. I'm sharing them here in the hope they might be useful to others on a similar path.

---
## Notebooks & Experiments
---

**1. Exploring ComfyUI: From Basic Pipelines to Advanced Models**

My work with ComfyUI focused on understanding how to programmatically control and orchestrate its components to build repeatable workflows.

*   **A Configurable SD1.5 Pipeline:** This was my foundational project to create a reusable, configuration-driven workflow for Stable Diffusion 1.5. It handles dynamic model loading, applies LoRAs, and serves as the base for later experiments.
    *   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/ComfyUI_SD15.ipynb)

*   **Adapting the Pipeline for FLUX.1-Schnell:** An experiment in adapting the SD1.5 workflow to the newer and much larger FLUX.1 architecture. A key challenge here was refining the memory management approach to handle the increased VRAM requirements.
    *   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/ComfyUI_Flux1-Schnell_Chroma.ipynb)

*   **Video Generation under Hardware Constraints (WAN 2.1):** A deep dive into aggressive memory management. The goal was to run the WAN 2.1 video model, which is too large for a free Colab GPU, by carefully loading and unloading models (like the UNET and text encoders) in stages.
    *   **Image to Video:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/Wan2.1_I2V_14B_FusionX-GGUF-WithLoRAs.ipynb)
    *   **Text to Video:**
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/Wan2.1_T2V_14B_FusionX-GGUF-WithLoRAs.ipynb)

---
**2. Working with the Hugging Face Diffusers Library**

These notebooks document my exploration of the popular `diffusers` library, a higher-level abstraction compared to ComfyUI.

*   **An SD1.5 Pipeline in Diffusers:** My initial implementation of a Stable Diffusion pipeline, including support for LoRAs. This notebook provides an interesting contrast to the more granular control offered by ComfyUI.
    *   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/HF-diffusers-SD15.ipynb)

*   **High-Resolution Generation with SDXL:** An exploration of the `diffusers` library for running the multi-part SDXL model architecture.
    *   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/HF-diffusers-SDXL.ipynb)

---
**3. Utility Scripts & Workflow Tools**

While working with these models, I found the need for a couple of utility tools.

*   **Security Utility: `.pt` to `.safetensors` Converter:** A simple script to batch-convert `.pt` model files to the more secure `.safetensors` format. I wrote this after not finding a simple, standalone tool for the task.
    **Only run this tool in a sandboxed environment, like Colab or a Virtual Machine, the process of converting the .pt file itself can trigger the malicious code (if any), then you can use the .safetensors safely in any environment.**
    *   [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://github.com/lfaga/Generative-AI-Notebook-Projects/blob/main/Pt2Safetensors.ipynb)

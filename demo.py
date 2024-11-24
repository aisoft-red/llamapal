import gradio as gr

css = ".center-title {text-align: center; font-weight: bold;}"
with gr.Blocks(css=css) as demo:
    with gr.Row():
        gr.Markdown("# LlamaPal", elem_classes="center-title")

    with gr.Row():
        with gr.Column():
            gr.Markdown("## On your own")
            gr.Image(
                value="./data/demo/intro.gif",
                type="filepath",
                interactive=True,
                label="Intro"
            )

        with gr.Column():
            gr.Markdown("## With a pal")
            gr.Image(
                value="./data/demo/processed_frames_image.gif",
                type="filepath",
                interactive=True,
                label="LlamaPal"
            )

if __name__ == "__main__":
    demo.launch()

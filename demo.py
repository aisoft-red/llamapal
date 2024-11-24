import gradio as gr

css = ".center-title {text-align: center; font-weight: bold;}"
with gr.Blocks(css=css) as demo:
    with gr.Row():
        gr.Markdown("# LlamaPal", elem_classes="center-title")

    with gr.Row():
        with gr.Column():
            gr.Markdown("## One on one")
            gr.Video(
                value="./data/demo/basketball_one_player.mp4",
                format="mp4",
                loop=True,
                autoplay=True
            )

        with gr.Column():
            gr.Markdown("## With a Pal")
            gr.Image(
                value="./data/demo/processed_frames_image.gif",
                type="filepath",
                interactive=False,
                label="LlamaPal"
            )

if __name__ == "__main__":
    demo.launch()

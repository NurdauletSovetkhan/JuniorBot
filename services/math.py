import matplotlib.pyplot as plt
import os
def render_latex_to_image(latex_code, filename="latex_example.png"):
    # Render via pyplot
    try:
        # Create graph
        fig, ax = plt.subplots(figsize=(6, 2))
        ax.text(0.5, 0.5, f"${latex_code}$", size=20, ha="center", va="center")
        ax.axis("off")

        # Save files
        output_path = os.path.join(os.getcwd(), filename)  # Сохраняем в текущей директории
        plt.savefig(output_path, format="png", bbox_inches="tight", dpi=300)
        plt.close(fig)

        print(f"✅ Изображение сохранено: {output_path}")
        return output_path  #Path to local file
    except Exception as e:
        print(f"❌ Ошибка рендеринга LaTeX: {e}")
        return None
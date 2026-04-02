import matplotlib.pyplot as plt
import matplotlib.patches as patches

def generate_probability_infographic():
    # Set up the figure with a dark background
    fig, ax = plt.subplots(figsize=(12, 8), facecolor='#1e1e26')
    ax.set_facecolor('#1e1e26')
    
    # Hide axes
    ax.axis('off')

    # 1. Title
    plt.text(0.5, 0.95, r"$\mathbf{Form\ 2 \cdot Partition\ by\ a\ discrete\ RV}\ Y \in \{y_1, \dots, y_n\}$", 
             color='white', fontsize=22, ha='center', fontweight='bold')

    # 2. Main Formula
    plt.text(0.5, 0.85, r"$P(B) = \sum_{i=1}^{n} P(B \mid Y = y_i) \cdot P(Y = y_i)$", 
             color='#a0c4ff', fontsize=26, ha='center')

    # 3. Sample Space Box
    # (x, y, width, height)
    main_box = patches.Rectangle((0.1, 0.55), 0.8, 0.15, linewidth=2, edgecolor='white', facecolor='none')
    ax.add_patch(main_box)
    plt.text(0.5, 0.71, "Sample Space", color='white', fontsize=16, ha='center', style='italic')

    # 4. Partitions
    colors = ['#ffadad', '#ffd6a5', '#fdffb6', '#caffbf', '#9bf6ff']
    labels = [r"$B \cap \{Y=y_1\}$", r"$B \cap \{Y=y_2\}$", r"$B \cap \{Y=y_3\}$", r"$\dots$", r"$B \cap \{Y=y_n\}$"]
    
    for i in range(5):
        width = 0.8 / 5
        x_pos = 0.1 + (i * width)
        # Colored sections
        rect = patches.Rectangle((x_pos, 0.55), width, 0.12, facecolor=colors[i], alpha=0.8)
        ax.add_patch(rect)
        # Text inside sections
        plt.text(x_pos + width/2, 0.61, labels[i], color='black', fontsize=13, ha='center', fontweight='bold')
        
        # 5. Arrows
        plt.annotate('', xy=(x_pos + width/2, 0.42), xytext=(x_pos + width/2, 0.54),
                     arrowprops=dict(arrowstyle='->', lw=2, color=colors[i]))

    # 6. Corrected Expansion Logic
    expansion = (r"$[P(B|Y=y_1) \cdot P(Y=y_1)] + [P(B|Y=y_2) \cdot P(Y=y_2)] + \dots + [P(B|Y=y_n) \cdot P(Y=y_n)]$")
    plt.text(0.5, 0.35, expansion, color='white', fontsize=18, ha='center', 
             bbox=dict(facecolor='#2d2d38', alpha=0.5, edgecolor='none', pad=10))

    # 7. Footer text
    footer = ("Use when conditioning on Y makes B easy to analyze.\n"
              "The discrete RV becomes the \"case selector.\"")
    plt.text(0.5, 0.15, footer, color='#cccccc', fontsize=14, ha='center', style='italic')

    # Save and Show
    plt.tight_layout()
    plt.savefig('total_probability_correct.png', dpi=300, facecolor=fig.get_facecolor())
    print("Success! 'total_probability_correct.png' has been generated.")
    plt.show()

if __name__ == "__main__":
    generate_probability_infographic()

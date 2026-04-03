import matplotlib.pyplot as plt

def draw_coin_sets():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

    # --- 1. Disjoint Case: The Single Coin ---
    # Heads and Tails are mutually exclusive.
    circle_h = plt.Circle((0.25, 0.5), 0.2, color='#e67e22', alpha=0.7)
    circle_t = plt.Circle((0.75, 0.5), 0.2, color='#2c3e50', alpha=0.7)
    
    ax1.add_patch(circle_h)
    ax1.add_patch(circle_t)
    
    ax1.set_title("CASE 1: SINGLE COIN (Disjoint)", fontsize=14, fontweight='bold', pad=20)
    ax1.text(0.25, 0.5, "HEADS", ha='center', color='white', fontweight='bold')
    ax1.text(0.75, 0.5, "TAILS", ha='center', color='white', fontweight='bold')
    
    ax1.text(0.5, 0.15, "Cannot happen at once", ha='center', fontsize=11, style='italic')
    ax1.text(0.5, 0.05, r"$P(H \cap T) = 0$", ha='center', fontsize=12, fontweight='bold')
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.axis('off')

    # --- 2. Independent Case: Two Different Coins ---
    # Results can overlap (both can be Heads).
    circle_c1 = plt.Circle((0.4, 0.5), 0.25, color='#f1c40f', alpha=0.6)
    circle_c2 = plt.Circle((0.6, 0.5), 0.25, color='#e74c3c', alpha=0.6)
    
    ax2.add_patch(circle_c1)
    ax2.add_patch(circle_c2)
    
    ax2.set_title("CASE 2: TWO COINS (Independent)", fontsize=14, fontweight='bold', pad=20)
    ax2.text(0.3, 0.5, "COIN 1\n(Heads)", ha='center', fontsize=10)
    ax2.text(0.7, 0.5, "COIN 2\n(Heads)", ha='center', fontsize=10)
    ax2.text(0.5, 0.5, "BOTH\nHEADS", ha='center', fontsize=9, fontweight='bold')
    
    ax2.text(0.5, 0.15, "One doesn't affect the other", ha='center', fontsize=11, style='italic')
    ax2.text(0.5, 0.05, r"$P(C1 \cap C2) = P(C1) \times P(C2)$", ha='center', fontsize=12, fontweight='bold')
    ax2.set_xlim(0, 1)
    ax2.set_ylim(0, 1)
    ax2.axis('off')

    plt.tight_layout()
    
    # Save the file as independence_vs_disjointness.png
    plt.savefig('independence_vs_disjointness.png', dpi=300)
    print("Image saved successfully as 'independence_vs_disjointness.png'")
    plt.show()

if __name__ == "__main__":
    draw_coin_sets()

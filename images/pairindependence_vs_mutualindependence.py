import matplotlib.pyplot as plt

def draw_independence_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
    
    # --- 1. Pairwise Independence (The "Weak" Link) ---
    ax1.set_title("PAIRWISE INDEPENDENCE\n(Bernstein's Coin Example)", fontsize=14, fontweight='bold')
    
    # Draw 3 circles in a triangle
    circles = {
        'A': (0.5, 0.75, '#3498db', "Coin 1 is H"),
        'B': (0.3, 0.35, '#e67e22', "Coin 2 is H"),
        'C': (0.7, 0.35, '#2ecc71', "Exactly 1 H")
    }
    
    for key, (x, y, color, label) in circles.items():
        circ = plt.Circle((x, y), 0.15, color=color, alpha=0.4)
        ax1.add_patch(circ)
        ax1.text(x, y, f"Event {key}\n{label}", ha='center', va='center', fontweight='bold')

    # Draw lines showing pairwise checks
    ax1.annotate('', xy=(0.35, 0.45), xytext=(0.45, 0.65), arrowprops=dict(arrowstyle='<->', color='gray'))
    ax1.annotate('', xy=(0.65, 0.45), xytext=(0.55, 0.65), arrowprops=dict(arrowstyle='<->', color='gray'))
    ax1.annotate('', xy=(0.4, 0.35), xytext=(0.6, 0.35), arrowprops=dict(arrowstyle='<->', color='gray'))

    ax1.text(0.5, 0.05, "P(A∩B) = P(A)P(B) ✓\nP(B∩C) = P(B)P(C) ✓\nP(A∩C) = P(A)P(C) ✓", 
             ha='center', bbox=dict(facecolor='white', alpha=0.8))
    ax1.text(0.5, -0.1, "BUT: If you know A and B are H,\nC is IMPOSSIBLE. They are linked!", 
             ha='center', color='red', fontweight='bold')

    # --- 2. Mutual Independence (The "Strong" Link) ---
    ax2.set_title("MUTUAL INDEPENDENCE\n(Three Separate Coins)", fontsize=14, fontweight='bold')
    
    # Draw 3 separate circles with no logic-linking
    circles_m = {
        'A': (0.2, 0.6, '#3498db', "Coin 1: H"),
        'B': (0.5, 0.6, '#e67e22', "Coin 2: H"),
        'C': (0.8, 0.6, '#2ecc71', "Coin 3: H")
    }
    
    for key, (x, y, color, label) in circles_m.items():
        circ = plt.Circle((x, y), 0.12, color=color, alpha=0.4)
        ax2.add_patch(circ)
        ax2.text(x, y, f"Event {key}\n{label}", ha='center', va='center', fontweight='bold')

    ax2.text(0.5, 0.3, "Knowing A and B tells you\nNOTHING about C.", ha='center', fontweight='bold')
    ax2.text(0.5, 0.05, r"$P(A \cap B \cap C) = P(A)P(B)P(C)$", 
             ha='center', fontsize=12, bbox=dict(facecolor='white', alpha=0.8))

    for ax in [ax1, ax2]:
        ax.set_xlim(0, 1)
        ax.set_ylim(-0.2, 1)
        ax.axis('off')

    plt.tight_layout()
    plt.savefig('pairindependence_vs_mutualindependence.png', dpi=300)
    print("Success: pairindependence_vs_mutualindependence.png saved.")
    plt.show()

if __name__ == "__main__":
    draw_independence_comparison()

import matplotlib.pyplot as plt

def generate_bayes_tree_exact():
    # Setup - Ultra dark theme
    fig, ax = plt.subplots(figsize=(14, 12), facecolor='#0b0b0b')
    ax.set_facecolor('#0b0b0b')
    
    # 1. Configuration - Based on 100,000 people from your note
    total_n = 100000
    root = (0.5, 0.94)
    d_node = (0.25, 0.72) 
    h_node = (0.75, 0.72)
    
    # Outcome Nodes
    d_pos = (0.12, 0.50) # True Positive
    d_neg = (0.38, 0.50) # False Negative
    h_pos = (0.62, 0.50) # False Positive
    h_neg = (0.88, 0.50) # True Negative

    def branch(p1, p2, color="#FFFFFF", lw=2):
        ax.annotate('', xy=p2, xytext=p1, 
                     arrowprops=dict(arrowstyle='->', color=color, lw=lw,  shrinkA=0, shrinkB=0))

    # --- Draw Branches ---
    branch(root, d_node, color='#00ffcc', lw=3) # Path to Disease
    branch(root, h_node, color='#ff4b4b', lw=3) # Path to Healthy
    
    branch(d_node, d_pos, color='#00ffcc', lw=2) # T+ Path
    branch(d_node, d_neg, color='#FFFFFF', lw=1)
    
    branch(h_node, h_pos, color='#ff4b4b', lw=2) # T+ Path (False Positive)
    branch(h_node, h_neg, color='#FFFFFF', lw=1)

    # --- Text Label Styles ---
    bg_clear = dict(facecolor='#0b0b0b', edgecolor='none', pad=1)
    label_style = {'color': '#cccccc', 'fontsize': 10, 'ha': 'center', 'bbox': bg_clear}
    count_style = {'color': '#ffd700', 'fontsize': 11, 'fontweight': 'bold', 'ha': 'center'} 
    node_title  = {'fontsize': 13, 'fontweight': 'bold', 'ha': 'center', 'va': 'bottom'}

    # 1. Top Section (Priors)
    plt.text(0.5, 0.98, f"Natural Frequency: {total_n:,} People", color='#ffd700', fontsize=16, ha='center', fontweight='bold')
    
    ax.text(0.35, 0.85, r"$P(D) = 0.001$", **label_style)
    ax.text(0.65, 0.85, r"$P(D^c) = 0.999$", **label_style)

    ax.text(0.25, 0.74, "HAS DISEASE (D)", color='#00ffcc', **node_title)
    ax.text(0.25, 0.69, "(100 People)", **count_style, va='top')
    
    ax.text(0.75, 0.74, "HEALTHY (D\u1d9c)", color='#ff4b4b', **node_title)
    ax.text(0.75, 0.69, "(99,900 People)", **count_style, va='top')

    # 2. Middle Section (Likelihoods)
    ax.text(0.14, 0.62, r"$P(T^+|D) = 0.99$", **label_style) # Sensitivity
    ax.text(0.62, 0.62, r"$P(T^+|D^c) = 0.01$", **label_style) # False Positive Rate
    
    ax.text(0.36, 0.62, "T- : 0.01", color='#F88585', fontsize=9, ha='center', bbox=bg_clear)
    ax.text(0.86, 0.62, "T- : 0.99", color="#F88585", fontsize=9, ha='center', bbox=bg_clear)

    # 3. Final Outcomes (Joint Probabilities)
    # True Positives
    ax.text(0.12, 0.43, r"$\mathbf{P(D \cap T^+)}$" + "\n0.00099", color='#00ffcc', fontsize=11, ha='center', va='top')
    ax.text(0.12, 0.35, "99 People", **count_style, va='top')
    
    # False Positives
    ax.text(0.62, 0.43, r"$\mathbf{P(D^c \cap T^+)}$" + "\n0.00999", color='#ff4b4b', fontsize=11, ha='center', va='top')
    ax.text(0.62, 0.35, "999 People", **count_style, va='top')

    # --- Calculation Box (Exactly as in Note) ---
    calc_text = (
        r"$\mathbf{P(D \mid T^+) = \frac{P(T^+ \mid D)P(D)}{P(T^+ \mid D)P(D) + P(T^+ \mid D^c)P(D^c)}}$" + "\n\n"
        r"$= \frac{99}{99 + 999} = \frac{99}{1098} \approx \mathbf{9.02\%}$"
    )
    
    plt.text(0.5, 0.12, calc_text, color='white', fontsize=18, ha='center', va='center',
             bbox=dict(facecolor='#1a1a1a', edgecolor='#00ffcc', boxstyle='round,pad=1.5', lw=2))

    # Footer Caption
    plt.text(0.5, -0.02, "The 999 False Positives swamp the 99 True Positives.", 
             color='#888888', fontsize=12, ha='center', style='italic')

    # Header
    plt.text(0.5, 1.06, "Medical Testing: Bayes' Theorem & LOTP", 
             color='white', fontsize=22, ha='center', fontweight='bold')

    ax.set_xlim(0, 1)
    ax.set_ylim(-0.05, 1.1)
    ax.axis('off')
    
    plt.savefig('bayes_note_final.png', dpi=300, bbox_inches='tight', facecolor='#0b0b0b')
    print("Success! Created 'bayes_note_final.png' based on your notes.")
    plt.show()

if __name__ == "__main__":
    generate_bayes_tree_exact()

import numpy as np
import matplotlib.pyplot as plt

# 1. Basic Style Setup (Avoids complex rcParams issues)
plt.style.use('dark_background')
fig = plt.figure(figsize=(12, 8), facecolor='#1a1a1c')
ax = fig.add_subplot(111)
ax.set_facecolor('#1a1a1c')

# 2. Generate the PDF curve (Normal Distribution)
x = np.linspace(-4, 4, 500)
y_pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)

# 3. Draw the main curve
ax.plot(x, y_pdf, color='#66d9ef', lw=2, alpha=0.8)
ax.fill_between(x, y_pdf, color='#66d9ef', alpha=0.1)

# 4. Highlight the "Infinitesimal Slice" [y, y + dy]
slice_x = 0.8
slice_w = 0.12
slice_y = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * slice_x**2)
ax.fill_between([slice_x, slice_x + slice_w], 0, [slice_y, slice_y], color='#f92672', alpha=0.9)

# 5. Add Text (Using raw strings for math)
# Title
ax.text(0, 0.55, "Form 3 · Partition by a continuous RV Y", 
        fontsize=22, ha='center', color='white', fontweight='bold')

# Corrected Formula (No commas)
formula = r"$P(B) = \int_{-\infty}^{\infty} P(B \mid Y = y) f_Y(y) dy$"
ax.text(0, 0.45, formula, fontsize=28, ha='center', color='#ae81ff')

# Annotation for the slice
ax.annotate('Infinitesimal Slice [y, y+dy]', 
            xy=(slice_x + 0.05, 0.05), xytext=(2, 0.2),
            arrowprops=dict(arrowstyle='->', color='white', lw=1.5),
            fontsize=14, color='#f92672')

# Footer logic
footer = "Use in continuous models. Each 'partition element' is now\nan infinitesimal slice [y, y+dy]."
ax.text(0, -0.12, footer, fontsize=15, ha='center', color='#cfcfc2', style='italic')

# 6. Final Polish
ax.set_ylim(-0.2, 0.6)
ax.set_xlim(-4, 4)
ax.axis('off')

# Save and Show
plt.savefig('partition_continuous.png', dpi=300, bbox_inches='tight')
print("Image saved as partition_continuous.png")
plt.show()

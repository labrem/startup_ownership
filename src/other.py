
import numpy as np
import matplotlib.pyplot as plt

def plot_simulation(stages, stats, title):

    # 1. Data Setup
    stages = stages.copy()
    data = stats.copy()

    # 2. Plot Creation
    fig, ax = plt.subplots(figsize=(9.5, 6))

    # Define colors and styles (re-added mean_color)
    line_color = '#ff6f3c'
    mean_color = '#007acc'
    text_color = '#333333'
    grid_color = '#cccccc'
    bg_color = '#fdfdfd'

    fig.set_facecolor(bg_color)
    ax.set_facecolor(bg_color)

    y_positions = np.arange(len(stages))

    # Loop through each stage to plot the horizontal bars and points
    for i, stage in enumerate(stages):
        # Unpack all data points for the stage, including the Mean
        p10, p25, p50, p75, p90, mean = (data['10th'][i], data['25th'][i], data['50th'][i],
                                        data['75th'][i], data['90th'][i], data['Mean'][i])
        
        ax.hlines(y=i, xmin=p10, xmax=p90, color=line_color, linewidth=2, zorder=2)
        
        points_x = [p10, p25, p50, p75, p90]
        ax.scatter(points_x, [i]*len(points_x), color=line_color, s=50, zorder=3)
        ax.scatter(mean, i, color=mean_color, s=120, zorder=4, edgecolors='white')

        value_labels = [f"{val:.1f}" for val in points_x]
        quantile_labels = ['10th', '25th', '50th', '75th', '90th']

        for j, x_pos in enumerate(points_x):
            ax.text(x_pos, i + 0.18, value_labels[j], ha='center', va='bottom', fontsize=8, color=text_color, fontweight='bold')
            ax.text(x_pos, i + 0.45, quantile_labels[j], ha='center', va='bottom', fontsize=7, color=text_color)

    # 3. Table and Text Formatting
    for i, stage in enumerate(stages):
        ax.text(2.5, i, stage, ha='right', va='center', fontsize=10, fontweight='bold')

    # 4. Styling and Final Touches
    ax.set_xscale('log')
    ax.set_xlim(2, 300)
    ax.set_ylim(-1, len(stages))

    # Hide all axes and spines
    ax.spines['bottom'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # Keep the horizontal grid lines
    ax.grid(axis='y', which='major', linestyle='-', color=grid_color, linewidth=1.5)
    ax.set_axisbelow(True)

    # Adjust title position
    ax.set_title('Founding Team Ownership Benchmarks (Log Scale)', loc='left', fontsize=14, fontweight='bold', pad=0)

    plt.tight_layout(rect=[0.05, 0.05, 0.95, 0.93])

    plt.show()

import matplotlib.pyplot as plt

def plot_lle_fd_scatter(lle_values, fd_values):
    if len(lle_values) != len(fd_values):
        raise ValueError("LLE and FD arrays must have the same length")
    
    plt.figure(figsize=(8, 6))
    for i, (lle, fd) in enumerate(zip(lle_values, fd_values)):
        plt.scatter(lle, fd, label=f'IMF {i+1}', s=60)
        plt.text(lle, fd + 0.01, f'{i+1}', fontsize=9, ha='center')
    plt.xlabel('Largest Lyapunov Exponent')
    plt.ylabel('Fractal Dimension (Box-Counting)')
    plt.title('Chaos Metric Comparison for IMFs')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.show()

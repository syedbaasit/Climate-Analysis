from matplotlib.ticker import MaxNLocator

cs = m.contourf(x, y, t2m_masked, levels=np.linspace(40, np.max(t2m_masked), 15), cmap='coolwarm')
c=plt.colorbar(cs)
c.set_label('Temperature (°C)', fontsize=15)
c.ax.yaxis.set_major_locator(MaxNLocator(integer=True))
c.set_label('Temperature (°C)', fontsize=15)


"""
LOO-PIT Overlay Plot
====================
_gallery_category: Model Checking
"""
import matplotlib.pyplot as plt

import arviz as az

az.style.use("arviz-doc")

idata = az.load_arviz_data("non_centered_eight")

az.plot_loo_pit(idata=idata, y="obs")

plt.show()

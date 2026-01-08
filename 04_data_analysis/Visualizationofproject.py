# Used AI in it



#!/usr/bin/env python3
"""
Tkinter + Matplotlib CRM-style Dashboard (sample data)

Save as dashboard_tk_matplotlib.py and run:
    python3 dashboard_tk_matplotlib.py

Uses:
 - tkinter (builtin)
 - matplotlib (may already be installed on your system)

Logo path (from your upload):
    /mnt/data/CRM-Report-1024x570-1010584651.png
"""

import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import math

# --------------------------
# Config / sample data
# --------------------------
LOGO_PATH = "/mnt/data/CRM-Report-1024x570-1010584651.png"  # <- uploaded image path

# KPI sample values
KPIS = {
    "Total Opportunities": 8442,
    "In Progress": 2036,
    "% Won": 62.25,
    "Estimated Revenue (M$)": 19.98,
    "Actual Revenue (M$)": 9.48,
}

# Stage donut
STAGES = [
    ("Won", 3988),
    ("Lost", 2418),
    ("In Progress", 2036),
]

# Product table sample
PRODUCTS = [
    ("GTX Basic", 1779, 415, 62.61, 2.58),
    ("MG Special", 1579, 423, 63.75, 2.21),
    ("GTXPro", 1428, 324, 62.59, 5.03),
    ("MG Advanced", 1360, 317, 59.54, 3.96),
    ("GTX Plus Basic", 1327, 326, 61.28, 3.53),
    ("GTX Plus Pro", 931, 218, 63.53, 3.52),
    ("GTK 500", 38, 14, 58.33, 0.46),
]

# Top accounts
TOP_ACCOUNTS = [
    ("Konex", 0.55),
    ("Kan-code", 0.53),
    ("Zumgilty", 0.42),
    ("Xx-zobam", 0.41),
    ("Hottechi", 0.36),
    ("Plussuin", 0.36),
    ("Donquatech", 0.35),
    ("Rangreen", 0.34),
    ("Cheers", 0.34),
    ("Singletechno", 0.33),
]

# Monthly data for combo chart
MONTHS = [
    ("2020 Jan", 300, 1.2),
    ("2020 Feb", 400, 1.4),
    ("2020 Mar", 450, 1.6),
    ("2020 Apr", 550, 1.8),
    ("2020 May", 600, 2.1),
    ("2020 Jun", 650, 2.3),
    ("2020 Jul", 900, 3.5),
    ("2020 Aug", 1100, 4.0),
    ("2020 Sep", 700, 2.5),
    ("2020 Oct", 500, 1.4),
    ("2020 Nov", 300, 0.8),
    ("2020 Dec", 200, 0.7),
    ("2021 Jan", 350, 1.2),
    ("2021 Feb", 450, 1.8),
]

# --------------------------
# App functions
# --------------------------
class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Pipeline Dashboard - Tkinter + Matplotlib")
        self.geometry("1200x780")
        self.configure(bg="#111217")

        # style
        style = ttk.Style(self)
        style.theme_use("default")
        style.configure("TFrame", background="#111217")
        style.configure("TLabel", background="#111217", foreground="#e5e7eb", font=("Helvetica", 10))
        style.configure("Header.TLabel", font=("Helvetica", 14, "bold"), foreground="#ffffff")
        style.configure("KPI.TLabel", font=("HelHvetica", 14, "bold"), foreground="#ffffff")
        style.configure("Small.TLabel", font=("elvetica", 9), foreground="#cbd5e1")

        # layout frames
        self.left_frame = ttk.Frame(self, width=240)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(12,6), pady=12)

        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(6,12), pady=12)

        # header (logo + title + refresh)
        self._build_header()

        # left filters
        self._build_filters()

        # main area: KPIs, charts, table
        self._build_kpis()
        self._build_main_charts_and_table()

        # initial draw
        self.update_all()

    def _build_header(self):
        header = ttk.Frame(self.main_frame)
        header.pack(fill=tk.X, pady=(0,8))

        # logo (try PhotoImage)
        try:
            self.logo_img = PhotoImage(file=LOGO_PATH)
            logo_label = tk.Label(header, image=self.logo_img, bg="#111217")
            logo_label.pack(side=tk.LEFT, padx=(0,12))
        except Exception:
            # fallback to plain text if image not loadable
            logo_label = ttk.Label(header, text="[Logo]", style="Header.TLabel")
            logo_label.pack(side=tk.LEFT, padx=(0,12))

        title_box = ttk.Frame(header)
        title_box.pack(side=tk.LEFT, anchor="w")

        title = ttk.Label(title_box, text="Pipeline Report", style="Header.TLabel")
        title.pack(anchor="w")
        subtitle = ttk.Label(title_box, text="Interactive dashboard — sample data", style="Small.TLabel")
        subtitle.pack(anchor="w")

        # refresh / date
        right_box = ttk.Frame(header)
        right_box.pack(side=tk.RIGHT, anchor="e")
        last_refresh_label = ttk.Label(right_box, text="Last Refresh", style="Small.TLabel")
        last_refresh_label.pack(anchor="e")
        import datetime
        lr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        lr_val = ttk.Label(right_box, text=lr, style="Small.TLabel")
        lr_val.pack(anchor="e")

    def _build_filters(self):
        f = ttk.Frame(self.left_frame)
        f.pack(fill=tk.X)

        ttk.Label(f, text="Filters", style="Header.TLabel").pack(anchor="w", pady=(0,6))

        # Year
        ttk.Label(f, text="Calendar Year").pack(anchor="w", pady=(6,0))
        self.year_var = tk.StringVar(value="All")
        year_cb = ttk.Combobox(f, textvariable=self.year_var, values=["All", "2020", "2021"], state="readonly")
        year_cb.pack(fill=tk.X, pady=2)
        year_cb.bind("<<ComboboxSelected>>", lambda e: self.update_all())

        # State
        ttk.Label(f, text="State").pack(anchor="w", pady=(6,0))
        self.state_var = tk.StringVar(value="All")
        state_cb = ttk.Combobox(f, textvariable=self.state_var, values=["All","NSW","VIC","QLD","WA","SA"], state="readonly")
        state_cb.pack(fill=tk.X, pady=2)
        state_cb.bind("<<ComboboxSelected>>", lambda e: self.update_all())

        # Account
        ttk.Label(f, text="Account").pack(anchor="w", pady=(6,0))
        accounts = ["All"] + [a for a,_ in TOP_ACCOUNTS]
        self.account_var = tk.StringVar(value="All")
        acct_cb = ttk.Combobox(f, textvariable=self.account_var, values=accounts, state="readonly")
        acct_cb.pack(fill=tk.X, pady=2)
        acct_cb.bind("<<ComboboxSelected>>", lambda e: self.update_all())

        # Sales agent
        ttk.Label(f, text="Sales Agent").pack(anchor="w", pady=(6,0))
        self.agent_var = tk.StringVar(value="All")
        agent_cb = ttk.Combobox(f, textvariable=self.agent_var, values=["All","Agent A","Agent B","Agent C"], state="readonly")
        agent_cb.pack(fill=tk.X, pady=2)
        agent_cb.bind("<<ComboboxSelected>>", lambda e: self.update_all())

        # spacer
        ttk.Label(f, text="").pack(pady=10)

    def _build_kpis(self):
        kpi_frame = ttk.Frame(self.main_frame)
        kpi_frame.pack(fill=tk.X, pady=(4,10))

        # create five KPI boxes
        self.kpi_labels = {}
        for i,(k,v) in enumerate(KPIS.items()):
            box = tk.Frame(kpi_frame, bg="#0b1220", padx=12, pady=10)
            box.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=6)
            label_title = ttk.Label(box, text=k, style="Small.TLabel")
            label_title.pack(anchor="w")
            label_value = ttk.Label(box, text=self._kpi_format(k,v), style="KPI.TLabel")
            label_value.pack(anchor="w", pady=(6,0))
            self.kpi_labels[k] = label_value

    def _build_main_charts_and_table(self):
        # two-column layout: left big charts, right smaller column for product table + accounts
        container = ttk.Frame(self.main_frame)
        container.pack(fill=tk.BOTH, expand=True)

        left = ttk.Frame(container)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        right = ttk.Frame(container, width=360)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=(12,0))

        # Left top: donut chart + product table next to it
        top_left = ttk.Frame(left)
        top_left.pack(fill=tk.X, pady=(0,8))

        self.fig_donut = plt.Figure(figsize=(4,3), dpi=90)
        self.ax_donut = self.fig_donut.add_subplot(111)
        self.canvas_donut = FigureCanvasTkAgg(self.fig_donut, master=top_left)
        self.canvas_donut.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

        # product table on the right of donut (inside top_left)
        table_holder = ttk.Frame(top_left)
        table_holder.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12,0))

        ttk.Label(table_holder, text="Product Performance", style="Header.TLabel").pack(anchor="w")
        cols = ("Product","Total Opp","In Progress","% Won","Est Revenue (M$)")
        self.tree = ttk.Treeview(table_holder, columns=cols, show="headings", height=8)
        for c in cols:
            self.tree.heading(c, text=c)
            # set widths
            if c=="Product":
                self.tree.column(c, width=160, anchor="w")
            else:
                self.tree.column(c, width=90, anchor="center")
        self.tree.pack(fill=tk.BOTH, expand=True, pady=(6,0))

        # Left bottom: combo chart (monthly revenue + opportunities)
        bottom_left = ttk.Frame(left)
        bottom_left.pack(fill=tk.BOTH, expand=True)

        ttk.Label(bottom_left, text="Estimated Revenue & Number of Opportunities", style="Header.TLabel").pack(anchor="w")

        self.fig_combo = plt.Figure(figsize=(8,3.5), dpi=90)
        self.ax_combo = self.fig_combo.add_subplot(111)
        self.canvas_combo = FigureCanvasTkAgg(self.fig_combo, master=bottom_left)
        self.canvas_combo.get_tk_widget().pack(fill=tk.BOTH, expand=True, pady=(6,0))

        # Right column: Top accounts bar chart and controls
        ttk.Label(right, text="Top 10 Accounts by Estimated Revenue", style="Header.TLabel").pack(anchor="w")
        self.fig_accounts = plt.Figure(figsize=(3.5,4.5), dpi=90)
        self.ax_accounts = self.fig_accounts.add_subplot(111)
        self.canvas_accounts = FigureCanvasTkAgg(self.fig_accounts, master=right)
        self.canvas_accounts.get_tk_widget().pack(fill=tk.BOTH, expand=False, pady=(6,0))

    def _kpi_format(self, key, value):
        if "Revenue" in key:
            return f"${value:,.2f}M"
        if key == "% Won":
            return f"{value:.2f}%"
        else:
            return f"{value:,}"

    def update_all(self):
        # In a real app, here you'd re-load / filter data based on selections.
        # For this sample, selections are acknowledged but we just re-render with sample data.
        self._update_kpis()
        self._draw_donut()
        self._populate_table()
        self._draw_combo()
        self._draw_accounts()
        # flush canvases
        self.canvas_donut.draw()
        self.canvas_combo.draw()
        self.canvas_accounts.draw()

    def _update_kpis(self):
        for k,v in KPIS.items():
            self.kpi_labels[k].configure(text=self._kpi_format(k,v))

    def _draw_donut(self):
        self.ax_donut.clear()
        labels = [s for s,_ in STAGES]
        sizes = [v for _,v in STAGES]
        # donut style
        wedges, texts = self.ax_donut.pie(sizes, labels=labels, startangle=140, wedgeprops=dict(width=0.5))
        self.ax_donut.set_aspect('equal')
        self.ax_donut.set_title("Total Opportunities by Stage", color="white")
        # label colors
        for t in texts:
            t.set_color("white")
        # center text
        total = sum(sizes)
        self.ax_donut.text(0,0, f"{total:,}\nTotal", ha='center', va='center', color="white", fontsize=10)
        self.fig_donut.patch.set_facecolor('#111217')
        self.ax_donut.patch.set_facecolor('#111217')

    def _populate_table(self):
        # clear
        for r in self.tree.get_children():
            self.tree.delete(r)
        # insert sample products
        for p in PRODUCTS:
            self.tree.insert("", tk.END, values=(p[0], p[1], p[2], f"{p[3]:.2f}%", f"{p[4]:.2f}"))

    def _draw_combo(self):
        self.ax_combo.clear()
        months = [m for m,_,_ in MONTHS]
        opps = [o for _,o,_ in MONTHS]
        revs = [r for _,_,r in MONTHS]

        x = range(len(months))
        # bar chart for opportunities (left axis)
        self.ax_combo.bar(x, opps, alpha=0.8)
        self.ax_combo.set_xticks(x)
        self.ax_combo.set_xticklabels(months, rotation=45, ha='right')
        self.ax_combo.set_ylabel("Opportunities")
        # second axis for revenue
        ax2 = self.ax_combo.twinx()
        ax2.plot(x, revs, marker='o', linewidth=2)
        ax2.set_ylabel("Estimated Revenue (M$)")
        self.ax_combo.set_title("Opportunities (bars) + Revenue (line)", color="white")
        self.fig_combo.patch.set_facecolor('#111217')
        self.ax_combo.patch.set_facecolor('#111217')
        # label colors
        for label in self.ax_combo.get_xticklabels():
            label.set_color("white")
        self.ax_combo.yaxis.label.set_color("white")
        ax2.yaxis.label.set_color("white")

    def _draw_accounts(self):
        self.ax_accounts.clear()
        names = [n for n,_ in TOP_ACCOUNTS[::-1]]  # reverse for horizontal bar
        vals = [v for _,v in TOP_ACCOUNTS[::-1]]
        y = range(len(names))
        self.ax_accounts.barh(y, vals)
        self.ax_accounts.set_yticks(y)
        self.ax_accounts.set_yticklabels(names)
        self.ax_accounts.set_xlabel("Estimated Revenue (M$)")
        self.ax_accounts.set_title("Top Accounts", color="white")
        self.fig_accounts.patch.set_facecolor('#111217')
        self.ax_accounts.patch.set_facecolor('#111217')
        for label in self.ax_accounts.get_yticklabels():
            label.set_color("white")
        self.ax_accounts.xaxis.label.set_color("white")


if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()

import time
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

class TestTool:
    LUtable_accessed = 0
    positions_evaluated = 0
    start_time = None
    end_time = None
    depth = None
    expected_winner = 1
    actual_winner = None
    results = dict()

    @staticmethod
    def increment_accessed():
        TestTool.LUtable_accessed += 1
    @staticmethod
    def increment_evaluated():
        TestTool.positions_evaluated += 1
    @staticmethod
    def start_timer():
        TestTool.start_time = time.perf_counter()
    @staticmethod
    def set_depth(d):
        TestTool.depth = d
    @staticmethod
    def set_winner(w):
        TestTool.actual_winner = w
    @staticmethod
    def end_timer():
        TestTool.end_time = time.perf_counter()
    @staticmethod
    def get_run_time():
        return TestTool.end_time - TestTool.start_time
    @staticmethod
    def reset():
        TestTool.LUtable_accessed = 0
        TestTool.positions_evaluated = 0
        TestTool.start_time = None
        TestTool.end_time = None
        TestTool.depth = None
        TestTool.actual_winner = None
    @staticmethod
    def save_results():
        TestTool.results[TestTool.depth] = {"Depth": TestTool.depth,
                                             "Positions Evaluated": TestTool.positions_evaluated,
                                             "Look Up Table Accessed": TestTool.LUtable_accessed,
                                             "Run Time": TestTool.get_run_time(),
                                             "Actual Winner": TestTool.actual_winner
                                             }
    
    @staticmethod
    def plot_results(): # Function provided by Claude AI
        if not TestTool.results:
            print("No results to plot.")
            return

        depths = sorted(TestTool.results.keys())
        positions   = [TestTool.results[d]["Positions Evaluated"]      for d in depths]
        lu_accesses = [TestTool.results[d]["Look Up Table Accessed"]   for d in depths]
        run_times   = [TestTool.results[d]["Run Time"]                 for d in depths]
        winners     = [TestTool.results[d]["Actual Winner"]            for d in depths]

        fig = plt.figure(figsize=(14, 9))
        fig.suptitle("AI Agent Performance vs. Search Depth", fontsize=16, fontweight="bold", y=0.98)

        gs = gridspec.GridSpec(2, 2, figure=fig, hspace=0.45, wspace=0.35)

        COLOR_BAR  = "#4C72B0"
        COLOR_LINE = "#DD8452"
        COLOR_LU   = "#55A868"

        # --- 1. Positions Evaluated ---
        ax1 = fig.add_subplot(gs[0, 0])
        ax1.bar(depths, positions, color=COLOR_BAR, edgecolor="white", width=0.6)
        ax1.set_title("Positions Evaluated", fontweight="bold")
        ax1.set_xlabel("Depth")
        ax1.set_ylabel("Count")
        ax1.set_xticks(depths)
        for bar, val in zip(ax1.patches, positions):
            ax1.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.01,
                    f"{val:,}", ha="center", va="bottom", fontsize=8)

        # --- 2. Lookup Table Accesses ---
        ax2 = fig.add_subplot(gs[0, 1])
        ax2.bar(depths, lu_accesses, color=COLOR_LU, edgecolor="white", width=0.6)
        ax2.set_title("Lookup Table Accesses", fontweight="bold")
        ax2.set_xlabel("Depth")
        ax2.set_ylabel("Count")
        ax2.set_xticks(depths)
        for bar, val in zip(ax2.patches, lu_accesses):
            ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.01,
                    f"{val:,}", ha="center", va="bottom", fontsize=8)

        # --- 3. Run Time ---
        ax3 = fig.add_subplot(gs[1, 0])
        ax3.plot(depths, run_times, marker="o", color=COLOR_LINE,
                linewidth=2.5, markersize=7, markerfacecolor="white", markeredgewidth=2)
        ax3.fill_between(depths, run_times, alpha=0.15, color=COLOR_LINE)
        ax3.set_title("Run Time (seconds)", fontweight="bold")
        ax3.set_xlabel("Depth")
        ax3.set_ylabel("Seconds")
        ax3.set_xticks(depths)
        for x, y in zip(depths, run_times):
            ax3.annotate(f"{y:.3f}s", (x, y), textcoords="offset points",
                        xytext=(0, 8), ha="center", fontsize=8)

        # --- 4. Winner per Depth ---
        ax4 = fig.add_subplot(gs[1, 1])
        unique_winners = sorted(set(w for w in winners if w is not None))
        cmap = plt.cm.get_cmap("tab10", max(len(unique_winners), 1))
        color_map = {w: cmap(i) for i, w in enumerate(unique_winners)}
        bar_colors = [color_map.get(w, "gray") for w in winners]

        bars = ax4.bar(depths, [1] * len(depths), color=bar_colors, edgecolor="white", width=0.6)
        ax4.set_title("Actual Winner by Depth", fontweight="bold")
        ax4.set_xlabel("Depth")
        ax4.set_yticks([])
        ax4.set_xticks(depths)
        for bar, w in zip(bars, winners):
            ax4.text(bar.get_x() + bar.get_width() / 2, 0.5,
                    str(w) if w is not None else "?",
                    ha="center", va="center", fontsize=11, fontweight="bold", color="white")

        legend_handles = [
            plt.Rectangle((0, 0), 1, 1, color=color_map[w], label=f"Player {w}")
            for w in unique_winners
        ]
        if legend_handles:
            ax4.legend(handles=legend_handles, loc="upper right", fontsize=8)

        plt.show()


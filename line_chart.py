"""一个简单的 Matplotlib 折线图示例。

运行方式：
    python line_chart.py

程序会显示 2026 年上半年每月销售额的折线图，并在当前目录生成
``monthly_sales_line_chart.png`` 图片文件。
"""

from pathlib import Path

import matplotlib.pyplot as plt


OUTPUT_FILE = Path("monthly_sales_line_chart.png")


def draw_line_chart() -> None:
    """绘制并保存一个包含标题、坐标轴标签和数据点标注的折线图。"""
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    sales = [120, 150, 135, 180, 210, 240]

    plt.figure(figsize=(8, 5))
    plt.plot(
        months,
        sales,
        marker="o",
        linestyle="-",
        linewidth=2,
        color="#1f77b4",
        label="Sales",
    )

    for month, value in zip(months, sales):
        plt.text(month, value + 4, str(value), ha="center", fontsize=9)

    plt.title("Monthly Sales Trend in 2026")
    plt.xlabel("Month")
    plt.ylabel("Sales (units)")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()

    plt.savefig(OUTPUT_FILE, dpi=150)
    plt.show()


if __name__ == "__main__":
    draw_line_chart()

"""Command-line interface for AI Carbon Footprint calculator."""

import json
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from ai_carbon_footprint.core import calculate_carbon_footprint
from ai_carbon_footprint.comparisons import get_comparisons
from ai_carbon_footprint.data import GPU_SPECS, CARBON_INTENSITY, DEFAULT_PUE


console = Console()


@click.group(invoke_without_command=True)
@click.pass_context
@click.option("--gpu", "-g", help="GPU model (e.g., A100)")
@click.option("--hours", "-h", type=float, help="Runtime in hours")
@click.option("--num-gpus", "-n", type=int, default=1, help="Number of GPUs")
@click.option("--pue", "-p", type=float, default=DEFAULT_PUE, help="PUE coefficient")
@click.option("--region", "-r", default="global", help="Geographic region")
@click.option("--utilization", "-u", type=float, default=1.0, help="GPU utilization (0-1)")
@click.option("--output", "-o", type=click.Choice(["text", "json"]), default="text")
def main(ctx, gpu, hours, num_gpus, pue, region, utilization, output):
    """Calculate carbon emissions from AI compute workloads."""
    if ctx.invoked_subcommand is None:
        if not gpu or hours is None:
            click.echo(ctx.get_help())
            return

        try:
            result = calculate_carbon_footprint(
                gpu, hours, num_gpus, pue, region, utilization
            )
            comparisons = get_comparisons(result["co2_kg"])

            if output == "json":
                output_data = {**result, "comparisons": comparisons}
                click.echo(json.dumps(output_data, indent=2, ensure_ascii=False))
            else:
                display_results(result, comparisons)

        except ValueError as e:
            console.print(f"[red]错误: {e}[/red]")
            raise click.Abort()


def display_results(result: dict, comparisons: list):
    """Display results in rich text format."""
    # Main results panel
    content = f"""[bold]GPU:[/bold] {result['gpu_name']} × {result['num_gpus']}
[bold]运行时间:[/bold] {result['hours']:.1f} 小时
[bold]GPU利用率:[/bold] {result['utilization']*100:.0f}%
[bold]PUE系数:[/bold] {result['pue']:.2f}
[bold]地区:[/bold] {result['region']} (碳强度: {result['carbon_intensity']:.3f} kg CO2/kWh)

[bold cyan]能耗:[/bold cyan] {result['total_energy_kwh']:.2f} kWh
[bold red]碳排放:[/bold red] {result['co2_kg']:.2f} kg CO2"""

    console.print(Panel(content, title="AI 算力碳排放计算结果", border_style="green"))

    # Comparisons table
    if comparisons:
        table = Table(title="具象化对比", show_header=True)
        table.add_column("对比项", style="cyan")
        table.add_column("相当于", justify="right", style="yellow")

        for comp in comparisons:
            equiv = comp["equivalent"]
            if equiv >= 1:
                equiv_str = f"{equiv:.1f} 个"
            else:
                equiv_str = f"1/{1/equiv:.1f} 个"

            table.add_row(f"{comp['emoji']} {comp['name']}", equiv_str)

        console.print(table)


@main.command()
def list_gpus():
    """List all supported GPU models."""
    table = Table(title="支持的GPU型号", show_header=True)
    table.add_column("型号", style="cyan")
    table.add_column("名称", style="white")
    table.add_column("TDP (W)", justify="right", style="yellow")
    table.add_column("类别", style="green")

    for model, spec in sorted(GPU_SPECS.items()):
        table.add_row(model, spec["name"], str(spec["tdp"]), spec["category"])

    console.print(table)


@main.command()
def list_regions():
    """List all supported regions and their carbon intensity."""
    table = Table(title="支持的地区及碳强度", show_header=True)
    table.add_column("地区代码", style="cyan")
    table.add_column("碳强度 (kg CO2/kWh)", justify="right", style="yellow")

    for region, intensity in sorted(CARBON_INTENSITY.items()):
        table.add_row(region, f"{intensity:.3f}")

    console.print(table)


if __name__ == "__main__":
    main()

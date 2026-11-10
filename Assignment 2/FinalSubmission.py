import pandas as pd
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context


def load_csv(filepath):
    if "drive.google.com/file/d/" in filepath and "/view" in filepath:
        file_id = filepath.split("/d/")[1].split("/")[0]
        filepath = f"https://drive.google.com/uc?id={file_id}"

    print(f"Initializing data import from source: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine='pyarrow', on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"Data import completed successfully in {load_time:.2f} seconds.")
        print(f"Total records processed: {len(df)}")
        print(f"Available data attributes: {list(df.columns)}")

        df = df.fillna(0)

        for col in ["unit_price", "quantity"]:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        if "order_date" in df.columns:
            df["parsed_order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

        required_fields = [
            "sales_region", "order_type", "unit_price", "quantity",
            "customer_type", "employee_name", "product_category",
            "order_number", "employee_id", "job_title",
            "order_date", "customer_name", "customer_state",
            "product_number", "produce_name"
        ]
        missing_fields = [field for field in required_fields if field not in df.columns]
        if missing_fields:
            print(f"NOTICE: The dataset is missing the following required attributes: {missing_fields}. Certain analytical reports may be impacted.")
        else:
            print("Data validation complete: All required schema attributes are present.")
        return df

    except Exception as e:
        print("System Error: Unable to process the specified CSV file. Details:", e)
        return None


# Individual Requirement 7: Prompt the user for a date range before performing an analysis
"""
AI Note: Generated with Gemini to satisfy Individual Requirement 7 (date range filtering with validation) using the prompt "can you please explain 
the algorithms for the personal task below using the corresponding function names and show me (line by line with pseudocode) how it would work?
'Add an analytic that shows sales by region and product, showing the percentage of the quantity and total sales per region and product.  
This percentage should be a new column in the pivot table.'
"""
def filter_by_date_range(data):
    if "order_date" not in data.columns:
        print("Notice: 'order_date' attribute is unavailable. Proceeding with the complete dataset.")
        return data

    dates = pd.to_datetime(data["order_date"], errors="coerce")
    valid_dates = dates.dropna()

    if valid_dates.empty:
        print("Notice: No valid dates found in 'order_date'. Proceeding with the complete dataset.")
        return data

    min_date = valid_dates.min().date()
    max_date = valid_dates.max().date()

    while True:
        print(f"\n--- Date Range Selection (Available Period: {min_date} to {max_date}) ---")
        print("Please specify the date range for this analysis (Format: YYYY-MM-DD, or press Enter for full range).")
        start_input = input(f"Start Date [Default: {min_date}]: ").strip()
        end_input = input(f"End Date   [Default: {max_date}]: ").strip()

        try:
            start_date = pd.to_datetime(start_input).date() if start_input else min_date
            end_date = pd.to_datetime(end_input).date() if end_input else max_date
        except ValueError:
            print("Formatting Error: Invalid date format entered. Please use YYYY-MM-DD (e.g., 2023-05-15).")
            continue

        if start_date > end_date:
            print("Range Error: The Start Date cannot be later than the End Date. Please re-enter.")
            continue

        if start_date < min_date or end_date > max_date:
            print(f"Notice: Selected dates extend beyond the dataset boundaries ({min_date} to {max_date}). Filtering within available bounds.")

        mask = (dates.dt.date >= start_date) & (dates.dt.date <= end_date)
        filtered_df = data.loc[mask].copy()

        if filtered_df.empty:
            print(f"Data Warning: No sales records exist between {start_date} and {end_date}. Please select a different date range.")
            continue

        print(f"Filter applied: Analyzing {len(filtered_df)} records from {start_date} to {end_date}.")
        return filtered_df


def display_initial_rows(data):
    total_rows = len(data)
    while True:
        print("\nEnter rows to display:")
        print(f"- Enter a number 1 to {total_rows}")
        print("- To see all rows, enter 'all'")
        print("- To skip preview, press Enter")
        response = input("Your choice: ").strip().lower()

        if response == "":
            print("Preview bypassed. Returning to main menu.")
            return

        if response == "all":
            print("\n--- Complete Sales Dataset ---")
            print(data)
            return

        try:
            num_rows = int(response)
        except ValueError:
            print(f"Invalid entry '{response}'. Please provide a valid integer between 1 and {total_rows}, 'all', or press Enter to skip.")
            continue

        if num_rows < 1 or num_rows > total_rows:
            print(f"Range Error: Please specify a number between 1 and {total_rows}.")
            continue

        print(f"\n--- Displaying Initial {num_rows} Records ---")
        print(data.head(num_rows))
        return


def total_sales_by_region_order_type(data):
    required = ["sales_region", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales_data,
        index="sales_region",
        columns="order_type",
        values="sale_price",
        aggfunc="sum",
        fill_value=0
    )
    print("\n--- Executive Summary: Total Sales Revenue by Region and Order Type ---")
    print(pivot_table.round(2))


def average_sales_by_region(data):
    required = ["sales_region", "customer_state", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales_data,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sale_price",
        aggfunc="mean",
        fill_value=0
    )
    print("\n--- Analytical Report: Average Sales Revenue by Region, State, and Order Type ---")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))

"""
I had used Gemini Argon for assistance with explaining line by line how to implement the predefined analytical tasks, using the prompt
'can you please explain the algorithms for the analytical tasks below using the corresponding function names and show me (line by line with
pseudocode) how it would work? for the print statements, can you use business formal language that would be appropriate for
a professional program?' along with the full copy pasted menu_options list as follows:
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order type", total_sales_by_region_order_type),
    ("Average sales by region with average sales by state and sale type", average_sales_by_region),
    ("Sales by customer type and order type by state", sales_by_customer_type),
    ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
    ("Total sales quantity and price customer type", total_sales_quantity_price_customer_type),
    ("Max and min sales price of sales by category", max_min_sales_price_by_category),
    ("Number of unique employees by region", unique_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Exit the program", exit_program) 
"""

def sales_by_customer_type(data):
    required = ["customer_state", "customer_type", "order_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales_data,
        index=["customer_state", "customer_type", "order_type"],
        values="sale_price",
        aggfunc="sum",
        fill_value=0
    )
    print("\n--- Analytical Report: Total Sales Revenue by State, Customer Segment, and Order Type ---")
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print(pivot_table.round(2))


def total_sales_quantity_price_by_region_product(data):
    product_col = (
        "produce_name" if "produce_name" in data.columns
        else "product_name" if "product_name" in data.columns
        else "product_number"
    )
    required = ["sales_region", product_col, "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales_data,
        index=["sales_region", product_col],
        values=["quantity", "sale_price"],
        aggfunc="sum",
        fill_value=0
    )
    print("\n--- Analytical Report: Total Unit Volume and Sales Revenue by Region and Product ---")
    with pd.option_context("display.max_rows", None, "display.width", 200):
        print(pivot_table.round(2))


def total_sales_quantity_price_customer_type(data):
    required = ["order_type", "customer_type", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales_data,
        index=["order_type", "customer_type"],
        values=["quantity", "sale_price"],
        aggfunc="sum",
        fill_value=0
    )
    print("\n--- Analytical Report: Total Unit Volume and Sales Revenue by Order Type and Customer Segment ---")
    print(pivot_table.round(2))


def max_min_sales_price_by_category(data):
    required = ["product_category", "quantity", "unit_price"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])
    pivot_table = pd.pivot_table(
        sales_data,
        index="product_category",
        values="sale_price",
        aggfunc=["sum", "max", "min"],
        fill_value=0
    )
    print("\n--- Analytical Report: Total Sales Revenue, Maximum Sale Price, and Minimum Sale Price by Category ---")
    print(pivot_table.round(2))


def unique_employees_by_region(data):
    required = ["sales_region", "employee_id"]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    pivot_table = pd.pivot_table(
        data,
        index="sales_region",
        values="employee_id",
        aggfunc="nunique",
        fill_value=0
    )
    pivot_table.columns = ["unique_employees"]
    print("\n--- Organizational Report: Unique Sales Personnel Headcount by Region ---")
    print(pivot_table)


def get_user_selection(options, prompt, required=False, single=False):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i+1}. {option}")

        input_prompt = (
            "Enter the number(s) of your choice(s), separated by commas: "
            if required
            else "Enter the number(s) of your choice(s), separated by commas (enter for no grouping): "
        )
        choice = input(input_prompt).strip()
        if not choice:
            if required:
                print("Selection Error: A valid input is required to proceed.")
                continue
            return []

        try:
            indexes = [int(i) for i in choice.split(',')]
        except ValueError:
            print("Formatting Error: Please enter numeric values separated by commas.")
            continue

        if any(i < 1 or i > len(options) for i in indexes):
            print(f"Range Error: All selections must be between 1 and {len(options)}.")
            continue

        selected = list(dict.fromkeys(options[i - 1] for i in indexes))
        if single and len(selected) != 1:
            print("Selection Error: Please select only a single parameter for this field.")
            continue
        return selected


def generate_custom_pivot_table(data):
    sales_data = data.copy()
    if "quantity" in sales_data.columns and "unit_price" in sales_data.columns:
        sales_data["sale_price"] = sales_data["quantity"] * sales_data["unit_price"]

    available_cols = [c for c in sales_data.columns if c != "parsed_order_date"]

    rows = get_user_selection(available_cols, "\nSelect rows:", required=True)

    col_options = [col for col in available_cols if col not in rows]
    cols = get_user_selection(col_options, "\nSelect columns (optional):", required=False)

    value_options = [
        c for c in sales_data.select_dtypes(include=['number']).columns
        if c != "parsed_order_date"
    ]
    if not value_options:
        print("Configuration Error: No numeric attributes are available for aggregation.")
        return
    values = get_user_selection(value_options, "\nSelect values:", required=True)

    agg_options = ['sum', 'mean', 'count']
    agg_funcs = get_user_selection(agg_options, "\nSelect aggregation function:", required=True)

    try:
        pivot_table = pd.pivot_table(
            sales_data,
            index=rows,
            columns=cols if cols else None,
            values=values,
            aggfunc=agg_funcs,
            fill_value=0
        )
    except Exception as e:
        print("Report Generation Error: Unable to construct pivot table with the selected parameters. Details:", e)
        return

    print("\n--- Custom Ad-Hoc Analytical Report ---")
    with pd.option_context("display.width", 200, "display.max_columns", None):
        print(pivot_table.round(2))


# Individual Requirement 5: Non-trivial sales analytic evaluating employee revenue share, AOV, customer reach, and regional rank
"""
AI Note: Generated with Gemini to satisfy Individual Requirement 5 (multi-KPI employee efficiency pivot analysis) using the prompt "can 
you please explain the algorithms for the personal task below using the corresponding function names and show me (line by line with pseudocode)
 how it would work? 'Implement a new non-trivial sales analytic (simple variations of existing analytics would not satisfy this requirement).'
"""
def employee_performance_efficiency_analysis(data):
    required = [
        "sales_region", "employee_name", "job_title",
        "order_number", "customer_name", "quantity", "unit_price"
    ]
    missing = [col for col in required if col not in data.columns]
    if missing:
        print("Report Generation Error: Missing required data attributes:", ", ".join(missing))
        return

    sales_data = data.assign(sale_price=data["quantity"] * data["unit_price"])

    pivot_table = pd.pivot_table(
        sales_data,
        index=["sales_region", "employee_name", "job_title"],
        values=["sale_price", "order_number", "customer_name", "quantity"],
        aggfunc={
            "sale_price": "sum",
            "order_number": "nunique",
            "customer_name": "nunique",
            "quantity": "sum"
        },
        fill_value=0
    )

    pivot_table = pivot_table.rename(columns={
        "sale_price": "total_revenue",
        "order_number": "unique_orders",
        "customer_name": "unique_customers",
        "quantity": "total_units"
    })

    pivot_table["avg_order_value"] = (
        pivot_table["total_revenue"] / pivot_table["unique_orders"].replace(0, pd.NA)
    ).fillna(0)

    regional_totals = pivot_table.groupby(level="sales_region")["total_revenue"].transform("sum")
    pivot_table["regional_rev_share_%"] = (
        (pivot_table["total_revenue"] / regional_totals.replace(0, pd.NA)) * 100
    ).fillna(0)

    pivot_table["regional_rank"] = (
        pivot_table.groupby(level="sales_region")["total_revenue"]
        .rank(ascending=False, method="min")
        .astype(int)
    )

    ordered_cols = [
        "regional_rank", "total_revenue", "regional_rev_share_%",
        "unique_orders", "avg_order_value", "unique_customers", "total_units"
    ]
    pivot_table = pivot_table[ordered_cols].sort_values(
        by=["sales_region", "regional_rank"], ascending=[True, True]
    )

    print("\n--- Executive KPI Report: Regional Sales Representative Efficiency & Revenue Share ---")
    with pd.option_context("display.max_rows", None, "display.width", 220, "display.max_columns", None):
        print(pivot_table.round(2))


def exit_program(data=None):
    print("Terminating session. Thank you for using the Sales Analytics System.")
    raise SystemExit(0)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Total sales by region and order_type", total_sales_by_region_order_type),
    ("Average sales by region with average sales by state and sale type", average_sales_by_region),
    ("Sales by customer type and order type by state", sales_by_customer_type),
    ("Total sales quantity and price by region and product", total_sales_quantity_price_by_region_product),
    ("Total sales quantity and price customer type", total_sales_quantity_price_customer_type),
    ("Max and min sales price of sales by category", max_min_sales_price_by_category),
    ("Number of unique employees by region", unique_employees_by_region),
    ("Create a custom pivot table", generate_custom_pivot_table),
    ("Employee performance & regional efficiency KPIs (Custom Analytic)", employee_performance_efficiency_analysis),
    ("Exit", exit_program)
)


def display_menu():
    while True:
        print("\n--- Sales Data Dashboard ---")
        for number, (description, _) in enumerate(menu_options, start=1):
            print(f"{number}. {description}")

        choice = input(f"\nPlease select an analytical operation (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid selection '{choice}'. Please enter a valid menu index between 1 and {len(menu_options)}.")


def main():
    csv_file = 'https://drive.google.com/file/d/1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA/view?usp=drive_link'
    sales_data = load_csv(csv_file)

    if sales_data is None:
        return

    non_analytic_actions = {display_initial_rows, exit_program}

    try:
        while True:
            selection = display_menu()
            _, action = menu_options[selection]

            # Part of individual requirement 7 as provided by Gemini: Ask the user what date range to use before performing an analysis
            if action not in non_analytic_actions:
                working_data = filter_by_date_range(sales_data)
                action(working_data)
            else:
                action(sales_data)
    except (KeyboardInterrupt, EOFError):
        print("\nSession terminated by user.")


if __name__ == "__main__":
    main()
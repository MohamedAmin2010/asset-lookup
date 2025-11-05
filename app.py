import pandas as pd 
from flask import Flask, request, render_template_string

# Load the Excel file
df = pd.read_excel("assets.xlsx", sheet_name="Sheet1")
df.columns = df.columns.str.strip()  # Clean column names

# ✅ Define the search function
def search_asset(asset_no):
    result = df[df['Asset no'] == asset_no]
    if result.empty:
        return None
    return result[['Description', 'Model', 'SN', 'Date', 'Location']]

# ✅ Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result_html = ""
    if request.method == "POST":
        try:
            asset_no = int(request.form["asset_no"])
            result = search_asset(asset_no)
            if result is not None:
                result_html = ""
                for _, row in result.iterrows():
                    result_html += f"""
                    <div style='border:1px solid #ccc; padding:10px; margin-bottom:10px; background:#f9f9f9;'>
                        <strong>Description:</strong> {row['Description']}<br>
                        <strong>Model:</strong> {row['Model'] if pd.notna(row['Model']) else 'N/A'}<br>
                        <strong>Serial Number (SN):</strong> {row['SN']}<br>
                        <strong>Date:</strong> {row['Date']}<br>
                        <strong>Location:</strong> {row['Location']}
                    </div>
                    """
            else:
                result_html = "<p style='color:red;'>Asset not found.</p>"
        except ValueError:
            result_html = "<p style='color:red;'>Please enter a valid number.</p>"

    return render_template_string("""
        <h2>🔍 Asset Lookup</h2>
        <form method="post">
            Asset No: <input name="asset_no">
            <input type="submit" value="Search">
        </form>
        <br>
        {{ result|safe }}
    """, result=result_html)

if __name__ == "__main__":
    app.run(debug=True)
    pip


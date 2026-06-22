import requests

def lookup_cve(product_name):

    try:
        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch={product_name}"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return []

        data = response.json()

        vulnerabilities = []

        for item in data.get("vulnerabilities", [])[:5]:

            cve = item.get("cve", {})

            vulnerabilities.append({
                "cve_id": cve.get("id", "N/A"),
                "description": cve.get("descriptions", [{}])[0].get("value", "No Description")
            })

        return vulnerabilities

    except Exception as e:
        print("CVE Lookup Error:", e)
        return []
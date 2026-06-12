import json
import sys

inp = sys.argv[1]
out = sys.argv[2]

with open(inp) as f:
    data = json.load(f)

results = []
rules = {}

for site in data.get("site", []):
    for alert in site.get("alerts", []):
        rule_id = alert["alert"].replace(" ", "_")

        rules[rule_id] = {
            "id": rule_id,
            "name": alert["alert"],
            "shortDescription": {"text": alert["alert"]},
            "defaultConfiguration": {
                "level": "error" if "High" in alert.get("riskdesc", "") else "warning"
            }
        }

        for inst in alert.get("instances", []):
            url = inst.get("uri", "")

            # ❗ 重要修正：httpsをSARIFに入れない
            if url.startswith("http"):
                uri = ""   # or "app/index.html"
            else:
                uri = url

            results.append({
                "ruleId": rule_id,
                "message": {
                    "text": f"{alert['alert']} - {url}"
                },
                "locations": [{
                    "physicalLocation": {
                        "artifactLocation": {
                            "uri": uri
                        }
                    }
                }]
            })

sarif = {
    "version": "2.1.0",
    "runs": [{
        "tool": {
            "driver": {
                "name": "OWASP ZAP",
                "rules": list(rules.values())
            }
        },
        "results": results
    }]
}

with open(out, "w") as f:
    json.dump(sarif, f, indent=2)
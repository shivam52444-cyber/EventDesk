from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown

console = Console()

def print_formatted_plan(plan: dict):
    venue = plan["venue"]
    logistics = plan["logistics"]
    marketing = plan["marketing"]
    total_spent = venue["estimated_cost"] + logistics["estimated_logistics_cost"]

    report_md = f"""
# 🎉 Event Master Plan

## 🏛️ 1. Selected Venue
* **Name:** {venue['venue_name']}
* **Address:** {venue['address']}
* **Capacity:** {venue['capacity']} Guests
* **Cost:** ₹{venue['estimated_cost']:,}
* **In-House Catering:** {"Yes ✅" if venue['has_inhouse_catering'] else "No ❌"}
* **Included Facilities:** {", ".join(venue['included_facilities'])}

---

## 🍽️ 2. Logistics & Catering
* **Catering:** {logistics['catering_menu_summary']} ({logistics['catering_vendor']})
* **Additional Equipment:** {", ".join(logistics['equipment_list'])}
* **Logistics Cost:** ₹{logistics['estimated_logistics_cost']:,}
* **Total Estimated Budget Used:** **₹{total_spent:,}**

---

## 📢 3. Marketing & Invitations
* **Target Audience:** {marketing['target_audience']}

### ✉️ Official Invitation Draft
```text
{marketing['invitation_message']}
```

### 📱 Social Media Posts
1. {marketing['social_media_posts'][0]}
2. {marketing['social_media_posts'][1]}
"""
    console.print(Panel(Markdown(report_md), title="Event Organizer AI", border_style="green"))

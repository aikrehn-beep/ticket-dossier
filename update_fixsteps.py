import re

with open('/home/aikrehn/.openclaw/workspace/projects/ticket-dossier/tablet.html', 'r') as f:
    content = f.read()

# Replace the Fix Steps section
old_html = '''<!-- Fix Steps -->
<div class="card">
<div class="c-h">Fix Steps <span style="font-weight:400;font-size:.85rem;color:#94a3b8;margin-left:8px">(tap checkbox to add to notes)</span></div>
<div class="c-b" id="fixSteps">
<div class="st" data-step="1" onclick="toggleStep(this)"><div class="chk"></div><div>Check Outlook updates: File - Office Account - Update</div></div>
<div class="st" data-step="2" onclick="toggleStep(this)"><div class="chk"></div><div>Run Safe Mode: outlook.exe /safe</div></div>
<div class="st" data-step="3" onclick="toggleStep(this)"><div class="chk"></div><div>Disable PDF preview: Trust Center - Attachment Handling</div></div>
<div class="st" data-step="4" onclick="toggleStep(this)"><div class="chk"></div><div>Office Repair: Settings - Apps - Office - Quick Repair</div></div>
</div>
</div>'''

new_html = '''<!-- Fix Steps -->
<div class="card">
<div class="c-h">Fix Steps <span style="font-weight:400;font-size:.85rem;color:#94a3b8;margin-left:8px">(tap checkbox to add to notes)</span></div>
<div class="c-b" id="fixSteps">
<div class="st" data-step="1" onclick="toggleStep(this)"><div class="chk"></div><div>Check Outlook updates: File - Office Account - Update</div></div>
<div class="st" data-step="2" onclick="toggleStep(this)"><div class="chk"></div><div>Run Safe Mode: outlook.exe /safe</div></div>
<div class="st" data-step="3" onclick="toggleStep(this)"><div class="chk"></div><div>Disable PDF preview: Trust Center - Attachment Handling</div></div>
<div class="st" data-step="4" onclick="toggleStep(this)"><div class="chk"></div><div>Office Repair: Settings - Apps - Office - Quick Repair</div></div>
</div>
<div id="aiSteps" style="display:none;margin-top:12px;border-top:1px solid #334155;padding-top:12px">
<div style="color:#60a5fa;font-size:.85rem;font-weight:600;margin-bottom:8px;text-transform:uppercase;letter-spacing:.5px">🤖 Suggested by AI</div>
<div id="aiStepsList"></div>
</div>
</div>'''

content = content.replace(old_html, new_html)

with open('/home/aikrehn/.openclaw/workspace/projects/ticket-dossier/tablet.html', 'w') as f:
    f.write(content)

print('Done!')
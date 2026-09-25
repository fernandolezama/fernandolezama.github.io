"""Build the standalone review page from editable content files."""
from pathlib import Path
from datetime import datetime
import html,json,re
root=Path(__file__).resolve().parent
def read(name):return json.loads((root/name).read_text())
def esc(s):return html.escape(str(s),quote=True)
def link(url,label,cls='text-link'):
    if not url.startswith(('https://','http://','#')):raise ValueError('Unsupported link: '+url)
    external=' target="_blank" rel="noopener"' if not url.startswith('#') else ''
    return f'<a href="{esc(url)}" class="{cls}"{external}>{esc(label)} <span aria-hidden="true">↗</span></a>'
records=read('publications.json')
for r in records:
    if r['type'] not in ['Journal','Conference','Book']:raise ValueError('Invalid publication type')
    if not re.fullmatch(r'\d{4}',str(r['year'])):raise ValueError('Invalid publication year')
    if not r['citation'].strip():raise ValueError('Empty citation')
records.sort(key=lambda r:int(r['year']),reverse=True)
news=read('news.json')
for n in news:datetime.strptime(n['date'],'%Y-%m')
news.sort(key=lambda n:n['date'],reverse=True)
profile=read('profile.json')
def news_card(n,heading):
    date=datetime.strptime(n['date'],'%Y-%m').strftime('%B %Y')
    action=link(n['link']['url'],n['link']['label']) if n.get('link') else ''
    return f'<article class="news-item"><div class="news-meta"><time datetime="{esc(n["date"])}">{date}</time><span class="news-category">{esc(n["category"])}</span></div><{heading}>{esc(n["title"])}</{heading}><p>{esc(n["text"])}</p>{action}</article>'
def roles(items):return ''.join(f'<li><strong>{link(x["url"],x["organization"]) if x.get("url") else esc(x["organization"])}</strong><div>{esc(x["role"])}<span class="role-detail">{esc(x["detail"])}</span></div></li>' for x in items)
def featured(r):
    url=r['links'][0]['url'] if r['links'] else '#publications'
    attrs=' target="_blank" rel="noopener"' if not url.startswith('#') else ''
    return f'<a class="paper" href="{esc(url)}"{attrs}><span class="paper-year">{esc(r["year"])}</span><div><h3>{esc(r.get("title",r["citation"]))}</h3><p>{esc(r.get("venue",""))}</p></div><span class="arrow" aria-hidden="true">↗</span></a>'
s=(root/'template.html').read_text()
replacements={'PUBLICATION_DATA':json.dumps(records,ensure_ascii=False).replace('</','<\\/'),'SELECTED_PUBLICATIONS':''.join(featured(r) for r in records if r.get('featured')),'LATEST_NEWS':''.join(news_card(n,'h3') for n in news[:3]),'ALL_NEWS':''.join(news_card(n,'h2') for n in news),'AFFILIATION_ROWS':roles(profile['affiliations']),'SERVICE_ROWS':roles(profile['professional_service'])}
for k,v in replacements.items():
    if k not in s:raise ValueError('Missing template field '+k)
    s=s.replace(k,v)
(root/'index.html').write_text(s)
print(f'Built six views, {len(records)} publications, {len(news)} news items and professional roles.')

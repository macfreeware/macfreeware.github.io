#!/usr/bin/env python3
"""Builds the Mac Freeware site (https://macfreeware.github.io) into the folder above tools/.

  python3 -I tools/build.py

English pages at /, Turkish at /tr/. Each app gets a page with schema.org SoftwareApplication
and FAQPage data; sitemap.xml, robots.txt and llms.txt are written too. FAQ and alternatives
text comes from tools/faq.py, the same text as in the app READMEs.
"""
import html
import json
import os
import re
import struct
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from faq import DATA as FAQ  # noqa: E402

BASE = "https://macfreeware.github.io"
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AUTHOR = "Rafet SAPANCI"
GITLAB = "https://gitlab.com/freeware2"
GITHUB = "https://github.com/macfreeware"

APPS = [
    {
        "id": "macmonitor", "name": "MacMonitor", "gl": "macmonitor", "gh": "MacMonitor",
        "download": "https://gitlab.com/freeware2/macmonitor/-/releases/permalink/latest/downloads/MacMonitor.pkg",
        "file": "pkg", "macos": "13", "macos_name": "Ventura",
        "category": "UtilitiesApplication",
        "tagline": {"en": "Menu bar CPU, RAM, network, disk and battery monitor", "tr": "Menü çubuğu CPU, RAM, ağ, disk ve pil izleyici"},
        "summary": {
            "en": "MacMonitor is a free, open-source macOS menu bar app that shows live CPU, RAM and network speed, with per-core load, memory breakdown, top processes, network usage history, free disk space and a long battery history one click away.",
            "tr": "MacMonitor, menü çubuğunda canlı CPU, RAM ve ağ hızını gösteren ücretsiz ve açık kaynak bir macOS uygulamasıdır; tek tıkla çekirdek yükleri, bellek dağılımı, en çok kaynak kullanan işlemler, ağ kullanım geçmişi, disk boşluğu ve uzun süreli pil geçmişi açılır.",
        },
        "features": {
            "en": [
                "Live CPU, RAM and network speed in the menu bar, each shown or hidden as you like, refreshed every 0.5 to 5 seconds",
                "Values turn red when CPU or RAM crosses your alert threshold",
                "Per-core load (efficiency and performance cores) and 60-second history graphs",
                "Memory split into App, Wired, Compressed and Free/Cached, as in Activity Monitor, plus swap",
                "Top six processes by CPU or memory",
                "Free, used and total space for every mounted disk, as Finder counts it",
                "Network tab: download and upload speed in MB/s or Mbit/s, daily to monthly usage, charts kept for 400 days",
                "Battery tab: charge, time remaining, power draw in watts, health and cycle count",
                "Battery history chart for 1 hour, 24 hours, 7 days, 30 days or 90 days, recorded once a minute; macOS shows only 24 hours",
                "Charging, plugged-in and screen-on time in the chart, with separate history windows and a list of charging sessions",
                "About 0.1% CPU and 40 MB of memory with the panel closed; connects only for an optional daily update check",
            ],
            "tr": [
                "Menü çubuğunda canlı CPU, RAM ve ağ hızı; her biri ayrı açılıp kapanır, 0,5 ile 5 saniye arası yenileme",
                "CPU ya da RAM uyarı eşiğini aşınca değer kırmızıya döner",
                "Çekirdek başına yük (verimlilik ve performans çekirdekleri) ve 60 saniyelik geçmiş grafikleri",
                "Etkinlik Monitörü'ndeki gibi Uygulamalar, Bağlı, Sıkıştırılmış ve Boş/Önbellek olarak bellek dağılımı ve takas alanı",
                "CPU'ya ya da belleğe göre en çok kaynak kullanan altı işlem",
                "Bağlı her diskin Finder'daki gibi hesaplanan boş, kullanılan ve toplam alanı",
                "Ağ sekmesi: MB/s ya da Mbit/s olarak indirme ve yükleme hızı, günlükten aylığa kullanım, 400 gün saklanan grafikler",
                "Pil sekmesi: şarj, kalan süre, watt olarak güç tüketimi, pil sağlığı ve döngü sayısı",
                "1 saat, 24 saat, 7 gün, 30 gün ya da 90 günlük pil geçmişi grafiği, dakikada bir kayıt; macOS yalnızca 24 saat gösterir",
                "Grafikte şarj, prizde ve ekran açık süreleri; ayrı geçmiş pencereleri ve şarj oturumları listesi",
                "Panel kapalıyken yaklaşık %0,1 CPU ve 40 MB bellek; yalnızca isteğe bağlı günlük güncelleme denetimi için bağlanır",
            ],
        },
        "shots": {
            "en": [("macmonitor-menubar.png", "MacMonitor in a light and a dark menu bar"),
                   ("macmonitor-overview.png", "Overview tab: CPU, cores and memory"),
                   ("macmonitor-disk.png", "Disk tab: free, used and total space"),
                   ("macmonitor-network.png", "Network tab: speed, usage and history chart"),
                   ("macmonitor-battery.png", "Battery tab: charge, history chart, health and cycles")],
            "tr": [("macmonitor-menubar.png", "Açık ve koyu menü çubuğunda MacMonitor"),
                   ("macmonitor-overview-tr.png", "Genel Bakış sekmesi: CPU, çekirdekler ve bellek"),
                   ("macmonitor-disk-tr.png", "Disk sekmesi: boş, kullanılan ve toplam alan"),
                   ("macmonitor-network-tr.png", "Ağ sekmesi: hız, kullanım ve geçmiş grafiği"),
                   ("macmonitor-battery-tr.png", "Pil sekmesi: şarj, geçmiş grafiği, sağlık ve döngü")],
        },
    },
    {
        "id": "maccalendar", "name": "MacCalendar", "gl": "maccalendar", "gh": "MacCalendar",
        "download": "https://gitlab.com/freeware2/maccalendar/-/releases/permalink/latest/downloads/MacCalendar.pkg",
        "file": "pkg", "macos": "13", "macos_name": "Ventura",
        "category": "UtilitiesApplication",
        "tagline": {"en": "Menu bar calendar and world clock", "tr": "Menü çubuğu takvimi ve dünya saati"},
        "summary": {
            "en": "MacCalendar is a free, open-source macOS menu bar calendar with a dual world clock and country flags, a month view, quick notes for any day and more than 400 cities.",
            "tr": "MacCalendar, ülke bayraklı çift dünya saati, aylık takvim, güne özel hızlı notlar ve 400'den fazla şehir sunan ücretsiz ve açık kaynak bir macOS menü çubuğu takvimidir.",
        },
        "features": {
            "en": [
                "Date and time in the menu bar in several formats, with an optional second city",
                "Dual clock with country flags, for example 🇹🇷 20:04 🇯🇵 02:04, in five layouts",
                "Month calendar with today highlighted and a Today button",
                "Quick notes for any day, marked on the calendar",
                "More than 400 cities and time zones, with custom labels",
                "English, Turkish or the system language; launch at login",
            ],
            "tr": [
                "Menü çubuğunda farklı biçimlerde tarih ve saat, isteğe bağlı ikinci şehir",
                "Ülke bayraklı çift saat, örneğin 🇹🇷 20:04 🇯🇵 02:04; beş dizilim",
                "Bugünün vurgulandığı aylık takvim ve Bugün düğmesi",
                "Her gün için takvimde işaretlenen hızlı notlar",
                "400'den fazla şehir ve saat dilimi, özel etiketler",
                "Türkçe, İngilizce ya da sistem dili; oturum açılışında başlatma",
            ],
        },
        "shots": {
            "en": [("maccalendar-menubar.png", "MacCalendar in the menu bar: date, Turkey and Japan times with flags"),
                   ("maccalendar-calendar.png", "Calendar window with the second clock and quick notes")],
            "tr": [("maccalendar-menubar.png", "Menü çubuğunda MacCalendar: tarih, bayraklarla Türkiye ve Japonya saati"),
                   ("maccalendar-calendar.png", "İkinci saat ve hızlı notlarla takvim penceresi")],
        },
    },
    {
        "id": "macrar", "name": "MacRAR", "gl": "macrar", "gh": "MacRAR",
        "download": "https://gitlab.com/freeware2/macrar/-/releases/permalink/latest/downloads/MacRAR.pkg",
        "file": "pkg", "macos": "15", "macos_name": "Sequoia",
        "category": "UtilitiesApplication",
        "tagline": {"en": "WinRAR-style archive manager", "tr": "WinRAR tarzı arşiv yöneticisi"},
        "summary": {
            "en": "MacRAR is a free, open-source, WinRAR-style archive manager for macOS: open, extract and create RAR, ZIP, 7Z and TAR archives, with a Finder right-click menu.",
            "tr": "MacRAR, macOS için ücretsiz ve açık kaynak, WinRAR tarzı bir arşiv yöneticisidir: RAR, ZIP, 7Z ve TAR arşivlerini açar, çıkarır ve oluşturur; Finder sağ tık menüsüyle gelir.",
        },
        "features": {
            "en": [
                "Look inside RAR, ZIP, 7Z and TAR archives without extracting them",
                "Extract everything or a selection, or drag files straight to the Finder",
                "Create RAR5/RAR4 (with RARLAB's rar), ZIP with AES-256, 7Z and TAR archives",
                "Finder right-click menu: compress to RAR or ZIP, extract, open",
                "Test, merge and compare archives; edit RAR and ZIP archives",
                "Password manager backed by the macOS Keychain",
            ],
            "tr": [
                "RAR, ZIP, 7Z ve TAR arşivlerinin içine çıkarmadan bakma",
                "Tümünü ya da seçilenleri çıkarma, dosyaları doğrudan Finder'a sürükleme",
                "RAR5/RAR4 (RARLAB'ın rar aracıyla), AES-256 parolalı ZIP, 7Z ve TAR oluşturma",
                "Finder sağ tık menüsü: RAR ya da ZIP olarak sıkıştır, çıkar, aç",
                "Arşivleri sınama, birleştirme ve karşılaştırma; RAR ve ZIP düzenleme",
                "macOS Anahtar Zinciri'ni kullanan parola yöneticisi",
            ],
        },
        "shots": {
            "en": [("macrar-main.png", "MacRAR main window browsing a folder of archives"),
                   ("macrar-finder.png", "MacRAR items in the Finder right-click menu")],
            "tr": [("macrar-main.png", "Arşiv klasörünü gösteren MacRAR ana penceresi"),
                   ("macrar-finder.png", "Finder sağ tık menüsünde MacRAR")],
        },
    },
    {
        "id": "maczilla", "name": "MacZilla", "gl": "maczilla", "gh": "MacZilla",
        "download": "https://gitlab.com/freeware2/maczilla/-/releases/permalink/latest/downloads/MacZilla.zip",
        "file": "zip", "macos": "14", "macos_name": "Sonoma",
        "category": "DeveloperApplication",
        "tagline": {"en": "FTP, FTPS and SFTP client", "tr": "FTP, FTPS ve SFTP istemcisi"},
        "summary": {
            "en": "MacZilla is a free, open-source, native FTP, FTPS and SFTP client for macOS in the spirit of FileZilla: two panes, tabs, a transfer queue, folder sync and a Site Manager.",
            "tr": "MacZilla, macOS için FileZilla tarzı, ücretsiz ve açık kaynak, yerel bir FTP, FTPS ve SFTP istemcisidir: iki panel, sekmeler, aktarım kuyruğu, klasör eşitleme ve Site Yöneticisi.",
        },
        "features": {
            "en": [
                "Two panes, tabs with one connection each, and drag and drop",
                "FTP, explicit and implicit FTPS, and SFTP through macOS's own ssh",
                "Concurrent transfer queue with speed limits and retry",
                "Folder comparison and one-click synchronizing",
                "Site Manager with groups and bookmarks; passwords in the Keychain",
                "Imports sites, bookmarks and passwords from FileZilla",
            ],
            "tr": [
                "İki panel, her biri ayrı bağlantı olan sekmeler, sürükle bırak",
                "FTP, açık ve örtük FTPS, macOS'un kendi ssh aracıyla SFTP",
                "Hız sınırlı ve yeniden denemeli eşzamanlı aktarım kuyruğu",
                "Klasör karşılaştırma ve tek tıkla eşitleme",
                "Gruplu ve yer imli Site Yöneticisi; parolalar Anahtar Zinciri'nde",
                "FileZilla'dan site, yer imi ve parola içe aktarma",
            ],
        },
        "shots": {
            "en": [("maczilla-main.png", "MacZilla main window with two panes, a comparison and the transfer queue"),
                   ("maczilla-sites.png", "MacZilla Site Manager with groups")],
            "tr": [("maczilla-main.png", "İki panel, karşılaştırma ve aktarım kuyruğuyla MacZilla ana penceresi"),
                   ("maczilla-sites.png", "Gruplu MacZilla Site Yöneticisi")],
        },
    },
    {
        "id": "macexplorer", "name": "MacExplorer", "gl": "macexplorer", "gh": "MacExplorer",
        "download": "https://gitlab.com/freeware2/macexplorer/-/releases/permalink/latest/downloads/MacExplorer.zip",
        "file": "zip", "macos": "15", "macos_name": "Sequoia",
        "category": "UtilitiesApplication",
        "tagline": {"en": "Windows Explorer-style file manager", "tr": "Windows Gezgini tarzı dosya yöneticisi"},
        "summary": {
            "en": "MacExplorer is a free, open-source, Windows Explorer-style file manager for macOS: tabs, dual pane, real Cut and Paste, a preview pane, and SFTP and FTP right in the window.",
            "tr": "MacExplorer, macOS için ücretsiz ve açık kaynak, Windows Gezgini tarzı bir dosya yöneticisidir: sekmeler, çift panel, gerçek Kes ve Yapıştır, önizleme bölmesi ve pencerenin içinde SFTP ile FTP.",
        },
        "features": {
            "en": [
                "Tabs in every pane and dual pane (F9); tabs move between panes and windows",
                "Address bar with steps like Explorer, and Windows column and menu names",
                "Real Cut, Copy and Paste that also works with Finder's clipboard",
                "Copy and move with progress, Replace / Skip / Keep both, and Undo / Redo for every file operation",
                "Icon, List and Details views with thumbnails, a preview pane (Alt+P) and Quick Look",
                "Search that also looks through subfolders in the background",
                "SFTP, FTP, FTPES and FTPS in the pane; SMB, WebDAV, AFP and NFS mounted as disks",
                "Browse ZIP, RAR, 7Z and TAR archives like folders; mount ISO and DMG images and create new ones",
                "Windows keyboard behaviour by default, Mac behaviour optional; function key bar",
                "14 themes with light and dark colours; updates itself from GitLab",
            ],
            "tr": [
                "Her panelde sekmeler ve çift panel (F9); sekmeler paneller ve pencereler arasında taşınır",
                "Gezgin'deki gibi adımlı adres çubuğu, Windows sütun ve menü adları",
                "Finder panosuyla da çalışan gerçek Kes, Kopyala ve Yapıştır",
                "İlerleme penceresi, Değiştir / Atla / İkisini de sakla ve tüm dosya işlemleri için Geri Al / Yinele",
                "Küçük resimli Simge, Liste ve Ayrıntılar görünümleri, önizleme bölmesi (Alt+P) ve Hızlı Bakış",
                "Alt klasörleri de arka planda tarayan arama",
                "Panelde SFTP, FTP, FTPES ve FTPS; disk olarak bağlanan SMB, WebDAV, AFP ve NFS",
                "ZIP, RAR, 7Z ve TAR arşivlerinde klasör gibi gezinme; ISO ve DMG bağlama ve oluşturma",
                "Varsayılan olarak Windows klavye davranışı, isteğe bağlı Mac davranışı; işlev tuşu çubuğu",
                "Açık ve koyu renkli 14 tema; GitLab'dan kendini günceller",
            ],
        },
        "shots": {
            "en": [("macexplorer-main.png", "MacExplorer main window with tabs and two panes"),
                   ("macexplorer-preview.png", "Preview pane showing a selected photo and its details"),
                   ("macexplorer-archive-dark.png", "Dark appearance with a ZIP archive open as a folder")],
            "tr": [("macexplorer-main.png", "Sekmeli ve iki panelli MacExplorer ana penceresi"),
                   ("macexplorer-preview.png", "Seçili fotoğrafı ve bilgilerini gösteren önizleme bölmesi"),
                   ("macexplorer-archive-dark.png", "Klasör gibi açılmış ZIP arşiviyle koyu görünüm")],
        },
    },
]

T = {
    "en": {
        "site_title": "Mac Freeware",
        "site_tag": "Small, free and open-source tools for macOS",
        "intro": "Every app here started because something on my own Mac was missing, slow or awkward. Once a tool made my daily work easier, I shared it: free, with its source code, under the GNU GPL.",
        "apps": "Apps",
        "download": "Download",
        "details": "Details",
        "common": "What they have in common",
        "common_items": [
            "<b>Free and open source</b> under the GNU GPL, version 3 or later. No ads, no accounts, no in-app purchases.",
            "<b>Native Mac apps</b> written in Swift and SwiftUI; no Electron. They run on Apple Silicon and Intel Macs.",
            "<b>In English and Turkish.</b>",
        ],
        "install": "Before you install",
        "install_text": "The apps are not notarized by Apple (that needs a paid developer account), so macOS blocks them the first time. Allow each app once in <b>System Settings ▸ Privacy &amp; Security ▸ Open Anyway</b>. Every release lists a SHA-256 checksum.",
        "features": "Features",
        "screens": "Screenshots",
        "faq": "Frequently asked questions",
        "req": "Requirements",
        "req_text": "macOS {v} {n} or later · Apple Silicon and Intel",
        "free": "Free · Open source (GPL-3.0)",
        "source": "Source code",
        "releases": "All releases",
        "readme": "Full documentation",
        "home": "All apps",
        "other": "Türkçe",
        "footer": "Independent projects by {a}. Not affiliated with Apple or with the other apps named on this site; those names belong to their owners.",
        "dl_label": "Download {name} for macOS ({f})",
    },
    "tr": {
        "site_title": "Mac Freeware",
        "site_tag": "macOS için küçük, ücretsiz ve açık kaynak araçlar",
        "intro": "Buradaki her uygulama, kendi Mac'imde bir şey eksik, yavaş ya da zahmetli olduğu için başladı. Bir araç günlük işimi kolaylaştırınca onu paylaştım: ücretsiz, kaynak koduyla birlikte, GNU GPL lisansıyla.",
        "apps": "Uygulamalar",
        "download": "İndir",
        "details": "Ayrıntılar",
        "common": "Ortak özellikleri",
        "common_items": [
            "GNU GPL sürüm 3 ya da sonrası ile <b>ücretsiz ve açık kaynak</b>. Reklam, hesap ya da uygulama içi satın alma yok.",
            "Swift ve SwiftUI ile yazılmış <b>yerel Mac uygulamaları</b>; Electron yok. Apple Silicon ve Intel Mac'lerde çalışır.",
            "<b>Türkçe ve İngilizce.</b>",
        ],
        "install": "Kurmadan önce",
        "install_text": "Uygulamalar Apple onayından (notarization) geçmedi; bunun için ücretli geliştirici hesabı gerekiyor. Bu yüzden macOS ilk açılışta engeller. Her uygulamaya <b>Sistem Ayarları ▸ Gizlilik ve Güvenlik ▸ Yine de Aç</b> ile bir kez izin verin. Her sürümde SHA-256 değeri yayımlanır.",
        "features": "Özellikler",
        "screens": "Ekran görüntüleri",
        "faq": "Sık sorulan sorular",
        "req": "Gereksinimler",
        "req_text": "macOS {v} {n} veya üstü · Apple Silicon ve Intel",
        "free": "Ücretsiz · Açık kaynak (GPL-3.0)",
        "source": "Kaynak kod",
        "releases": "Tüm sürümler",
        "readme": "Ayrıntılı belgeler",
        "home": "Tüm uygulamalar",
        "other": "English",
        "footer": "{a} tarafından geliştirilen bağımsız projeler. Apple ile ya da bu sitede adı geçen diğer uygulamalarla bağlantılı değildir; bu adlar sahiplerine aittir.",
        "dl_label": "{name}'ı macOS için indir ({f})",
    },
}


def png_size(name):
    with open(os.path.join(OUT, "assets", "img", name), "rb") as f:
        head = f.read(24)
    return struct.unpack(">II", head[16:24])


def figure(name, alt, up):
    """Screenshots are 2x captures: show them at half their pixel size; wide strips span the row."""
    w, h = png_size(name)
    wide = " wide" if w > 2 * h or w >= 1600 else ""
    return (f'<figure class="shot{wide}"><img src="{up}assets/img/{name}" width="{w // 2}" height="{h // 2}" '
            f'alt="{esc(alt)}" loading="lazy" decoding="async"><figcaption>{esc(alt)}</figcaption></figure>')


def esc(s):
    return html.escape(s, quote=True)


def md_inline(s, app, lang):
    """Minimal Markdown for the FAQ answers: code, bold, links."""
    s = esc(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    readme = f"{GITLAB}/{app['gl']}/-/blob/main/README{'.tr' if lang == 'tr' else ''}.md"
    s = re.sub(r"\[([^\]]+)\]\(#([^)]+)\)", lambda m: f'<a href="{readme}#{m.group(2)}">{m.group(1)}</a>', s)
    return s


def plain(s):
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s


def parse_faq(app, lang):
    text = FAQ[app["name"]][lang]["faq"]
    parts = re.split(r"\n### ", "\n" + text.split("\n", 1)[1])
    qa, note = [], ""
    for p in parts[1:]:
        q, a = p.split("\n", 1)
        a = a.strip()
        m = re.search(r"\n*<sub>(.*)</sub>\s*$", a, re.S)
        if m:
            note = m.group(1).strip()
            a = a[:m.start()].strip()
        qa.append((q.strip(), a))
    return qa, note


def url(lang, app=None):
    prefix = "/tr" if lang == "tr" else ""
    return f"{BASE}{prefix}/{app['id']}/" if app else f"{BASE}{prefix}/"


def rel(lang, app=None, depth=0):
    """Relative link from a page at the given depth below its language root."""
    up = "../" * depth
    return f"{up}{app['id']}/" if app else (up or "./")


def page(lang, title, desc, canonical, alt_url, body, jsonld, depth_to_root):
    t = T[lang]
    other = "en" if lang == "tr" else "tr"
    css = "../" * depth_to_root + "assets/style.css"
    ld = "\n".join(f'<script type="application/ld+json">{json.dumps(j, ensure_ascii=False)}</script>' for j in jsonld)
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="{lang}" href="{canonical}">
<link rel="alternate" hreflang="{other}" href="{alt_url}">
<link rel="alternate" hreflang="x-default" href="{canonical if lang == 'en' else alt_url}">
<meta property="og:type" content="website">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canonical}">
<meta name="color-scheme" content="light dark">
<link rel="stylesheet" href="{css}">
{ld}
</head>
<body>
<header class="top"><div class="wrap">
<a class="brand" href="{('../' * depth_to_root + ('tr/' if lang == 'tr' else '')) or './'}">{esc(t['site_title'])}</a>
<nav><a href="{alt_url}" hreflang="{other}" lang="{other}">{esc(t['other'])}</a></nav>
</div></header>
<main class="wrap">
{body}
</main>
<footer class="wrap foot">
<p>{t['footer'].format(a=esc(AUTHOR))}</p>
<p><a href="{GITLAB}">GitLab</a> · <a href="{GITHUB}">GitHub</a></p>
</footer>
</body>
</html>
"""


def app_jsonld(app, lang, qa):
    t = T[lang]
    return [
        {
            "@context": "https://schema.org",
            "@type": "SoftwareApplication",
            "name": app["name"],
            "description": app["summary"][lang],
            "applicationCategory": app["category"],
            "operatingSystem": f"macOS {app['macos']} or later",
            "url": url(lang, app),
            "downloadUrl": app["download"],
            "image": f"{BASE}/assets/img/{app['id']}-icon.png",
            "screenshot": [f"{BASE}/assets/img/{f}" for f, _ in app["shots"][lang]],
            "featureList": app["features"][lang],
            "isAccessibleForFree": True,
            "license": "https://www.gnu.org/licenses/gpl-3.0.html",
            "inLanguage": ["en", "tr"],
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
            "author": {"@type": "Person", "name": AUTHOR},
            "sameAs": [f"{GITLAB}/{app['gl']}", f"{GITHUB}/{app['gh']}"],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": plain(a)}}
                for q, a in qa
            ],
        },
    ]


def build_app(app, lang):
    t = T[lang]
    qa, note = parse_faq(app, lang)
    alt = FAQ[app["name"]][lang]["alt"]
    other = "en" if lang == "tr" else "tr"
    gl_readme = f"{GITLAB}/{app['gl']}/-/blob/main/README{'.tr' if lang == 'tr' else ''}.md"
    shots = "\n".join(figure(f, a, "../" + ("../" if lang == "tr" else "")) for f, a in app["shots"][lang])
    feats = "\n".join(f"<li>{esc(x)}</li>" for x in app["features"][lang])
    faqs = "\n".join(f"<details><summary><h3>{esc(q)}</h3></summary><p>{md_inline(a, app, lang)}</p></details>" for q, a in qa)
    img = f'../{"../" if lang == "tr" else ""}assets/img/{app["id"]}-icon.png'
    body = f"""
<p class="crumb"><a href="../">{esc(t['home'])}</a></p>
<section class="hero app">
<img class="icon" src="{img}" width="112" height="112" alt="{esc(app['name'])} icon">
<div>
<h1>{esc(app['name'])}</h1>
<p class="tag">{esc(app['tagline'][lang])}</p>
<p class="lead">{esc(app['summary'][lang])}</p>
<p class="alt">{alt}</p>
<p class="actions"><a class="btn" href="{app['download']}">{esc(t['dl_label'].format(name=app['name'], f=app['file']))}</a></p>
<p class="meta">{esc(t['free'])} · {esc(t['req_text'].format(v=app['macos'], n=app['macos_name']))}</p>
<p class="links"><a href="{gl_readme}">{esc(t['readme'])}</a> · <a href="{GITLAB}/{app['gl']}/-/releases">{esc(t['releases'])}</a> · <a href="{GITLAB}/{app['gl']}">{esc(t['source'])}: GitLab</a> · <a href="{GITHUB}/{app['gh']}">GitHub</a></p>
</div>
</section>
<section><h2>{esc(t['features'])}</h2><ul class="feats">{feats}</ul></section>
<section><h2>{esc(t['screens'])}</h2><div class="shots">{shots}</div></section>
<section><h2>{esc(t['faq'])}</h2><div class="faq">{faqs}</div>
<p class="note">{esc(note)}</p></section>
<section><h2>{esc(t['install'])}</h2><p>{t['install_text']}</p></section>
"""
    title = (f"{app['name']} – {app['tagline'][lang]} for macOS (free)" if lang == "en"
             else f"{app['name']} – {app['tagline'][lang]} (macOS, ücretsiz)")
    return page(lang, title, app["summary"][lang], url(lang, app), url(other, app), body, app_jsonld(app, lang, qa), 1 if lang == "en" else 2)


def build_index(lang):
    t = T[lang]
    other = "en" if lang == "tr" else "tr"
    prefix = "" if lang == "en" else "../"
    cards = []
    for app in APPS:
        cards.append(f"""<article class="card">
<a href="{app['id']}/"><img class="icon" src="{prefix}assets/img/{app['id']}-icon.png" width="80" height="80" alt="{esc(app['name'])} icon"></a>
<h3><a href="{app['id']}/">{esc(app['name'])}</a></h3>
<p class="tag">{esc(app['tagline'][lang])}</p>
<p>{esc(app['summary'][lang])}</p>
<p class="alt">{FAQ[app['name']][lang]['alt']}</p>
<p class="actions"><a class="btn" href="{app['download']}">{esc(t['download'])} ({app['file']})</a> <a class="btn ghost" href="{app['id']}/">{esc(t['details'])}</a></p>
</article>""")
    common = "".join(f"<li>{x}</li>" for x in t["common_items"])
    body = f"""
<section class="hero"><div>
<h1>{esc(t['site_title'])}</h1>
<p class="tag">{esc(t['site_tag'])}</p>
<p class="lead">{esc(t['intro'])}</p>
</div></section>
<section><h2>{esc(t['apps'])}</h2><div class="grid">{''.join(cards)}</div></section>
<section><h2>{esc(t['common'])}</h2><ul class="feats">{common}</ul></section>
<section><h2>{esc(t['install'])}</h2><p>{t['install_text']}</p></section>
"""
    jsonld = [
        {"@context": "https://schema.org", "@type": "WebSite", "name": t["site_title"], "url": url(lang), "inLanguage": lang,
         "description": t["site_tag"]},
        {"@context": "https://schema.org", "@type": "ItemList", "name": t["apps"],
         "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(lang, a), "name": a["name"]} for i, a in enumerate(APPS)]},
    ]
    title = f"{t['site_title']} – {t['site_tag']}"
    return page(lang, title, t["site_tag"] + ": " + ", ".join(a["name"] for a in APPS) + ".", url(lang), url(other), body, jsonld, 0 if lang == "en" else 1)


def llms_txt():
    lines = ["# Mac Freeware", "",
             "> Small, free and open-source (GPL-3.0) native macOS apps by " + AUTHOR + ", written in Swift and SwiftUI. "
             "They run on Apple Silicon and Intel Macs and have English and Turkish interfaces. No ads, no accounts, no in-app purchases.", "",
             "## Apps", ""]
    for a in APPS:
        lines.append(f"- [{a['name']}]({url('en', a)}): {a['summary']['en']} Free alternative to: {plain(re.sub(r'<[^>]+>', '', FAQ[a['name']]['en']['alt']))} Requires macOS {a['macos']}+. Download: {a['download']}")
    lines += ["", "## Source code and documentation", ""]
    for a in APPS:
        lines.append(f"- [{a['name']} README]({GITLAB}/{a['gl']}/-/raw/main/README.md): full documentation, install steps and FAQ (GitLab; mirror: {GITHUB}/{a['gh']})")
    lines += ["", "## Optional", "", f"- [Türkçe site]({BASE}/tr/): the same pages in Turkish", f"- [GitLab group]({GITLAB})", f"- [GitHub organization]({GITHUB})", ""]
    return "\n".join(lines)


CSS = """:root{--bg:#fbfbfd;--fg:#1d1d1f;--muted:#6e6e73;--card:#fff;--line:#e3e3e8;--accent:#0a66d8;--accent-fg:#fff;--alt:#f2f6fc}
@media (prefers-color-scheme:dark){:root{--bg:#141416;--fg:#f2f2f4;--muted:#a1a1a8;--card:#1f1f23;--line:#2f2f35;--accent:#4c9bff;--accent-fg:#0b0b0d;--alt:#1b2230}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--fg);font:16px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--accent)}.wrap{max-width:980px;margin:0 auto;padding:0 20px}
.top{border-bottom:1px solid var(--line);background:var(--card)}.top .wrap{display:flex;justify-content:space-between;align-items:center;height:56px}
.brand{font-weight:700;color:var(--fg);text-decoration:none;font-size:18px}
h1{font-size:40px;line-height:1.1;margin:0 0 6px}h2{font-size:24px;margin:44px 0 14px}h3{font-size:18px;margin:0}
.hero{display:flex;gap:28px;align-items:flex-start;padding:40px 0 8px}.hero .icon{flex:none;border-radius:22%}
.tag{color:var(--muted);font-size:18px;margin:0 0 12px}.lead{font-size:18px;margin:0 0 12px}
.alt{background:var(--alt);border-radius:10px;padding:10px 14px;margin:0 0 16px}
.btn{display:inline-block;background:var(--accent);color:var(--accent-fg);padding:10px 18px;border-radius:999px;text-decoration:none;font-weight:600;margin:0 8px 8px 0}
.btn.ghost{background:transparent;color:var(--accent);border:1px solid var(--accent)}
.meta{color:var(--muted);margin:4px 0}.links{font-size:15px}.crumb{margin:20px 0 0;font-size:15px}
.grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px}
.card{background:var(--card);border:1px solid var(--line);border-radius:16px;padding:22px}.card .icon{border-radius:22%}.card h3{font-size:22px;margin-top:8px}.card h3 a{color:var(--fg);text-decoration:none}
.feats{padding-left:20px}.feats li{margin:6px 0}
.shots{display:flex;flex-wrap:wrap;gap:22px;justify-content:center;align-items:flex-start}.shot{margin:0;flex:0 1 auto;max-width:100%}.shot.wide{flex-basis:100%}.shot img{max-width:100%;height:auto;display:block;margin:0 auto}
figcaption{color:var(--muted);font-size:14px;text-align:center;margin-top:6px}
.faq details{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:12px 16px;margin:0 0 10px}
.faq summary{cursor:pointer;list-style:none}.faq summary::-webkit-details-marker{display:none}.faq summary h3{display:inline}
.faq summary::before{content:"+";display:inline-block;width:1.2em;color:var(--accent);font-weight:700}.faq details[open] summary::before{content:"–"}
.faq p{margin:10px 0 2px}.note{color:var(--muted);font-size:13px}
code{font:14px ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--alt);padding:1px 5px;border-radius:5px}
.foot{color:var(--muted);font-size:14px;border-top:1px solid var(--line);margin-top:56px;padding-top:18px;padding-bottom:40px}
@media (max-width:720px){h1{font-size:32px}.hero{flex-direction:column;gap:16px;padding-top:28px}.grid{grid-template-columns:1fr}}
"""


def write(path, text):
    full = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)


def main():
    write("assets/style.css", CSS)
    urls = []
    for lang in ("en", "tr"):
        base = "" if lang == "en" else "tr/"
        write(f"{base}index.html", build_index(lang))
        urls.append(url(lang))
        for app in APPS:
            write(f"{base}{app['id']}/index.html", build_app(app, lang))
            urls.append(url(lang, app))
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
          + "".join(f"  <url><loc>{u}</loc></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    write("llms.txt", llms_txt())
    write(".nojekyll", "")
    write("404.html", page("en", "Page not found – Mac Freeware", "Page not found", BASE + "/", BASE + "/tr/",
                           '<section class="hero"><div><h1>Page not found</h1><p><a href="/">Mac Freeware apps</a> · <a href="/tr/">Türkçe</a></p></div></section>', [], 0))
    print("built", len(urls), "pages into", OUT)


if __name__ == "__main__":
    main()

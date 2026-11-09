# macfreeware.github.io

Source of [macfreeware.github.io](https://macfreeware.github.io), the site of the Mac Freeware apps (MacMonitor, MacCalendar, MacRAR, MacZilla, MacExplorer, MacNote++).

The pages are generated: edit `tools/build.py` (apps, features, screenshots) or `tools/faq.py` (FAQ and alternatives, shared with the app READMEs), then run

```bash
python3 -I tools/build.py
```

and commit the result. GitHub Pages serves the `main` branch as is (`.nojekyll`).

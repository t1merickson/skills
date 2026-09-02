# Site architecture recipes

Treat these as hypotheses to verify against the current artifact.

- **Static HTML:** mirror assets, preserve paths, and test from the intended local origin.
- **ES modules:** `file://` often blocks module fetches. Prefer a tiny local server or a build that bundles modules; do not contort source solely to permit double-click launch unless that is a requirement.
- **Vite/React SPA:** capture the built asset graph or rebuild from source. Verify client routes and root-relative assets under the archive base path.
- **Next.js/App Router:** inspect both DOM asset references and serialized payloads that hydration can reintroduce. Disable or rewrite server-only routes explicitly.
- **WordPress:** check `wp-sitemap.xml` before writing a parser. Its child maps often expose the complete bounded page inventory even when `/wp-json/` is unavailable. Media paths are predictable, but assume at least one asset breaks the pattern rather than silently trusting the count.
- **Cargo and other hosted builders:** embedded state can reveal the complete page inventory without a crawl. Cargo originals commonly live under `/t/original/`, asset delivery may require an ordinary browser user agent, and captured boot state may contain an origin redirect that must be disabled and documented for local replay.

Common implementation traps:

- assets embedded in JSON, CSS, template literals, service workers, or runtime-generated URLs;
- replacement strings interpreting special dollar sequences—use function replacements;
- Python 3.14+ surfacing `socket.TimeoutError` directly from `urllib.request`; catch timeout, connection, and OS errors as well as `URLError`/`HTTPError` in resumable crawlers;
- infinite animation loops defeating virtual-time waits—use bounded command timeouts;
- WebGL buffers reading blank through DOM canvas APIs—capture through the compositor;
- lazy media needing a bounded scroll pass before completeness checks;
- a local archive that looks correct only because service-worker or browser cache still contains the live site.

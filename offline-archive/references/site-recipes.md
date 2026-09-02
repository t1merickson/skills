# Site architecture recipes

Treat these as hypotheses to verify against the current artifact.

- **Static HTML:** mirror assets, preserve paths, and test from the intended local origin.
- **ES modules:** `file://` often blocks module fetches. Prefer a tiny local server or a build that bundles modules; do not contort source solely to permit double-click launch unless that is a requirement.
- **Vite/React SPA:** capture the built asset graph or rebuild from source. Verify client routes and root-relative assets under the archive base path.
- **Next.js/App Router:** inspect both DOM asset references and serialized payloads that hydration can reintroduce. Disable or rewrite server-only routes explicitly.
- **WordPress:** public sitemaps may provide a bounded inventory when an API is unavailable. Their availability is not permission to ignore site policy or fetch unrestricted media trees.
- **Cargo and other hosted builders:** embedded state can reveal the public page inventory. Do not mutate captured state merely to defeat an origin redirect without documenting and testing the transformation.

Common implementation traps:

- assets embedded in JSON, CSS, template literals, service workers, or runtime-generated URLs;
- replacement strings interpreting special dollar sequences—use function replacements;
- infinite animation loops defeating virtual-time waits—use bounded command timeouts;
- WebGL buffers reading blank through DOM canvas APIs—capture through the compositor;
- lazy media needing a bounded scroll pass before completeness checks;
- a local archive that looks correct only because service-worker or browser cache still contains the live site.
